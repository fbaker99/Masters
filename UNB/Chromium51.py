'''
Created on Nov. 7, 2022

@author: fionabaker
'''

from scipy.integrate import solve_ivp
import radioactivedecay as rad
import numpy as np
from scipy.constants import Avogadro as NA
import matplotlib.pyplot as plot
import statistics
import scipy.stats as stats


FLUX = 2e14   # n/cm2 s

ABUNDANCECr50 = 0.0435

iso_list = ['Cr-51', 'Cr-51']

Chromium = 'Cr-50'

CROSS_SECTIONCr50 = 1.59E-23 # cm^2

CrDensity = 7.19 #g/cm^3


def ChromiumProduction(Flux_CR):
    nuc = rad.Nuclide(Chromium)
    N_atomic = CrDensity * NA * ABUNDANCECr50 / nuc.atomic_mass
    macro_cross_Cr = CROSS_SECTIONCr50 * N_atomic
    production_term = Flux_CR * macro_cross_Cr * FLUX
    
    return production_term


def initial_decay_constant(isotope):
    #calculates the initial number of atoms (0) and the decay constant 
    nuc = rad.Nuclide(isotope)
    decay_constant = np.log(2) / nuc.half_life('d') 
    N0_atoms = 0
    
    return N0_atoms, decay_constant


def decay_function(t, y, k1, Flux_CR):
   
    P_Cr50 = ChromiumProduction(Flux_CR)

    dCr51 = P_Cr50 - k1 * y[0]
    return dCr51

#defines a function that returns the inital the number of atoms and the decay constant for each isotope
#uses a for loop to obtain the activity every year for 600 days
time = [0, 600]
time_solutions = []
for i in range(0, 601, 1):
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
colours = ['magenta', 'magenta']

#for loop to plot the ODE for each isotope for the given time interval
for answer, color in zip(solution.y, colours):
    plot.plot(solution.t, answer, color, linestyle ='-', marker = '.')

#specifies the font and titles of the x and y labels
font = {'family': 'arial', 'color': 'black', 'weight': 'normal', 'size': 12,}
plot.xlabel('Time (days)', fontdict = font, labelpad=8)
plot.ylabel('Number of Atoms', fontdict=font, labelpad=8)

#specifies the information for the legend (corresponding isotope)
labels = ['Cr-51']
plot.legend(labels, ncol=1, edgecolor='black', loc='best')
plot.tick_params(axis="both",direction="in")

#specifies the error bars
#plot.errorbar(solution.t, solution.y[1], xerr = 1, yerr = 1E11, fmt = '.') 

#displays the plot and saves it as a .png file
plot.show()
plot.savefig('Activity_Plot_Cr51.png', dpi=300)


#stats

#linear fit 
#pearson correlation (correlation coefficient) = r
#Coefficient of Determination = r2
xx = time_solutions
yy = solution.y[1]
r = statistics.correlation(xx, yy)
r2 = r**2

rpb = stats.pointbiserialr(xx, yy)
print(rpb)

print(r)
print(r2)

#standard deviation of the population P
x = np.array([time_solutions])
y = np.array([solution.y[1]])

combined_array = np.vstack((x,y))

std = np.std(combined_array,axis=0)

std = np.std((x,y),axis=0)

print(std)
