#1 predicted outcome: 5
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 predicted outcome: (number_of_days_in_a_week_silicon_or_triangle_sides) function undefined
def number_of_military_branches():
    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 predicted outcome: 5
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 predicted outcome: 5
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 predicted outcome: 5, and none
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 predicted outcome: 3,5, error
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 predicted outcome: 25
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 predicted outcome: 100, and 10
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 predicted outcome: 7, 14, 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 predicted outcome: 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 predicted outcome: 500, 300, 300, none, 300 (Solution: 500, 500, 300, 500)
b = 500
print(b) #500
def foobar():
    b = 300
    print(b) #300
print(b) #500
foobar()
print(b) #500


#12 predicted outcome: 500, 300, 300, 300, none, 300 (Solution: 500, 500, 300, 500)
b = 500
print(b) #500
def foobar():
    b = 300
    print(b) #300
    return b
print(b) #500
foobar()
print(b) #500


#13 predicted outcome: 500, 300, 300, 300, 500, 300 (Solution: 500, 500, 300, 300)
b = 500
print(b) #500
def foobar():
    b = 300
    print(b) #300
    return b 
print(b) #500
b=foobar()
print(b) #300


#14 predicted outcome: 1, 2, and 3 (solution 1, 3, 2)
def foo():
    print(1) #1
    bar() # this becomes 3
    print(2) #2
def bar():
    print(3)
foo()

#15 predicted outcome: 1, 5, 10, 3, 5, 10 (Solution 1, 3, 5, 10)
def foo():
    print(1) # 1
    x = bar() # this becomes 3 from function below
    print(x) # 5 bar() becomes 5 after return statement
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y) # 10