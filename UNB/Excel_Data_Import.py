'''
Created on Nov. 7, 2022

@author: fionabaker
'''

#this module plots all the activities
#this module obtains the ODE data and exports it to an excel file

import Cobalt60 as Co60
import Cobalt58 as Co58
import Iron59 as Fe59
import Iron55 as Fe55
import Manganese54 as Mn54
import Chromium51 as Cr51
import Nickel63 as Ni63

import numpy as np
import pandas as pd


Co60_Column1 = 'time'
Co60_Column2 = 'Co-60 Activity'
Co60_data = pd.DataFrame({Co60_Column1:np.array(Co60.time_solutions), Co60_Column2:np.array(Co60.solution.y[1])})

Co58_Column1 = 'time' 
Co58_Column2 = 'Co-58 Activity'
Co58_data = pd.DataFrame({Co58_Column1:np.array(Co58.time_solutions), Co58_Column2:np.array(Co58.solution.y[1])})

Fe59_Column1 = 'time' 
Fe59_Column2 = 'Fe-59 Activity'
Fe59_data = pd.DataFrame({Fe59_Column1:np.array(Fe59.time_solutions), Fe59_Column2:np.array(Fe59.solution.y[1])})

Fe55_Column1 = 'time' 
Fe55_Column2 = 'Fe-55 Activity'
Fe55_data = pd.DataFrame({Fe55_Column1:np.array(Fe55.time_solutions), Fe55_Column2:np.array(Fe55.solution.y[1])})

Mn54_Column1 = 'time' 
Mn54_Column2 = 'Mn54 Activity'
Mn54_data = pd.DataFrame({Mn54_Column1:np.array(Mn54.time_solutions), Mn54_Column2:np.array(Mn54.solution.y[1])})

Cr51_Column1 = 'time' 
Cr51_Column2 = 'Cr51 Activity'
Cr51_data = pd.DataFrame({Cr51_Column1:np.array(Cr51.time_solutions), Cr51_Column2:np.array(Cr51.solution.y[1])})

Ni63_Column1 = 'time' 
Ni63_Column2 = 'Ni63 Activity'
Ni63_data = pd.DataFrame({Ni63_Column1:np.array(Ni63.time_solutions), Ni63_Column2:np.array(Ni63.solution.y[1])})


with pd.ExcelWriter('Activity.xlsx') as writer:
    Co60_data.to_excel(writer, sheet_name='Co60', index=False)
    Co58_data.to_excel(writer, sheet_name='Co58', index=False)
    Fe59_data.to_excel(writer, sheet_name='Fe59', index=False)
    Fe55_data.to_excel(writer, sheet_name='Fe55', index=False)
    Mn54_data.to_excel(writer, sheet_name='Mn54', index=False)
    Cr51_data.to_excel(writer, sheet_name='Cr51', index=False)
    Ni63_data.to_excel(writer, sheet_name='Ni63', index=False)
    

    


