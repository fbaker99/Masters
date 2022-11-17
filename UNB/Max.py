'''
Created on Nov. 10, 2022

@author: fionabaker
'''


 #Read closely what Part 2 is asking for. Write a function that takes the following variables as arguments:
#xt = target bullseye’s x position (m) 
#yt = target bullseye’s y position (m) 
#V0 = arrow’s initial velocity (m/s) 
#q = arrow’s angle when fired (°) 
#x0 (=0m), 
#y0 (=1m) 
#g (=9.8m/s2), 
#and t (=0.5s) 
#are not required as parameters as they will be constants. 
#This function should return the distance between where the arrow is after 0.5 seconds and the bullseye of the target. 
#Notes:
# • The arrow cannot go below 0m (cannot go into the virtual ground). 
# This means that if the y-value of the arrow is negative, it must be calculated at 0. 
#• Assume that targets are not solid and that an arrow can pass through them with no resistance. 
#• Alongside returning the distance, this function should also print the end location of the arrow (x and y coordinates). 
#• Should test this function before continuing with the rest of the project 

import math

x0 = 0 #m 
y0 = 1 #m 
g = 9.8 #m/s2) 
t = 0.5 #s 
Vf = 0 #m/s

#xt = 75


print(math.cos(2))
print()

def bullseye(xt, yt, V0, q):
    V0x = V0*math.cos(q)
    V0y = V0*math.sin(q)
    xt = x0 + t*V0x 
    yt = y0 + t*V0y + (1/2)*g*(t**2)
    return xt, yt

print(bullseye(75,3.015,150,2))

Work = 0.9*1.148*1000*(1-(0.1**((1.334-1)/1.334)))

Wcompressor = (1.004*(293)*(1-(10**((0.714-1)/.714))))/0.87

T2 = 293*((1+(1/0.87))*(10**((1.4-1)/1.4)-1))
print(T2)

y = 0.4365+(33-30)*(0.5050-0.4365)/(5)
print(y)

y0 = 0.4365+(5-4.2455)*(0.5050-0.4365)/(5.6267-4.2455)
print(y0)

y2 = 7.8461+(33-30)*(8.0148-7.8461)/(5)
print(y2)

y3 = 7.8461+(5-4.2455)*(8.0148-7.8461)/(5.6267-4.2455)
print(y3)