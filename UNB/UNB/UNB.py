'''
Created on May 13, 2022

@author: fbaker
'''
while True:
    user_input = str(input('Say "Hello"'))
    if user_input == 'Hello':
        print('Goodbye')
        break
    else:
        print('This input is invalid. Please say "Hello"')