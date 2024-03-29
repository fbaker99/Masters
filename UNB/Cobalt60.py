'''
Created on Nov. 8, 2022

@author: fionabaker
'''

from scipy.integrate import solve_ivp
import radioactivedecay as rad
import numpy as np
from scipy.constants import Avogadro as NA
import matplotlib.pyplot as plot

FLUX = 2e14  # n/cm2 s

ABUNDANCECo59 = 1

#the first elemment in the list will hold the intial decay consant at t = 0
iso_list = ['Co-60', 'Co-60']

Cobalt = 'Co-59'

CROSS_SECTIONCo59 = 3.7E-23 # cm^2

CoDensity = 8.9 #g/cm^3

#defines a function that calulates the production term
def CobaltProduction(Flux_CO):
    nuc = rad.Nuclide(Cobalt)
    N_atomic = CoDensity * NA * ABUNDANCECo59 / nuc.atomic_mass
    macro_cross_Co = CROSS_SECTIONCo59 * N_atomic
    production_term = Flux_CO * macro_cross_Co * FLUX
    
    return production_term


#defines a function that returns the inital the number of atoms and the decay constant for each isotope
def initial_decay_constant(isotope):
    nuc = rad.Nuclide(isotope)
    decay_constant = np.log(2) / nuc.half_life('y') 
    N0_atoms = 0
    
    return N0_atoms, decay_constant


def decay_function(t, y, k1, Flux_CO):
   
    P_Co59 = CobaltProduction(Flux_CO)

    dCo60 = P_Co59 - k1 * y[0]
    return dCo60


#uses a for loop to obtain the activity every year for 40 years
time = [0, 40]
time_solutions = []
for i in range(0, 41, 1):
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

#prints the ODE solution
print('Solution to the ODE, Co-60:', np.array(solution.y[1]))

#array of colors to correspond with each isotope in the isotopes list
colours = ['darkviolet', 'darkviolet']

#for loop to plot the ODE for each isotope for the given time interval
for answer, color in zip(solution.y, colours):
    plot.plot(solution.t, answer, color, linestyle ='-', marker = '.')

#specifies the font and titles of the x and y labels
font = {'family': 'arial', 'color': 'black', 'weight': 'normal', 'size': 12,}
plot.xlabel('Time (years)', fontdict = font, labelpad=8)
plot.ylabel('Number of Atoms', fontdict=font, labelpad=8)

#specifies the information for the legend (corresponding isotope)
labels = ['Co-60']
plot.legend(labels, ncol=1, edgecolor='black', loc='best')
plot.tick_params(axis="both",direction="in")


#displays the plot and saves it as a .png file
plot.show()
plot.savefig('Activity_Plot_Co60.png', dpi=300)
