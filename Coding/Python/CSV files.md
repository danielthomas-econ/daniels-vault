---
color: "#20bf6b"
sticker: lucide//file-spreadsheet
tags:
  - py-syntax
---
CSV files are a way of *storing spreadsheets as text files.* Each item in a CSV is separated by a comma. CSV is short for "Comma Separated Values".

Since CSV's are very common, there are Python libraries we can use to handle these files. This is the basic code required to open and read a CSV file in Python:
~~~python
import csv # Imports the csv library

with open("January.csv") as file: # Opens the csv file
  reader = csv.reader(file) # reads the contents of the csv file into the 'reader' variable
  line = 0

  for row in reader: # loop to output each row in the 'reader' variable one at a time.
    print (row)
    ~~~
However, the output looks very ugly here as it is directly printing the raw data from the CSV without any additional formatting. We can improve the look of our output by using the `.join()` function. 
~~~python
for row in reader: 
	print (", ".join(row)) # adds a comma and space and then joins data
~~~
In this code, Python goes through every row in the `reader` variable (where we stored the CSV), and **will print the data followed by a comma and a space, and continue printing in this format for all the items in the row.** This makes our output look much more neat.

## Using CSVs as dictionaries
We can use similar logic with CSVs as we do with [[Dictionaries|dictionaries]] by using the `.DictReader()` function. Example:
~~~python
import csv # Imports the csv library

with open("January.csv") as file: 
  reader = csv.DictReader(file) # Treats the file as a dictionary 
  line = 0
  for row in reader: 
    print (row["Net Total"])
~~~
Previously, we set the value of the `reader` variable to `csv.reader(file)`.  This does read all the contents of the CSV, but with `csv.DictReader(file)`, we can treat this CSV as a dictionary. Now if we print `(row["Net Total"])`, it will go through all the values associated with the `key` `"Net Total"` and print only those values out. This is *useful if we want to print out only a certain row or column.* 

We can then add `total += float(row["Net Total"])` within the loop and print it with `print(f"Total: {total}")`. This keeps a running total of the "net total" value. It also **converts out data to a float because even numbers are stored as text in CSVs.**


