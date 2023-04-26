'''
Created on April. 24, 2023

@author: fionabaker
'''

import math
import numpy as np

class SteamGenerator:
    def __init__(self, lengths, nodes, diameters, velocities):
        self.lengths = lengths
        self.nodes = nodes
        self.diameters = diameters
        self.velocities = velocities
    
    def separate_by_nodes(self):
        sections = []
        for node in self.nodes:
            section = {"inlet piping length": self.lengths[self.nodes.index(node)], 
                       "inlet piping diameter": self.diameters[self.nodes.index(node)],
                       "inlet piping velocity": self.velocities[self.nodes.index(node)]}
            sections.append(section)
        return sections

    def diameter_squared(self):       
        sections = self.separate_by_nodes()
        d2 = [section["inlet piping diameter"] * section["inlet piping diameter"] for section in sections]
        return d2
    
    def area(self):
        section = self.diameter_squared()
        area = []
        multiplier = math.pi/4
        for i in section:
            area.append(i*multiplier)
        return area
    

#Function that calculate sthe Archard Equation
def archard_equation(k, L, A, F):
    V = []
    tube = SteamGenerator(lengths, nodes, diameters, velocities)
    for A in tube.area():
        V.append(k * A * L / F)
    return (V)

#Function that calculate sthe Archard Equation
def archard(k, D, H, F):
    W = []
    tube = SteamGenerator(lengths, nodes, diameters, velocities)
    for D in tube.nodes:
        W.append(F * k * D / H)
    return W

#from GID line 23    
diameters = [44.3, 50, 106, 5.68, 5.68, 5.68, 5.68]
velocities = [1530, 1200, 270, 985, 985, 985, 985]
lengths = [477.6, 281.8, 78.6, 350, 350, 350, 350]
nodes = [477.6, 281.8, 78.6, 350, 350, 350, 350]

#Archard Constants
k = 5e-4 #mm/Nm, Wear Characteristic of Stellite 6 Alloy
L = 1 # sliding distance in m (length of node)
F = 15 # normal force in Newtons
tube = SteamGenerator(lengths, nodes, diameters, velocities)
A = tube.area()

D = tube.nodes #distance of each node (sliding distance)
H = 490 # Vickers hardness

print(D)

print(A)
V = archard_equation(k, L, A, F)
print(V)

W = archard(k, D, H, F)
print(W)

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



