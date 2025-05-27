---
color: var(--mk-color-pink)
sticker: lucide//image-plus
tags:
  - html-syntax
---
You cannot simply insert images into HTML. To add an image to your HTML file, you must:
- Save the file (preferably in a separate folder)
- Name it properly *(preferably without spaces)*
- Tell HTML where to find it

To insert images, we use `<img src = "image_path.extension">` . We can also add other arguments other than `src`, like `alt` (text displayed if image doesn't load) or `width` (width of the image). **The value of `src` can also be an external weblink to add a picture from the internet.** 

> [!NOTE]
> The `<img>` tag is called a **void element.** This means it contains only its own attributes and doesn't enclose anything. Therefore, there is no `</img>` tag.

Example of images:
~~~html
    <body>
    <h1> HTML is a markdown language </h1>
    <p> Obsidian uses markdown too. There are certainly some similarities between the two. </p>
    <p> I am learning HTML to understand how to create a website. </p>
    <img src = "images/random_pic_from_obsidian.png" width = 50%>
    </body>
~~~
This inserts an image with 50% of its width. Remember to **include the file path starting from the current directory.**
![[Pasted image 20240606115501.png]]

