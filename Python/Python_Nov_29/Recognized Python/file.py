num1 = 42 # variable declaration, number initialized
num2 = 2.3 # variable declaration, decimal/float initialized
boolean = True # variable declaration, boolean initialized.
string = 'Hello World' # variable declaration, string initialized

# variable declaration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# variable declaration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# variable declaration, tuples
fruit = ('blueberry', 'strawberry', 'banana')

# print to console, to check type
print(type(fruit))

# print to console, list access value
print(pizza_toppings[1])

# add a single item to the list
pizza_toppings.append('Mushrooms')

# print to console, dictionary access value
print(person['name'])

# change one of the values in dictionary
person['name'] = 'George'

# change or add value in dictionary
person['eye_color'] = 'blue'

# print to console, to check typles access value
print(fruit[2])

# conditional if, evalute then print to console, conditional else, evaluate then print to console.
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# conditional if, evalute then print to console, conditional else if, evaluate then print to console, conditional else, evaluate then print to console.
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop starts at 0, and goes upto 5 and stops.
for x in range(5):
    print(x)

# for loop starts at 2, and goes upto 5 and stops.
for x in range(2,5):
    print(x)

# for loop starts at 2, and goes upto 10 and stops, increments by 3
for x in range(2,10,3):
    print(x)

# while loop variable declaration
x = 0
while(x < 5):
    print(x) # print to console
    x += 1 # incrementing value x

# delete the last value in the list
pizza_toppings.pop()

# delete designated value within the index
pizza_toppings.pop(1)

# print to console dictionary 
print(person)

# delete designated value from dictionary
person.pop('eye_color')

# print to console dictionary
print(person)

# for loop through a premade list
for topping in pizza_toppings:
    if topping == 'Pepperoni': # conditional if
        continue # continue to next line
    print('After 1st if statement') # print to console
    if topping == 'Olives': # conditional if
        break # stops the for loop 

# function value declaration
def print_hello_ten_times():
    for num in range(10): # for loop starts at 0 and stops at 10
        print('Hello') # print to console

# calling the function
print_hello_ten_times()

# function value declaration with parameter
def print_hello_x_times(x):
    for num in range(x): # for loop through and stop at number x
        print('Hello') # print to console

# function call arguement 4
print_hello_x_times(4)

# function value declaration with given parameter
def print_hello_x_or_ten_times(x = 10):
    for num in range(x): # for loop starts at 0, and stops at 10
        print('Hello') # print to console

# function call upto 10
print_hello_x_or_ten_times()

# function call upto 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)

# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)