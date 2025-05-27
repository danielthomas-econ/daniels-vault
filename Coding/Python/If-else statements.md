---
sticker: lucide//check-check
color: "#20bf6b"
tags:
  - py-syntax
---
Quick access:
- [[#Syntax|Syntax]]
- [[#Printing if statements|Printing if statements]]
- [[#Else statements|Else statements]]
- [[#[[Errors#2. SyntaxError|SyntaxErrors]]|[[Errors#2. SyntaxError|SyntaxErrors]]
- [[#Nesting if statements|Nesting if statements]]
- [[#Using logical conditions with if statements|Using logical conditions with if statements]]
- [[#elif statement|elif statement]]
- [[#Double conditions:|Double conditions:]]
- [[#[[Errors#2. SyntaxError|SyntaxError]]|[[Errors#2. SyntaxError|SyntaxError]]


## Syntax
Use `==` to define an if condition. ``==`` means you are asking Python to check if two things are *exactly* the same.

## Printing if statements
The if statement simply checks if the condition is met. To print its output, we need to type a print command **within one indent** of the `if` command. Remember to *use a colon* after the if statement to start the indent on the next line.

Example:
```python
myName = ("What is your name? ")
if myName == "Daniel":
 print ("Welcome Daniel!")
 ```

## Else statements
The else statement is used if the condition is not met in the `if` statement. In this situation, Python executes the alternative, which is the else statement. It must be the **first thing** **unindented** after the `if` and be *in line with the if statement.*

Example:
```python
myName = input("What's your name?: ")
if myName == "David":
 print("Welcome Dude!")
 print("You're just the baldest dude I've ever seen")
else:
 print("Who on earth are you?!")
 ```
 Note that the indentation of both `if` and `else` are the same, and the `print` commands are all typed after the first indent. Again, we must *use a colon* after the `else` statement and before the start of the indent.

## [[Errors#2. SyntaxError|SyntaxErrors]]
Missing `==` or using only `=`:
```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs = "cat":
  print("Meow")
else:
  print("Woof")
  ```
Here, the `if` statement is `if catsOrDogs = "cat":`
The syntax for `if` requires `==`, so we get the following SyntaxError
```python
File "main.py", line 2
    if catsOrDogs = "cat":
                  ^
SyntaxError: invalid syntax
```

Forgetting to put a colon after the `if` statement:
```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat"
  print("Meow")
else:
  print("Woof")
```
Here, the `if` statement is `if catsOrDogs == "cat"`
The syntax requires a colon at the end of the `if` statement, so it should be `"cat":` in this case. We get the following SyntaxError
```python
  File "main.py", line 2
    if catsOrDogs == "cat"
                         ^
SyntaxError: invalid syntax
```

## Nesting if statements
Nesting is when you put an `if` statement inside another `if` statement. In this case, the second `if` statement will be *one indent in* and its respective `print` statement will be another indent in.

Example:
~~~python
tvShow = input("What is your favorite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
~~~
We can see that the `if faveCharacter` statement is nested inside the `if tvShow` statement. Therefore, the code will only proceed to ask for `faveCharacter` if the input matches the requirements of the `if tvShow` statement.
~~~python
What is your favorite tv show? peppa pig
Ugh, why?
Who is your favorite character? george
Nah, Daddy Pig's the greatest
~~~
Here, out output matches the requirement of `if tvShow` since we answered with `peppa pig`. Therefore, Python proceeds to ask us for the `faveCharacter` input. 

~~~python
What is your favorite tv show? paw patrol
Aww, sad times
~~~
The output changes if we answer `paw patrol`. Since we do not satisfy the condition of `if tvShow`, the `faveCharacter` question isn't asked since it is nested inside the `if tvShow` condition.

## Using logical conditions with if statements
Logical conditions are conditions such as `and`, `or`, `not` etc. A common mistake when using these conditions is that we input the following.
~~~python
name = input("Name: ")
if name == "Dave" or "dave":
  print("Hi Dave")
  ~~~
While this doesn't give an error, it might not always work as intended. To ensure it always work, we must **restate the question** by assigning the condition to the variable again. We do it by:
~~~python
name = input("Name: ")
if name == "Dave" or name == "dave":
  print("Hi Dave")
~~~
We restated the question by adding `name ==` after the `or` condition. This makes sure that Python knows we are assigning the logical condition to the variable `name` again.

## elif statement
`elif` is short for **else if.** It allows you to add alternate questions for the same input. They go *in between* `if` and `else` statements. Make sure that the `elif` indent is the same as the indent for `if` and `else`. The `print` commands under `elif` must also match the indent of print commands under `if` and `else`.
 
Example:
~~~python
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")
  ~~~

## Double conditions:
We can output a certain thing when two conditions are met using the `and` command.

Example:
~~~python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password > ")
if username == "mark" and password == "password":
  print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
  print("Hey there Suzanne!")
else:
  print("Go away!")
  ~~~
Now the code will only print a welcome message to Mark or Suzanne if **both the username and password match** the conditions in the if statement.

## [[Errors#2. SyntaxError|SyntaxError]]
We get an `invalid syntax` error if the `elif` command is not between `if` and `else`.

Example:
~~~python
print("SECURE LOGIN")
username = input("Username > ")

if username == "mark":
  print("Welcome Mark!")
else:
  print("Go away!")
elif username == "suzanne":
  print("Hey there Suzanne!")
  ~~~

We get the following error:
~~~python  
File "main.py", line 8
    elif username == "suzanne":
    ^
SyntaxError: invalid syntax
~~~

To fix this, just move the `elif` statement to the line after `print("Welcome Mark!")`.