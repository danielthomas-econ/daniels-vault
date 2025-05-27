---
color: var(--mk-color-yellow)
tags:
  - quantecon
---
Quick access:
- [[#Selecting data|Selecting data]]
	- [[#Selecting data#Slicing notation|Slicing notation]]
	- [[#Selecting data#List notation|List notation]]
	- [[#Selecting data#Selecting rows and columns simultaneously|Selecting rows and columns simultaneously]]
	- [[#Selecting data#Conditional selection|Conditional selection]]
- [[#Query|Query]]
- [[#Creating subsets|Creating subsets]]
- [[#Apply|Apply]]
- [[#Changing dataframes|Changing dataframes]]


Dataframes are basically very optimized excel spreadsheets.
## Selecting data
### Slicing notation
`df[2:5]` - Selects rows from index 2 to index 4.

### List notation
`df[['country','tcgdp']` - Selects the columns by passing the names of columns as arguments

### Selecting rows and columns simultaneously 
`df.iloc[row_slice, column_slice]` or `df.loc[row_slice, [list of column names]]` - Two ways to select a set of rows and columns. When using `df.loc`, you don't need to put the `row_slice` in square brackets

### Conditional selection
`df.loc[df.column_name > condition]` - Selects only those rows where the value of the column is greater than the condition.


## Query
Queries are a nice way to use conditional selection in a easy to understand manner. Eg: `df.query("country in ['Argentina', 'India', 'South Africa'] and POP > 40000")`


## Creating subsets
Real world data is usually massive and will have many columns that we simply do not need. To make our work more computationally efficient, its best to get rid of those columns. 

We can create a subset of the dataset by just creating a new `dataframe` entirely. Eg:
~~~python
df_subset = df[['country', 'POP', 'tcgdp']]
df_subset
~~~
This creates a dataset with just these three columns. You can also save it into a csv for later use using `df_subset.to_csv('pwt_subset.csv', index=False)`.

## Apply
`df.apply(function)` is a method to apply a function to all the columns in the dataset. Alternatively, you can also specify a list of columns to `df` and then use `apply`, and it'll apply the function to all those columns. Eg: `df.apply(max)`

We can also use `df.applymap(function)` to apply the function *to all individual entries* in the dataset. Eg:
~~~python
# replace all NaN values by 0
def replace_nan(x):
    if type(x)!=str:
        return  0 if np.isnan(x) else x
    else:
        return x

df.applymap(replace_nan)
~~~

## Changing dataframes
`df.where(condition, replacement)` - It keeps the rows that we select through the condition and replaces all other rows with the `replacement` argument. Eg: `df.where(df.POP >= 20000, False)`.