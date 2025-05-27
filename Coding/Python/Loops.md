---
color: "#20bf6b"
sticker: lucide//refresh-cw
tags:
  - py-syntax
---
Quick access:
[[Loops#while loop|while loop]]
[[Loops#continue command|continue command]]
[[Loops#exit() command|exit() command]]
[[Loops#For loop|for loops]]
	[[Loops#range function|range function]]

## while loop
This is a loop that runs as long as the `True` or `False` (capital T and F) are met. We can use the `break` command to stop the loop, otherwise it might end up being an infinite loop. `break` will stop the loop and it will **read the next unindented line of code,** even if there is more code within the loop.

~~~python
while True:
  print("This program is running")
print("Aww, I was having a good time 😭")
~~~
This code runs forever and only outputs "This program is running" because there is no `break` command to stop it.
~~~python
while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")
~~~
This code will stop if `goAgain` is no due to the `break` command within the loop. It reads the next unindented line, which is the `print` command.

## Continue command
The `continue` command in a loop brings the user back to the question. Unlike `break` which runs the next unindented line, `continue` will start the code from the start and ask the first question again.
~~~python
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
~~~
In this code, if the user replies with "right", the loop asks the question again. There is no ending here, so the code keeps asking the question as long as the user replies with "right".

## exit() command
The command `exit()` completely stops running all code. In the example above, the problem was that the loop kept repeating and there was no way to win. The only way the above code would stop is if you answered left.
~~~python
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")
~~~
In this code, the `exit()` command on line 11 means that if the user replies anything other than left or right, they win the game. When they win, the code stops and doesn't ask for anything further as the user has already won. Example output:
~~~python
You are in a corridor, do you go left or right?
> right
You are in a corridor, do you go left or right?
> neither
Ahh! You're a genius, you've won
~~~

## For loop
A `while` loop is used when we *don't know how many times the loop will repeat.* `for` loops fix this problem, and are basically `while` loops but specifies the number of times the loop will repeat. Let's compare the two functions.

This is a counter using a `while` loop:
~~~python
counter = 0
while counter < 10:
  print(counter)
  counter += 1
  ~~~

This is the same counter using a `for` loop:
~~~python
for counter in range(10):
  print(counter)
~~~

`for` can be a much shorter way to loop. We can see that the syntax for the command is:
`for variable in range (value):`
	`repeat this code`

### range function
`range` creates a **list of numbers** in the range you provide. If you only give one number, `range` creates a list of all numbers from 0 to one less than the number you gave. Therefore, `range (10)` makes a list of all numbers from 0 to 9.

It has the following syntax:
`range (starting val, value to end before, increment)`

~~~python
for i in range (0, 1000000, 25):
  print(i)
~~~
This code prints all numbers from 0 to 1,000,000 with an increment of 25. We can also use negative increments.
~~~python
for i in range(10, -1, -1):
  print(i)
~~~
This code prints all numbers from 10 to 0. Python will print all numbers **until** the 2nd value. Therefore, it stops at the value right before the 2nd one. Since 2nd value here is -1, it will stop at 0, which is before -1 if we go backwards from 10.