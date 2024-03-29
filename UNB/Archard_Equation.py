'''
Created on April. 24, 2023

@author: fionabaker
'''

import math
import matplotlib.pyplot as plot

#class function to call properties from the PHTS including velocity, diameter, and length of each node
class SteamGenerator:
    def __init__(self, lengths, nodes, diameters, velocities):
        self.lengths = lengths
        self.nodes = nodes
        self.diameters = diameters
        self.velocities = velocities

#this funcion seperates the class into nodes    
    def separate_by_nodes(self):
        sections = []
        for node in self.nodes:
            section = {"inlet piping length": self.lengths[self.nodes.index(node)], 
                       "inlet piping diameter": self.diameters[self.nodes.index(node)],
                       "inlet piping velocity": self.velocities[self.nodes.index(node)]}
            sections.append(section)
        return sections

#this function calculates the diameter squared for each node
    def diameter_squared(self):       
        sections = self.separate_by_nodes()
        d2 = [section["inlet piping diameter"] * section["inlet piping diameter"] for section in sections]
        return d2
 
#this function calculates the area at each node   
    def area(self):
        section = self.diameter_squared()
        area = []
        multiplier = math.pi/4
        for i in section:
            area.append(i*multiplier)
        return area

#Function that calculates the Archard Equation using a change in sliding dstance 
def archard(k, D, H, F):
    W = []
    tube = SteamGenerator(lengths, nodes, diameters, velocities)
    for D in tube.nodes:
        W.append(F * k * D / H)
    return W

def archard_rate(k, V, H, F):
    WR = []
    tube = SteamGenerator(lengths, nodes, diameters, velocities)
    for V in tube.velocities:
        WR.append(F * k * V / H)
    return WR

#Function that calculates the Archard Equation using a change in area and sliding distance
def archard_eqn(A, D, k, F):
    WV = [A * D * k / F for A, D in zip(A, D)]
    return WV

#Function that calculate sthe Archard Equation using a change in area and constant distance (length of node)
def archard_equation(k, L, A, F):
    V = []
    tube = SteamGenerator(lengths, nodes, diameters, velocities)
    for A in tube.area():
        V.append(k * A * L / F)
    return (V)


#from GID line 23    
diameters = [44.3, 50, 106, 5.68, 5.68, 5.68, 5.68]
velocities = [1530, 1200, 270, 985, 985, 985, 985]
lengths = [477.6, 281.8, 78.6, 350, 350, 350, 350]
nodes = [477.6, 281.8, 78.6, 350, 350, 350, 350]

#Archard Constants
k = 5e-4 #mm/Nm, Wear Characteristic of Stellite 6 Alloy
L = 1 # sliding distance in m (length of node)
F = 15 # normal force in Newtons
H = 490 # Vickers hardness

tube = SteamGenerator(lengths, nodes, diameters, velocities)
A = tube.area()
print(A)

D = tube.nodes #distance of each node (sliding distance)
print(D)

V = archard_equation(k, L, A, F)
print(V)

W = archard(k, D, H, F)
print(W)

WR = archard_rate(k, V, H, F)
print(WR)

WV = archard_eqn(A, D, k, F)
print(WV)

#tube = SteamGenerator(lengths, nodes, diameters, velocities)
#sections = tube.separate_by_nodes()
#print(sections)

#tube1 = SteamGenerator(lengths, nodes, diameters, velocities)
#section1 = tube1.diameter_squared()
#print(section1)

#tube2 = SteamGenerator(lengths, nodes, diameters, velocities)
#section2 = tube2.area()
#print(section2)

#line 305 & 312 GID
#Fuel_Channel_Diameter = 12*1.3
#Fuel_Channel_length = 49.5*1.3

# example data
#x = [1, 2, 3, 4, 5, 6, 7]
#y1 = V
#y2 = W
#y3 = WV

# plot the lists
#plot.plot(x, y1, label='sliding distance')
#plot.plot(x, y2, label='area')
#plot.plot(x, y3, label='sliding distance and area')

# add labels and legend
#plot.xlabel('node #')
#plot.ylabel('Cobalt Wear [m^3]')
#plot.title('Cobalt Wear')
#plot.legend()

# show the plot
#plot.show()


# Define your lists
# example data
y1 = V
y2 = W
y3 = WR
y4 = WV

# Plot the lists with different colors
plot.plot(y1, color='blue')
plot.plot(y2, color='black')
plot.plot(y3, color='red')
plot.plot(y4, color='yellow')

# Customize the plot with title, labels, and legend
plot.title('Wear of Stellite 6')
plot.xlabel('node #')
plot.ylabel('wear[m^3]')
plot.legend(['sliding distance', 'area', 'sliding distance and area'])

# Show the plot
plot.show()
