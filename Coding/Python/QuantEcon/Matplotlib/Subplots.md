---
color: var(--mk-color-blue)
tags:
  - quantecon
---


Subplots allow us to create multiple plots in a single figure. The code looks like this:
~~~python
num_rows, num_cols = 3,2
fig, axes = plt.subplots(num_rows, num_cols, figsize = (10,10))
x = np.linspace(-4,4,150)
for i in range(num_rows):
    for j in range(num_cols):
        m,s = uniform(-1,1), uniform(1,2) # mean and sd again
        y = norm.pdf(x, loc=m, scale=s)
        axes[i,j].set_xticks([-4,0,4])
        axes[i,j].set_yticks([])
        cur_title = f"$\mu$ = {m:.2}, $\sigma$ = {s:.2}"
        axes[i,j].set_title(cur_title)
        axes[i,j].plot(x,y)
plt.show()
~~~

**The most important change is that we must use `axes.[i,j]` (with row and column reference) when using any methods.** Besides that, its largely just a `for` loop with normal plotting.

## Custom subplots
You can *create a local version of subplots* and call that instead of `plt.subplots()`. To do this, simply define a function named `subplots()` with the customizations you want. Eg:
~~~python
def subplots():
    #Custom subplots with axes through the origin
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')

    ax.grid()
    return fig, ax
~~~
If we add this code,
~~~python
fig, ax = subplots() # uses our local version of subplots
x = np.linspace(-5,5,100)
y = np.exp(x)
ax.plot(x,y,'g-',label="exponential")
ax.legend()
plt.show()
~~~
our output becomes:
![[Pasted image 20250402100037.png|center|400]]


