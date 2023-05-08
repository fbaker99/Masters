'''
Created on May. 4, 2023

@author: fionabaker
'''

import math
import matplotlib.pyplot as plot

class Section():
    def __init__(self):
        self.NodeNumber = None
        self.Diameter = None
        self.Velocity = None
        self.Length = None
        self.Distance = None 

def diameter_squared(section):
    d2 = [d**2 for d in section.Diameter]
    return d2

def area(section):
    section_d2 = diameter_squared(section)
    area = []
    multiplier = math.pi/4
    for i in section_d2:
        area.append(i*multiplier)
    return area

InletFeeder = Section()
InletFeeder_2 = Section()
FuelChannel = Section()
FuelChannel_2 = Section()
OutletFeeder = Section()
OutletFeeder_2 = Section()

SteamGenerator = [Section() for each in range(87)]
SteamGenerator_2 = [Section() for each in range(87)]
SteamGenerator_3 = [Section() for each in range(87)]
SteamGenerator_4 = [Section() for each in range(87)]

InletSections = [InletFeeder, InletFeeder_2]
OutletSections = [OutletFeeder, OutletFeeder_2]
FuelSections = [FuelChannel, FuelChannel_2]

SteamGeneratorSections = [
    SteamGenerator, SteamGenerator_2, SteamGenerator_3, SteamGenerator_4
    ]

for InletPiping in InletSections:
    InletPiping.NodeNumber = 7
    InletPiping.Diameter = [44.3, 50, 106, 5.68, 5.68, 5.68, 5.68]
    InletPiping.Velocity = [1530, 1200, 270, 985, 985, 985, 985]
    InletPiping.Length = [477.6, 281.8, 78.6, 350, 350, 350, 350]
    
for Channel in FuelSections:
    Channel.NodeNumber = 12
    Channel.Diameter = [1.3] * Channel.NodeNumber
    Channel.Velocity = [
        883.08, 890.66, 900.3, 910.64, 920.97, 932.68, 945.08, 958.17, 973.32,
         989.16, 1073.89, 1250.92
        ]
    Channel.Length = [49.5] * Channel.NodeNumber
    
for OutletPiping in OutletSections: 
    OutletPiping.NodeNumber = 9   
    OutletPiping.Velocity = [1619, 1619, 1619, 1619, 857, 857, 857, 306, 1250]
    OutletPiping.Length = [17, 3.5, 139.5, 432, 225.5, 460.3, 460.3, 400, 100]
    OutletPiping.Diameter = [6.4, 6.4, 6.4, 6.4, 8.9, 8.9, 8.9, 116, 40.8]

#archard fuction with a chance in sliding distance
#can change the output to be sliding velocity to get wear rate
def archard(k, D, H, F):
    W = []
    for Distance in D:
        W.append(F * k * Distance / H)
    return W

#archard fuction with a chance in area and sliding distance
def archard_eqn(A, L, F, k):
    WV = [A_i * L_i * (k / F) for A_i, L_i in zip(A, L)]
    return WV

#Archard Constants
k = 5e-4 #mm/Nm, Wear Characteristic of Stellite 6 Alloy
L = 1 # sliding distance in m (length of node)
F = 15 # normal force in Newtons
H = 490 # Vickers hardness

# Calls the archard function with the required arguments 
#can be changed using inlet feeder, steam generator, fuel channel properties
W = archard(k, OutletFeeder.Length, H, F)
print(W)

#Calls the archard function with the required arguments
WV = archard_eqn(area(OutletFeeder), OutletFeeder.Length, F, k)
print(WV)

y1 = W
y2 = WV

# Plot the lists with different colors
plot.plot(y1, color='blue')
plot.plot(y2, color='red')

# Customize the plot with title, labels, and legend
plot.title('Wear of Stellite 6')
plot.xlabel('node #')
plot.ylabel('wear[m^3]')
plot.legend(['sliding distance', 'sliding distance and area'])

# Show the plot
plot.show()
