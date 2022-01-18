# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    show = []
    for i in range(num, -1, -1):
        show.append(i)
    return show

print(countdown(5))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([3,4]))

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([3,4,5,6,7,8,9]))

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    show = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            show.append(list[i])
    print(len(show))
    return show

print(values_greater_than_second([4,4,9,2,2,4,2,1,6,0]))
print(values_greater_than_second([5]))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size,value):
    show = []
    for i in range(0, size):
        show.append(value)
    return show

print(length_and_value(2,3))
print(length_and_value(8,4))