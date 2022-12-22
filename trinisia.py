import math

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: length * width == Area

def footage(length,width):
    
#ask users to imput length and width of home in float so that values can also have decimals:
    # length = float(input('What is the length of your home? '))
    # width = float(input('What is the width of your home? '))
#set an equation that multiplies both values to find area
    area = length * width
    print(f'The square footage of your home is {area} square feet.')
    return area

# footage (5,4)


# 2) Has a function to calculate the circumference of a circle

def circumference(radius):

#ask user to imput radius of circle:
    # radius = float(input('Input circumference of circle here: '))
#use math. to use pi value in math module:
    circle = 2 * math.pi * radius
    print(f'The circumference of your circle is: {circle}')
    return circle

# circumference()

##### ***** PLEASE SEE MODULE ****** #####

#combining the two using user input to select calculation type:

def which_one ():
    equation = input('What can I help you calculate today? ')
    if equation.lower() == "squarefootage":
        length = float(input('What is the length of your home? '))
        width = float(input('What is the width of your home? '))
        area = length * width
        print(f'The square footage of your home is {area} square feet.')
    elif equation.lower() == "circumference":
        radius = float(input('Input circumference of circle here: '))
        circle = 2 * math.pi * radius
        print(f'The circumference of your circle is: {circle}')
    else:
        print('Unfortunately, I am not programmed to calculate that.')
    return

which_one()