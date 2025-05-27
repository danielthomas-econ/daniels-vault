---
sticker: lucide//text-cursor-input
color: "#20bf6b"
tags:
  - py-syntax
---
## Syntax

```python
input("What's your name?:")
```

Pretty much the same as the [[Coding/Python/Print statement|print]] command.

Output: 
```
What's your name?:
```

It lets the user input whatever they want, with the string being displayed to help the user know what they're supposed to input.


## Casting
### Equality and inequality symbols
~~~python
equal
5 == 5

not equal
3 != 5

greater than
5 > 3

greater than or equal to
5 >= 3

less than
3 < 5

less than or equal to
3 <= 5
~~~

### int and float function
The `int` function tells Python that whatever we are trying to input is a whole number. This is required because Python *always assumes the value of `input` to be a string.* Therefore, we must specify if we are inputting numbers using `int` or `float`. 
~~~python
myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
~~~
While this code seems quite simple, it doesn't work. We get the following error:
~~~python
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    if myScore > 100000:
TypeError: '>' not supported between instances of 'str' and 'int'
~~~
We get a TypeError since Python cannot use the `>` condition between two different datatypes (string and integer here). This is because whatever we input as `myScore` ends up as a string value. To fix this, we use the `int` argument.
~~~python
myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")
  ~~~
The `int` argument's parentheses must **entirely enclose the `input` function.**  

The `float` function works the exact same way, only difference is that it is used to store *numbers with decimals.* Example:
~~~python
myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
~~~
