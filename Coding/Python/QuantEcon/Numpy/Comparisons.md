---
color: var(--mk-color-orange)
tags:
  - quantecon
---

## Comparisons
As a rule, comparisons are done element wise.
~~~python
z = np.array([2, 3])
y = np.array([2, 3])
z == y
~~~
~~~python
array([ True,  True])
~~~
Now if we change the first element of `y` to `5`,
~~~python
y[0] = 5
z == y
~~~
~~~python
array([False,  True])
~~~
`numpy` returns `False` as `5 != 2`, but returns `True` for the second element as it is unchanged and `3 = 3`. 


## Extraction
We can also compare against scalars.
~~~python
z = np.linspace(0, 10, 5)
z
~~~
~~~python
array([ 0. ,  2.5,  5. ,  7.5, 10. ])
~~~
~~~python
z > 3
~~~
~~~python
array([False, False,  True,  True,  True])
~~~

This is very useful because we can **compare against the scalar and then only select the indices that return `True` values.** This can be done like:
~~~python
z[z > 3]
~~~
~~~python
array([ 5. ,  7.5, 10. ])
~~~
With one line of code, we've extracted all the elements greater than 3 from the array.

