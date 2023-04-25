'''
Created on Mar. 23, 2023

@author: fionabaker
'''

import math

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

    def multiply_by_value(self, value):
        sections = self.separate_by_nodes()
        multiplied_sections = [[section["inlet piping length"] * value, section["inlet piping diameter"] * value, section["inlet piping velocity"] * value] for section in sections]
        return multiplied_sections

#from GID line 23    
diameters = [44.3, 50, 106, 5.68, 5.68, 5.68, 5.68]
velocities = [1530, 1200, 270, 985, 985, 985, 985]
lengths = [477.6, 281.8, 78.6, 350, 350, 350, 350]
nodes = [477.6, 281.8, 78.6, 350, 350, 350, 350]

tube = SteamGenerator(lengths, nodes, diameters, velocities)
sections = tube.separate_by_nodes()
print(sections)

sections_multiplied = tube.multiply_by_value(2)
print(sections_multiplied)


# Constants
HARDNESS_STELLITE = 490  # Vickers hardness number for Stellite
WEAR_COEFFICIENT = 5e-4 #mm/Nm, Wear Characteristic of Stellite 6 Alloy
# Example usage
pressure = 500  # MPa
sliding_distance = 1e-3  # m

#Calculates wear volume of Stellite 6 using Archard equation
def archard_equation_stellite(pressure, sliding_distance):
    wear_volume = (WEAR_COEFFICIENT * pressure * sliding_distance) / HARDNESS_STELLITE
    return wear_volume

wear_volume = archard_equation_stellite(pressure, sliding_distance)
print("Wear volume for Stellite: {:.2e} m^3".format(wear_volume))

#Calculates wear volume of Stellite 6 using Archard equation
# f: wear coefficient
# L: sliding distance
# A: contact area
# N: normal force

f = 5e-4 #mm/Nm, Wear Characteristic of Stellite 6 Alloy
L = 1 # sliding distance in m (length of node)
A = math.pi * (0.02 ** 2) # contact area in m^2 (assuming a cylinder with radius 0.02 m)
N = 15 # normal force in Newtons

def archard_equation(f, L, A, N):
    V = (f * L * A) / N
    return V

V = archard_equation(f, L, A, N)
print("Wear volume for Stellite: {:.2e} m^3 ".format(V))

# Stellite-6 properties
stellite_hardness = 44 # in Rockwell C
stellite_k = 5e-4 # wear coefficient

# Example input values
force = 15 # in Newtons
distance = 0.001 # in meters

# Archard equation for wear volume
def archard_wear_volume(force, distance, hardness, k):
    wear_volume = (k * force * distance) / (hardness ** 2)
    return wear_volume


# Calculate wear volume
wear_volume = archard_wear_volume(force, distance, stellite_hardness, stellite_k)
print(f"Wear volume for Stellite-6: {wear_volume:.2e} cubic meters")

#line 305 & 312 GID
#Fuel_Channel_Diameter = 12*1.3
#Fuel_Channel_length = 49.5*1.3




