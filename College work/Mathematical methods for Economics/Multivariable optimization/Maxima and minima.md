---
color: var(--mk-color-orange)
tags:
  - "#sem2-flashcards/mme/multivariable_optimization"
---

## FOC for two variables
A necessary condition for a differentiable function $f(x,y)$ to have a maximum or a minimum at some interior point $(x_{0},y_{0})$ of its domain is that *$(x_{0},y_{0})$ is a stationary point of the function.* These are points where $f'_{1}(x_{0},y_{0})=0$ and $f'_{2}(x_{0},y_{0})=0$. However, this is not a sufficient condition for a maximum or minimum.
![[WhatsApp Image 2025-05-16 at 17.48.32_9a8574de.jpg]]
Although $P,Q$ and $R$ are all stationary points, only $P$ is a maximum.

## Definition of maxima and minima
Let $f(x_{1},x_{2},\dots,x_{n})$ be a function defined over a set $S$ in $\mathbb{R}^n$. Let $c=(c_{1},c_{2},\dots,c_{n})$ belong to $S$. $c$ is the maximum of the function if $f(c)>f(x)$ $\forall$ $x \in S$. Reverse the inequality for a minima. We can also say that **if c maximizes f over S, then c minimizes -f over S.** 

## Increasing transformation of functions
A useful result is that *maximizing a function is equivalent to maximizing a strictly increasing transformation of that function.* While we'd get the same maximum point, the maximum value will be different due to the transformation, so we must be careful when using this result.

Eg: If we want to maximize $f(x,y)$, we can maximize $af(x,y)+b$ $(a>0)$ or $\ln f(x,y)$ as both are strictly increasing transformations of $f(x,y)$.

Formally stating this: Let $g(x_{1},x_{2},\dots,x_{n})=F(f(x_{1},x_{2},\dots ,x_{n}))$.
Then,
i) if $F$ is *increasing* and $c=(c_{1},c_{2},\dots,c_{n})$ maximizes $f$ over $S$ $\implies$ $c$ also maximizes $g$ over $S$.
ii) if $F$ is *strictly increasing,* then $c$ maximizes $f$ over $S$ $\iff$ $c$ maximizes $g$ over $S$.

**Proof:**
i) As $c$ maximizes $f$ over $S$, we can say $f(c)\geq f(x)$ $\forall$ $x \in S$. This tells us that $g(x) \leq F(f(x))\leq F(f(c)) \leq g(c)$ ($\because$ $F$ is increasing). Therefore, $g(c) \geq g(x)$ $\forall$ $x \in S$ $\implies$ $c$ maximizes $g$.
ii) same but with strict inequalities


## Extreme value theorem
If $f$ is a **continuous function over a closed, bounded set** $S$ in $\mathbb{R}^n$, then there exists both a maximum $c=(c_{1},c_{2},\dots,c_{n})$ and a minimum $d=(d_{1},d_{2},\dots,d_{n})$ in $S$.


## Steps to find maximum and minimum values
For a function $f(x)$ defined in a closed, bounded set $S$ in $\mathbb{R}^n$,
1) Find all the *stationary points of $f$ in the interior of $S$*
2) Find the largest and smallest value of $f$ on the boundary of $S$
3) Compute the value of the function at all the points in steps 1 and 2

The largest and smallest function value will be your maximum and minimum value.

Example: Find the extreme points and values for $f(x,y)=x^{2}+y^{2}+y-1$, $S=\{(x,y):x^{2}+y^{2} \leq 1\}$
?
Ans) First find the partial derivatives to find the interior stationary points. $f_{1}'(x,y)=2x=0 \implies x=0$ and $f_{2}'(x,y)=2y+1=0 \implies y = \dfrac{-1}{2}$
Therefore, we have a single stationary point $\left( 0, \dfrac{{-1}}{2} \right)$.
Let $g$ be $f$ on the boundary of $S$. Therefore, **$g$ is just $f$ but with the boundary condition substituted in.** Therefore, $g=y$. Since $x^{2}+y^{2} = 1$, both $x$ and $y$ lie on an interval $[-1,1]$. Therefore, the maximum and minimum values of $g$ are $1$ and $-1$. So we have three stationary points in total, $\left( 0, \dfrac{{-1}}{2} \right)$, $(0,-1)$ and $(0,1)$. Substituting, we get $\dfrac{{-5}}{4}$, $-1$ and $1$ as the function values respectively. Therefore, $\left( 0, \dfrac{{-1}}{2} \right)$ is the minimum while $(0,1)$ is the maximum of the function.