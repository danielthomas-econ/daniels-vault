---
color: var(--mk-color-orange)
tags:
  - "#sem2-flashcards/mme/multivariable_optimization"
aliases:
---
Quick access:
- [[#Definition|Definition]]
	- [[#Definition#Using level sets|Using level sets]]
- [[#Properties of quasi concave and convex functions|Properties of quasi concave and convex functions]]
- [[#Bordered Hessian matrix|Bordered Hessian matrix]]
- [[#Determinant criterion|Determinant criterion]]
- [[#Flashcards|Flashcards]]

## Definition
A function $f$ defined over the convex set $S$ in $\mathbb{R}^{n}$ is *quasi-concave* $\iff$ for all $x,x_{0} \in S$ and all $\lambda \in [0,1]$, we have
$$f(x) \geq f(x_{0}) \implies f((1-\lambda)x + \lambda x_{0}) \geq f(x_{0})$$

Another way of expressing this is
$$f((1-\lambda)x + \lambda x_{0}) \geq \min\left\{f(x),f(x_{0})\right\}$$

On the other hand, *quasi-convex* functions are defined as
$$\begin{align}
f(x_{0}) \geq f(x) \implies f(x_{0})& \geq f((1-\lambda)x_{0} + \lambda x)  \\
\max\left\{f(x),f(x_{0})\right\} &\geq f((1-\lambda)x_{0}+\lambda x)
\end{align}$$
Here is a graphical representation of the definition *for quasi-convexity.* This function is actually quasi-concave too, so this is called a **quasi-linear function.** Clearly, quasi-linear functions don't have to be strictly linear functions.
![[Pasted image 20250531095248.png]]

Let's try to understand the definition of quasi-concave functions for now. The definition makes sense since **you can think of a quasi-concave function to be a loosely defined concave function, so it can be allowed to violate some properties of a concave function.** Our definition must also satisfy:
$$\begin{align}
\text{If} f(x) \text{ is concave, then it is quasi concave} \\
\text{If } f(x) \text{ is convex, then it is quasi convex}
\end{align}$$

Concave functions have the graph above the line connecting two points on the graph. Quasi-concave functions don't always have this. However, we can say that *for a quasi-concave function, the function value in between two points is always greater than or equal to the minimum of the two points.* Therefore, the function never goes below the minimum of the two points, which would start going in the convex direction of things (since convex means function is below the line connecting two points). An example of a quasi-concave function (that is not concave) is:
![[5CQqu.jpg|center|400]]

This is another example of a quasi-concave function. Note that *although the two individual pieces of the function are convex, the function as a whole is quasi-concave.* 
![[6pJc7.jpg|center|400]]

### Using level sets
We can rewrite these definitions in context of a level set. For some $a \in \mathbb{R}$, let $P_{a}=\left\{x \in S:f(x) \geq a\right\}$. **This subset of $S$ is called the upper level set for the function** $f$. 

A function $f$ is stb *quasi-concave if the upper level set is convex for all $a$*. Symmetrically, $f$ is quasi-convex if the lower level set is convex (not concave!). Note that for both definitions, *we need a convex set.* 

We can also say that $f$ is quasi-convex if $-f$ is quasi-concave (and vice versa). It's just like how a negative sign changes curvature for normal concavity/convexity.

A very useful result regarding level sets is that
$$\text{A level set is convex if} \begin{cases}
\text{the set is empty} \\
\text{there is only 1 element in the set} \\
\text{the set is defined in an interval}
\end{cases}$$
**This provides a quick alternate way to check for the convexity of a level set without using the line in the set definition.**

## Properties of quasi concave and convex functions
![[WhatsApp Image 2025-05-31 at 10.46.55_53ea20e9.jpg]]
This tells us that:
1) Adding functions of the same quasi-curvature doesn't guarantee it remains of the same quasi-curvature.
2) *Strictly increasing functions preserve quasi-curvature, while strictly decreasing functions flip it.* 

## Bordered Hessian matrix
A bordered Hessian is simply a regular [[Partial derivatives with many variables#Hessian matrix|Hessian]] "bordered" by *an extra row and column consisting of the first order partials of the function, with zero at the top left corner.* It looks like:
$$\begin{bmatrix}
0 & f_{1}'(x) & \dots & f_{n}'(x) \\
f_{2}'(x) & f_{11}''(x) & \dots & f_{1n}''(x) \\
. \\
. \\
. \\
f_{n}'(x) & f_{n 1}''(x) & \dots & f_{nn}''(x)
\end{bmatrix}$$

## Determinant criterion
Define the bordered Hessian determinants as $D_{r}(x)$, $r=1,\dots,n$.

For *quasi-concavity,*
Necessary condition: $(-1)^{r}D_{r}(x) \geq 0$
Sufficient condition: $(-1)^{r} D_{r}(x) > 0$
for $r=2,\dots,n+1$ and all $x \in S$ (convex set domain). **Note that we do not test for $r=1$**, **since that is always by definition zero and would make the sufficiency condition always fail.** 

In other words:
Necessary condition: Bordered Hessian is negative semidefinite
Sufficient condition: Bordered Hessian is negative definite







## Flashcards
Q1) Prove that if $f(x)$ is concave, then $f(x)$ is quasi-concave.
?
Ans) To prove $f(x)$ is quasi-concave, **we must show that its upper level set is convex.** Let $P_{a}=\left\{x \in S: f(x) \geq a\right\}$ be our level set, where $f$ is a function defined on the convex set $S$. Consider two points $x,y \in P_{a}$. This means $f(x) \geq a, f(y) \geq a$. *Since $S$ is convex, any line connecting points in $S$ belongs to $S$*. Therefore, $(1-\lambda)x + \lambda y \in S$. Since we are told $f(x)$ is concave, we know that
$$\begin{align}
f((1-\lambda)x + \lambda y) &\geq (1-\lambda)f(x) + \lambda f(y) \\
&\geq (1-\lambda)a + \lambda a \\
&= a
\end{align}$$
Therefore, $f((1-\lambda)x+\lambda y) \geq a$, which means it belongs to the upper level set. This tells us that *if $x$ and $y$ belong to the upper level set, then the line connecting them, $(1-\lambda)x+\lambda y$ also belongs to the upper level set.* Hence, we have shown the upper level set is convex. Therefore, $f(x)$ is quasi-concave.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Prove that if $f$ is quasi-concave and $F$ is a strictly increasing function, $F(f(x))$ is quasi-concave.
?
Ans) Suppose we have $F(f(x))\geq F(f(x_{0}))$, so then $f(x)\geq f(x_{0})$ (so $f(x_{0})$ is $\min\left\{f(x),f(x_{0})\right\}$). Since $f$ is quasi-concave, by definition $f((1-\lambda)x+\lambda x_{0}) \geq f(x_{0})$. **Since $F$ is strictly increasing, we can apply it to both side and preserve the inequality.** Therefore, $F(f((1-\lambda)x+\lambda x_{0})) \geq F(f(x_{0}))$. This shows that $F(f(x))$ is quasi-concave by definition.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q3) Show that $f(x) = e^{-x^{2}}$ is quasi-concave. What about $\ln(f(x))$ and $\dfrac{1}{f(x)}$ (for $x>0$)?.
?
Ans) The upper level sets of $f(x)$ are $\left\{x:e^{-x^{2}} \geq a\right\}$. Let's find the extrema of this function. $f'(x)=-2xe^{-x^{2}}=0$ $\implies x=0$. $f''(x)=-2e^{-x^{2}} + 4x^{2}e^{-x^{2}}$. $f''(0)=-2 < 0$ $\implies x=0$ is a max. $f(0)=1$. Therefore, the max value this function takes is $1$. *If $a=1$*, *then the upper level set is just a single number $x=0$*. *If $a>1$*, *then the upper level set is empty.* If $a<1$, then the upper level set is defined by the inequality $e^{-x^{2}} \geq a$ $\implies -x^{2} \geq \ln a$ $\implies x^{2} \leq \ln a$, **and the values of $x$ satisfying this lie in an interval.** We know that if an upper level set is empty, a singleton, or an interval, it is convex. Therefore, *the upper level set here is convex, so the function is quasi-concave.* 
.
$\ln$ is a strictly increasing function, and a strictly increasing function of a quasi-concave function is quasi-concave. We can show this as $\ln(e^{-x^{2}})=-x^{2}$. $x^{2}$ is a convex function, so $-x^{2}$ is concave $\implies$ it is quasi-concave. Also, $\dfrac{1}{e^{-x^{2}}}=e^{x^{2}}$. The second derivative is $2e^{x^{2}} + 4x^{2}e^{x^{2}}>0$. Therefore, $e^{x^{2}}$ is convex $\implies$ it is quasi-convex.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q4) Show that the Cobb-Douglas function $z=Ax_{1}^{a_{1}}x_{2}^{a_{2}}\dots x_{n}^{a_{n}}$ $(a_{i},A >0)$ is always quasi-concave.
?
Ans) Take $\ln$ on both sides. $\ln z= \ln A+a_{1} \ln x_{1}+\dots+a_{n}\ln x_{n}$. *Since $\ln z$ is the sum of concave functions, it is concave, and also quasi-concave.* We know that taking a strictly increasing function of a quasi-concave function will yield a quasi concave function. Therefore, $e^{\ln z}=z$ is quasi concave as it is a strictly increasing function of a quasi-concave function.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>