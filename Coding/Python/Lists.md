---
color: "#20bf6b"
sticker: lucide//list-checks
tags:
  - py-syntax
---
Lists are used when you want to store more than one value with a certain variable. We define lists the same way we define variables, but we use `[]` to enclose a list. Example: `timetable = ["Computer Science", "Math", "English", "Art", "Sport"]`.
When counting the items in a list, **Python starts from 0.** Therefore, element 0 in this list is Computer Science, element 1 is Math etc. *Each element is called an index.* 

Quick access:
[[Coding/Python/Lists#Printing lists|Printing lists]]
[[Coding/Python/Lists#Lists and Loops|Lists and loops]]
[[Coding/Python/Lists#Enumerate function|Enumerate function]]
[[Coding/Python/Lists#List comprehension|List comprehension]]
[[Coding/Python/Lists#Dynamic lists|Dynamic lists]]
	[[Coding/Python/Lists#Pop function|Pop function]]
[[Coding/Python/Lists#List slicing|List slicing]]
[[Coding/Python/Lists#Unpacking a list|Unpacking a list]]
[[Coding/Python/Lists#Tables (2D lists)|Tables (2D lists)]]
	[[Coding/Python/Lists#Dynamic 2D list|Dynamic 2D list]]
	[[Coding/Python/Lists#Printing 2D lists|Printing 2D lists]]

----
## Important methods
- We can *remove all items* in a list using the `list_name.clear()` function. This keeps the same list name, but returns an empty list instead.

- We can *reverse a list* using `list_name.reverse()`.

- We can *sort a list in ascending order* using `list_name.sort()`, however, this also changes the original list. If you want the sorted list to be a new list, use `new_list = sorted(list_name)`.

- We can *copy a list* using `list_new = list_old.copy()`. **Do NOT use `list_new = list_old`, as this will change the old list too when you update `list_new`.** Using `.copy()` ensures that all changes in the new list do not affect your original list.

- We can *count the number of a certain item* using `list_name.count(item)`. In `list = [1,2,2,2,4,5]`, using `list.count(2)` would give us the output `3` because the number `2` appears three times.

- We can *find the first index of an item* using `list_name.index(item)`. Additionally, the method also has the arguments `start` and `end` after `item` to search within a specific index range. In `list = [1,2,2,2,4,5]`, using `list.index(2)` would return `1`, **since the first occurrence of `2` is in index `1`**.
----

## Printing lists
While we can define lists the same way we define variables, **we cannot print them the same way.** If we use the above example, using `print(timetable)` gives us the output `['Computer Science', 'Math', 'English', 'Art', 'Sport']`, which feels weird with all the brackets. Instead, we use `print(timetable[1])`, which prints out index 1 from our list.

If you want to *change an index* in a list, then we use `list_name [index] = ` to update a certain index in the list. Example: `timetable[4]= "Watch TV"`. If we want to print the updated list, we have to *place the print statement after* the line to change the index.

## Lists and Loops
Lists are much more effective when combined with [[Loops]]. To use them together, we use the following syntax:
`for new_variable in list_name:`
	`repeat the code`
Under this structure, Python reads through each value of the list *and runs the indented code accordingly.* We can use this to print out all the contents of a list for example.
~~~python
timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
for lesson in timetable:
  print(lesson)
  ~~~
In this code, Python understands that the variable `lesson` refers to the indices in the list `timetable`. When the `for` loop starts running, the first index is printed, then the loop continues printing the second, third, fourth etc. index and eventually outputs the entire list.

## Enumerate function
The `enumerate()` function **lets you iterate over any list while keeping track of its index position.** The basic syntax is `for index, item in enumerate(iterable):`. This returns a pair of values: the index number and the item being iterated over. For example:
~~~python
names = ["Alice", "Bob", "Charlie"] 
for index, name in enumerate(names): 
	print(f"Index: {index}, Name: {name}")
~~~
This will output the following, showing how the `index` variable keeps track of the index.
~~~Python
Index: 0, Name: Alice
Index: 1, Name: Bob
Index: 2, Name: Charlie
~~~

We can also **specify a starting index** using the `start` argument. This changes the syntax to `for index, name in enumerate(names, start=1)`. Here, *index starts at 1.* 

## List comprehension
List comprehension is a method in which we use `for` and `if` statements to create a new list. Example:
~~~python
# Using list comprehension to create a list of squares for numbers 0-9
squares = [x**2 for x in range(10)]
print(squares)
~~~
Here, we put the definition of `squares` in `[]` so Python understands we are trying to create a list. Using list comprehension, **we define the condition of list items within the square brackets.** Now Python understands that the *items in the list are the squares of all values of `x` until `10`.* This gives us the output `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`.

We can use as many `for` and `if` statements as we want in list comprehension. Another example is:
~~~python
# Creating a list of squares for even numbers 0-9
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)
~~~
It is the same one as before, except with an additional statement to check if `x` is even. This tells Python to *only proceed with squaring the number if `x < 10` and `x` is even.* Our list `even_squares` is now equal to `[0, 4, 16, 36, 64]`.

## Dynamic lists
Dynamic lists are **blank lists to which we can add or remove items as we go.**  We start by defining a blank list using `list_name[]`.  Using the `list_name.append` argument, we can add items to the list. Example:
~~~python
while True:
  item = input("What's next on the Agenda?: ")
  myAgenda.append(item)
  printList()
  ~~~
This code asks for the next item on your agenda as an input, and then appends that to the list `myAgenda` and prints it out using a subroutine called `printList()`. To *insert an item in a specific position in the list,* we use `list_name.insert(index, item)`. Example: `myAgenda.insert(2, "play music")` will add "play music" as the 3rd item in the list (2nd index).

If we want to *remove an item,* we just replace `.append` with `.remove`. The problem with removing items from lists is that **sometimes the item you want to remove is not in the list.** In that case, you'll get a ValueError like this:
~~~python
Traceback (most recent call last):
  File "main.py", line 16, in <module>
    myAgenda.remove(item)
ValueError: list.remove(x): x not in list
~~~
To fix this, we can use a *nested if statement* to check if the item we want to remove is in the list or not. We can do this by:
~~~python
    if item in list_name:
      list_name.remove(item)
    else:
      print(f"{item} was not in the list")
~~~
This way, our code won't instantly crash if we input something that is not in the list.

### Pop function
The `list_name.pop()` function **removes and returns the last item** in a list. However, we can also **specify a certain index** instead of removing the last item by default. `.pop()` will return a specific item in the list, but it also pops it out of the list, meaning the list will no longer contain that specific item.
~~~python
mylist = [1, 2, 3, 4]
removed_item = mylist.pop()  # Removes and returns the last item, 4
print(removed_item)  # Output: 4
print(mylist)  # Output: [1, 2, 3]

# Specifying an index
removed_item = mylist.pop(1)  # Removes and returns the item at index 1, which is 2
print(removed_item)  # Output: 2
print(mylist)  # Output: [1, 3]
~~~

## List slicing
List slicing is very similar to [[Strings#String slicing|string slicing]]. For example, using `for key in list(key)[:10]` will run the `for` loop for the first $10$ items in the `key` list. You can also set up the variables to print a certain range. Eg: `for key in list(key)[start:start+10]` will print $10$ items after the value of the `variable` start.

### Negative string slicing

## Unpacking a list
Unpacking a list is the *process of distributing the elements of the list across multiple variables.* For example:
~~~python
my_list = [1, "Hello", 3.14]
a, b, c = my_list  # Unpacking the list

print(a)  # Output: 1
print(b)  # Output: Hello
print(c)  # Output: 3.14
~~~
We assigned the values `a, b, c` to `my_list`. It will **assign the variables to their corresponding values based on order.** Therefore, `a` gets index `0`, `b` gets index `1` and so on.

*If you assign too many or too few variables, you get a* [[Errors#10. ValueError|ValueError]] because the number of variables and number of indices don't match. If you want to fix the scenario when we use too few variables, **we have to use the `*` operator along with another variable.** In context of list unpacking, `*` stores excess items in a list in the variable `*` is assigned to (usually called `rest`). Example:
~~~python
my_list = [1, 2, 2, 2, 4, 5]
a, b, *rest = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(rest)  # Output: [2, 2, 4, 5]
~~~
Had we not used the `*`, we would get a `ValueError` because there aren't enough variables. `*rest` stores all the remaining indices into `rest`, making it a good way to avoid unnecessary errors when unpacking lists. **We can also use `*rest` in the middle of unpacking our variables.** Example:
~~~python
my_list = [1, 2, 2, 2, 4, 5]
a, *rest, b = my_list
print(a)  # Output: 1
print(rest)  # Output: [2, 2, 2, 4]
print(b)  # Output: 5
~~~
Now, `a` and `b` are assigned to the first and last indices, and `*rest` is assigned to everything else. 

## Tables (2D lists)
Tables in Python are basically **2D lists.** Vertical data is used for *fields* while horizontal data is used to *store the records.*
We can create tables using `listname = [row index][column index]`.
We can lay out a 2D list by **putting lists inside a list** like this:
~~~python
my2DList = [ ["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"] ]`
~~~
Here, we have 3 lists all within the list `my2DList`. We separate these lists with a comma. To print a single row, we can use `print(my2DList[0])`. This tells Python to print the first index in `my2DList`, and it'll output `['Johnny', 21, 'Mac']`.

**To print a single piece of data,** we use `print(my2DList[1][2])`. This tells Python to print *go to row index 1 and print column index 2.* Here, the first index is Sian's list (Python starts counting from $0$, so 2nd list is the 1st for it). `[2]` tells Python to print the second index within Sian's list, which is "PC".

Changing the value of any index remains the same. If we want to change "PC" to "Linux" in the above example, we use `my2DList[1][2] = "Linux"`. Now the value is updated and Sian's list becomes `['Sian', 19, 'Linux']`.

### Dynamic 2D list
It's the same concept as normal [[Coding/Python/Lists#Dynamic lists|dynamic lists]] with a slight difference. Here, we set a variable named `row = [xyz]`, where `xyz` is whatever values the row must take. Then we can use `listname.append(row)` to add this row to our 2D list. 

### Printing 2D lists
Using a normal list printing subroutine like the one below *will print out the list with all the brackets and commas.* It simply looks strange.
~~~python
for row in listname:
	print (row)
~~~

To fix this, we must **print each item individually.** This way, Python doesn't output the whole row but rather the individual values within each row. We can do this with the below subroutine:
~~~python
def prettyPrint():
  print() 
  for row in listname: 
    for item in row: 
      # item refers to each item in the column for that row
     print(f"{item:^10}", end=" | ")     
    print() 
  print()
~~~
The subroutine starts by calling each row in order. Once it calls a certain row, it'll go to the indented `for` loop which *calls each item in the row.* It then prints out the item. In the above subroutine, they've used alignment and ended with | to make the output looks more like a table.
