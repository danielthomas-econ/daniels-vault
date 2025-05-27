---
color: "#20bf6b"
sticker: lucide//check-square
tags:
  - py-syntax
---
## Syntax
Subroutines tell Python that a piece of code exists. We can use subroutines instead of loops. A subroutine is defined by:
`def (subroutine name) (arguments):`

Example:
~~~python
def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

rollDice()
~~~
Here, `rollDice` is the subroutine's name, and the *indented code is the argument* for the subroutine. To execute the argument, we call the subroutine using `rollDice()`. Make sure the code to call the subroutine **is not in the indented argument.** 


## [[Errors#2. SyntaxError|SyntaxError]]
This can pop up if we *forget the parentheses before the colon.*
Eg:
~~~python
def countToFive:
  for i in range(1, 6):
    print(i)

countToFive()
~~~

We get the following error:
~~~python
  File "main.py", line 1
    def countToFive:
                   ^
SyntaxError: invalid syntax
~~~


## [[Errors#3. IndentationError|IndentationError]]
This can pop up if we *forget to indent the subroutine's argument.*
Eg:
~~~python
def countToFive():
for i in range(1, 6):
  print(i)

countToFive()
~~~

We get the following error:
~~~python
  File "main.py", line 2
    for i in range(1, 6):
    ^
IndentationError: expected an indented block
~~~
Just indent the `for` and `print` statement by one block.


## Parameters
We put the parameter (also called argument) in the `()` in the subroutine. To call a parameter, run `subroutine_name(parameter)`. Previously, we'd leave the parentheses blank when running subroutines, but now we can execute it along with a parameter. Example:
~~~python
def whichCake(ingredient):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")

whichCake("chocolate")
~~~

If we run this code, we get the following output:
~~~python
Mmm, chocolate cake is amazing
~~~

In this code, we've made a subroutine called `whichCake` and created a parameter called `ingredient`. The subroutine's argument explains what Python must do with the value of `ingredient`. We then call the subroutine and put `"chocolate"` in the brackets in place of `ingredient`. This tells Python that *the value of ingredient is chocolate.* Therefore, it outputs the corresponding `if` statement. If we called `whichCake("broccoli")`, we'd get the `elif` output.

We can also have **multiple parameters** for one subroutine and get their values using user inputs. Example:
~~~python
def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")
whichCake(userIngredient, userBase, userCoating)
~~~
Here, `whichCake` has three parameters: `ingredient`, `base` and `coating`. We use the subroutine's arguments to define what each variable does, and we can use the `input` statements to get their values and then call `whichCake`.

## Return function
`return` puts a certain value obtained back into the subroutine. Eg:
~~~python
#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin

myPin = pinPicker(4) #4 means we want 4 random numbers
print(myPin)
~~~
Here, we've created an empty string called `pin`. Using concatenation, we update the pin using the `+=` operator to have any random integer between 0,9. The number of integers depends on the value of the parameter `number`. Finally, we `return` the pin so Python knows the value of the new `pin` variable. If we delete the `return` function, our output will simply be "`None`".

## [[Errors#1. NameError|NameError]]
The below code does not work and instead gives us a NameError.
~~~python
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

areaOfTriangle (5, 22)
print(area)
~~~
We get the following output:
~~~python
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    print(area)
NameError: name 'area' is not defined
~~~
Although the variable `area` is defined, it is **only defined within the subroutine `areaofTriangle`**. We *cannot call `area` outside its subroutine.* To fix it, we just add `area = areaofTriangle(5,22)`. Now, the variable `area` is defined outside the subroutine and Python will print it.