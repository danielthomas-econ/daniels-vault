---
sticker: lucide//tags
color: var(--mk-color-pink)
tags:
  - html-syntax
---
So far, our CSS code gave a set format for all tags based on their types. Therefore, our code would **modify all tags of one type.** However, sometimes we'd like to just modify a certain subset of tags within a type. Let's assume we want to modify only certain `<p>` tags. We can do this by *assigning classes only to the tags we want to modify.* Example:
~~~html
<p> Obsidian uses markdown too. There are certainly some similarities between the two. </p>

<p class = "small_text"> I am learning HTML to understand how to create a website. </p>
~~~
We have two `<p>` tags here, but the second one is assigned to the class `small_text`. Now, if we want to assign attributes only to the `small_text` class, we can do this with:
~~~css
p{
    font-family: monospace;
    font-size: 18px;
    text-align:center;
  }

.small_text{
    font-style: italic;
    font-weight: bold;
  }
~~~
On top we have the attributes common to all `<p>` tags, and the next block defines attributes specific to the `small_text` class. **Remember to put the dot before the class name** while referencing it in CSS. Now the 2nd paragraph with the `small_text` class will have all 5 attributes, while the regular `<p>` tag will only have the first 3 attributes.

Before:
![[Pasted image 20240608195045.png]]
After:
![[Pasted image 20240608195056.png]]
