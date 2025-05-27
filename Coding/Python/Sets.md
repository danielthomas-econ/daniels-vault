---
color: var(--mk-color-green)
tags:
  - py-syntax
sticker: lucide//git-merge
---
Sets are another collection datatype in Python, similar to tuples, lists and dictionaries. What makes sets different is that they are **unique, unordered and mutable.** Since they are unordered, they also *cannot be accessed through an index* like [[Coding/Python/Lists|lists]] can. Sets are defined using `{}` like [[Dictionaries|dictionaries]], but we store single values and not pairs. Eg: `set = {1,2,3}`.
If we define a set with duplicate values, it will automatically discard them and print a set with only unique values. Eg: Printing `set = {1,2,3,1,2}` will print `{1,2,3}`.

Quick access:
[[Sets#The set() function|The set() function]]
	[[Sets#Creating an empty set|Creating an empty set]]
[[Sets#Union, intersection and difference|Union, intersection and difference]]
	[[Sets#Symmetric difference|Symmetric difference]]
	[[Sets#Update method|Update method]]
[[Sets#Subsets and Supersets|Subsets and Supersets]]
[[Sets#Disjoint sets|Disjoint sets]]
[[Sets#Frozen sets|Frozen sets]]

---
## Important methods
- We can *add items to a set* using `set.add(item)`. We cannot specify any index to place the item in since sets are unordered.

- We can *remove elements from a set* using `set.remove(item)`. We can also use `set.discard(item)`. The main difference is that `.discard()` **will not raise a [[Errors#4. KeyError|KeyError]] if the item isn't found in the set.** `.remove()` will simply raise a `KeyError` and exit the program if you enter an item that isn't in the set.

- We can *remove all items from a set* using `set.clear()`.

- We can *remove a random item* using `set.pop()`. Since sets are unordered, there is no last item which `.pop()` can remove. Therefore, it will arbitrarily pick a value. It returns this value and then removes it from the set.

- We can *create a copy of a set* using `set1 = set2.copy()`. Using `set1 = set2` is bad because any changes in `set1` will also affect `set2`. Using the `.copy()` method ensures that the original set is not affected.
---
## The set() function
Unsurprisingly, using `set(iterable_item)` converts any iterable into a set. However, things get a little interesting because of the properties of a set.

The first property is *sets are unique.* If we pass any iterable item with duplicates through a set, it will **remove the duplicates and return a set with unique items.** For example:
~~~python
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)
~~~
will output `{1, 2, 3, 4, 5}`, eliminating the duplicate `2` and `4`. This also works on strings. If we run `set("Hello")`, it returns `{'o', 'H', 'e', 'l'}`. *We can see that the duplicate `l` has been removed and the letters are jumbled up.* This brings us to the second property of sets, they are **unordered.** Due to this property, the set will print letters in an arbitrary order, since order doesn't matter.

### Creating an empty set
We face a small problem when creating an empty set, as *both dictionaries and sets are defined by* `{}`. Therefore, if we simply type `myset = {}`, **Python will always assume it is a dictionary.** To create an empty set, we must use `myset = set()`. Assigning no arguments to `set()` tells Python that the variable `myset` is an empty set.


## Union, intersection and difference
These operations on sets in Python are *just like their mathematical definitions.* Let us assume three sets:
~~~python
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}
~~~
To calculate the union of two sets, we use `set1.union(set2)`. If we run `evens.union(primes)`, we get `{2, 3, 4, 5, 6, 7, 8}` (remember, no duplicates).

If we run `odds.intersection(evens)`, we get `set()` as the output, signifying a null set with no elements in it since there are no common terms in the sets.

The **difference of two sets is calculated by removing all common elements and returning the first set.** Here, the order of writing the sets matters. If we run `evens.difference(primes)`, we get `{4, 6, 8}`. On the other hand, running `primes.difference(evens)` gives us `{3, 5, 7}`. *Therefore, difference of two sets is not commutative (just like subtraction).* 

### Symmetric difference
There is another method called `.symmetric_difference()`. In simple terms, **it is the union of two sets minus their intersection.** Mathematically, we can write it as $A\Delta B = A\cup B - A\cap B$. ($\Delta$ denotes symmetric difference).

We can see difference between evens and primes (both ways) above. Running `evens.symmetric_difference(primes)` gives us `{3, 4, 5, 6, 7, 8}`. This is completely different from the regular difference method. 

> [!Important] Symmetric difference is commutative
> Unlike the regular difference method, the order of sets in symmetric difference doesn't matter. Therefore, $A\Delta B = B\Delta A$. This is because the symmetric difference of two sets is just their union minus their intersection. Since **both union and intersection are commutative operations, symmetric difference is also commutative.**

### Update method
`set1.update(set2)` is like *the union of the sets, but it modifies `set1` to the union.* If we just use the `union` method, it returns a new set, and `set1` stays the same. Example:
~~~python
set1 = {1,2,3,4,5,6,7}
set2 = {1,3,5,7,9,11,13}

print(set1)

set1.update(set2)
print(set1)
~~~
will give us the output:
~~~python
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7, 9, 11, 13}
~~~
We've print `set1` twice, once before the `update` method and once after. *Although we print `set1` both times, we can see its been updated to the equivalent of `set1.union(set2)`*.

We can do this for other operations using `.intersection_update`, `.difference_update` etc. instead of just `.update`.

## Subsets and Supersets
We can check if `set1` is a subset of `set2` using `set1.issubset(set2)`. 
~~~python
set1 = {1,2,3,4,5,6,7}
set2 = {1,3,5}

print(set1.issubset(set2))
~~~
The above code will return `False` since `set1` is not a subset of `set2`. This is because **there are elements in `set1` that aren't in `set2`, like `4,6,7`**. If we flip the command to `print(set2.issubset(set1))`, then it will return `True` because *all elements in `set2`, i.e. `1,3,5`, can be found in `set1`*. This makes `set2` a subset of `set1`.

**Supersets are the opposite of subsets.** If `set2` is the subset of `set1`, then `set1` is the superset of `set2` *because it contains all elements of `set2` (and more).* We use the `.issuperset()` method to check for supersets.

## Disjoint sets
`set1` is said to be disjoint from `set2` if *their intersection is a null set.* In other words, the two sets are disjoint if they have no common elements. Example:
~~~python
set1 = {2,4,6,8,10}
set2 = {1,3,5,7,9}

print(set2.isdisjoint(set1))
~~~
This code will return `True` because there isn't a single common element between `set1` and `set2`. **However, if I update `set1` to have the item `1`, then the sets are no longer disjoint because they have the common element `1`**.

## Frozen sets
Frozen sets are *sets which cannot be changed after their creation.* In other words, they have the **immutability property,** like a [[Tuples|tuple]]. The main difference between tuples and frozen sets are that tuples are ordered, while frozen sets are unordered. We can create a frozen set using `set1 = frozenset({1,2,3,4,5})`. The argument passed through `frozenset` can be *any iterable item,* like a list, string or another set. Printing a `frozenset` will return `frozenset({1, 2, 3, 4, 5})`.

You cannot run any operation on a frozen set that violates the immutability property. So operations like `.add()`, `.remove()` or `.update()` will not work because they change the set itself. However, *operations like union and intersection will work because the set stays the same after the operation.*


