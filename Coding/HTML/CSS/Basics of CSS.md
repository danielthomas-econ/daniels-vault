---
color: var(--mk-color-pink)
sticker: lucide//file-check
tags:
  - html-syntax
---
CSS is short for *cascading style sheets.* The main goal of CSS is to help **beautify a web page.** Previously, coders had to specifically mention how each element had to look. CSS helps us create *settings and formats* which we can apply to parts of our page.

We can add our CSS to a different file and link it to our HTML file. For example, you can create a CSS document called `style.css` and link it to your HTML file using:
~~~html
<head>
<link href="style.css" rel="stylesheet" type="text/css" />
</head>
~~~

The default format for a CSS file would be something like:
~~~css
html, body {
  height: 100%;
  width: 100%;
}
~~~
This CSS code tells the `<head>` and `<body>` tags how to look. They have a height & width of 100% (i.e. they fill the page).

Important points:
- **Curly braces are important** - They surround the style for each tag
- Every line inside the style **must end with a semi colon**
- You can pick a specific font using font family. However, it is recommended to use general style since your specific font may not be supported on all browsers.

> [!NOTE] Comment syntax
> The syntax to comment a piece of CSS is to enclose it within `/*` and `*/`
> 

