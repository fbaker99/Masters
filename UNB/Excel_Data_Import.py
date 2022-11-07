'''
Created on Nov. 7, 2022

@author: fionabaker
'''

import Cobalt60 as Co60
import Cobalt58 as Co58

import numpy as np
import pandas as pd



Co60_data = pd.DataFrame(np.array(Co60.time_solutions),np.array(Co60.solution.y[1]))
#Co60_time_data = np.array(Co60.time_solutions)
Co60_Column = ['time', 'Co-60 Activity']
#Co60_data = pd.DataFrame({Co60_Column1:Co60_time_data,Co60_Column2:Co60_activity_data})
Co60_data.to_excel('Activity.xlsx', sheet_name='Co60')#index=False)

Co58_data = pd.DataFrame(np.array(Co58.time_solutions),np.array(Co58.solution.y[1]))
#Co60_time_data = np.array(Co60.time_solutions)
Co58_Column = ['time', 'Co-58 Activity']
#Co60_data = pd.DataFrame({Co60_Column1:Co60_time_data,Co60_Column2:Co60_activity_data})
Co58_data.to_excel('Activity.xlsx', sheet_name='Co58')#index=False)

with pd.ExcelWriter('Activity.xlsx') as writer:
    Co60_data.to_excel(writer, sheet_name='Co60')
    Co58_data.to_excel(writer, sheet_name='Co58')

#Co60_data.to_excel('Activity.xlsx', engine='xlsxwriter') 
