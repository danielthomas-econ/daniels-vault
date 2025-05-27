---
color: var(--mk-color-orange)
tags:
  - quantecon
---
This note goes over all the features of `np.random` I've used so far.



## Standard normal distributions
~~~python
np.random.randn(number)
~~~
`.randn` generates *independent and identically distributed* standard normal graphs, the number of which is determined by the argument passed in place of `number` above.


## Between 0 and 1
~~~python
np.random.random(number)
~~~
`.random` generates numbers in the interval `[0,1)`.

## Generating n random integers
~~~python
np.random.randint(low=a, high=b size=n)
~~~
Creates an array of random integers of length `n` elements, with the lowest value being `a` and the largest being `b`.

## Array that sums up to one
~~~python
np.random.dirichlet(np.ones(n))
~~~
Uses the *Dirichlet distribution* to create an array of length `n` that will sum up to one. *This is very useful for creating probability distributions.* The argument to the function can be anything, but using `np.ones(n)` will create a uniform random partition of 1.