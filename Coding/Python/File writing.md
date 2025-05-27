---
color: "#20bf6b"
sticker: lucide//file-terminal
tags:
  - py-syntax
---
Quick access:
- [[#Types of modes:|Types of modes:]]
- [[#Reading from a file|Reading from a file]]
- [[#Autosave|Autosave]]
- [[#Autosave#try and except command|try and except command]]
- [[#Handling errors|Handling errors]]
- [[#Handling errors#Traceback mode|Traceback mode]]

When we normally input variables in Python, the *data is stored to the device RAM.* The problem here is that once the program has finished executing, the RAM is erased and we have to re-enter all the information. To avoid this tedious task, we can *save the information to files instead,* which are **stored on our disk** and not wiped out after execution. We can do this using the following code:
~~~python
f = open("savedFile.txt", "w")
f.write("Hello there")
f.close()
~~~
The first line has a lot of syntax. It must be written in the format `variable = open("fileName.fileType", mode)`. 
### Types of modes:
- `w` - **Write:** Opens file for writing, *creates one if it doesn't exist* 
- `w+` - **Write and read:** 
- `r` - **Read:** Opens the file for reading (default)
- `r+` - **Read and write:** Opens the file for reading and writing
- `a` - **Append:** Add to the end of the file
- `a+` - **Append or create:** Add to the end of the file, *creates one if it doesn't exist*
- `b` - **Binary mode:** Stores data other than text like images/videos, *cannot be used alone*
- `wb` - **Write and binary mode:** Combines write and binary to *create/overwrite a file* with binary data

Line 2 using `f.write` writes the string to the end of the file. `f.close` saves the file to your system. We can use `a+` and f-strings to make our text files look better. Right now, if we add an input, it keeps being added to the same line. We can use `f-strings` and `\n` to **add new inputs to the next line.** 
~~~python
f = open("newsavedFile.txt", "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
~~~

## Reading from a file
~~~python
f = open("filenames.list", "r")
contents = f.read()
f.close()

contents = contents.split()

print(contents)
~~~
We open the file as normal, but we use `r` permission for read only. Using `f.read()` will load the contents of the file into a variable called `contents`. Once we do that, we can close the file to save RAM and print `contents` if we want to.

We can also use the `.split()` command on `contents`. This will *break up each line of the file into a row in a list.* This helps us examine separate items easily.

If you want to *only read one line,* simply replace `.read()` with `.readline()`. We can also use `.readline().strip()` if we want to remove the empty line between each new line in the file. We can turn this into a loop to individually print out each line from the file.
~~~python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  
  if contents == "":
    break
  #The last line in the file will be a blank
  #We break the loop if the line read is a blank

  print(contents)
  # Moved the print after the break so it won't output the final blank line.

f.close()
~~~

## Autosave
Below is an example of code using an autosave. We use `f.write()` and `f.close()` right at the end of the `while` loop so that *upon completing one cycle, the data is automatically saved* before Python starts the next cycle of the loop.
~~~python
myEvents = []

def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event,date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)

  f = open("calendar.txt", "w")
  f.write(str(myEvents)) # Need to cast the list to a single string
  f.close()

  ~~~

However, there is a problem here. Since we start the code with `myEvents = []`, **the list gets reset every time we run the program.**  To solve this, we can load pre-existing data into the list at the start. We can do this with the `eval()` function. It runs the code in brackets and returns the working code. In the below example, it runs `f.read()` and *outputs the data from the file.* This output is then set as the value of the `myEvents` list, so that our data is not overwritten every time.
~~~python
myEvents = []

f=open("calendar.txt","r") 
myEvents = eval(f.read())
f.close()
~~~

### try and except command
The problem with the code above is that if the file `calendar.txt` doesn't exist, your code will crash and give the error message `FileNotFoundError: [Errno 2] No such file or directory`. To avoid this, we can use the `try` and `except` command.

The syntax for this command is like an `if-else` statement. **First, you write `try:` and then Python will try to run the indented code. If it fails for any reason, it will move on to the code under the `except:` block.**  Example:
~~~python
myStuff = []

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()

except:
  print("ERROR: Unable to load")
  ~~~
Here, Python will first run the code under the `try` block. If the file `stuff.mine` doesn't exist, that code will crash. **Thanks to the `try` block, this piece of code crashing doesn't break the whole program.** If `stuff.mine` doesn't exist, Python will simply run the code under the `except` block and print our own error message without breaking our code.

## Handling errors
`try` and `except` are great, but they have one big issue: *they don't tell you what the problem is.* To fix this, **we can tell `except` what kind of errors to look for.** 

Using `Exception` (with a capital E) tells `except` to look for every possible error message. We can then store the output of `Exception` in a variable and print it.
~~~python
myStuff = []

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()

except Exception as err:
  print("ERROR: Unable to load")
  print(err)
  ~~~

While the previous code would simply say `ERROR: Unable to load`, this will print out the exact error. *The value of `Exception` is stored in the variable `err`, and we can print it to find out the problem.* Using this code, we get the output shown below, which is much more useful for fixing these errors.
~~~python
ERROR: Unable to load
[Errno 2] No such file or directory: 'Stuff.mine'
~~~

### Traceback mode
We can even get rid of the `err` variable and **print out the entire traceback message,** which is the red error tracing Python prints, if we want. To do this, *we can set a variable called `debugMode` to `True` or `False`*. This lets us quickly change if we want to show the traceback or not using this one variable. Using an `if` statement within the `except` block, we can check if `debugMode` is set to `True` and then print the whole error message.
~~~python
debugMode = True
myStuff = []

try:
  f.open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()

except Exception:
  print("ERROR: Unable to load")

  if debugMode:
    print(traceback)
  ~~~
This will give us the following output:
![[Pasted image 20240502101443.png]]

