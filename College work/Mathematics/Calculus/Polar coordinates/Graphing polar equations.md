---
color: var(--mk-color-pink)
tags:
  - sem1-flashcards/math_ge/calc/polar
---
Quick access:
[[Graphing polar equations#Steps to plot a polar graph|Steps to plot a polar graph]]
[[Graphing polar equations#Family of curves|Family of curves]]
	[[Graphing polar equations#1. $r=a, cos theta, sin theta$ (circle)|1. Circle]]
	[[Graphing polar equations#2. $ theta=c$ (Straight line)|2. Straight line]]
	[[Graphing polar equations#3. $r= theta$ (spiral)|3. Spiral]]
	[[Graphing polar equations#4. $r=a pm b cos theta or b sin theta$ (limacons)|4. Limacons and their variations]]
	[[Graphing polar equations#5. $r=a cos n theta or sin n theta$ (rose petals)|5. Rose petals]]	
	[[Graphing polar equations#6. $r {2}=a {2} cos 2 theta or sin 2 theta$ (lemniscate)|6. Lemniscate]]

## Steps to plot a polar graph
We typically follow this procedure while graphing polar equations:
- Check for symmetries
- Find the value of $r$ for relevant values of $\theta$ (depending on symmetry)
- Put the values in a table so its easy to understand
- Draw reference lines at the angles we've chosen in our table
- Plot the points on these reference lines 
- Use symmetry to plot the other parts of the graph

> [!Warning] Remember to **sketch the direction**
> Always put an arrow pointing to where the graph is going when you draw polar graphs.

Example: ![[Pasted image 20240927110351.png]]
You can see how he followed all the steps here. The only difference is that instead of using a table, *he used a graph in the $r,\:\theta$ plane to visualize that $r$ decreases from $0$ to $\pi$*.

## Family of curves
### 1. $r=a,\:\cos \theta,\:\sin \theta$ (circle)
$r=a$ gives us circles with a radius of $a$ centered at the pole. $r=a\cos \theta$ is a family of circles with center $(\dfrac{a}{2},0)$ and radius $\dfrac{a}{2}$. $r=\sin \theta$ gives us the same, but the circles are centered at $(0, \frac{a}{2})$ instead (both these coordinates are in cartesian).
![[Pasted image 20241001094504.png]]

### 2. $\theta=c$ (Straight line)
This gives us a never ending line that follows the angle of $\theta$. 
![[Line.webp|center|500]]

### 3. $r=\theta$ (spiral)
![[CNX_Precalc_Figure_08_04_021F.jpg|center]]

### 4. $r=a \pm b\cos \theta\:or\:b\sin \theta$ (limacons)
A limacon (pronounced $lee-mah-sohn$) is a type of *distorted circle.* It can have a dimple, oval, loop etc. based on the relation between $a$ and $b$.

If $\dfrac{a}{b}=1$, then it is called a **cardioid** since it looks like a heart. When $\dfrac{a}{b}<1$, the limacon will have an **inner loop.** If the value of $\dfrac{a}{b}$ lies between 1 and 2, then it will be a **dimpled limacon** with a small dip on one side. If $\dfrac{a}{b}$ is more than 2, then we have a **convex limacon,** which is very close to a circle but with a tiny dent.
![[maxresdefault-1.jpg]]
### 5. $r=a \cos n\theta \:or\sin n\theta$ (rose petals)
This family of curves form rose petals. *The value of $n$ tells us how many petals are there.* $n$ is odd $\implies$ $n$ petals, but if $n$ is even, we have $2n$ petals. The value of $a$ tells us the furthest distance from the pole.
Example: $r=2\cos(2\theta)$.
![[Pasted image 20240927115326.png]]

### 6. $r^{2}=a^{2}\cos 2\theta\:or\sin 2\theta$ (lemniscate)
A lemniscate is basically an *infinity symbol.* In this case, we have $r^{2}$, so the value of the $\cos$ or $\sin$ function must be positive. Therefore, the curve will have no defined values in two quadrants. However, due to negative values of $r$, we may see the curve show up in more than 2 quadrants.

We can see that **lemniscates with $\cos$ are horizontal (they lie down) and the ones with $\sin$ are along a diagonal (only present in quadrants 1 and 3).**
![[Pasted image 20241001100158.png]]