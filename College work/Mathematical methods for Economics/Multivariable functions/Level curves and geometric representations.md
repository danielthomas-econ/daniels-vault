---
color: var(--mk-color-teal)
tags:
  - "#sem2-flashcards/mme/multivariable_functions"
---
Quick access:
- [[#Surfaces in 3D spaces|Surfaces in 3D spaces]]
- [[#Level curves|Level curves]]
	- [[#Level curves#Economic applications|Economic applications]]
	- [[#Level curves#First derivative of a level curve|First derivative of a level curve]]
	- [[#Level curves#Second derivative of a level curve|Second derivative of a level curve]]
	- [[#Level curves#General equation for tangent to a level curve|General equation for tangent to a level curve]]


## Surfaces in 3D spaces
Just like how we'd graph a function of one or two variables, we can graph $f(x,y,z)=c$ and *the outcome will be a surface in 3D space.* 

For example, if we have $px+qy+rz=m$, plotting this would give a surface. This specific equation actually has economic applications too. Consider an individual with $m$ income in a market with three goods at prices $p,q,$ and $r$. Only triples $(x,y,z)$ can be bought to fully utilize income. This equation is called **the budget plane.** 

## Level curves
The level curve $z=c$ for a function $z=f(x,y)$ is *the set of all points $(x,y)$ that satisfy $f(x,y)=c$*. Thinking of it geometrically, consider a surface in 3D space. At height $z=c$, **cut a plane parallel to the $xy$ plane and project it onto the $xy$ plane.** The projection of the intersection onto the $xy$ plane is called the level curve at height $c$ for $z$. Note that this idea **can be generalized to $n$ variables to get level surfaces of functions.** 

### Economic applications
*IC curves are level curves* as they show all combinations of goods $x$ and $y$ that give a fixed $c$ level of satisfaction to the consumer. ^cbbb6c

In production theory, if $f(x_{1},x_{2},\dots,x_{n})$ is a production function, then $f(x_{1},x_{2},\dots,x_{n})=z_{0}$, where $z_{0}$ is some constant, is called an *isoquant.* It shows all possible combinations of inputs to get the same level of output $z_{0}$.

These figures should give you a better idea of what a level curve is. 
![[WhatsApp Image 2025-05-29 at 13.39.58_d387505e.jpg]]
![[WhatsApp Image 2025-05-29 at 13.39.59_e045a9ad.jpg]]

### First derivative of a level curve
We want to find the **derivative of a level curve, which is essentially its slope.** Let's consider $y=f(x)$. Now we have $F(x,f(x))=c$. Since this is entirely a function of $x$, let's say $u(x)=F(x,f(x))$, where $u(x)=c$.

Differentiating both sides gives us $u'(x)=F_{1}'(x,f(x))\cdot 1 + F_{2}'(x,f(x))\cdot f'(x)$, which equals zero since $u(x)$ is a constant. Therefore, we get $f'(x)= \dfrac{{-F_{1}'(x,f(x))}}{F_{2}'(x,f(x))}$. This is exactly what we want. Therefore,
$$\text{Slope of the level curve} = \dfrac{{-F_{1}'(x,y)}}{F_{2}'(x,y)}$$
Obviously, this only works if $F_{2}'\ne 0$. This is useful because *it gives us the derivative of $y$ wrt $x$ even if it is impossible to differentiate explicitly for $y$*.

### Second derivative of a level curve
Differentiate $f'(x) = \dfrac{{-F_{1}'(x,y)}}{F_{2}'(x,y)}$ using quotient rule to get the second derivative. It becomes really long and tedious, so here's the shortest formula for the second derivative:
![[WhatsApp Image 2025-05-29 at 15.08.24_02fe487a.jpg]]
The determinant may look daunting, but it is simply the determinant of the [[Quasi concavity#Bordered Hessian matrix|bordered hessian matrix]] of the function $F(x,y)=c$. Therefore, the second derivative becomes the bordered hessian divided by the cube of the first partial wrt $y$.

### General equation for tangent to a level curve
Since we know the slope of the level curve, we can simply substitute this into the point slope form for equation of a line. This gives us $y-y_{0} = \dfrac{{-F_{1}'}}{F_{2}'}(x-x_{0})$. We can simplify this and write it in the form $F_{1}'(x,y)(x-x_{0})+F_{2}'(x,y)(y-y_{0})=0$.

$$\text{Tangent to a level curve: }F_{1}'(x,y)(x-x_{0})+F_{2}'(x,y)(y-y_{0})=0$$

Observe that this can be written in dot product form as $(F_{1}'(x,y),F_{2}'(x,y)) \cdot (x-x_{0},y-y_{0}) = 0$. This is nothing but the dot product of the [[Gradients and directional derivatives#Gradient|gradient]] and $(x-x_{0},y-y_{0})$. The vector $(x-x_{0}, y-y_{0})$ represents the tangent vector as $x_{0},y_{0} \to 0$. **Since the dot product of gradient and the tangent is zero, they are orthogonal.** 