---
color: "#20bf6b"
sticker: lucide//curly-braces
tags:
  - py-syntax
---
Quick access:
- [[#Dictionary|Dictionary]]
- [[#Important methods|Important methods]]
	- [[#Important methods#[[Errors#2. SyntaxError|SyntaxError while using f-strings|[[Errors#2. SyntaxError|SyntaxError while using f-strings]]
- [[#Dictionaries and loops|Dictionaries and loops]]
- [[#2D dictionaries|2D dictionaries]]
	- [[#2D dictionaries#Accessing single items|Accessing single items]]

## Dictionary
Dictionaries are similar to lists, but it *gives each value a key* and links them. These are written as `key:value` pairs. Dictionaries are defined using curly brackets `{}`. However, we still use `[]` when printing an item from a dictionary. Example:
~~~python
myUser = {"name": "David", "age": 128}
print(myUser["name"])
~~~
Here, the **key = name, value = David.** If we want to print David, we should ask Python to print the key `name` from the dictionary `myUser`. To change a value in a dictionary, we use `dictionary[key]="value"`. 
Example: `myUser["name"] = "The legendary David"` changes the value of `name` from David to The legendary David.

----
## Important methods
- We can *remove a key* using `dictionary.pop('key')` or `del dictionary['key']`.

- We can *access all keys or values* using `dictionary.keys()` or `dictionary.values()`, which will return a list containing all keys/values.

- We can *access all keys and values* using `dictionary.items()`, which returns a list of tuples of all keys and values. It is mostly **used for iterating over both keys and values** in a loop.

- We can *copy a dictionary* using `newdict = olddict.copy()`. Don't simple use `newdict = olddict`, as any changes in `newdict` will also reflect in `olddict`.

- We can *merge two dictionaries* using `dict1.update(dict2)`. Assume `dict1` had the keys `name, age, email` and `dict2` has the keys `name, age, city`. Using the command will **update `dict1` to have all 4 keys, including `city`. Additionally, the values of `name` and `age` will be overwritten and will be the values found in `dict2`**.
---

### [[Errors#2. SyntaxError|SyntaxError]] while using f-strings
~~~python
myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser["name"]} and your age is {myUser["age"]}")
~~~
This code will not run and gives the following error:
~~~python
  File "main.py", line 3
    print(f"Your name is {myUser["name"]} and your age is {myUser["age"]}")
                                  ^
SyntaxError: invalid syntax
~~~
When printing dictionaries using `f-string`, we should define `name` in single quotes. Using `{myUser['name']}` will output what we intend.

## Dictionaries and loops
Dictionaries are slightly harder to use with loops compared to using lists and loops. This is because a dictionary has two parts: the key and its value. If we try to print a dictionary like how we print a list, *we'll only get the values and not the key.* Using `dictionary_name.values()` isolates the `value` datatype and again only prints values without a key.
~~~python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
for i in myDictionary:
  print(myDictionary[i])

myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
for value in myDictionary.values():
  print(value)
  ~~~
If we want to print both key name and value, we need to use the `dictionary_name.items()` function like this:
~~~python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}: {value}")
~~~
We define two variables `name` and `value` in the loop and use `f-strings` to print it out. This gives us our desired output:
~~~python
name: Ian
health: 219
strength: 199
equipped: Axe
~~~

You can use nested if statements to make comments about a certain key or value. This `if` statement must be within our printing `for` loop. 
~~~python
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
~~~
Here, Python will print all values of `name` until it comes across `name = strength`. Then, it'll run the nested if statement and give a comment based on the value of strength.

This code creates a blank dictionary called `website` at the start by assigning all values to None. Then it creates a `for loop` where it uses the `dictionary_name.keys()` function to **access all keys in the dictionary** `website`. Then, it uses an `f-string` to print an `input` statement using the key value. Lastly, it prints out the names and values in the dictionary.
~~~python
website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")
  ~~~

## 2D dictionaries
2D dictionaries can have *subkeys and subvalues.* This means each `key` can have a `value` which is a full dictionary itself. Within the `value` dictionary, each `key` is called a `subkey` and each value is a `subvalue`.

To dynamically add to a 2D dictionary, we use `listname[row_name]={key:value, key:value, ....}`. It is the same as adding to a normal dictionary, but this time `row_name` is the name of the new `key`, and we are setting its `value` to an entire dictionary.

~~~python
clue = {}
def prettyPrint():
  print()
  for key, value in clue.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key, end=": ")
    for subKey, subValue in value.items():
      # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
      print(subKey, subValue, end=" | ")
    print()
    
while True:
  name = input("Name: ")
  location = input("Location: ")
  weapon = input("Weapon: ")

  clue[name] = {"location": location, "weapon":weapon} 

  prettyPrint()
  ~~~
The `prettyPrint()` subroutine here shows how to print these dynamic dictionaries. It starts off by going through every `key:value` pair in `clue.items()` and prints the `key`. This is the **main key** and its value is a dictionary. The nested `for` loop checks the `subkeys` and `subvalues` within each main `key` and prints them. We are essentially *running two normal dictionary printing for loops* because we have a dictionary inside a dictionary.

### Accessing single items
To access single items in 2D dictionaries, we just *use two square brackets,* just like normal dictionaries.
~~~python
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"])

print(courseProgress["Erica"]["daysCompleted"])
~~~
Here, we have three dictionaries `john`, `janet`, and `erica`. We create a 2D dictionary called `courseProgress` and store each dictionary within that. If we want to access Erica's information, we `print(courseProgress["Erica"])`. This prints the entire dictionary associated with the `key` `"Erica"`. Therefore, the output will be the same as line 3. 

To access a single item within each dictionary, use line 9. It tells Python to search for the `key` `"daysCompleted"` within the dictionary associated to the `key` `"Erica"`.