# 4.13.3: Greeting
# Juan Salcedo
# 2.6.19


name = input("What is your name? ")

def greeting():
    print("Hi there " + name + "! ")
    print("Nice to meet you")

greeting()


# 4.13.4: Functions and Variables
# Juan Salcedo
# 2.6.19


x = 11

def print_something():
    x = 13
    print(x)

print_something()
print(x)



# 4.13.5: Functions & Variables - Part 2
# Juan Salcedo
# 2.14.19

my_variable = 3.6745

def something():
    print(my_variable + 10)

something()


# 4.13.6: Functions and Variables, Part 3
# Juan Salcedo
# 2.18.19

def print_number(x):
    print(str(x))

print_number(12)
print_number('\n' + 'Hello World')


# 4.14.4: Name and Age
# Juan Salcedo
# 2.18.19

def name_and_age(name, age):
    print('\n', 'Hi, My name is', name, 'and I am', str(age), 'years old.')

name_and_age('Juan Salcedo', 15)
name_and_age('Dr. Suess', 22)
name_and_age('Mike', 56)


# 4.14.5: Default Parameters Values
# Juan Salcedo
# 2.19.19


def print_two_numbers(x, y = 20):
    print('\n''First number:', x)
    print('Second Number;', y)

print_two_numbers(5, 67)
print_two_numbers(23)

# 4.14.7: Print Mutiple Times
# Juan Salcedo
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('\n''Hello Computer Scientist', 10)

# 4.14.7: Print Mutiple Times
# Juan Salcedo
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('\n''Hello Computer Scientist', 10)

# 4.16.3: Enter a Number
# Juan Salcedo
# 2/20/19

try:
    my_num = int(input('Enter a integer: '))
    print('Your number: ' + str(my_num))

except ValueError:
    print('That was not an integer')

# 4.14.4: Name and Age
# Juan Salcedo
# 2.18.19

def name_and_age(name, age):
    print('\n', 'Hi, My name is', name, 'and I am', str(age), 'years old.')

name_and_age('Juan Salcedo', 15)
name_and_age('Dr. Suess', 22)
name_and_age('Mike', 56)

# 4.16.6: Temperature Converter
# Juan Salcedo
# 2.20.19

def celcius_to_fahrenheit(celcius):
    return celcius * 1.8 + 32

def fahrenheit_to_celcius(fahrenheit):
    return(fahrenheit - 32) / 1.8

try:
    c = float(input('Enter a temperature in celcius: '))
    print('In fahrenheit:', round(celcius_to_fahrenheit(c), 2))

    f = float(input('Enter a temperature in fahrenheit: '))
    print('In celsius:', round(fahrenheit_to_celcius(f), 2))

except ValueError:
    print('You must enter a float')

# 4.16.7: Enter a positive number
# Juan Salcedo
# 2/21/19

def retrieve_positive_number():
    while True:
        try:
            number = int(input('Enter a positive number: '))
            if number >0:
                return number
            else:
                print('That number was not positive!')
        except ValueError:
            print('That was not a number, silly goose.')


