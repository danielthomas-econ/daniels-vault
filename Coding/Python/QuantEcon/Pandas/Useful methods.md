---
color: var(--mk-color-yellow)
tags:
  - quantecon
---
Quick access:
- [[#Index column|Index column]]
	- [[#Index column#Adding an index|Adding an index]]
	- [[#Index column#Referencing an index|Referencing an index]]
	- [[#Index column#Removing an index|Removing an index]]
- [[#Renaming columns|Renaming columns]]
- [[#Sorting values|Sorting values]]

## Index column
### Adding an index
By default, `pandas` adds a serial number column to index your dataframe. You can instead use a column in your dataframe as the index column using `df.set_index(column_name)`.

### Referencing an index
**You cannot reference an index column like you do with a normal column.** Instead, you can reference it using `df.index`. There is no need to specify its name.

### Removing an index
You can use `df = df.reset_index()` to remove a column from being the index.

## Renaming columns
`df.rename(columns={'old_name': 'new_name'}, inplace=True)`

You can also use `df.columns = [list of new names]`, but then the list must have the same number of elements as the number of columns in the dataframe.

## Sorting values
`df.sort_values(by='column_name', ascending=True/False')` - Sorts in ascending/descending order for the given column.