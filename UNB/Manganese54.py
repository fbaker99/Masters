'''
Created on Nov. 7, 2022

@author: fionabaker
'''

from scipy.integrate import solve_ivp
import radioactivedecay as rad
import numpy as np
from scipy.constants import Avogadro as NA
import matplotlib.pyplot as plot

FLUX = 2e14   # n/cm2 s

ABUNDANCEFe54 = 0.0584

iso_list = ['Mn-54', 'Mn-54']

Iron = 'Fe-54'

CROSS_SECTIONFe54 = 2.5E-24 # cm^2

FeDensity = 7.874 #g/cm^3

def IronProduction(Flux_FE):
    nuc = rad.Nuclide(Iron)
    N_atomic = FeDensity * NA * ABUNDANCEFe54 / nuc.atomic_mass
    macro_cross_Fe = CROSS_SECTIONFe54 * N_atomic
    production_term = Flux_FE * macro_cross_Fe * FLUX
    
    return production_term

def initial_decay_constant(isotope):
    # based on input isotope (iso), calcs decay constant 
    nuc = rad.Nuclide(isotope)
    decay_const = np.log(2) / nuc.half_life('y') 
  
    if isotope == iso_list[0]:
        input_atoms = 0
    else:
        input_atoms = 0     
    N0_atoms = input_atoms
    
    return N0_atoms, decay_const

def decay_function(t, y, k1, Flux_FE):
   
    P_Fe54 = IronProduction(Flux_FE)

    dMn54 = P_Fe54 - k1 * y[0]
    return dMn54

#defines a function that returns the inital the number of atoms and the decay constant for each isotope
#uses a for loop to obtain the activity every year for 8 years
time = [0, 10]
time_solutions = []
for i in range(0, 11, 1):
    time_solutions.append(i)
    
#the for loop is used to input the initial decay of each isotope into the empty arrays
IV_y = []
k = []

# For loop used to solve ODEs
for isotope in iso_list:
    k.append(initial_decay_constant(isotope)[1])
    IV_y.append(initial_decay_constant(isotope)[0])
solution = solve_ivp(decay_function, time, IV_y, t_eval=time_solutions,args=(k), dense_output = True)
#uses the scipy.integrate function to calcule the ODE for each isotope


#array of colors to correspond with each isotope in the isotopes list
colours = ['darkorange', 'darkorange']

#for loop to plot the ODE for each isotope for the given time interval
for answer, color in zip(solution.y, colours):
    plot.plot(solution.t, answer, color, linestyle ='-', marker = '.')

#specifies the font and titles of the x and y labels
font = {'family': 'arial', 'color': 'black', 'weight': 'normal', 'size': 12,}
plot.xlabel('Time (years)', fontdict = font, labelpad=8)
plot.ylabel('Number of Atoms', fontdict=font, labelpad=8)

#specifies the information for the legend (corresponding isotope)
labels = ['Mn-54']
plot.legend(labels, ncol=1, edgecolor='black', loc='best')
plot.tick_params(axis="both",direction="in")

#displays the plot and saves it as a .png file
plot.show()
plot.savefig('Activity_Plot_Mn54.png', dpi=300)
