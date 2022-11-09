'''
Created on Nov. 7, 2022

@author: fionabaker
'''

from scipy.integrate import solve_ivp
import radioactivedecay as rad
import numpy as np
from scipy.constants import Avogadro as NA
import matplotlib.pyplot as plot


FLUX = 2e14  # n/cm2 s

ABUNDANCENi62 = 0.0363

iso_list = ['Ni-63', 'Ni-63']

Nickel = 'Ni-62'

CROSS_SECTIONNi62 = 1.46E-23 # cm^2

NiDensity = 8.902 #g/cm^3


def NickelProduction(Flux_NI):
    nuc = rad.Nuclide(Nickel)
    N_atomic = NiDensity * NA * ABUNDANCENi62 / nuc.atomic_mass
    macro_cross_Ni = CROSS_SECTIONNi62 * N_atomic
    production_term = Flux_NI * macro_cross_Ni * FLUX
    
    return production_term


def initial_decay_constant(isotope):
    #calculates the initial number of atoms (0) and the decay constant 
    nuc = rad.Nuclide(isotope)
    decay_constant = np.log(2) / nuc.half_life('y')    
    N0_atoms = 0
    
    return N0_atoms, decay_constant

def decay_function(t, y, k1, Flux_NI):
   
    P_Ni62 = NickelProduction(Flux_NI)

    dNi63 = P_Ni62 - k1 * y[0]
    return dNi63


#defines a function that returns the inital the number of atoms and the decay constant for each isotope
#uses a for loop to obtain the activity every year for 800 years
time = [0, 800]
time_solutions = []
for i in range(0, 801, 1):
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
colours = ['maroon', 'maroon']

#for loop to plot the ODE for each isotope for the given time interval
for answer, color in zip(solution.y, colours):
    plot.plot(solution.t, answer, color, linestyle ='-', marker = '.')

#specifies the font and titles of the x and y labels
font = {'family': 'arial', 'color': 'black', 'weight': 'normal', 'size': 12,}
plot.xlabel('Time (years)', fontdict = font, labelpad=8)
plot.ylabel('Number of Atoms', fontdict=font, labelpad=8)

#specifies the information for the legend (corresponding isotope)
labels = ['Ni-63']
plot.legend(labels, ncol=1, edgecolor='black', loc='best')
plot.tick_params(axis="both",direction="in")

#displays the plot and saves it as a .png file
plot.show()
plot.savefig('Activity_Plot_Ni63.png', dpi=300)
