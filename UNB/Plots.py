'''
Created on Nov. 7, 2022

@author: fionabaker
'''


import Cobalt60
import Cobalt58

import matplotlib.pyplot as plot

t = linspace(0, 2*math.pi, 400)
a = sin(t)
b = cos(t)
c = a + b


plot.plot(t, b, 'b')
plot.plot(t, c, 'g') 
plot.show()