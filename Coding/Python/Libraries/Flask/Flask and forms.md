---
color: var(--mk-color-teal)
tags:
  - py-libraries
---
Flask can be used in combination with the [[Forms|form]] tag to process data in a dynamic way.

Quick access:
[[Flask and forms#Handling incoming data|Handling incoming data]]
[[Flask and forms#Conditional answers based on user input|Conditional answers based on user input]]
[[Flask and forms#Requesting url arguments for GET|Requesting url arguments for GET]]


### Handling incoming data
Although we included the `action = /process` property in our `<form>` tag, we haven't made `@app.route('/process')` yet. When we create the `/process` route, *we need to mention the method POST (in all caps).* To do this, we need a new import called `request`. Once we do that, we can define the subroutine under `/process`. Our code looks like:
~~~python
from Flask import Flask, request

@app.route('/process', methods=["POST"])

def process():
  return request.form
~~~
The `request.form` command will return all the user's choices in the form of a dictionary.

### Conditional answers based on user input
Since `request.form` saves all the user's choices in a dictionary, **we can load it into a variable and give our output based on their inputs.** For example:
~~~python
def process():
  page = ""
  form = request.form

  if form["baldies"] == "david":
    page += f"You're alright {form['username']}"
  else:
    page += f"You've picked wrong {form['username']}"

  return page
~~~
Here, we have a blank variable called `page` and we set the variable `form` as the `request.form` dictionary. **Remember we had to name each `<input>` or `<select>` tag? We use those names to reference the specific tag (i.e. form question) here.** So we use `form["name"]` to load the user's choice from the dictionary and we can then use `if-else` statements to compare and give a conditional output.

### Requesting url arguments for GET
If you import `request` along with `Flask` at the start, you can use `request.args` to pull any arguments from the URL.
~~~python
@app.route('/', methods=["GET"])
def index():
  return request.args
~~~
If you run this in the default `/` url which has no arguments, you get an empty dictionary.
![[Pasted image 20240614121617.png]]
*If you manually add arguments to the url, they will appear in the dictionary.* Add `?` before the first variable and `&` between variables. Example:
![[Pasted image 20240614121757.png]]

We can also use `if` statements to personalize the variables in the url. Example:
~~~python
@app.route('/', methods=["GET"])
def index():
  get = request.args
  if get["name"].lower() == "david":
    return "Hello baldie"

  return "No data"
~~~
Here, we set the variable `get` to be the dictionary output of `request.args`. Now if the url has the variable `name` set to `david`, then it prints out a personalized message. *Using an `else` statement is optional here* since it will default to `No data` if the `if` condition isn't met.

 **If the variable is not provided in the URL, attempting to access it directly with`get["variable"]` will raise a [[Errors#4. KeyError|KeyError]]**, leading to a bad request response from Flask.