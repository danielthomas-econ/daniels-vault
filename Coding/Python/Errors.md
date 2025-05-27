---
sticker: lucide//alert-triangle
color: "#eb3b5a"
tags:
  - errors
---
## Quick access:
[List of all exception messages](https://www.w3schools.com/python/python_ref_exceptions.asp)
### Common errors:
[[Errors#1. NameError|NameError]]
[[Errors#2. SyntaxError|SyntaxError]]
[[Errors#3. IndentationError|IndentationError]]
[[Errors#4. KeyError|KeyError]]
[[Errors#5. I/O operation error|I/O operation error]]
[[Errors#6. IndexError|IndexError]]
[[Errors#7. UnicodeDecodeError|UnicodeDecodeError]]
[[Errors#8. AttributeError|AttributeError]]
[[Errors#9. TypeError|TypeError]]
[[Errors#10. ValueError|ValueError]]

### Specific errors:
[[Errors#'clear' command not working|'clear' command not working]]
[[Errors#You get 'None' when printing an output|You get 'None' when printing an output]]
[[Errors#Lists are being duplicated when saved to a file|Lists are being duplicated when saved to a file]]
## 1. NameError
Incorrectly defined syntax, might be due to:
- getting the name of a function wrong
- you misspell it
- get the capitalization wrong

Example:
```python
Print("Hello World")
```

We get the following error:
```python
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    Print("What could go wrong?")
NameError: name 'Print' is not defined
```

We used the Print command, which doesn't exist. The right command is *print,* with a small p, not Print.

### NameError due to variable not defined
Sometimes, you might assign a variable, but when trying to print it, Python throws a NameError. Example:
~~~python
  for row in reader: 
    print (row["Net Total"])
    total += float(row["Net Total"] )

print(f"Total: {total}")
~~~
Trying to print this gives us the error `NameError: name 'total' is not defined` although we can clearly see `total` is defined. This is because **the variable is a local variable within a function or a loop.** To get around this, we must *first define it outside the loop.* We can do this by simply adding `total = 0` in the line before the `for` loop.

## 2. SyntaxError
Incorrect or incomplete syntax, might be due to:
- you have the order of the symbols wrong
- you forgot `()` or  " "

Example:
```python
print "Hello World"
```

We get the following error:
```python
  File "main.py", line 1
    print "Hello Again"
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello Again")?
```
Here we forgot to put the parentheses around our string. The SyntaxError points it out to us as well. 

If we forget the double quotes to enclose the string, we get "EOL while scanning string literal" as an error (EOL = End of Line)
```python
drink = input("Do you prefer coffee or tea?)
```

Output:
```python
  File "main.py", line 1
    drink = input("Do you prefer coffee or tea?)
                                               ^
SyntaxError: EOL while scanning string literal
```

### [[Coding/Python/Print statement#String concatenation|String concatenation]]:
```python
yourName = input("Name: ")
whatYear = input("What year is it?: ")
print(yourName "thinks it is" whatYear)
```

We get the following error:
```python
  File "main.py", line 3
    print(yourName "thinks it is" whatYear)
                   ^
SyntaxError: invalid syntax
```

We forgot the commas here, therefore we get a SyntaxError. To fix it, we use `print(yourName, "thinks it is", whatYear)`.

## 3. IndentationError
Forgot to indent the statements within an if-else argument.
```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
else:
print("Woof")
```

We get the following error message:
```python
  File "main.py", line 5
    print("Woof")
    ^
IndentationError: expected an indented block
```
Python expected the line `print("Woof")` to be one indent in as per the syntax, so we should just move it to the same indent as `print("Meow")` to fix it.

## 4. KeyError
This happens when the `key` you are trying to access is not in the dictionary. I got the following error:
~~~python
  File "d:\Daniel's Things\Coding projects\replit challenges\replitchallenges.py", line 75, in <module>
    stat1 = deck[teachername][chosen_stat] = int(deck[teachername][chosen_stat])
KeyError: 6
~~~
This is because I entered a value of `6` for the variable `chosen_stat` thinking that it will access the 6th subkey. However, Python expects to receive *the actual name of the subkey, not its number.*  Here, the 6th subkey is `Baldness`, so I should've entered that to get this code to work. 

The workaround I used here is I made a dictionary which **assigned each stat name to a number.** Now if the user inputs a number, it converts that number to the assigned stat. Eg: Inputting 6 will output `Baldness` as the value of `chosen_stat` so that I no longer encounter any `KeyError`.
~~~python
# assign the stats to a number
stat_mapping = {
                   1: "Intelligence",
                   2: "Humour",
                   3: "Looks",
                   4: "Teaching",
                   5: "Coolness",
                   6: "Baldness"
                    }

 # converts the stat number into its actual name
chosen_stat = stat_mapping[chosen_stat]
~~~

## 5. I/O operation error
~~~python
f = open("savedFile.txt", "a")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
whatText = input("> ")
f.write(f"{whatText}\n")
~~~
An I/O error happens here because Python cannot properly save the file. `f.close()` in line 4 should be after the last `f.write()` command.

## 6. IndexError
An IndexError may occur *when you modify a list while iterating over it.* Example:
~~~python
for i in range(len(inventory)):
	if item == inventory[i][0]:
		inventory.remove(inventory[i])
        print(f"{green}{item} has been removed from your inventory.{white}")
~~~

You will get the following error message which says `IndexError: list index out of range`.
![[Pasted image 20240503103551.png]]

This happens because we are **removing an item from the list `inventory` while in the middle of a loop that's iterating over `inventory`.** This changes the length of `inventory`, but the *loop is still trying to access elements based on the original length.* This can lead to an IndexError if the loop tries to access an index that no longer exists.

To fix this, we can instead **store the value of `i` that needs to be removed using a flag variable.** Example:
~~~python
for i in range(len(inventory)):
   if item == inventory[i][0]:
	   item_exists = True
       j = i # store the index of the item to remove
~~~

Now, we have stored the value of the index we want to remove in `j`. Later we can use `inventory.remove(inventory[j])` to remove the index. Since this is done outside the loop, we are not iterating over the loop again and there will be no problem here.

## 7. UnicodeDecodeError
This happens when *Python cannot decode a certain character from your file.* In my case, Python couldn't decode the byte `0x9d` because it was not a valid character in Windows `cp1252` encoding. To fix this, **we can use UTF-8 encoding instead.**  To do that, just add an extra argument when opening the file.
~~~python
with open ("replit challenges/music streaming challenge/100MostStreamedSongs.csv", encoding='utf-8') as file:
~~~

## 8. AttributeError
This happens when you *ask a function to do something it cannot do.* For example, `list.append()` works but `list.blahblah()` will not work and you'll get an `AttributeError` saying `list object has no attribute 'blah blah'`.

In my case, I used:
~~~python
tweet = input("Tweet away: ")
timestamp = datetime.now().time()
db[timestamp] = tweet
~~~
This code gave me the error `AttributeError: 'datetime.time' object has no attribute 'lstrip'`. The problem here is that `timestamp`, which is a date, was being used as a key in the database. **It is automatically converted into a string and then stripped of white spaces.** However, you can't do that to a date. To fix it, just *cast `timestamp` as a string* in the first place, so that the key can automatically strip it with no problems. To do this, use `timestamp = str(datetime.now().time())`.

## 9. TypeError
This happens when you *run operations on unsupported datatypes.* For example, trying to change a value in a [[Tuples|tuple]] will give you this error, because the `tuple` datatype doesn't support item assignment. In my case, I got the error `TypeError: quote_from_bytes() expected bytes`. The problem was I used:
~~~python
for key in range(10):
	print(f"{key}: {db[key]}"
    ~~~
This gives `key` an integer value, which doesn't work for [[replit db|replit's database.]] I had to use [[Lists#List slicing|list slicing]] to cut out the first $10$ values of the list instead of using the `range(10)` argument. My corrected code is:
~~~python
  key = list(key)
  for key in list(key)[:10]:
    print(f"{key}: {db[key]}")
~~~

## 10. ValueError
A `ValueError` in Python is when *a function receives an argument of correct type but with an inappropriate value.* It indicates that the operation or function received a value that has the right type but an unacceptable or out-of-range value. For example, trying to *unpack a list with more elements than variables* provided for unpacking can lead to a `ValueError`. Running the following code:
~~~python
my_list = [1, 2, 3]
a, b = my_list
~~~
We will get a `ValueError` because the **number of variables (values) and indices in the list (also values) do not match.**
~~~python
ValueError: too many values to unpack (expected 2)
~~~


---
## 'clear' command not working
Sometimes VSCode can give the following error when trying to use `os.system('clear')` : 'clear' is not recognized as an internal or external command,
operable program or batch file.

This is because `clear` is used for Unix based devices and `cls` is used for Windows. In this situation, replace it with `os.system("cls" if os.name == "nt" else "clear")`


## You get 'None' when printing an output
Sometimes you can get the word "None" at the end of your output like this:![[Pasted image 20240415105609.png]]
This is because you are printing a certain subroutine, and by default Python tries to print its output. If you don't include a `return` argument in the subroutine, Python doesn't know what to print and prints "None".
![[Pasted image 20240415105719.png]]
My code is correct here, the problem is the subroutine `textcolor`. ![[Pasted image 20240415105807.png]]
I fixed this by adding a null `return` at the end of the subroutine. This way, every time `textcolor` is called, it returns a null value at the end so Python doesn't print "None" in my final output. The new output looks like this:
![[Pasted image 20240415105912.png]]

## Lists are being duplicated when saved to a file
My input was "Sword, Shield, Sword", which is meant to be saved as a 2D list in `inventory.txt`. However, the file saved it as seen below![[Pasted image 20240503090306.png]]
To fix this, change the [[File writing#Types of modes:|file permission]] from `a` to `w`. The problem was that when you use `append`, *Python doesn't erase the contents of the file and just adds to the end of it.* Therefore, my list was just added over again and again. Using `write` **erases the old contents and replaces it with the new value of the `inventory` list,** therefore eliminating any duplicates.

## Images don't load on [[Flask]]
I spent nearly an hour trying to figure out why my Flask app didn't load local images from `static`. The problem was that *Flask looks for static in the `/` directory.* At first, I didn't understand what this meant, but it just means it looks for `static` in the same directory as your flask app.

My flask app (`replitchallenges.py`) was in the `Coding projects/replit challenges` directory, but `static` was in the `Coding projects/html` directory. Therefore, for Flask to access `html`, **it should go one directory upward then into the `html` folder.** We can do this by using `app = Flask(__name__, static_folder='../html/static')`.

> [!Important] Navigate up one path directory
> In commonly used file system notation, we use `..` to move up one directory. Since the `static_folder` parameter now starts with `..`, Flask first moves out of `replit challenges` (where our app is) and goes up to `Coding projects`. Then it goes down to `/html/static`. 
> To move up two levels in a directory, you would use `../../`, and to move up three levels, you would use `../../../`. **Each `../` moves up one level in the directory structure from the current directory.**
> Remember this notation because it could be useful in other situations too.

