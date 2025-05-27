---
color: var(--mk-color-teal)
tags:
---
## Flask library
`from flask import Flask` allows you to create your own web server. The reason Flask is different from just using HTML/CSS is that it can be used to build **dynamic web apps** that change depending on the user.

Quick access:
[[Flask basics#Basic Flask code|Basic Flask code]]
[[Flask basics#Add more pages|Add more pages]]
[[Flask basics#Display HTML code|Display HTML code]]
[[Flask basics#Images with Flask|Images with Flask]]
[[Flask basics#fStrings|fStrings]]
[[Flask basics#Replace|Replace]]
[[Flask basics#Links|Links]]
[[Flask basics#Templating|Templating]]
[[Flask basics#Redirecting|Redirecting]]

### Basic Flask code
~~~python
from flask import Flask # Imports the flask library

app = Flask(__name__) # Starts the Flask application. The 'app' variable is very important. We'll be using that later.


@app.route('/') # Tells the code what to do if we've gone to our web address with just a / after the URL
def index(): # Tells the code which webpage to show. This subroutine will display the 'Hello from Flask' page
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81) # This line should ALWAYS come last. It's the line that turns on the Flask server.
~~~

### Add more pages
`@app.route('/name')` - Creates a new page named after whatever comes after the `/`.

### Display HTML code
~~~python
@app.route('/home')
def home():
	page = """ All your HTML code here """
	return page
~~~
The whole point of Flask is to integrate [[HTML]] with Python. The code template above creates a subroutine called `home` under the `/home` address of our website. The contents displayed on `/home` will be the HTML code stored in the `page` variable that we print. Running this on VSCode gives:
![[Pasted image 20240610081345.png]]
We can now see the links on which our Flask website is running. Visit `link/home` to view the code under the `page` variable. 
![[Pasted image 20240610081548.png]]
The website now displays the code I entered under the `home` subroutine.

### Images with Flask
`app = Flask(__name__, static_folder="static")` - Allows you to *access locally stored images* on a Flask website. By default, Flask can only access images connected to web URLs, not local images.

This creates a folder called `static`, which is the default filename that Flask looks for. You can create any subfolders within the `static` folder. Replace the local image links with its position in the `static` folder's directory to load images on your website. 

Example: `<img src="static/images/picard.jpg" width = 30%>` will load `picard.jpg` from the `images` subfolder under the main `static` folder.

You can also use the `static_url_path` parameter instead of `static_folder`, but that didn't work for me on VS Code. Remember to add a leading `/` if using the `url_path` parameter. **If your images don't load, click [[Errors#Images don't load on Flask|here]] and check if you are facing the same problem.** 

### fStrings
Simply type `f` before the triple quotes that enclose the HTML code. This **makes the whole HTML code into a** f-string. We can define a variable inside our subroutine and then call the variable inside our HTML code. Example:
~~~python
@app.route('/home')
today = datetime.date.today()
page = f""" A lot of random text
that we can use in our
HTML website {today}."""
return page
~~~

### Replace
You can use *placeholder text in your HTML* and then use the `.replace()` function in the Flask code to add a variable there. For example, we used `<h1> {name}'s Portfolio</h1>` in our HTML. In Python, we can now use:
~~~python
myname = "Daniel Thomas"
page = page.replace("{name}", myname)
~~~
This replaces all the instances of `{name}` in our HTML with the variable `myname` we have assigned in Python.

### Links
~~~python
from flask import Flask

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
  page = f"""<html><body>
  <p><a href = "/home">Go home</a></p>
  </body>
  </html>"""
  
  return page
~~~
This creates a link within our landing page which guides users to the home page.

### Templating
The purpose of templates are to **store the HTML elsewhere** so it doesn't get too large in the main Python file. 

To do this, create a folder called `templates` (plural) and store your HTML there. Create a `static` folder with `images` and `css` as subfolders if needed. Now we should *read the HTML file* into our Python file. The process is nearly identical to [[File writing| how we write files]] in Python.

Previously, we'd store the entire HTML code in the `page` variable. This time, we will leave `page` blank and open our HTML file. Then, **we will read the contents of the HTML file into the `page` variable.** Example:
~~~python
@app.route('/')
def index():
  myName = "David"
  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  return page
  ~~~

### Redirecting
`from flask import Flask, redirect` - Adding this additional import lets you redirect users to a different link, *which is useful if the link is very long.* This way, you can effectively create your own link shortener. Example:
~~~python
from flask import Flask, redirect

@app.route('/77')
def seventySeven():
  return redirect("https://replit.com/@replit/Day-77-Solution#main.py")
  
  return page
~~~
Now instead of the long replit link, we just use `link/77` to access the same website.