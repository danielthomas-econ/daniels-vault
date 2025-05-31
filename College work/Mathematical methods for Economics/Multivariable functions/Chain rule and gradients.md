---
color: var(--mk-color-teal)
tags:
  - "#sem2-flashcards/mme/multivariable_functions"
---
Quick access:
- [[#Chain rule|Chain rule]]
	- [[#Chain rule#Two variable case|Two variable case]]
	- [[#Chain rule#The generalized chain rule|The generalized chain rule]]
- [[#Directional derivatives|Directional derivatives]]
	- [[#Directional derivatives#Second directional derivative|Second directional derivative]]
- [[#Gradient|Gradient]]
- [[#Flashcards|Flashcards]]

## Chain rule
### Two variable case
If we have $z=F(x,y)$ and $x=f(t)$, $y=g(t)$, then we can write $z$ as $F(f(t),g(t))$. Differentiating using the chain rule gives us $F_{1}'(f(t),g(t))f'(t)+F_{2}'(f(t),g(t))g'(t)$. In neater notation, we can say:
$$\dfrac{dz}{dt}= F_{1}'(x,y) \dfrac{dx}{dt} + F_{2}'(x,y) \dfrac{dy}{dt}$$

This is called **the total derivative** of $z$ wrt $t$. *We first consider the change in $x$*, *but we must scale it by how much it changed due to a change in $t$*. That's why we have the term $F_{1}'(x,y) \dfrac{dx}{dt}$. Same logic holds for $y$ and the second term. The total derivative is the sum of the changes contributed by a change in both $x$ and $y$ due to the change in $t$.

You can use this same logic if $x$ and $y$ depend on more than one same parameter. Consider $x=f(t,s)$ and $y=g(t,s)$. Then we have:
$$\begin{align}
\dfrac{dz}{dt} &= F_{1}'(x,y) \dfrac{dx}{dt} + F_{2}'(x,y) \dfrac{dy}{dt} \\
\dfrac{dz}{ds} &= F_{2}'(x,y) \dfrac{dx}{ds} + F_{2}'(x,y) \dfrac{dy}{ds}
\end{align}$$

### The generalized chain rule
Many times we encounter functions of $n$ variables. If they depend on the same parameters, we can use the general chain rule. This would be a case where $z=F(x_{1},x_{2},\dots,x_{n})$, $x_{1}=f_{1}(t_{1},t_{2},\dots,t_{m}),\dots,x_{n} = f_{n}(t_{1},t_{2},\dots,t_{m})$. 

Once again, we use the same logic as the previous case but generalize this to $n$ variables. This gives us:
$$\dfrac{ \partial z }{ \partial t_{j} } = \dfrac{ \partial z }{ \partial x_{1} } \dfrac{ \partial x_{1} }{ \partial t_{j} } + \dots+ \dfrac{ \partial z }{ \partial x_{n} } \dfrac{ \partial x_{n} }{ \partial t_{j} } $$

If we want to find the change of $z$, a function of $x_{i}$, wrt $t_{j}$, **first consider the change in $z$ due to a change in $x_{i}$, and then scale that by how much $x_{i}$ changes due to a change in** $t_{j}$. Add all the terms up to get the derivative using the chain rule. 

Clearly, a change in the basic variable $t_{j}$ gives rise to a chain reaction. This tells us that $t_{j}$ changes $x_{i}$ which changes $z$, for each $x_{i}$. *Starting at the basic variable and working your way up the reaction to the final variable like this makes solving questions based on chain rule a lot easier.*

## Directional derivatives
Consider $z=f(x,y)$. We know how to find the partial derivatives $f_{1}'(x,y)$ and $f_{2}'(x,y)$. These partial derivatives have a drawback: *they only tell us the rate of change along the x and y axis.* What if we pick some other direction? Why should we restrict ourselves to just observing rate of change in the $x$ and $y$ axis?

Directional derivatives fix this. Consider $(h,k)$ to be the vector pointing to the direction we want to find the derivative of. Let's define the directional function as $g(t)=f(x_{0}+th,y_{0}+tk)$. This tells us the value of $f$ as we move in the direction $(h,k)$. Taking the derivative of this, we get the equation $g'(t)=f_{1}'(x_{0}+th,y_{0}+tk)h + f_{2}'(x_{0}+th,y_{0}+tk)k$.

To get the derivative at $(x_{0},y_{0})$ and not some other point on the line, we set $t=0$. This gives us $g'(0)=f_{1}'(x_{0},y_{0})h+f_{2}'(x_{0},y_{0})k$. **If the length of the direction vector $(h,k)$ is 1, then this is our directional derivative.** It is denoted by $D_{h,k}f(x_{0},y_{0})$.

$$\text{Directional derivative: }D_{h,k}f(x_{0},y_{0})=f_{1}'(x_{0},y_{0})h + f_{2}'(x_{0},y_{0})k$$

### Second directional derivative
The second directional derivative is given by $D^{2}_{h,k}f(x_{0},y_{0})=f_{11}''(x_{0},y_{0})h^{2}+2f_{12}''(x_{0},y_{0})hk + f_{22}''(x_{0},y_{0})k^{2}$. Just remember this as *differentiating with x once gives h cause of chain rule (same for y and k), so if you see x differentiated n times, multiply the term with $h^n$ due to the chain rule.* This is just a simple way to logically remember the formula. The derivation is given in the textbook:
![[WhatsApp Image 2025-05-29 at 14.37.47_9d7f5999.jpg|center|500]]

## Gradient
The gradient is the *vector of all first order partials.* It is denoted by $\nabla f$. Therefore, $\nabla f(x_{1},x_{2},\dots,x_{n}) = \left( \dfrac{ \partial f }{ \partial x_{1} }, \dfrac{ \partial f }{ \partial x_{2} },\dots,\dfrac{ \partial f }{ \partial x_{n} } \right)$.

The gradient vector **captures how fast and in which direction f increases the most. The magnitude of the gradient tells us the rate of change.** We can use the angle between two vectors formula to show $D=\lvert\lvert \nabla f \rvert\rvert \cdot \lvert\lvert (h,k) \rvert\rvert \cdot \cos \theta$. Since $(h,k)$ is a unit vector, it simplifies to $\lvert\lvert \nabla f \rvert\rvert \cos \theta$, which is maximum when $\theta=0$. Therefore, when the gradient and direction vector point in the same direction, there is maximal increase in $f$.

The gradient can be called the *master direction of change* as it tells you the direction with the most change and the rate of that change. **If you want to see the rate of change in a particular direction, just project the gradient onto that direction.** That's why the directional derivative is just the dot product of the gradient and the direction vector.

We can see this as the directional derivative was found to be $f_{1}'(x_{0},y_{0})h+f_{2}'(x_{0},y_{0})k$. We can *rewrite this in dot product form* to get $(f_{1}'(x_{0},y_{0}),f_{2}'(x_{0},y_{0})) \cdot (h,k)$, where $(h,k)$ is a unit vector. *Therefore, the directional derivative can be rewritten as $\nabla f(x_{0},y_{0}) \cdot (h,k)$*.

As seen [[Level curves and geometric representations#General equation for tangent to a level curve|here,]] the **gradient is also orthogonal to the tangent of a level curve.**


## Flashcards
Q1) ![[Pasted image 20250529183331.png|center|350]]
?
Ans) Substituting all the given information in the original function, we get $x=f(g(w,t),h(t))$. Differentiating wrt $t$ using the chain rule gives us $x_{t}' = f_{1}'(g(w,t),h(t)) \cdot g_{t}'(w,t) + f_{2}'(g(w,t),h(t)) \cdot h'(t)$. The first term is the product of two negative numbers, and the second is product of two positive numbers. **Therefore, the sum is necessarily positive, which means a rise in tax rate will necessarily increase demand.**
.
Alternatively, you can start thinking from the basic variable. Changing $t$ changes $p$, which changes $x$. Similarly, changing $t$ changes $a$, which changes $x$. This gives us $x_{t}' = \dfrac{ \partial p }{ \partial t }\dfrac{ \partial x }{ \partial p } + \dfrac{ \partial a }{ \partial t }\dfrac{ \partial x }{ \partial a }$. Again, this is the sum of two positive numbers so the derivative is necessarily positive.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>


