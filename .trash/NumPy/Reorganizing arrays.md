---
sticker: 
color: var(--mk-color-orange)
tags:
  - ai-ml
---
Quick access:
[[Reorganizing arrays#Reshaping arrays|Reshaping arrays]]
[[Reorganizing arrays#Stacks|Stacks]]
	[[Reorganizing arrays#Vertical stacks|Vertical stacks]]
	[[Reorganizing arrays#Horizontal stacks|Horizontal stacks]]


## Reshaping arrays
We can use `array.reshape((new shape))` to change the shape of an array. For example:
~~~python
before = np.array([[1,2,3,4], 
                   [5,6,7,8]])
print(before)

after = before.reshape((8,1))
print(after)
~~~
This will create an array called `after` that is just a reshape of array `before`. Since we've set `after` to be of the shape `(8,1)`, it will have 8 rows and 1 column, i.e. it'll be in just one straight column. The output looks like:
~~~python
[[1 2 3 4]
 [5 6 7 8]]

[[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]]
~~~

You can even **reshape arrays into different dimensions,** as long as they have *the same number of elements.* The array `before` has 8 elements, so we can reshape it into a 3D array of shape `(2,2,2)` since this shape also has three elements. We can do this using `after = before.reshape((2,2,2))`. Running the previous codeblock with this line instead will output:
~~~python
[[1 2 3 4]
 [5 6 7 8]]

[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
~~~
As we can see, the array `after` is now 3D (with 3 brackets), having two matrices each with two rows and two columns.


## Stacks
### Vertical stacks
We can vertically stack arrays *(row-wise)* using `np.vstack`. It takes a group of arrays and stacks them on top of each other *to make a new array.* Example:
~~~python
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2]))
~~~
This will output a new array by combining `v1` and `v2`. 
~~~python
[[1 2 3 4]
 [5 6 7 8]]
~~~

`v1` and `v2` were of the shape `(4,)`, and the `vstack` array is of the shape `(2,4)`. This is because the `v1` and `v2` were 1 dimensional with 4 columns. However, **the `vstack` array is two dimensional and adds an extra row, making the shape `(2,4)`**. Therefore, we can say that if we combine `n` arrays of shape `(m,)`, `vstack` will output an array of `(n,m)`.

You can add as many arguments in a `vstack` command as you please. For example, we can even run `vstack = np.vstack([v1,v2,v2,v2])` which has 4 arguments. Printing this array will give us:
~~~python
[[1 2 3 4]
 [5 6 7 8]
 [5 6 7 8]
 [5 6 7 8]]
~~~

### Horizontal stacks
Horizontal stacks are *column-wise* stacking, and we can do it with `np.hstack`. Using the same arrays as before, let's run a codeblock using `hstack`.
~~~python
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

hstack = np.hstack([v1,v2, v2])
~~~
Since `hstack` follows column-wise stacking, **our output will be each array added to a new column.** Since each array here has 4 columns, the output we get will have 4 $\times$ 3 = 12 columns.
~~~python
[1 2 3 4 5 6 7 8 5 6 7 8]
~~~

Using 2D arrays will give us a better understanding of how `hstack` functions.
~~~python
v1 = np.array([[1,1,1,1], 
               [2,2,2,2]])

v2 = np.array([[3,3,3,3],
               [4,4,4,4]])

hstack = np.hstack([v1,v2])
~~~
This will output the following array:
~~~python
[[1 1 1 1 3 3 3 3]
 [2 2 2 2 4 4 4 4]]
~~~
As we can see, **array `v1` was placed to the left of `v2`**. Had we used `vstack`, `v1` would be *on top* of `v2`. That is the fundamental difference between column-wise and row-wise stacking.

