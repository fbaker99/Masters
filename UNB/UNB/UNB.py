'''
Created on Nov. 4, 2022

@author: Fiona

'''

'''
Created on Nov. 3, 2021

@author: olgap
'''

from scipy.integrate import solve_ivp
import radioactivedecay as rd
import numpy as np
from scipy.constants import Avogadro as NA
import matplotlib.pyplot as plot


FLUX = 2e14 * 3600  # n/cm2 h

ABUNDANCEFe58 = 0.00282
ABUNDANCEFe54 = 0.0584
ABUNDANCENi58 = 0.681
ABUNDANCENi62 = 0.0363
ABUNDANCECr50 = 0.0435
ABUNDANCECo59 = 1

iso_list = ['Co-60', 'Co-58'] #'Cr-51', 'Fe-59', 'Fe-55', 'Mn-54', 'Ni-63']
Cobalt = 'Co-59'
Nickel = 'Ni-58'


CROSS_SECTIONCo59 = 3.7E-23 # cm^2
CROSS_SECTIONNi58 = 1.46E-25 # cm^2

CROSS_SECTIONFe58 = 1.14E-24 # cm^2
CROSS_SECTIONFe54 = 2.5E-24 # cm^2
CROSS_SECTIONNi62 = 1.46E-23 # cm^2
CROSS_SECTIONCr50 = 1.59E-23 # cm^2

CoDensity = 8.9 #g/cm^3
NiDensity = 8.902 #g/cm^3



def CobaltProduction(Flux_CO):
    nuc = rd.Nuclide(Cobalt)
    N_atomic = CoDensity * NA * ABUNDANCECo59 / nuc.atomic_mass
    macro_cross_Co = CROSS_SECTIONCo59 * N_atomic
    production_term = Flux_CO * macro_cross_Co * FLUX
    
    return production_term

#def NickelProduction(Flux_NI):
  #  nuc = rd.Nuclide(Nickel)
  #  N_atomic = NiDensity * NA * ABUNDANCENi58 / nuc.atomic_mass
  #  macro_cross_Ni = CROSS_SECTIONNi58 * N_atomic
  #  production_term = Flux_NI * macro_cross_Ni * FLUX
    
  #  return production_term


def initial_val_decay_const(isotope):
    # based on input isotope (iso), calcs decay constant 
    nuc = rd.Nuclide(isotope)
    decay_const = np.log(2) / nuc.half_life('y') 
  
    if isotope == iso_list[0]:
        input_atoms = 0
    else:
        input_atoms = 0     
    N_0_atoms = input_atoms
    
    return N_0_atoms, decay_const


def decay_function(t, y, k1, Flux_CO):
   
    P_Co59 = CobaltProduction(Flux_CO)

    dCo60 = P_Co59 - k1 * y[0]
    return dCo60


#defines a function that returns the inital the number of atoms and the decay constant for each isotope

#uses a for loop to obtain the data at every year for 10 years
time = [0, 10]
time_solutions = []
for i in range(0, 11, 1):
    time_solutions.append(i)
    
#the for loop is used to input the initial decay of each isotope into the empty arrays
IV_y = []
k = []

# For loop used to solve ODEs
for isotope in iso_list:
    k.append(initial_val_decay_const(isotope)[1])
    IV_y.append(initial_val_decay_const(isotope)[0])
solution = solve_ivp(decay_function, time, IV_y, t_eval=time_solutions,args=(k), dense_output = True)
#uses the scipy.integrate function to calcule the ODE for each isotope


#array of colors to correspond with each isotope in the isotopes list
colours = ['mediumslateblue', 'mediumturquoise']

#for loop to plot the ODE for each isotope for the given time interval
for answer, color in zip(solution.y, colours):
    plot.plot(solution.t, answer, color, linestyle ='-', marker = '.')

#specifies the font and titles of the x and y labels
font = {'family': 'arial', 'color': 'black', 'weight': 'normal', 'size': 12,}
plot.xlabel('Time (years)', fontdict = font, labelpad=8)
plot.ylabel('Number of Atoms/cm^3', fontdict=font, labelpad=8)

#specifies the information for the legend (corresponding isotope)
labels = ['Co-60']
plot.legend(labels, ncol=1, edgecolor='black', loc='upper right')
plot.tick_params(axis="both",direction="in")

#displays the plot and saves it as a .png file
plot.show()
plot.savefig('Decay_Plot.png', dpi=300)
