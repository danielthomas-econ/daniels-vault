---
color: var(--mk-color-green)
tags:
  - py-syntax
sticker: lucide//diamond
---
Tuples are a data type similar to [[Coding/Python/Lists|lists.]] The main difference is that **a tuple cannot be changed after its creation.** This is called *immutability.* A tuple is usually defined by enclosing a list in parentheses `()`. Eg: `my_tuple = (1, "Hello", 3.14)`. However, you can also define a tuple by just listing the items separated by commas, and Python will automatically add the missing `()`.

We can convert a list or any iterable item (item which can be looped) using the `tuple()` function. Example: `mytuple = tuple([1, "Hello", 3.14])` converts the list to be the same tuple we used above. We can also do the reverse, using `mylist = list(mytuple)`, which will change it back into a list. Since tuples themselves are iterable, *we can run loops on tuples.* 

Accessing an item in a tuple is the same as a list. We simply use `tuplename[index]` to access a specific index in our tuple. However, *we can't replace items in tuples like we do in lists* because tuples are immutable. If you try `tuplename[index] = xyz`, you will get a [[Errors#9. TypeError|TypeError]] saying object doesn't support item assignment. 
 
We can use most methods of [[Coding/Python/Lists#Important methods|list manipulation]] with tuples too, as long as it doesn't conflict with the immutability of a tuple.

## Importance of tuples
Tuples are very similar to lists. The biggest difference is that **tuples are more optimized than lists.** Since tuples are immutable and cannot change, Python can make some background optimizations knowing that a tuple will always stay the same. We can prove this by comparing a list and tuple with the same values.
~~~python
import sys

# Define an alphanumerical list and tuple
alphanum_list = [1, "two", 3, "four", 5]
alphanum_tuple = (1, "two", 3, "four", 5)

# Print their byte sizes
print(f"List size: {sys.getsizeof(alphanum_list)} bytes")  
print(f"Tuple size: {sys.getsizeof(alphanum_tuple)} bytes")
~~~
This returns:
~~~python
List size: 104 bytes
Tuple size: 80 bytes
~~~
We can see that **this tuple is 24 bytes less than its identical list.** We can run a similar experiment to test the iteration speed (1 billion iterations) over the same tuple and list.
~~~python
import timeit

list = timeit.timeit(stmt = "[1, 'two', 3, 'four', 5]", number = 1000000000)
tuple = timeit.timeit(stmt = "(1, 'two', 3, 'four', 5)", number = 1000000000)

print(f"Time taken by list: {list}")
print(f"Time taken by tuple: {tuple}")
~~~
This returns:
~~~python
Time taken by list: 61.26197540014982
Time taken by tuple: 15.224687499925494
~~~
We can see a significant difference here. **The same list took 4 times longer to iterate over.** Seeing the memory and performance gains of tuple, it is a *good replacement for lists in very large datasets that **satisfy the immutability criteria.***
