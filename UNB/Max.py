'''
Created on Nov. 10, 2022

@author: fionabaker
'''

import math


# Take input of all the elements as a string 
input = input("\nEnter the refracted indices as comma seperated values: ")

# Use map function to wrap-up them and converting to desired data type.
list = list (map(str, input.split()))
print(list)

L = [int(x) for x in input("Enter multiple values\n").split(', ')]
print("\nThe values of input are", L)