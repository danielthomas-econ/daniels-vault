---
color: var(--mk-color-yellow)
tags:
  - quantecon
---
Quick access:
- [[#Creating a series|Creating a series]]
- [[#Describing a series|Describing a series]]
- [[#Indexing series|Indexing series]]


A `Series` is like a column of data.
## Creating a series
You create a series using `pd.Series(data)`. For example, `s = pd.Series((1,2,3,4))`. *Since `Series` is built on `numpy`*, *it supports many similar operations.* Eg: `np.abs(s), s*100`

## Describing a series
You can describe a series using `seriesname.describe()`. This gives you a long list of statistical info about your series.
~~~
count    4.000000
mean    -0.848639
std      0.626167
min     -1.546348
25%     -1.166150
50%     -0.901615
75%     -0.584104
max     -0.044981
dtype: float64
~~~

## Indexing series
One big advantage that `pandas` series have over `numpy` arrays is that the indices of series is more flexible. For example, we can use:
~~~python
s.index = ['AMZN', 'AAPL', 'MSFT', 'GOOG']
s
~~~
This list is now the name of each index of our series. Printing the series gives us:
~~~
AMZN   -0.689278
AAPL    0.208559
MSFT    1.384111
GOOG    0.777084
dtype: float64
~~~
In fact, *`Series` work like fast dictionaries* with the limitation that every item must be of the same type. We can even use dictionary syntax on series. Eg: `s['AMZN']` returns the value of the `AMZN` index, `'AAPL' in s` returns `True`.
