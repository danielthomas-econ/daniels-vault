---
color: var(--mk-color-orange)
tags:
  - ai-ml
---
Quick access:
[[Accessing and changing arrays#Accessing an index|Accessing an index]]
	[[Accessing and changing arrays#Accessing a whole row/column|Accessing a whole row/column]]
	[[Accessing and changing arrays#Accessing a range of indices|Accessing a range of indices]]
	[[Accessing and changing arrays#Indexing using a list|Indexing using a list]]
[[Accessing and changing arrays#Changing elements in an array|Changing elements in an array]]
	[[Accessing and changing arrays#Changing a whole row/column|Changing a whole row/column]]

## Accessing an index
We can access a specific index in an array using `array[row, column]`. *Keep in mind that Python indexing starts at `0`*, so you'll need to enter one number lower than your intended target. The code below outputs `2,6,2`.
~~~python
a = np.array([1,2,3])

b = np.array([[1,2,3], 
              [4,5,6]])

c = np.array([[[1, 2], 
               [3, 4]],

              [[5, 6], 
               [7, 8]]])

print(a[1])
print(b[1,2])
print(c[0,0,1])
~~~
The output for array `a` and `b` are self explanatory. Since array `c` has a dimensionality greater than 3, we can't simply use the `[row,column]` way to access an index. **The first number should represent which 2D matrix we are trying to access.** It's like the output of `.shape`, where the *first value of the tuple shows the number of `n-1` dimension arrays are present in our array of dimension `n`* [[Basics of arrays#^d74870|(click here to read it).]] In this case, our first number in `c[0,0,1]` is `0`. This means we are *accessing the first 2D matrix.* Within that, we want to access the element in the first row and second column, which will return `2`.

We can also use negative notation here. `b[1,-2]` will return `5` here, because it is the second from last element in row `2` of the matrix `b`. **When using negative notation, we don't have to worry about starting our index from `0`**. This is because the last element is accessed by `-1`, and not by `0`. So accessing the fourth last element is done using `-4`, and not `-3`. 


### Accessing a whole row/column
It's the same thing as accessing an index. We maintain the same format of `[row, column]` and so on for higher dimensions. The difference is *we replace one of the values with `:`*, like how we do with list/string slicing. **To access a whole row, we replace the column argument with `:` and vice versa.** Example:
~~~python
b = np.array([[1,2,3], 
              [4,5,6]])

print(b[0, :])
print(b[:, 0])

~~~
This will output `[1 2 3]` and then `[1 4`]. `b[0, :]` refers to the *first row, whole column,* so Python prints the first row and all the columns in it, i.e. the entire first row. `b[:, 0]` prints the *whole row, first column.* This returns the first column and all the rows in it, i.e. the entire first column.

### Accessing a range of indices
Accessing a range of indices is very similar to string slicing. We use `array[startindex:stopindex:stepsize]`. 
~~~python
a = np.array([[1,2,3,4,5,6,7], 
              [8,9,10,11,12,13,14]])

print(a[0, ::2])
~~~
This code will return `[1 3 5 7]`. The `0` picks the first row, while `::2` means pick all columns but *step every 2 columns.*

### Indexing using a list
We can handpick the values we wish to select using a list, **since `numpy` indexing can take in a list as an argument.** For example:
~~~python
a = np.array([1,2,3,4,5,6,7,8,9])
a = a[[1,2,8]]
print(a)
~~~
This tells Python to *select elements in array `a` according to the list we've used as an argument.* Therefore, we're accessing the 1st, 2nd and 8th index, meaning our output will be `[2 3 9]`.

## Changing elements in an array
To change an element, we must equate `array[row, column]` to our new value. The below code tells Python to *check the 2nd row, 6th column, and change that value to 20.* This means that our array `a` now replaces `13` with `20`.
~~~python
a = np.array([[1,2,3,4,5,6,7], 
              [8,9,10,11,12,13,14]])

a[1,5] = 20
~~~

### Changing a whole row/column
Just like before, we must define the range of elements we want to change, and then assign it to a value. Example:
~~~python
a = np.array([[1,2,3,4,5,6,7], 
              [8,9,10,11,12,13,14]])

a[0,:] = 20
~~~
This code *replaces the entire first row with 20.* Our new array becomes
~~~python
[[20 20 20 20 20 20 20] 
 [ 8  9 10 11 12 13 14]]
 ~~~

You can replace your selection with a list, instead of having just one number throughout. Example:
~~~python
a = np.array([[1,2,3,4,5,6,7], 
              [8,9,10,11,12,13,14]])

a[0,:] = [0,1,0,1,0,1,0]
~~~
This replaces the whole first row with an alternating series of `0` and `1`. Our new array becomes:
~~~python
[[ 0  1  0  1  0  1  0]
 [ 8  9 10 11 12 13 14]]
 ~~~

When using this method, **make sure that the length of the list and the length of the selection are the same.** If they differ, Numpy will throw a [[Errors#10. ValueError|ValueError]] because the lengths aren't the same. Example:
~~~python
a = np.array([[1,2,3,4,5,6,7], 
              [8,9,10,11,12,13,14]])

a[0,:] = [1,2]
~~~
This gives us the following error message:
~~~python
  File "d:\Daniel's Things\Coding projects\test.py", line 6, in <module>
    a[0,:] = [1,2]
    ~^^^^^
ValueError: could not broadcast input array from shape (2,) into shape (7,)
~~~
The problem is our selection `a[0,:]` is `7` elements wrong, i.e. its shape is `(7,)`, while our list was only of shape `(2,)`. *Make sure the shapes of the selection and your replacement list match.*

This method isn't limited to lists only, I used the example of lists since we are using a 2D array here. **Your replacement must be of the same dimension as the selection.** This shouldn't be a problem if you remember to match the shapes of the selection and replacement.





