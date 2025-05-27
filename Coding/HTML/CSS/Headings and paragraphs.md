---
color: var(--mk-color-pink)
sticker: lucide//heading-1
tags:
  - html-syntax
---
## Headings
Go to your CSS file (we'll assume it is called `style.css`) and enter the following:
~~~css
h1{
  font-family: sans-serif;
  font-size: 24px;
  color: blue;
  background-color: #d3d345;
}
~~~
This bit of CSS code now tells our HTML file to follow this exact formatting rule for **all** `<h1>` tags in our document. Let's look at a before and after of our webpage.
Before:
![[Pasted image 20240607092533.png]]
After:
![[Pasted image 20240607092549.png]]
We can clearly see that every attribute of the `<h1>` tag mentioned in `style.css` has been changed according to our formatting.

Sometimes, we want **different heading sizes to have different rules.** We can add `h2` as part of the same `h1` CSS formatting, but the problem here is both `h1` and `h2` have the same font size. *We can simply add another rule for `h2`* specifying the smaller font size. Now, `h2` will take both formats, but override the `font-size` argument with the second one.
~~~css
h1, h2{
  font-family: sans-serif;
  font-size: 24px;
  color: blue;
  background-color: #d3d345;
  text-align:center;  
}

h2{
  font-size: 12px;
}

~~~
It works similar to [[Object oriented programming#Inheritance|sub-classes]] in object oriented programming, where the *sub-class gets all the properties of the parent class but has its own unique ones too.* In case of conflict, the attribute given only to the sub-class is given priority over the parent class' attributes.


## Paragraphs
The properties for paragraphs are rather similar to the ones for headings.
~~~css
p {
  font-family: sans-serif;
  font-size: 10px;
  color: blue;
  margin-bottom: 5px;
}
~~~
`margin-bottom` can be used to *fix awkward looking spacings* between paragraphs.

## Alignment
~~~css
h1{
  font-family: sans-serif;
  font-size: 24px;
  background-color: #d3d345;
  text-align:center;
}

p{
  font-family: monospace;
  font-size: 10px;
  text-align:center;
}
~~~
The parameter `text-align` can take the arguments `center`, `right` or `left`.
