---
color: var(--mk-color-pink)
sticker: lucide//list
tags:
  - html-syntax
---
There are two types of lists in HTML, ordered and unordered lists. These types are represented using the `<ol>` and `<ul>` tags respectively. **An ordered list creates a numerically ordered list, while an unordered list creates a bullet point list.** We use the `<li>` tag to enclose items within our list. Example:

~~~html
    <h2> Benefits of Obsidian:</h2>
    <ul>
        <li>Linking</li>
        <li>Markdown Support</li>
        <li>Graph View</li>
        <li>Plugins</li>
        <li>Local Storage</li>
    </ul>
~~~
Since we use an unordered list (`<ul>` tag), we get the below result.
![[Pasted image 20240606140229.png]]
Using `<ol>` instead of `<ul>` gives us a numerically ordered list, seen below.
![[Pasted image 20240606140322.png]]

