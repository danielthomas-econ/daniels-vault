---
color: var(--mk-color-orange)
tags:
  - quantecon
---


## Matrix multiplication
Use the `@` symbol.
~~~python
A = np.ones((2, 2))
B = np.ones((2, 2))
A @ B
~~~
Output:
~~~python
array([[2., 2.],
       [2., 2.]])
~~~   

**Note:** Using `@` on vectors will give you the dot product.