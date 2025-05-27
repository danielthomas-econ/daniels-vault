---
color: var(--mk-color-orange)
tags:
  - ai-ml
---
Quick access:
[[Indexing and Boolean masking#What is Boolean masking?|What is Boolean masking?]]
[[Indexing and Boolean masking#Boolean indexing|Boolean indexing]]
	[[Indexing and Boolean masking#Inverting your arguments|Inverting your arguments]]
	[[Indexing and Boolean masking#Remember the parentheses|Remember the parentheses]]

## What is Boolean masking?
Boolean masking is the process of *creating a boolean array where each element represents `True` or `False` based on a given condition.* We can use this array to manipulate only the elements which meet (or don't meet) the specified criteria. Example:
~~~python
data = np.genfromtxt('data.txt', delimiter = ',')

print(data > 50)
~~~
I'm taking the same `data.txt` file we've used before, and applying the condition `> 50`. This will **output a boolean array and will show the result for each element.**
~~~python
[[False False False False  True  True False False False False False False
  False False False False False False]
 [False False False False  True  True False  True False False False False
  False False False False False False]
 [False False False False  True False False False  True False False False
  False False False False  True  True]]
~~~

## Boolean indexing
Indexing in `numpy` allows you to access and manipulate elements of an array. When combined with boolean values, *we can perform condition-based selections.*

The boolean array above simply shows `True` or `False` for each element. To select all elements greater than 50, we can use:
~~~python
data = np.genfromtxt('data.txt', delimiter = ',')

condition = data[data > 50]

print(condition.astype(int))
~~~
This code tells Python to create an array called `condition` by **going into the array `data` and only selecting the values greater than 50.** Now we've created a new array only with values greater than 50. Therefore, *its output will give us numerical values,* not just the boolean output.
~~~python
[196  75 766  75  55 999  78  76  88]
~~~

We can also use *multiple arguments* using `&`. For example, we can print all values greater than 50 but less than 100 using 
~~~python
condition = data[(data > 50) & (data < 100)]
~~~
This will return the array `[75 75 55 78 76 88]`, which clearly meets the criteria.

### Inverting your arguments
Using the `~` symbol before your argument means *Python will query the exact opposite argument.* Therefore, if you run `data[~(data > 50)]`, you will get all values that **are not** greater than 50. Therefore, the output will be:
~~~python
[ 1 13 21 11  4  3 34  6  7  8  0  1  2  3  4  5  3 42 12 33  4  6  4  3
  4  5  6  7  0 11 12  1 22 33 11 11  2  1  0  1  2  9  8  7  1]
~~~


### Remember the parentheses
Simply using `data[data > 50 & data < 100]` will not work, and will return a very long [[Errors#9. TypeError|TypeError]] message.
~~~python
TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe'
~~~
This is because the ***`bitwise and` operator `&` has higher precedence than relational operators like `>` and `<`***. This means our expression will be interpreted as `data[data > (50 & data) < 100]`. Python will *group the terms nearest to `&`, but now our argument doesn't make sense.* This is why we must put each argument within parentheses, as it avoids this conflict with operator precedence.