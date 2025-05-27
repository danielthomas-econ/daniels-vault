---
color: var(--mk-color-blue)
tags:
  - quantecon
---
Quick access:
- [[#Import statement|Import statement]]
- [[#Plotting|Plotting]]
	- [[#Plotting#Label|Label]]
	- [[#Plotting#Viewing the graph|Viewing the graph]]
	- [[#Plotting#Legend|Legend]]
	- [[#Plotting#Transparency|Transparency]]
- [[#The object oriented way|The object oriented way]]

## Import statement
`import matplotlib.pyplot as plt`
Note that the plotting features are under `pyplot`, so if we simply name `matplotlib as plt` and try to run our code, it won't work.


## Plotting
`plt.plot(x-axis, y-axis, label = ' ')`
This plots the thing that you want to plot (usually an array).

### Label
You can also use LaTeX inside your labels. Eg: `label="$y=\sin(x)$`.

### Viewing the graph
There's no point plotting a graph if we can't view it. At the end of your code, type `plt.show()` to print the graph.
### Legend
The label we defined in the plotting statement is the legend of our graph. We can view this by adding the line `plt.legend()` in our code.

`plt.legend(loc="location")` will place the legend wherever location is specified. For example, we can set `location` as `upper center`.

### Transparency
We can change the transparency by changing the argument `alpha`, which ranges from 0 to 1. A smaller alpha makes the graph more transparent, while a larger alpha makes it more opaque.
![[Pasted image 20250322174021.png|center|400]]
## The object oriented way
~~~python
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
~~~
Here, the first line returns a pair where:
- `fig` is a `Figure` instance, like a blank canvas
- `ax` is an `AxesSubplot` instance, like a frame to plot in

This means that **`plot()` is actually a method of `ax`**.

