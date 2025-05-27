---
color: var(--mk-color-pink)
sticker: lucide//form-input
tags:
  - html-syntax
---
The `<form>` tag in HTML is used to *create an HTML form for user input.* The data we collect is useless if we cannot see it. To see the data, we use the `post` and `action` methods to send our data to a specific location. We do this by:
~~~html
<form method = "post" action = "/process">
    
</form>
~~~
This takes the data we have collected in the form and uses the `post` method to send our data to the `/process` url using the `action` command.

Quick access:
[[Forms#Input|Input]]
[[Forms#Buttons|Buttons]]
[[Forms#Dropdown menus|Dropdown menus]]

#### To process the form data using Flask, click [[Flask and forms#Handling incoming data|here]]
## Input
`<input>` tags obviously collect user input. They have many different types so that we can collect different datatypes. **Every `<input>` tag must have a `name` property,** as it acts like an identifier. Example:
~~~html
<form method = "post" action = "/process">
    <p>Name: <input type="text" name="username"> </p>
</form>
~~~
This creates a little box with the text "Name" beside it.
![[Pasted image 20240612125512.png]]
The `name` property is simply used to *identify* this specific input box, and it isn't visible to the user. **Only the text within the `<p>` tag can be seen by the user.** Once we type in our data and hit enter, it sends our data to the `url/process`. Right now, it gives us an error as we haven't prepared that link yet.

Sometimes, we have **required fields** that the user must enter, and optional fields. To make this distinction, we can use the `required` property of the `<input>` tag:
~~~html
<p>Name: <input type="text" name="username" required> </p>
~~~

We can see many different types of input boxes here, like `text`, `Email`, `url`, `number` and `hidden`. The `hidden` tag is used when you have some *important data for the backend that the users don't need to see.* The `password` tag hides the user's input with dots and has an option to view the text.
~~~html
<form>
    <p>Name: <input type="text" name="username"> </p>
    <p>Email: <input type="Email" name="email"> </p>
    <p>Website: <input type="url" name="website"> </p>
    <p>Age: <input type="number" name="age"> </p>
    <p>Password: <input type="password" name = "pwd"> </p>
    <p><input type="hidden" name="userID" value="232"> </p>
    
  </form>
~~~

## Buttons
Unsurprisingly, the tag for creating a button is `<button>`. In code, it looks like:
~~~html
  <button type="submit">Save Data</button>
~~~
Just like `<input>`, the `<button>` tag also has a `type` property. Once we add all the boxes in the above example and our button, our form will look like this:
![[Pasted image 20240612130120.png]]
Buttons can be of `submit`, `reset` or `button` type. `submit` is the default type and submits the user data when clicked. `reset` sets all inputs back to their original value. *`button` is used as a placeholder for custom behaviors* (usually defined by JavaScript). It has no real function and doesn't submit a form.

### Circular buttons
Strangely, **circular buttons are created using the `<input>` tag** and not using the `<button>` tag. We use `<input>` and set `type = "radio"` and we get buttons like the ones in MS Forms. Example:
~~~html
<p> Are you made of metal? </p>
<input type = "radio" name = "metal" value = "yes"> Yes <br>
<input type = "radio" name = "metal" value = "no"> No <br>
~~~
This will display the question like this:
![[Pasted image 20240614084135.png]]

## Dropdown menus
We can create drop down menus using the `<select>` tag. This is like an unordered list. Just like the `<ul>` tag needs `<li>` to create an item inside it, **`<select>` needs the `<option>` tag to create an item in it.**  Once again, `<select>` needs a `name` property to be used as an identifier. We also give each `<option>` tag a `value` property to identify it. *The `value` property helps the form identify and store our choice.* Example:
~~~html
<p>
  Fave Baldy: 
  <select name="baldies">
    <option value = "david">David</option>
    <option value = "jean luc">Jean Luc Picard</option>
    <option value = "yul">Yul Brynner</option>
  </select>
</p>
~~~
This creates the following dropdown menu:
![[Pasted image 20240612130857.png]]

There are some properties we can use to customize our `<option>` tags. These are:
- `selected` makes the option the **default selection** when the page loads.
- `disabled` ensures that the **user cannot select this option again** after choosing another option.
- `hidden` makes the **option not visible in the dropdown list** once the user clicks on the dropdown to make a selection.

I used these properties to make a blank first option in the dropdown, so that the *user sees a blank option first* when the form loads. This also prevents the first option from being the default. This is beneficial because the **user may forget to answer the question, and the form will auto submit the first option** as the user's answer. It looks like:
![[Pasted image 20240614090036.png]]
*I used all three attributes in the first blank option to make sure its the default when the page loads and that the user cannot submit this blank option.* The code is:
~~~html
<p> What is your favourite food? </p>

<select name="food">

<option value="" selected disabled hidden></option>
<option value="oil">Oil - Premium Grade</option>
<option value="pizza">Pizza - With Pineapple</option>
<option value="electricity">Electricity - 100% Renewable</option>
<option value="data">Data Packets - Extra Bytes</option>

</select>
~~~

## Methods
When creating our `<form>` tag and `@app.route`, we need to specify the `method` property. So far, we've used the `post` method, but there's also another method called `get`.

With `post`, the **data in the form can't be seen by your browser.** For example, if you create a shopping cart on a website, it saves the data using `post`. If you copy the cart link and send it to someone, they will see a blank cart, and not the items you have added. *The link for you will be different than the link for other users.* With `get`, the **data is in the url itself.** This means if you share a link that uses `get`, then everyone who opens it will see the same thing. Simply replace `"POST"` with `"GET"`.
~~~python
@app.route('/', methods=["GET"])
~~~
