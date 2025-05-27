---
color: var(--mk-color-charcoal)
tags:
  - sem1-flashcards/mme
---
Quick access:
[[Inverse functions#Definition|Definition]]
[[Inverse functions#Finding an inverse|Finding an inverse]]
[[Inverse functions#Properties of inverse functions|Properties of inverse functions]]

[[Inverse functions#Flashcards|Flashcards]]

## Definition
Let $f$ be a function with domain $A$ and range $B$. If $f$ is [[Types of functions#Injective function (one-to-one)|one-to-one,]] it has an inverse function $g$ with domain $B$ and range $A$. The function $g$ is given by the following rule: For each $y\in B$, the value $g(y)$ is the unique number $x$ in $A$ s.t. $f(x)=y$. Therefore,
$$g(y)=x\iff f(x)=y$$

An inverse function is typically denoted by $f^{-1}$.

## Finding an inverse
If we're given a function $y=f(x)$, we know that the inverse is $x = g(y)$. *Therefore, we must isolate the x term to get a function in terms of x.* This is our inverse function. Eg: $f(x)=4x-3$. Therefore, $x=\dfrac{{y+3}}{4}$. Therefore, our inverse function $g(y)$ is $\dfrac{{y+3}}{4}$.

Sometimes we are given functions where it is hard to simply extract the value of $x$, like $y=3x^9+x^3-6x^{2}+4$. For functions like this, we have a simple criteria we can use:
$$\begin{align}
\text{If f is }&\text{differentiable, then f has an inverse on }I\text{ if:} \\
&\text{i) }f'(x)>0 \text{ for all }x \text{ in the interval} \\
&\text{ii) }f'(x)<0 \text{ for all }x \text{ in the interval}
\end{align}$$
Therefore, if a function is strictly increasing/decreasing in an interval, it has an inverse in that interval.

## Properties of inverse functions
The most important property of inverse functions is that **they are mirror images of each other along the line $y=x$**. Eg: The graphs of $x^{3}$ and $x^{1/3}$. ![[Pasted image 20250102182910.png]]

Another property is that for two inverse functions $f$ and $g$, $g'(y)=\dfrac{1}{f'(x)}$. We can differentiate $g(f(x))=x$ to get $g'(f(x))f'(x)=1$
Since $f(x)=y$, we get $g'(y)=\dfrac{1}{f'(x)}$. **Since they are just reciprocals of each other, $f'$ and $g'$ will always have the same sign.** Therefore, a function and its inverse will either both be increasing, or both be decreasing.

Lastly, *two inverse functions will always have opposite curvatures.* Since $g$ is $f$ reflected about $y=x$, this reflection means $g$ has the opposite curvature of $f$.


## Flashcards
Q1) Find the inverse of the function $y=2x^{2}-x^4$ in $[0,1]$.
?
Ans) Since the function is increasing in $[0,1]$, we can say that it has an inverse in the interval.
$x^4-2x^{2}+y=0$. Let $z=x^{2}$. Therefore, $z^{2}-2z+y=0$. Solve using quadratic formula. $z=\dfrac{{2\pm \sqrt{ 4-4y }}}{2}=1\pm \sqrt{ 1-y }$.
Therefore, $x^{2}=1\pm \sqrt{ 1-y }\implies x=\sqrt{ 1\pm \sqrt{ 1-y } }$. *We know $x\in[0,1]$ (domain of the function), but $\sqrt{ 1+\sqrt{ 1-y } }>1$, so it is outside the domain.* Therefore, our inverse function is $g(y)=\sqrt{ 1-\sqrt{ 1-y } }$
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

