---
color: var(--mk-color-orange)
tags:
  - quantecon
---


## What is broadcasting?
In element-wise operations, **arrays may not have the same shape.** To fix this, `numpy` uses broadcasting, which *automatically expands arrays to the same shape whenever possible.*

Eg: Suppose `a` and `b` are arrays, and `a` is of the shape `(3,3)` and `b` is of the shape `(3,)`. When adding the two, *`numpy` will automatically expand `b` to `(3,3)`.* 
~~~python
a = np.array(
        [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]])
b = np.array([3, 6, 9])

a + b
~~~
This will output:
~~~python
array([[ 4,  8, 12],
       [ 7, 11, 15],
       [10, 14, 18]])
~~~
As we can see, even though `b` is just a flat array, adding `b` to `a` has **added `b` to all the rows of `a`.** This is how the operation looks visually:
![[Pasted image 20250319183635.png]]

In some cases, **both the operands will be expanded.** If `a` has shape `(3,)` and `b` has shape `(3,1)`, both `a` and `b` will be expanded to have the shape `(3,3)`.
~~~python
a = np.array([3, 6, 9])
b = np.array([2, 3, 4])
b.shape = (3, 1)

a + b
~~~
This will output:
~~~python
array([[ 5,  8, 11],
       [ 6,  9, 12],
       [ 7, 10, 13]])
~~~
Visually, the operation now looks like:
![[Pasted image 20250319183839.png]]

