---
sticker: lucide//printer
color: var(--mk-color-green)
tags:
  - py-syntax
---
Quick access:
- [[#Syntax|Syntax]]
- [[#Printing variables|Printing variables]]
	- [[#Printing variables#Printing in color|Printing in color]]
- [[#end argument|end argument]]
- [[#sep argument|sep argument]]
- [[#Hiding the white cursor|Hiding the white cursor]]

## Syntax

```python
print("Hello World")
```

Basic print command, print("string")

If you want to add a big paragraph of text, use triple quotes.
Input:
![[Pasted image 20240329105031.png]]

Output:
![[Pasted image 20240329105058.png]]

> [!Tip]
> You can use print() to print an empty line

## Printing variables
When printing variables, do not use quotes.

```python
print(varName) is correct
print("varName") just prints it as a string
```


### Printing in color
To print in color, type print `("\033[text colorm")`. For example, `print ("\033[32m")` prints everything in green as the code for green is 32. Some common color codes are given below.
![[Pasted image 20240331202906.png]]
[List of all color codes](https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007)

Example:
```python
print("Hello, you're a", "\033[32m", "good", "\033[0m", "person")
```

Output:
![[Pasted image 20240331203025.png]]
The code `\033[32m` tells Python to print everything after that in green, while `\033[0m` tells Python that everything after it should be white. 


## end argument
By default, Python automatically hits enter after each print statement and goes to the next line. Using `end`, you can change that to whatever you want.
~~~python
for i in range(0, 100):
  print(i, end=", ")
  ~~~
This outputs all the numbers from $0$ to $100$. Unlike using normal `print(i)`, where each number is in a new line, all numbers will be separated by a comma. 
![[Pasted image 20240413201253.png]]
The output looks like this now.
~~~python
#new line
for i in range(0, 100):
  print(i, end="\n")
#tab indent
for i in range(0, 100):
  print(i, end="\t")
#vertical tab
for i in range(0, 100):
  print(i, end="\v")
~~~
These are some special arguments we can use with `end`.

## sep argument
`sep` is short for separator and is a better version of `end` which we can use when concatenating string. Sometimes, using `end("")` can result in weird double spacing while concatenating string. Using `sep("")` avoids that.

## Hiding the white cursor
We use the special print argument `'\033[?25l` to turn off the blinking white cursor and `\033[?25h` to turn it back on. Without cursor hiding, we get an annoying rectangle while we print our numbers. It looks like this:
![[Pasted image 20240413202431.png]]
We can change that with the code below:
~~~python
import os, time
print('\033[?25l', end="")
for i in range(1, 101):
  print(i)
  time.sleep(0.2)
  os.system("clear")
~~~
Now it looks like this:
![[Pasted image 20240413202553.png]]
