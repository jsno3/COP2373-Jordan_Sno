
from math import cos, radians


def get_hypotenuse(dist, angle):
    return dist/cos(radians(angle))


def main():
    while True:
        d = float(input("Please enter the adjacent side's length (0 to exit): "))
        while d < 0:
            print("The length of the adjacent side must be greater than zero")
            d = float(input("Please enter the adjacent side's length (0 to exit): "))
        if d == 0:
            print('Bye, Bye!')
            break
        a = float(input('Please enter the nearest angle: '))
        while a <= 0.0 or a >= 90:
            print("The nearest angle must be between 0 and 90 degrees.")
            a = float(input('Please enter the nearest angle: '))
        print('The Hypotenuse is', get_hypotenuse(d, a))


main()
