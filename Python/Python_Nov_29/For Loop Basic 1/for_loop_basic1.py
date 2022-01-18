# Basic - Print all integers from 0 to 150.
for x in range(0, 151, 1):
    print(x)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for y in range(5, 1001, 5): 
    print(y)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def numbers():
    for s in range(1, 101, 1):
        if s % 10 == 0:
            print("Coding Dojo")
        elif s % 5 == 0:
            print("Coding")
        else:
            print(s)
numbers()

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

total = 0
for h in range(1, 5000001, 2):
        total = total + h
print(total)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for i in range(2018, 0, -4):
    print(i)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flexible(lowNum, highNum, mult):
    for b in range(lowNum, highNum+1):
        if b % mult == 0:
            print(b)
flexible(2, 9, 3)