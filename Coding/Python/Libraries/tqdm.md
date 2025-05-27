---
sticker: lucide//loader-2
tags:
  - py-libraries
color: var(--mk-color-teal)
---
`pip install tqdm` - Allows you to create progress bars in the terminal.

Quick access:
[[tqdm#Basic use case|Basic use case]]
[[tqdm#Descriptions|Descriptions]]
	[[tqdm#Postfix|Postfix]]

## Basic use case
`from tqdm import tqdm` - Imports the `tqdm` module. *To use `tqdm` progress bars, we just wrap the function we want to track within a `tqdm()` argument.* For example:
~~~python
results = []

for i in tqdm(range(10000)):
    results.append(math.factorial(i))
~~~
This is a simple piece of code that calculates the factorial of all numbers till 10,000. Normally, we'd do `for i in range(10000)`. However, we want `tqdm` to track how far `range` has gone for our progress bar. **Therefore, we wrap `range` within a `tqdm()` argument.** Now, the `tqdm` library will display the progress of the `range` function in the terminal. It looks like:
![[Pasted image 20240713203233.png]]

We can also use `tqdm` in [[Coding/Python/Lists#List comprehension|list comprehension]] scenarios. We can get the same output if we use `results = [math.factorial(i) for i in tqdm(range(10000))]`. This implementation is *slightly faster,* running at `694 iterations/sec` and completing in 14 seconds.

> [!Important] `trange` function 
> Since functions involving range are commonly used with `tqdm`, the library comes along with a function called `trange`, which is basically a `range` function pre-wrapped in a `tqdm` argument.

## Descriptions
We can use `.set_description` to describe a `tqdm` progress bar. For example:
~~~python
with trange(1000) as t:
    for i in t:    
        t.set_description(f"Iteration number {i}")
        t.set_postfix(something = i)
        results.append(math.factorial(i))
        time.sleep(0.01)
~~~
Here, we've used `with` to call the `trange(1000)` object as `t`. *We've described the `tqdm` object using `.set_description`*. Be careful when doing this, since you can't use this method on an integer or a non-`tqdm` object.

### Postfix
We can add **extra info at the end of the progress bar** using `.set_postfix`. In the codeblock above, I've use `t.set_postfix(something = i)`. *We can use additional keyword arguments when creating a postfix,* which is why I used the variable `something` as my keyword here. You can see the `something = 999` at the very end of the progress bar here.
![[Pasted image 20240713210114.png]]
This is usually used when to display values like `loss` or `accuracy` when training AI or ML models.