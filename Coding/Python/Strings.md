---
color: "#20bf6b"
sticker: lucide//strikethrough
tags:
  - py-syntax
---
Quick access:
- [[#String manipulation|String manipulation]]
- [[#f-strings|f-strings]]
- [[#Alignment|Alignment]]
- [[#String slicing|String slicing]]
	- [[#String slicing#Skipping indices|Skipping indices]]
	- [[#String slicing#Splitting a string|Splitting a string]]
- [[#String concatenation|String concatenation]]
	- [[#String concatenation#Efficient concatenation|Efficient concatenation]]
---
## String manipulation
We can come across problems with capitalization when using `if` statements. For example:
~~~python
name = input("What's your name? ")
if name == "David" or name == "david":
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")
  ~~~
This works fine if the user inputs David or david, but if he inputs DAVid, it's not going to work as intended. To fix this, we can use the following adjustments:
- `stringName.lower()` - Makes the whole string lowercase
- `stringName.upper()` - Makes the whole string upper case
- `stringName.title()` - Capitalizes the *first letter of every word*
- `stringName.capitalize()`- Capital letter for the **first letter of the first word**
- `stringName.strip()` - Removes any space at the start of the string

Example:
~~~python
name = input("What's your name? ")
if name.lower().strip() == "david": 
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")
~~~

You can also use this to **modify inputs directly.** Here is an example of a code used to check for duplicates in a list:
~~~python
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ").strip().capitalize()
  if addItem not in myList:
    myList.append(addItem)
  printList()
~~~

> [!info] Order matters!
> When manipulating string, always use `.strip()` first since **order matters.** If you use `.capitalize()` first, Python checks that and then proceeds to check for `.strip()`. However, since you've already gone past the first space, *it won't strip anything* and you'll be left with the same code.

## f-strings
f-strings (short for format strings) are an easier way to concatenate strings. In the past, we'd concatenate like this:
~~~python
name = "Katie"
age = "28"
pronouns = "she/her"

print("This is", name, "using", pronouns, "pronouns and is age", age)
~~~
Using f-strings, we can output the same code using:
~~~python
name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))
~~~
We use `{}` as placeholders and the `format` argument to determine what goes in the brackets. You can also use f-strings to **set local variables** within the string itself.
~~~python
name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))
~~~
We can also use f-strings like this:
~~~python
name = "Katie"
age = "28"
pronouns = "she/her"

response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

print(response)
~~~
The variables used in this type of f-string have to be already defined previously.

## Alignment
To align our output, we use the following syntax:
`f{variable: alignment symbol   no. of spaces}`
Alignment symbol guide:
`< left`
`^ center`
`> right`

We can see an example below:
~~~python
for i in range(1, 31):
  print(f"Day {i: <2} of 30")
  ~~~
This code will try to input two spaces wherever it can to ensure the output is properly aligned.

Before alignment:
![[Pasted image 20240414191832.png]]
After alignment:
![[Pasted image 20240414191854.png]]
## String slicing
You can index strings just like indexing lists. Strings are a collection of individual characters, so we can ask Python to output a certain character just like list indexing. Example:
~~~python
myString = "Hello there my friend."
print(myString[0])
~~~
This outputs the **first character** from the string, which is the letter H. To print a range, we use `:` to define a range of indices to be printed.
~~~python
myString = "Hello there my friend."
print(myString[6:11])
~~~
**Spaces are also included as an index.** Therefore, if we `print(myString[5])`, we get a blank output. This is why we start with index 6 (remember to count from $0$). The end of the range must be *one number ahead* of where we want the string slice to end. In our code, the letter e is index $10$ but we print till index $11$ because Python ignores the last one.

Leaving the first or last index in a range empty defaults to $0$. `print(myString[:11])` will print "Hello there" and `print(myString[12:])` will print "my friend".

> [!NOTE] Strings are immutable
> We cannot use `myString[0] = "x"` to change the value of the first index. This is because strings are an *immutable datatype,* so we cannot assign a new value to an index, like we can do with mutable datatypes like strings.

### Skipping indices
We know the string slice brackets have two arguments, starting and ending index. However, there's a third index which tells **how many indices are to be skipped.** 
~~~python
myString = "Hello there my friend."
print(myString[0:6:2])
~~~
In the above code, it prints **every second index** between index $0$ and $6$. Therefore, the output here is `Hlo` as it alternates between letters and prints.

We can also use the third argument to ***print text backwards*** using a negative argument. 
~~~python
myString = "Hello there my friend."
print(myString[::-1])
~~~
This prints the exact reverse of the string since it *starts slicing backwards.* Using `[::1]` ends up printing the same string with no manipulation at all

### Splitting a string
We can split a string to output each word, just like how we print a list.
~~~python
myString = "Hello there my friend."
print(myString.split())
~~~
Using `.split()` outputs `['Hello', 'there', 'my', 'friend.']`.


## String concatenation
You can use concatenation to connect variables and string in a print statement.

```python
myName = input("What's your name? ")
myLunch = input("What are you having for lunch? ")
print(myName, "is going to be chowing down on", myLunch, "very soon!")
```

We can see that the variables myName and myLunch are in the same print statement as the string. To do this, **separate the string and variables using commas as done above.** Always make sure the string is in quotes. Instead of commas, *you can also add two strings with the addition operator to concatenate them.*

### Efficient concatenation
Using `+` for concatenation is actually very slow. **Since Python strings are immutable by nature, Python has to create a new string each time you concatenate, instead of just updating the old one.** While this is fine if we are just concatenating a handful of items, if we are iterating over a large list, there is a large performance overhead.

Eg:
~~~python
num = num + str(i)
~~~
Python creates a new string by allocating memory for the combined string, copying all characters from `num`, appending the characters in `str(i)` and assigning the new object back to `num`. The time complexity is $O(n^{2})$.

**The most efficient way to do this is to use `.join()`**. Eg:
~~~python
num = ''.join(str(i) for i in range(1, 1000000))
~~~

It avoids constant recalculating and reallocating by computing the total final length (in C) and allocates memory for the entire final string, *so it only copies each substring exactly once.* This is $O(n)$.

`+` is like building a brick wall by tearing it down and rebuilding each time you want to add a new brick. `.join()` is like laying all the bricks in one go after planning their positions.