'''
Created on May 16, 2022

@author: fbaker
'''
'''
Created on Nov. 3, 2021

@author: olgap
'''

from scipy.integrate import solve_ivp
import radioactivedecay as rd
import numpy as np
from scipy.constants import Avogadro as NA
import matplotlib.pyplot as plt

# this wasn't in the Background Reading, but is a nice way to set all the
# plot axis and label font face and font size all in one fell swoop
from matplotlib import rcParams
rcParams['font.family'] = 'arial'
rcParams['font.size'] = 12

FLUX_list = [2e14, 4e14]  # n/cm2 s
FLUX_list = [i* 3600 for i in FLUX_list] # n/cm2 h
abund_U235 = 0.719/100
YIELD_Sm149 = .0108 # fraction
YIELD_I135 = 0.061
YIELD_Xe135 = 0.003

iso_list = ['Pm-149', 'Sm-149']
fuel_iso = 'U-235'

posion='Xe'

def fission_rate_U(Flux_n):
    nuc = rd.Nuclide(fuel_iso)
    sigma_f = 587 # b
    sigma_f_cm2 = sigma_f * 10 ** (-24)
    
    N_atomic = 19.1 * NA * abund_U235 / nuc.atomic_mass
    
    macro_cross_f = sigma_f_cm2 * N_atomic
    
    production_term = Flux_n * macro_cross_f
    
    return production_term


def burnup_rate(Flux_n):
    
    fuel_iso = iso_list[1]
    # nuc = rd.Nuclide(fuel_iso)
    sigma_a = 41000 # b
    sigma_a_cm2 = sigma_a * 10 ** (-24)
    burnup_term = Flux_n * sigma_a_cm2
    
    return burnup_term


def initial_val_decay_const(iso):
    # based on input isotope (iso), calcs decay constant 
    
    nuc = rd.Nuclide(iso)
    decay_const= np.log(2) / nuc.half_life('h') 
  
    if iso == iso_list[0]:
        input_atoms = 0
    else:
        input_atoms = 0     
    N_0_atoms = input_atoms
    
    return N_0_atoms, decay_const


def decay_functs(t, y, k1, FP_yield, Flux_n):
   
    P1= fission_rate_U(Flux_n) * FP_yield
    BurnUp = burnup_rate(Flux_n)
    
    dy0 = P1 - k1 * y[0]
    dy1 = k1 * y[0] - BurnUp * y[1]

    dy = [dy0, dy1]
    
    return dy


def solutions_and_plots(iso_list, t_input, FP_yield):
    
    overalltime_range = [0, 500]
    initialvalues_y_0 = []
    prod_consump_terms = []

    # Create the time samples for the output of the ODE solver.
    # I use a large number of points, only because I want to make
    # a plot of the solution that looks nice.
    t_eval = []
    for i in range(0, 500, 20):
        t_eval.append(i)
        
    t_eval = t_eval
    labels = []
    for iso in iso_list:
        initialvalues_y_0.append(initial_val_decay_const(iso)[0])
    
    prod_consump_terms.append(initial_val_decay_const(iso_list[0])[1])
    prod_consump_terms.append(FP_yield)
    
    colours_Sm = ['navy', 'mediumvioletred', 'lightcoral', 'lightgreen']
    colours2_Pm = ['blue', 'magenta', 'salmon', 'forestgreen']
    
    for colr, colr2, flux in zip(colours_Sm, colours2_Pm, FLUX_list):
        
        if flux == FLUX_list[0]:
            prod_consump_terms.append(flux)
        else:
            prod_consump_terms.pop()
            prod_consump_terms.append(flux)
        
        sol = solve_ivp(
            decay_functs, overalltime_range, initialvalues_y_0, t_eval=t_eval, 
            args=(prod_consump_terms), dense_output = True
            )
    
        if len(FLUX_list) > 1:
            if len(FLUX_list) == 2:
                labels.append(iso_list[0] + ' ' + str(flux) + 
                              ' n/(cm$^2$h)'
                              )
                labels.append(iso_list[1] + ' ' + str(flux) + 
                              ' n/(cm$^2$h)'
                              )
            
            else:
                labels.append(str(flux) + ' n/(cm$^2$h)')
        else:
            labels.append(iso_list[0])
            labels.append(iso_list[1])
            
        if len(FLUX_list) <= 2:
            plt.plot(
                t_eval, sol.y[0], color = colr2, linestyle ='-', marker = '.'
                )
        else:
            None
            
        # always want Sm-149 concentration
        plt.plot(t_eval, sol.y[1], color = colr, linestyle ='--', marker = '.')
        
    
    # could instead call individually, but loop above is better
    # plt.plot(t_eval, sol.y[0])
    # plt.plot(t_eval, sol.y[1])
    
    plt.xlabel('Time (h)', labelpad=8)
    if len(FLUX_list) > 2:
        plt.ylim(0, 8e16)
        plt.ylabel('Number of Atoms of Sm-149 per cm$^3$', labelpad=8)
        ncols = 2
    else:
        plt.ylim(0, 5e17)
        plt.ylabel('Number of Atoms per cm$^3$', labelpad=8)
        ncols = 2
        
    plt.legend(
        labels, ncol=ncols, edgecolor='black', loc='upper center', fontsize=11
        )
    plt.tick_params(axis="both",direction="in")
    plt.show()
    # plt.savefig('SmEqm_multiflux_2fluxes.png', dpi=300)
    
    return sol.sol(t_input)

solutions_and_plots(
    iso_list, t_input=168*3, FP_yield=YIELD_Sm149
    )
