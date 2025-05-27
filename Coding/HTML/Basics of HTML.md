---
sticker: lucide//file-check
tags:
  - html-syntax
color: var(--mk-color-pink)
---
## Tags
Tags are the basis of HTML. They usually come in pairs, in the format `<tag> </tag>`. We should **start every HTML document with the html tag** `<html>` and end it with `</html>`.

## Head and title
`<head>` is an important tag that *gives a lot of information on behind the scenes work.* Nested within `<head>`, we have `<title>`. `<title>` gives the text that will be displayed on the user's tab when they open a webpage.

HTML is usually written in nested form like this. However, that doesn't really matter. It plays no role in how HTML code is interpreted, but it is *standard practice to make code more readable.*
~~~html
<html>
	<head>
		<title>
		</title>
	</head>
	
	<body>
	</body>
</html>
~~~

## Headings
Headings are used within the `<body>` tag and come in pre-defined sizes, with `h1` being the largest.
~~~html
<html>
	<head>
		<title>
		Learning HTML
		</title>
	</head>
	
	<body>
	<h1> HTML is a markdown language </h1>
	<h2> Obsidian uses markdown too </h2>
	<h3> There are certainly some similarities </h3>
	</body>
</html>
~~~
The different sized headings look like the different sizes of Obsidian headings depending on the number of hashes used.
![[Pasted image 20240606112844.png]]

## Paragraphs
Text within `<p>` creates a paragraph for your website. Example:

~~~html
<body>
  <h1>Dave's World of Baldies</h1>
  <h2>Welcome to our website!</h2>

  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>
  
</body>
~~~
This gives us the following paragraphs:
![[Pasted image 20240606113958.png]]

## Comments
You can comment in HTML using `<!-- This is a comment -->`. Comments can also stretch across multiple lines as long as they are enclosed correctly.
~~~html
<!--
    This is a multi-line comment.
    It can span several lines.
-->
~~~
