---
color: var(--mk-color-blue)
tags:
  - quantecon
---

## Set a title for the graph
`ax.set_title(" ")` gives your graph a title.

## Controlling axis ticks
We can use `ax.set_xticks()` or `ax.set_yticks()` to control the numbers shown on the x and y axis. For example,
~~~python
ax.set_yticks(np.linspace(-1,1,5))
ax.set_xticks(np.linspace(0,10, 11))
~~~
It looks like this:
![[Pasted image 20250322174402.png|center|400]]