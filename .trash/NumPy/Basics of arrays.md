---
color: var(--mk-color-orange)
tags:
  - ai-ml
---
`import numpy as np` - It is a multidimensional array library, meaning **you can use `numpy` to store your data in arrays of any dimension.** Here's the [documentation](https://numpy.org/doc/stable/user/index.html).

Quick access:
[[Basics of arrays#What are arrays?|What are arrays?]]
[[Basics of arrays#Creating an array|Creating an array]]
[[Basics of arrays#Size, dimension and shape of an array|Size, dimension and shape of an array]]
[[Basics of arrays#Datatype and memory usage|Datatype and memory usage]]

## What are arrays?
Arrays are a type of data structure used to store and retrieve data. *We typically visualize an array like a grid,* with each cell storing an element of our data. A one-dimensional array would look like a list:
![[Pasted image 20240701182420.png|center]]

A two-dimensional array looks like a table:
![[Pasted image 20240701182803.png|center]]

A three-dimensional array would be like many 2D arrays stacked on top of each other, like going from a square to a cube.

## Creating an array
We can create a one-dimensional array using `a = np.array([1,2,3])`. We put our array in `[]` like a list, and pass it as an argument through `.array()`. **To create a two-dimensional array, we use a list within a list.** Example:
~~~python
b = np.array([[1,2,3], 
              [4,5,6]])
print(b)
~~~
There is no need to align it like this, but it makes it easier to visualize. Printing the array (with or without the alignment) will still output:
~~~python
[[1 2 3]
 [4 5 6]]
 ~~~

## Size, dimension and shape of an array
The size of an array is simply *the number of elements in each array.* We calculate this using the `.size` attribute. The below code will return `3,6,8`.
~~~python
a = np.array([1,2,3])
b = np.array([[1,2,3], [4,5,6]])
c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

print(a.size)
print(b.size)
print(c.size)
~~~

We know these arrays can go up to `n` dimensions, so we use the `.ndim` (short for number of dimensions) method to find the dimensions. Example:
~~~python
a = np.array([1,2,3])
b = np.array([[1,2,3], [4,5,6]])
c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
~~~
This will output `1,2,3`.

We can view the shape of an array using the `.shape` attribute. **This returns a tuple representing its dimensions.** For a 1D array, it will output `(n,)` to represent `n` elements. A 2D array will be `(n,m)`, where `n = rows` and `m = columns`. For higher dimensions, *the first item will represent how many arrays of one dimension lower can fit in it.* This means that for a **4D array of shape `(a,b,c,d)`, `a` represents the number of 3D arrays that fit in the 4D array,** and `b` represents the number of 2D arrays that fit in the 3D array. The last two items will be the same `(n,m)` format of 2D arrays. Example: ^d74870
~~~python
a = np.array([1,2,3])
b = np.array([[1,2,3],
			  [4,5,6]])

c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

print(a.shape)
print(b.shape)
print(c.shape)
~~~
This will output:
~~~python
(3,)
(2, 3)   
(2, 2, 2)
~~~
The array `a` is a vector, having `1` dimension. Array `b` is a matrix, being two vectors stacked on top of each other. *Array `c` is a 3D array of shape`(2,2,2)`*. The first `2` here means we can fit `2` 2D arrays (matrices) inside the 3D array. Each of these matrices then have `2` rows and `2` columns.

## Datatype and memory usage
We use the `.dtype` attribute to check the datatype of an array. By default, it is usually `int32`. This means **each element takes up 4 bytes of memory (32 bit integer/8 bits per byte).** The space taken in memory of an array having `n` elements will be `n * 4 bytes`.

For an `int16` array, each *element takes up 2 bytes in memory* (16/8). If we want to define an array as an `int16` array, we should do that while defining the array by adding an argument to the array's definition. Example: `a = np.array([1,2,3], dtype ='int16')`.

If you want to know *how much memory each element takes up,* use the `.itemsize` attribute. This will return `4` for `int32` and `2` for `int16`. To find the *total size of each array,* use the `.nbytes` (number of bytes) attribute. Since I've stuck to the default `int32` datatype, the size of these arrays will be `4 * [3,6,8]` (output of `.size`). Therefore, the code below returns `[12,24,32]`.
~~~python
a = np.array([1,2,3])
b = np.array([[1,2,3], [4,5,6]])
c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

print(a.nbytes)
print(b.nbytes)
print(c.nbytes)
~~~
