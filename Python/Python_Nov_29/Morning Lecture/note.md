# Javascript VS Python

## Javascript
```js
var name = "Tyler"
var someList = ["cookies", "tomatos", "pies"]

function nameOfFunction(name){
    console.log("hello world")

    // if name is equal to "tyler"
    if (name === "Tyler"){
        console.log("Yeah!")
    } else if (name === "Pablo"){
        console.log("Awesome!")
    } else {
        console.log("something else")
    }
}

    // for loop
    for (let i=0; i < list.length; i++){
        let item = list[i]
    } 

console.log("out of function")

```
A Function becomes what it returns !IMPORTANT!

## Python
```py
name = "Tyler"
someList = ["cookies", "tomatos", "pies"]

def name_of_function():
    print("hello world")

    if name == "Tyler"
        print("Yeah!")
    elif name == "Pablo"
        print("Awesome!")
    else:
        print("something else")
    
    for idx in range(len(list)):
        item = list[idx]
        print(item)

    for item in list:
        print(item)

def some_function(name):
    pass

print("out of function")
```

__Differences__
- don't have to put "var"
- Indentation is important in python, not so much in javascript
- snake case VS camel case
- print VS console.log


# Data Types

1. "" string
1. 1 numbers -> int, float
1. true | True | 1, false | False | 0 ->bools
1. [] lists -> arrays
1. {} dict -> obj
1. (x1,x2) -> tuple

## strings
do strings have an idx -> YES
```py
def a_function(str):
    for char in str:
        print(char) # -> T y l e r 
        