---
color: var(--mk-color-orange)
tags:
  - quantecon
---

## Element-wise functions
`numpy` provides some standard functions that act element-wise on arrays like `log, exp, sin` etc. Eg:
~~~python
z = np.array([1, 2, 3])
np.sin(z)
~~~
This will output:
~~~python
array([0.84147098, 0.90929743, 0.14112001])
~~~

*Since these functions act element-wise on arrays, they're called vectorized functions.* Sometimes, they're also called `ufuncs`, short for universal functions.


### where function
`arrayname.where(condition, true, false)` - Will return `true` if the element in the array satisfies the condition, `false` if it doesn't. **It is a vectorized alternative to an `if-else` statement.** Eg: Suppose we have the array
~~~python
array([0.27783809, 0.82533296, 0.33311616, 1.58429178])
~~~
Using the `where` function,
~~~python
np.where(x > 0, 1, 0)  # Insert 1 if x > 0 true, otherwise 0
~~~
It will output all `1` since all the elements are greater than `0`.
~~~python
array([1, 1, 1, 1])
~~~
