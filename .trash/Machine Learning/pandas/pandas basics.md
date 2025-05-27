---
color: var(--mk-color-orange)
tags:
  - ai-ml
---
`import pandas as pd` allows you to create dataframes and is the basis of data analysis with Python.

Quick access:
[[pandas basics#Reading a file|Reading a file]]
[[pandas basics#Print the start of a dataframe|Print the start of a dataframe]]
[[pandas basics#Print random rows|Print random rows]]
[[pandas basics#View dataframe info|View dataframe info]]
[[pandas basics#View dimensions of the dataframe|View dimensions of  the dataframe]]
[[pandas basics#Find the max/min value|Find the max/min value]]
[[pandas basics#Get a statistical description of your dataframe|Get a statistical description of your dataframe]]
[[pandas basics#Sorting columns|Sorting columns]]
[[pandas basics#Find the frequency of certain data points|Finding the frequency of certain data points]]
[[pandas basics#Creating a new column|Creating a new column]]

## Reading a file
`df = pd.read_csv('file.csv', index_col=' ')` - Stores the value of the csv into the variable `df`.  The parameter `index_col` is used to *define the first column of the dataframe.* 

## Print the start of a dataframe
`df.head(number)` - Prints the first few rows and columns of the table instead of the whole thing. We can just use `df.head()` or specify a number of rows to be printed.

## Print random rows
`df.sample(number)` - Prints one random row in your dataframe or a specified number of random rows.

## View dataframe info
`df.info()` - Shows some important information about your dataframe like columns, number of characters, datatypes etc. Example:
~~~python
<class 'pandas.core.frame.DataFrame'>
Index: 172821 entries, aa to zyzzyvas
Data columns (total 2 columns):
 #   Column      Non-Null Count   Dtype
---  ------      --------------   -----
 0   Char Count  172821 non-null  int64
 1   Value       172821 non-null  int64
dtypes: int64(2)
memory usage: 4.0+ MB
~~~

## View dimensions of the dataframe
`df.shape` - Shows you the number of columns and rows in your dataframe.

## Find the max/min value
`df['column'].max()` - Shows you the maximum value for the selected column. You can also just use `df.max()` and *find the maximum value of every single column.* `.max()` can be replaced with `.min()`.

## Get a statistical description of your dataframe
`df.describe()` - Gives you a table with statistical data for all your numeric columns. Example:
![[Pasted image 20240520143710.png]]

## Sorting columns
`df.sort_values(by=['column'], ascending = True/False)` - Sorts a certain column in ascending or descending order.

## Find the frequency of certain data points
`df['column'].value_counts()` - Prints a table showing the most and least frequent datapoints.

## Creating a new column
`df ['column'] = xyz` - Creates a new column based on the rules you give it. For example, `df['Ratio'] = df['Value'] / df['Char Count']` will create a new column called Ratio, and it will be equal to the corresponding value divided by character count.