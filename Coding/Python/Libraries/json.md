---
color: var(--mk-color-teal)
sticker: lucide//file-json-2
tags:
  - py-libraries
---
JSON (JavaScript object notation) is a **text based way of describing how a [[Dictionaries#2D dictionaries|2D dictionary]] might look.** This is important when sending messages to other websites and getting a message back and decoding it. Most of the time, the *message we get back will be in JSON format, and we need to interpret it in Python as a 2D dictionary* to make sense of it. Example:

Quick access:
[[json#Basic JSON code|Basic JSON code]]
[[json#Printing readable JSON output|Printing readable JSON output]]
[[json#Output a piece of data|Output a piece of data]]
[[json#Saving images|Saving images]]

### Basic JSON code
~~~python
import requests # import the required library

result = requests.get("https://randomuser.me/api/") # ask the site for data and store it in a variable

print(result.json()) # interpret the data in the variable as json and print it.
~~~
This pulls data from the website in JSON form, and then `result.json()` converts the JSON code into a Python dictionary.

> [!Warning] The requests library isn't pre-installed
> You must use `import requests` to use the `.json()` command. The `requests` library is also not pre-installed, so you'll need to `pip install requests` to install it in your environment, and only then can you run the `.json()` command. Check [[Coding/Python/Libraries/requests]] for more info.


### Printing readable JSON output
~~~python
import requests, json #imports the json library

result = requests.get("https://randomuser.me/api/")
user = result.json() #a dictionary containing the user's data
print(json.dumps(user, indent=2)) #outputs the json to the console with an indent to make it more readable.
~~~
Using `json.dumps()` helps us print the json output in a more readable way, which looks like:
![[Pasted image 20240617104804.png]]

### Output a piece of data
From the above image, we can see the dictionary's structure and use that to *output a specific piece of information* about our user. For example, if we want to print the first and last name of a user, we can use:
~~~python
import requests, json 

result = requests.get("https://randomuser.me/api/")
user = result.json() 

name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}""" # Get the first and last names from the results dictionary and assign to a variable

print(name) # output the variable
~~~
Once again, we set the variable `user` to the dictionary output of `result.json()`. When trying to output a specific value, **understanding the dictionary structure properly is important.** `user["results"][0]["name"]["first"]` checks the dictionary `user` and goes into the `results` key first. Within results, it goes to the first key (i.e. `[0]`) and then goes to the `name` key in that. *Carefully observe the brackets to understand where a key starts and ends, and if one key is enclosed within another.* Within `name`, we can see three keys: `title`, `first` and `last`. We only need to output the `first` and `last` key, so we select those two as the last keys in our dictionary reference.

### Saving images
~~~python
image = f"""{user["results"][0]["picture"]["medium"]}""" # Get the user's profile picture and assign to a variable
picture = requests.get(image) #downloads the image
f = open("image.jpg", "wb") # opens the image.jpg file for writing in binary (data of the image will be added to the repl)
f.write(picture.content) #writes the image to the file  
f.close() #closes the file
~~~
This loads the dictionary location of the picture into the `image` variable and downloads it with `picture = requests.get(image)`. Once we have our `picture` variable, we open a file called `image.jpg` and **then use `picture.content` to write to the `image.jpg` file with the `wb` (write & binary) permission.**

### Using an external API
~~~python
import requests, json

result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) # get a random dad joke from the site endpoint and assign to a variable. The second argument (the header request) tells the script to return the json data as a string.

joke = result.json()
print(joke["joke"])
~~~
This uses the `icanhazdadjoke` API to print a random joke. The argument `headers` is within the `requests.get()` argument and **it tells the code that we don't want the website back, we want JSON data in a specific format.** Read the API documentation to understand what to use.