---
color: var(--mk-color-orange)
tags:
  - "#sem2-flashcards/mme/multivariable_optimization"
---

## Saddle points
We know that local maxima and minima are just the maximum and minimum values of the function in a given interval. The same [[Maxima and minima#FOC for two variables|FOC]] applies here, the partials must be equal to zero. However, this is a *necessary but not sufficient* condition. Therefore, **we can have a case when the partials equal zero, but we don't have a local max or min. This is called a saddle point.** 

![[WhatsApp Image 2025-05-30 at 09.03.17_cfc1b862.jpg]]
We can see that although both partials are clearly zero at the origin, that is neither a max or a min (not even local) of the function. Let's look at the function closely. We have $f(x,y) = x^{2}-y^{2}$. From the graph, *we notice that the x values of the function are always positive, but the y values of the function are always negative.* In other words, $f(x,0)\geq 0$ and $f(0,y) \leq 0$. Therefore, at the origin, *the function is moving in two different directions.* This is basically what a saddle point is.

## Second order conditions for functions of two variables
Let's consider $z=f(x,y)$, with $(x_{0},y_{0})$ being a stationary point. This tells us that $(x_{0},y_{0})$ is either a local max, min or a saddle point. We can find out exactly which case using SOCs.

Suppose $(x_{0},y_{0})$ is a local maximum. Let's define $g(x)=f(x,y_{0})$ and $h(y)=f(x_{0},y)$ (keeping one variable fixed in each case). If this is a maximum, we know from single variable optimization that $g''(x)<0$. **Since we've kept $y$ fixed here, the double derivative of $g$ is essentially the partial of $f$ twice wrt $x$**. This means that $g''(x)=f_{11}''(x_{0},y_{0}) \leq 0$. Similarly, $h(y) = f_{22}''(x_{0},y_{0}) \leq 0$.

**However, these conditions only tell us that $(x_{0},y_{0})$ is a maximum in a direction parallel to the $x$ and the $y$ axis.** This is because we started by assuming $x$ and $y$ to be fixed in the two functions. **It does not tell us if its a maximum when looking at other directions.** We need $f_{12}''$ and $f_{21}''$ to tell us the change in other directions too. Since these are the same (Young's Theorem), we'll only consider $f_{12}''$. Using this, we can derive the following *sufficient but not necessary conditions:*
![[WhatsApp Image 2025-05-30 at 09.22.10_79f393c1.jpg]]
