---
color: var(--mk-color-teal)
tags:
  - "#sem2-flashcards/mme/multivariable_functions"
---
Quick access:
- [[#Directional derivatives|Directional derivatives]]
	- [[#Directional derivatives#Second directional derivative|Second directional derivative]]
- [[#Gradient|Gradient]]

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

The gradient vector **captures how fast and in which direction f increases the most.** We can use the angle between two vectors formula to show $D=\lvert\lvert \nabla f \rvert\rvert \cdot \lvert\lvert (h,k) \rvert\rvert \cdot \cos \theta$. Since $(h,k)$ is a unit vector, it simplifies to $\lvert\lvert \nabla f \rvert\rvert \cos \theta$, which is maximum when $\theta=0$. Therefore, when the gradient and direction vector point in the same direction, there is maximal increase in $f$.

The gradient can be called the *master direction of change* as it tells you the direction with the most change and the rate of that change. **If you want to see the rate of change in a particular direction, just project the gradient onto that direction.** That's why the directional derivative is just the dot product of the gradient and the direction vector.

We can see this as the directional derivative was found to be $f_{1}'(x_{0},y_{0})h+f_{2}'(x_{0},y_{0})k$. We can *rewrite this in dot product form* to get $(f_{1}'(x_{0},y_{0}),f_{2}'(x_{0},y_{0})) \cdot (h,k)$, where $(h,k)$ is a unit vector. *Therefore, the directional derivative can be rewritten as $\nabla f(x_{0},y_{0}) \cdot (h,k)$*.

As seen [[Level curves and geometric representations#General equation for tangent to a level curve|here,]] the **gradient is also orthogonal to the tangent of a level curve.**

