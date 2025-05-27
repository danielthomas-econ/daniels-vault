---
color: "#2d98da"
sticker: lucide//database
tags:
  - py-libraries
---
## replit database
`from replit import db` allows you to store data in a replit database. Drag and drop the database icon from the left pane into one of the windows.

Quick access:
[[replit db#Storing data|Storing data]]
[[replit db#Accessing data|Accessing data]]
[[replit db#Removing data|Removing data]]
[[replit db#Accessing by prefix|Accessing by prefix]]
[[replit db#Keys and dictionaries|Keys and dictionaries]]
[[replit db#Print all keys with a loop|Print all keys with a loop]]
[[replit db#Key doesn't exist|Key doesn't exist]]

### Storing data
`db["key_name"] = key_value` - Stores the key in the database. Example: `db["test"] = "Hello there"`. Now the key `test` is stored in our database, and we do not need it for further code.

### Accessing data
`keys = db.keys()` - Stores the value of *all keys* in the variable `keys`, which can then be printed out. You can also set a variable equal to a specific key and print it out. Eg: `key = db["test"]`.

### Removing data
`del db["key_name"]` - Deletes a key

### Accessing by prefix
`var = db.prefix("key_name")` - Helps you *access all keys starting with a certain word.* This is useful if you name your keys like `login1, login2, login3` etc. If you use `matches = db.prefix("login")` and `print(matches)`, it will **print out all key names** starting with the word `login`.

### Keys and dictionaries
`db["key_name"] = {dictionary}` - Lets you set the value of a database key to a dictionary. This way *you can associate more than one value* with this key. Eg: `db["david"] = {"username": "dmorgan", "password":"baldy1"}`. We can either print out the whole dictionary or a specific key in the dictionary using 
~~~python
value = db["david"]
print(value["password"])
~~~
Here, we are assigning the variable `value` to the dictionary. To print out a certain key, we use `value["dictionary_key"]` and it will only print that out. We can also just use `print(value)`, but that outputs `ObservedDict(value={'username': 'dmorgan', 'password': 'baldy1'})`.

### Print all keys with a loop
~~~python
keys = db.keys()
for key in keys:
  print(f"{key}: {db[key]}")
  ~~~
This code loops through all keys in our database and prints it out for us. *`key` represents the name of each key,* while `db[key]` prints out its actual value.

### Key doesn't exist
Using `try-except` with the `pass` command under `except` tells Python to **just continue.** This is useful if a key we try to access doesn't exist. It would throw an error, but we can use `pass` to **bypass any error message.** However, it is better to replace `pass` with an actual error message. Using `pass` is just a *quick band-aid solution* and doesn't actually help us understand what error we are facing. Eg:
~~~python
try:
  value = db["key"]
except:
  pass
~~~
