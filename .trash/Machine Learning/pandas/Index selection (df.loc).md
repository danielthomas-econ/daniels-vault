---
color: var(--mk-color-orange)
tags:
  - ai-ml
---
`df.loc[]` is the basic argument used for index selection in pandas.

Quick access:
[[Index selection (df.loc)#Access a certain index|Access a certain index]]
[[Index selection (df.loc)#Finding indices with a certain value|Finding indices with a certain value]]

## Access a certain index
`df.loc['index_name', 'column_name']` - Shows you information about a certain index.  `df.loc["microspectrophotometries"]` (no column argument) will output:
~~~python
Char Count     24
Value         317
Name: microspectrophotometries, dtype: int64
~~~
This says that our index is named `microspectrophotometries`. There are two columns, `char count` and `value`, and `df.loc` shows the value of each column for the index we choose.

`df.loc[]` **can also take multiple columns as an argument, i.e. a list.** Example: `df.loc[["pinfish", "glowing", "microbrew", "enfold", "superheterodyne"]]` will output:
![[Pasted image 20240520144152.png|center]]

You can keep the list as the first argument and a column as the 2nd one using `df.loc[[list of indices], column]`.

## Finding indices with a certain value
`df.loc[df['column'] == number]` - Outputs all the indices with the column value equal to the number.

Just using `(df['column'] == number)` will return a boolean array. *It will check every single item in the column to check if it matches the number* and then prints out the whole array. By putting this whole term inside another `df.loc[]`, we are only selecting those indices which returned `True` and then printing them.
![[Pasted image 20240520145807.png]]

We can also **find indices that match two value requirements** using
~~~python
df.loc[
    (df['column1'] == num1) &
    (df['column2'] == num2)
]
~~~
