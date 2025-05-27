---
color: var(--mk-color-orange)
tags:
  - ai-ml
---
There is a very long list of mathematical operations that we can perform using `numpy`. I can't note it all down, and I'll only list whatever was in the `freeCodeCamp.org` video. Click here to check the documentation for [math routines](https://numpy.org/doc/stable/reference/routines.math.html)  and [linear algebra.](https://numpy.org/doc/stable/reference/routines.linalg.html)

Quick access:
[[Math in NumPy#Arithmetic operations on a whole array|Arithmetic operations on a whole array]]
	[[Math in NumPy#Sum and product of all values in an array|Sum and product of all values in an array]]
[[Math in NumPy#Trigonometry|Trigonometry]]
[[Math in NumPy#Linear algebra|Linear algebra]]
	[[Math in NumPy#Matrix multiplication|Matrix multiplication]]
	[[Math in NumPy#Determinant of a matrix|Determinant of a matrix]]
[[Math in NumPy#Statistics|Statistics]]
	[[Math in NumPy#Min/Max value in an array|Min/Max value in an array]]
	[[Math in NumPy#Common statistical tools|Common statistical tools]]

## Arithmetic operations on a whole array
Simply using `arrayname operation value` will *modify all items in the array* according to the operation and value given. If we run the code below, we will get `[3 4 5 6]` because Python adds `2` to all the elements in our array. *We can do this with other operations too,* like subtraction or multiplication. We can also **perform operations on two arrays** just like this.
~~~python
a = np.array([1,2,3,4])
a = a + 2
print(a)
~~~

### Sum and product of all values in an array
`np.sum` gives us a total sum of all items in an array. The code below will return `21`, as it is the sum of all elements in the array. We can replace `.sum` with `.prod` to multiply all elements in the array, and we get `720`.
~~~python
stats = np.array([[1,2,3], [4,5,6]])
print(np.sum(stats))
~~~

## Trigonometry
We can apply trigonometric functions to `numpy` arrays using `np.function_name(array)`. Example: `np.sin(a)` will return an array with the `sin` values of all items in array `a`. **This works with all trig functions and their arc variants.** Adding an `h` to the end of the attribute gives the hyperbolic variants, `np.sinh` for example.

We can also *calculate the hypotenuse* of a right triangle with sides `x` and `y` using `np.hypot(x,y)`. Another useful trig function in `numpy` is the *degree to radian converter* (and vice versa) using `np.deg2rad(x)` or `np.rad2deg(x)`.

## Linear algebra
### Matrix multiplication
If we have arrays `a` and `b`, both of shape `(m,n)`, then we can directly multiply them using `a*b`. However, if they have different shapes, using `*` will give us a [[Errors#10. ValueError|ValueError.]] To multiply matrices of different shapes, we use `np.matmul(array1, array2)`. Example:
~~~python
a = np.ones((2,3)).astype(int)
b = np.full((3,2), 3)

print(f"Matrix a = {a}")
print(f"Matrix b = {b}")
print(f"Their product is {np.matmul(a,b)}")
~~~
This code will output:
~~~python
Matrix a = [[1 1 1]
 	        [1 1 1]]

Matrix b = [[3 3]
            [3 3]
            [3 3]]

Their product is [[9 9]
                  [9 9]]
# I aligned the matrices here
 ~~~
We use `.matmul` (or even `.dot`) to multiply two matrices of different shapes. However, there are rules for matrix multiplication. **We can only multiply matrices of order `(m,n)` and `(n,p)`, and this will give us an output of `(m,p)`**. In the above code, `a` is of the order `(2,3)` and `b` is of the order `(3,2)`. Here, `m = 2, n = 3, p = 2`. Therefore, their product will be of the order `(2,2)`, which is `(m,p)`.

### Determinant of a matrix
We can calculate the determinant of a matrix using `np.linalg.det(array)`. For example:
~~~python
a = np.identity(3)
print(np.linalg.det(a))
~~~
Since we've set `a` to an identity matrix, its determinant is `1`, which is the output of this code.

## Statistics
### Min/Max value in an array
We use `np.min` or `np.max` to find the minimum or maximum value in an array. The below code will return `1` then `6`.
~~~python
stats = np.array([[1,2,3], [4,5,6]])
print(np.min(stats))
print(np.max(stats))
~~~
We can also apply the `axis` argument set to either `0` or `1` to check the min/max value along columns or rows.

### Common statistical tools
`numpy` lets us compute the mean, median, standard deviation, variance, percentile etc. of an array.
~~~python
stats = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(np.mean(stats))
print(np.median(stats))
print(np.std(stats))
print(np.var(stats))
print(np.percentile(stats, 25))
~~~
This code will return:
~~~python
5.0
5.0
2.581988897471611
6.666666666666667
3.0
~~~

> [!Warning] Numpy doesn't have a mode function
> Unfortunately, there is no built in mode function for `numpy`. We have to rely on other libraries like `scipy.stats` for its `stats.mode` function.