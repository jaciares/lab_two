"""
    Filename: lab_two.py
    Course: SDEV 300
    Author: John Aciares
    Program Purpose: lab_two.py is a menu-driven python application that can
    generate a secure password, calculate and format a percentage, count
    how many days from 'today' until July 4, 2025, and can calculate the
    volume of a right circular cylinder.


"""
import datetime
import math
import random
import string
import sys


def error_int_message():
    """
    error_int_message() prints the error message:
    Please enter a positive integer
    :return: None
    """
    print('\tPlease enter a positive integer. ')


def generate_secure_pwd(length, num_of_upper, num_of_lower,
                        num_of_digit, num_of_special):
    """
    Generates a secure password based on defined password requirements
    :param: secure_password
    :return:
    """
    while True:
        try:
            length = int(input('\tHow long should the password be? '))
            if length <= 0:
                error_int_message()
                continue

        except ValueError:
            error_int_message()
            continue
        else:
            break

    while True:
        try:
            num_of_upper = int(input
                               ('\tMinimum number of upper case characters? '))
            if num_of_upper <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    while True:
        try:
            num_of_lower = int(input('\tMinimum number of lower case '
                                     'characters? '))
            if num_of_lower <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    while True:
        try:
            num_of_digit = int(input('\tMinimum number of digit characters? '))
            if num_of_digit <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    while True:
        try:
            num_of_special = int(input('\tMinimum number of special '
                                       'characters? '))
            if num_of_special <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    # Defining String data type
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation

    # Putting together the number of string types into secure_pwd.
    secure_pwd = lowercase * num_of_lower + uppercase * num_of_upper \
                 + numbers * num_of_digit + special_chars * num_of_special

    user_password = random.sample(secure_pwd, length)

    password = ''.join(user_password)

    # Output to user their generated password.
    print('*' * 90)
    print(' Password Generated: ' + str(password))

    # Send user back to beginning of menu.
    menu()


def calc_and_format_percentage(numerator, denominator, precision):
    """
    calc_and_format_percentage takes three parameters in order to calculate
    and format a percentage.

    :param numerator:
    :param denominator:
    :param precision:
    :return: Null
    """
    while True:
        try:
            numerator = int(input('\tEnter a positive integer numerator: '))
            if numerator <= 0:
                error_int_message()
                continue

        except ValueError:
            error_int_message()
            continue
        else:
            break

    while True:
        try:
            denominator = int(input('\tEnter a positive denominator: '))
            if denominator <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    while True:
        try:
            precision = int(input('\tEnter a positive integer float '
                                  'precision: '))
            if precision <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    # Calculating percentage.
    percentage_calc = (numerator / denominator) * 100

    # Formatting percentage_calc with 'precision' argument.
    formatted_percentage_calc = \
        'a = {0:.{1}f}'.format(percentage_calc, precision)

    # Output to user the calculated percentage.
    print('\n\n' + '*' * 90)
    print(str(numerator) + ' / ' + str(denominator) + ' yields ' +
          str(formatted_percentage_calc) + ' percent')
    menu()


def how_many_days():
    """
    how_many_days() gets the current date and time from the user's system.
    Then calculates how many days it will take from current_time to
    future_date.

    :return: None
    """
    # Creating object current_time
    current_time = datetime.datetime.now()

    future_date = datetime.datetime(2025, 7, 4)

    calc_how_many_days = future_date - current_time

    print('\n\n' + '*' * 90)
    print(str(calc_how_many_days.days) + ' days until target date '
          + 'Fri Jul 04, 2025')

    # Send user back to the beginning of the menu.
    menu()


def calc_law_cosines(a_to_c_length, c_to_b_length, angle_of_c):
    """
    calc_law_cosines() uses the law of cosines formula (leg_of_triangle) to
    calculate the leg of a triangle based on parameters.

    :param a_to_c_length:
    :param c_to_b_length:
    :param angle_of_c:
    :return: None
    """
    while True:
        try:
            a_to_c_length = int(input('\tEnter a positive integer for line a '
                                      '<-> c length: '))
            if a_to_c_length <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    while True:
        try:
            c_to_b_length = int(input('\tEnter a positive integer for line c '
                                      '<-> b length: '))
            if c_to_b_length <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    while True:
        try:
            angle_of_c = int(input('\tEnter a positive integer for angle of '
                                   'C in the triangle: '))
            if angle_of_c <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    # Convert the angle degrees of angle C to radians
    degrees_to_radians = angle_of_c * (math.pi / 180)

    # Using Law of Cosines to calculate the leg of a triangle.
    leg_of_triangle = math.sqrt(
        a_to_c_length * a_to_c_length + c_to_b_length * c_to_b_length - 2
        * a_to_c_length * c_to_b_length * math.cos(degrees_to_radians))

    # Output to user the leg of a triangle calculation, with precision of 2
    print('\n\n' + '*' * 90)
    print('\t' + str('{:.2F}'.format(leg_of_triangle) + ' is the length of C'))

    # Send the user back to the beginning of menu() to make another selection.
    menu()


def calc_volume_cylinder(radius, height):
    """
    calc_volume_cylinder() calculates the volume of a right circular cylinder
    based on the parameters input by the user.
    Then outputs formatted_right_cylinder to the user.

    :param radius:
    :param height:
    :return:
    """
    while True:
        try:
            radius = int(input('\tEnter a positive integer for the radius of '
                               'the cylinder: '))
            if radius <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break

    while True:
        try:
            height = int(input('\tEnter a positive integer for the height of '
                               'the cylinder: '))
            if height <= 0:
                error_int_message()
                continue
        except ValueError:
            error_int_message()
            continue
        else:
            break
    # Calculating the volume of a right circular cylinder
    calc_volume_right_cylinder = (math.pi * radius * radius) * height

    # Formatting calc_volume_right_cylinder up 5 decimal places.
    formatted_right_cylinder = round(calc_volume_right_cylinder, 5)

    # Output to user calculated answer rounded up 5 decimal places.
    print('\n' + '*' * 90)
    print('\t' + str(formatted_right_cylinder) +
          ' is the volume of the Right Circular Cylinder')

    # Sending user back to main menu to make another selection.
    menu()


def menu():
    """
    menu() is the menu for all the things this application can do. The user
    can make a selection by inputting a-f.
    :return: None
    """
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
        generate_secure_pwd(length=0, num_of_upper=0, num_of_lower=0,
                            num_of_digit=0, num_of_special=0)

    elif user_selection == 'b':
        calc_and_format_percentage(numerator=0, denominator=0, precision=0)
    elif user_selection == 'c':
        how_many_days()
    elif user_selection == 'd':
        calc_law_cosines(a_to_c_length=0, c_to_b_length=0, angle_of_c=0)
    elif user_selection == 'e':
        calc_volume_cylinder(radius=0, height=0)
    elif user_selection == 'f':
        sys.exit()
    else:
        print("You must enter a valid selection! Enter a - f.")
        menu()


def main():
    """
    main() is the main function of lab_two.py and runs the menu() function.
    :return:
    """
    menu()


if __name__ == "__main__":
    main()
