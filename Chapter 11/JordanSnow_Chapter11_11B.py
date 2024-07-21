""" This program is intended to determine the length of the hypotenuse of a right triangle,
given two pieces of information from the user: the nearest angle, measured in degrees,
and the length of the adjacent side.
"""

# Import cos & radians, from math
from math import cos, radians

# Define 'get_hypotenuse' passing in 'dist' and 'angle'
def get_hypotenuse(dist, angle):

    # Return algorithm that uses cosine to determine the length of the hypotenuse
    return dist/cos(radians(angle))

# Define main
def main():

    # While loop to continue program until the user enters '0'
    while True:

        # Set variable 'd' equal to the input from the user for the adjacent side's length (converted to a float)
        d = float(input('Please enter the adjacent side's length (0 to exit): '))

        # While loop to ensure that the size of the nearest angle is larger than zero
        while d < 0:

            # Print statement to inform user the length of the adjacent side needs to be greater than zero
            print('The length of the adjacent side must be greater than zero')

            # Set variable d equal to the input of the user for the adjacent side's length (converted to a float)
            d = float(input('Please enter the adjacent side's length (0 to exit): '))

        # If statement - if d is equal to 0:
        if d == 0:

            # Print statement to say goodbye
            print('Bye, Bye!')

            # Break to end program
            break

        # Set variable 'a' equal to the input from the user for the nearest angle (converted to a float)
        a = float(input('Please enter the nearest angle: '))

        # While loop to ensure that the value of 'a' is greater than 0 or less than 90
        while a <= 0.0 or a >= 90:

            # Print statement to inform user the value of the nearest angle must be between 0 and 90 degrees
            print('The nearest angle must be between 0 and 90 degrees.')

            # Set variable 'a' equal to the input from the user for the nearest angle (converted to a float)
            a = float(input('Please enter the nearest angle: '))

        # Print statement
        print('The Hypotenuse is', get_hypotenuse(d, a))


# Call main
main()
