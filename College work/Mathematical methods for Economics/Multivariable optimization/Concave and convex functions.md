---
color: var(--mk-color-orange)
tags:
  - "#sem2-flashcards/mme/multivariable_optimization"
---
Quick access:
- [[#Graphical representation|Graphical representation]]
- [[#Mathematical representation|Mathematical representation]]
	- [[#Mathematical representation#Jensen's inequality|Jensen's inequality]]
- [[#Useful conditions for concavity and convexity|Useful conditions for concavity and convexity]]
- [[#Second derivative tests|Second derivative tests]]
	- [[#Second derivative tests#Sufficient conditions for global extrema|Sufficient conditions for global extrema]]
- [[#Flashcards|Flashcards]]

## Graphical representation
We know that for a single variable function, connecting any two points on the curve can tell us if the function is concave or convex. *If a line connecting any two points on the curve always lies above the curve, the function is convex.* Recall that convex $\implies$ $f''(x) \geq 0$. We can remember this condition by remembering that second derivative is *positive,* so the line must lie *above* the function. If the line is always below the curve, the function is concave.
![[Convex_b.png|center|400]]


## Mathematical representation
We know that for a concave function, the line always lies below the curve. Mathematically, this means $\text{graph} \geq \text{line}$ at all points in the line segment. *If we can express a point on the graph and a point on the line mathematically and show it holds true for all points, we can show the function is concave.*

![[Pasted image 20250530111901.png|center|300]]

Look at the above image. Consider the points $x_{0}$ and $x_{1}$. The corresponding points on the graph are $f(x_{0})$ and $f(x_{1})$. We know the parametric equation of a line segment connecting $a$ and $b$ is $(1-\lambda )a + \lambda b$ for $\lambda \in [0,1]$. **Therefore, the equation of our line is $(1-\lambda)f(x_{0}) + \lambda f(x_{1})$ for $\lambda \in [0,1]$**.

Once again, we can use the parametric equation of a line to find some point between $x_{0}$ and $x_{1}$. We'll then evaluate the function at this point. **Therefore, the equation of our function is $f((1-\lambda)x_{0} + \lambda x_{1})$ for $\lambda \in [0,1]$**.

Now that we have the equation of our function and line, we can say that *for a concave function:*
$$f((1-\lambda)x_{0}+\lambda x_{1}) \geq (1-\lambda)f(x_{0})+\lambda f(x_{1}), \:\:\lambda \in[0,1]$$
You can remember the direction of the inequality as $f((1-\lambda)x_{0}+\lambda x_{1})$ represents the function value, since we have $f$ on the outside. Therefore, this must be the greater side for a concave function.

### Jensen's inequality
Jensen's inequality (in the discrete case) is simply a generalization of this idea to $n$ variables. A function $f$ of $n$ variables is **concave** on a convex set $S$ in $\mathbb{R}^n$ $\iff$ $\forall$ $x_{1},x_{2},\dots,x_{m}$ in $S$ and all $\lambda_{1},\lambda_{2},\dots,\lambda_{_{m}} \geq 0$ with $\lambda_{1}+\lambda_{2}+\dots+\lambda_{m}=1$, then
$$f(\lambda_{1}x_{1}+\lambda_{2}x_{2}+\dots+\lambda_{m}x_{m}) \geq \lambda_{1}f(x_{1})+\lambda_{2}f(x_{2})+\dots+\lambda_{m}f(x_{m})$$


## Useful conditions for concavity and convexity
![[WhatsApp Image 2025-05-30 at 12.30.06_103f10f0.jpg]]

## Second derivative tests
We'll discuss functions of two variables here, but the concept generalizes to $n$ variables.
![[WhatsApp Image 2025-05-30 at 12.47.15_f6adb93d.jpg]]
This is somewhat similar to SOCs for concavity/convexity in the single variable case. **The signs of the partials have the same requirement as the single variable case. What's new is that the determinant of the Hessian must be positive for both cases.**

In other words, you can say:
$$\begin{align}
f \text{ is concave} \iff \text{Hessian is -ve semidefinite} \\
f \text{ is convex} \iff \text{Hessian is +ve semidefinite}
\end{align}$$
The conditions for $f_{11}''$ and $f_{22}''$ come from **assessing the semidefiniteness of the Hessian** using [[Quadratic forms#^b3a207|prinicpal minors.]] 

*If we want strict concavity/convexity, we need to check for definiteness (not semi) of the Hessian.* Note that the condition for strict concavity is NOT iff, it's a one way implication. Hessian is negative definite $\implies$ $f$ is strictly concave, but not the other way around.

### Sufficient conditions for global extrema
Just like how concave $\implies$ $f''(x_{0}) < 0$ $\implies$ maxima (if $x_{0}$ is a stationary point) in the single variable case, we can say the same for multivariable optimization.

Let $(x_{0},y_{0})$ is an interior stationary point of a function $f(x,y)$ **in a convex domain** $S$. Let $f_{11}'' = A, f_{12}''=f_{21}''=B$ and $f_{22}''=C$. Then,
$$\begin{align}
A \leq 0, C \leq 0, AC  - B^{2} \geq 0 &\implies (x_{0},y_{0}) \text{ is a MAX for }f(x,y) \text{ in }S \\
A \geq 0, C \geq 0, AC-B^{2} \geq 0 &\implies (x_{0},y_{0}) \text{ is a MIN for } f(x,y) \text{ in } S
 \end{align}$$

In other words, *if the second partials wrt x and y and the determinant of the Hessian is negative at $(x_{0},y_{0})$*, *then it is a maximum point in $S$*.

If the **Hessian is indefinite and none of the leading principal minors are zero, we have a saddle point.**


## Flashcards
Q1) Consider the linear function $f(x)=a\cdot x+b = a_{1}x_{1}+a_{2}x_{2}+\dots+a_{n}x_{n}+b$, where $a$ is a constant vector and $b$ is a constant number. Show that $f$ is both concave and convex.
?
Ans) If $f$ is both concave and convex, then for any $x_{1},x_{2}$ in the domain, $f((1-\lambda)x_{1}+\lambda x_{2})=(1-\lambda)f(x_{1})+\lambda f(x_{2})$. Simplifying the RHS, *we should replace the vector $x$ with this inequality.* Therefore, RHS becomes $a \cdot[(1-\lambda)x_{1}+\lambda x_{2}]+b$. **An important point to note is that we often write $b = (1-\lambda)b+\lambda b$ so that we can take $\lambda$ common.** Expanding, we get $(1-\lambda)a\cdot x_{1}+\lambda a\cdot x_{2} + (1-\lambda)b + \lambda b$. Taking $\lambda$ terms common, we get $(1-\lambda)(a\cdot x_{1}+b)+\lambda(a\cdot x_{2}+b)=(1-\lambda)f(x_{1})+\lambda f(x_{2})$. Therefore, $f((1-\lambda)x_{1}+\lambda x_{2})=(1-\lambda)f(x_{1})+\lambda f(x_{2})$ for $\lambda \in[0,1]$. This tells us that the function is both concave and convex for all $(x_{1},x_{2})$ in the domain.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

