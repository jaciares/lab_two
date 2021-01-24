"""
    Filename: lab_two.py
    Course: SDEV 300
    Author: John Aciares
    Program Purpose: lab_two.py is a menu-driven python application that can
    generate a secure password, calculate and format a percentage, count
    how many days from 'today' until July 4, 2025, and can calculate the
    volume of a right circular cylinder.


"""
import sys


def generate_secure_pwd():
    pass


def calc_and_form_percentage():
    pass


def how_many_days():
    pass


def calc_law_cosines():
    pass


def calc_volume_cylinder():
    pass


def menu():
    print('*' * 90)
    print('Welcome to the Python SDEV300 Lab 2 Application.')

    # User input
    user_selection = input("""
    What would you like to do today?
    a. Generate a Secure Password
    b. Calculate and format a percentage
    c. How many days from today until July 4, 2025?
    d. Use the Law of Cosines to calculate the leg of a triangle
    e. Calculate the volume of a Right Circular Cylinder
    f. Exit Program
    
    Enter selection: """)

    if user_selection == 'a':
        generate_secure_pwd()
    elif user_selection == 'b':
        calc_and_form_percentage()
    elif user_selection == 'c':
        how_many_days()
    elif user_selection == 'd':
        calc_law_cosines()
    elif user_selection == 'e':
        calc_volume_cylinder()
    elif user_selection == 'f':
        sys.exit()
    else:
        print("You must enter a valid selection!")
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()
