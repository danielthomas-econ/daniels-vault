---
sticker: lucide//diff
color: "#20bf6b"
tags:
  - py-syntax
---
## Operators
~~~python
adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)
~~~

Output:
~~~python
7
-1
128
10.0
25
3
7
~~~


## Rounding off
To round off numbers, we use the `round` function. We have to specify two things: what we are rounding and to how many places we are rounding. The syntax is:
`round(what to round, no. of places rounded)`
Example:
~~~python
myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = myBill / numberOfPeople
answer = round(answer,2)
print("You all owe", answer)
~~~
This takes `answer` and rounds it to two decimal points. We get the following output:
~~~python
What was the bill?: 120
How many people?: 7
You all owe 17.14
~~~

Without the `round` function, Python will output `answer` as `17.142857142857142`, which doesn't make much sense for splitting the bill. Rounding helps give us a sensible output.
