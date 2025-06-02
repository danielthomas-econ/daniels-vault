---
color: var(--mk-color-teal)
tags:
  - "#sem2-flashcards/mme/multivariable_functions"
---
Quick access:
- [[#Definition|Definition]]
- [[#Euler's theorem|Euler's theorem]]
- [[#Properties of a homogenous function|Properties of a homogenous function]]
- [[#Homothetic functions|Homothetic functions]]
- [[#Flashcards|Flashcards]]

## Definition
A function $f$ is stb homogenous of degree $k$ if for all $(x,y)$ in the domain, $f(tx,ty)=t^{k}f(x,y)$ for $t>0$. This means *multiplying both the variables by a positive factor $t$ will return the function value multiplied by $t^k$*. Alternatively, if you can express it in terms of $u=x^{k}f\left( \dfrac{y}{x} \right)$, the function is homogenous of degree $k$. You can read more about it in [[Euler's theorem on homogenous functions|this note.]]

## Euler's theorem
Euler's theorem is **both a necessary and sufficient condition for homogeneity.** Therefore,
$$f(x,y)\text{ is homogenous of degree } k \iff x\dfrac{ \partial f }{ \partial x } +y\dfrac{ \partial f }{ \partial y }  =kf(x,y)$$
This result holds if $f$ is a function of $n$ variables too.

## Properties of a homogenous function
Let $f(x,y)$ be homogenous of degree $k$.

Then we know that $f(tx,ty)=t^{k}f(x,y)$. *Keep $y$ and $t$ constant and differentiate partially wrt $x$*. This gives us $tf_{1}'(tx,ty)=t^{k}f_{1}'(x,y) \implies f_{1}'(tx,ty)= t^{k-1}f_{1}'(x,y)$. Clearly, $f_{1}'(x,y)$ is homogenous of degree $k$. The argument is symmetric for $f_{2}'(x,y)$. Therefore, **the first degree partials of $f$ are homogenous of degree $k-1$**.

If we replace $t$ with $\dfrac{1}{x}$, we get $f\left( 1, \dfrac{y}{x} \right)= \left( \dfrac{1}{x} \right)^{k}f\left( x,y \right)$. Therefore, we can write $f(x,y)=x^{k}f\left( 1, \dfrac{y}{x} \right)$. Similarly, replacing $t$ with $\dfrac{1}{y}$ tells us that $f(x,y)= y^{k}f\left( \dfrac{x}{y},1 \right)$. Therefore, we can say that $f(x,y)=x^kf\left( 1, \dfrac{y}{x} \right)=y^kf\left( \dfrac{x}{y}, 1 \right)$.

Since $f_{1}'(x,y)$ and $f_{2}'(x,y)$ are both homogenous of degree $k-1$, we can apply Euler's theorem to them. This tells us that:
$$\begin{align}
xf_{11}''(x,y)+yf_{12}''(x,y)=(k-1)f_{1}'(x,y) \\
xf_{21}''(x,y)+yf_{22}''(x,y)=(k-1)f_{2}'(x,y)
\end{align}$$
By [[Partial derivatives with many variables#Young's theorem|Young's theorem,]] we know $f_{12}''=f_{21}''$. *We'll multiply the first equation by $x$ and second by $y$ and add the two.* This gives us $x^{2}f_{11}'' +2xyf_{12}'' + y^{2}f_{22}'' =(k-1)[xf_{1}'+yf_{2}']$. From Euler's theorem, we know $xf_{1}'+yf_{2}'=kf$. Therefore, we end up with
$$x^{2}f_{11}''+2xyf_{12}''+y^{2}f_{22}''=k(k-1)f(x,y)$$


All this tells us three important properties of a function $f(x,y)$ that is homogenous of degree $k$:
$$\begin{align}
1. f_{1}'(x,y)\text{ and }f_{2}'(x,y) &\text{ are homogenous of degree }k-1 \\
2.f(x,y) =&\: x^{k}f\left( 1, \dfrac{y}{x} \right) = y^{k}f\left( \dfrac{x}{y},1 \right) \\
3.\: x^{2}f_{11}'' + 2xy&f_{12}'' + y^{2}f_{22}'' = k(k-1)f(x,y)
\end{align}$$

## Homothetic functions
The function $f(x_{1},x_{2},\dots x_{n})$ is called homothetic if for $x,y \in D$, $f(x)=f(y)$ and $t>0$ $\implies$ $f(tx)=f(ty)$. 

**All homogenous functions are homothetic, but not all homothetic functions are homogenous.** If $f(x)$ is homogenous of degree $k$, then $f(tx)=t^{k}f(x)=t^{k}f(y)=f(ty)$. Therefore, $f(x)=f(y)$ $\implies$ $f(tx)=f(ty)$ $(t>0)$ for all homogenous functions.

We can also state that *$F(x)$ is homothetic if it can be written as $H(f(x))$*, *where $H$ is strictly increasing and $f$ is a homogenous function of degree* $k$. This is how we usually define homothetic function in microeconomics. So$$F \text{ is homothetic } \iff \text{ strictly increasing function of a homogenous function}$$
Do note that you won't always always have a homothetic function written as an increasing homogenous function. This result simply means that you can write $F$ as a strictly increasing homogenous function. You may see homothetic functions written in other forms too.

We can prove this. Suppose $F(x)$ is homothetic and $F(x)=F(y)$. This would mean $H(f(x))=H(f(y))$. *Since $H$ is strictly increasing,* $f(x)=f(y)$. Since $f$ is homogenous of degree $k$, for $t>0$ we can say that$$F(tx) = H(f(tx))=H(t^{k}f(x))=H(t^{k}f(y))=H(f(ty))=F(ty)$$
Therefore, $F(x)=F(y)\implies F(tx)=F(ty)$ for $t>0$.








## Flashcards
Q1) If $f(x,y)$ is homogenous of degree $k$, show that $f_{1}'(x,y)$ and $f_{2}'(x,y)$ are homogenous of degree $k-1$.
?
Ans) We know that $f(tx,ty)=t^{k}f(x,y)$. *Keep $y$ and $t$ constant and differentiate partially wrt $x$*. This gives us $tf_{1}'(tx,ty)=t^{k}f_{1}'(x,y) \implies f_{1}'(tx,ty)= t^{k-1}f_{1}'(x,y)$. Clearly, $f_{1}'(x,y)$ is homogenous of degree $k$. The argument is symmetric for $f_{2}'(x,y)$. Therefore, **the first degree partials of $f$ are homogenous of degree $k-1$**.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Prove that $F(x)$ is a homothetic function if it can be written as $H(f(x))$, where $H$ is a strictly increasing function and $f(x)$ is homogenous of degree $k$.
?
Ans) Suppose $F(x)=F(y)$. This would mean $H(f(x))=H(f(y))$. *Since $H$ is strictly increasing,* $f(x)=f(y)$. Since $f$ is homogenous of degree $k$, for $t>0$ we can say that$$F(tx) = H(f(tx))=H(t^{k}f(x))=H(t^{k}f(y))=H(f(ty))=F(ty)$$
Therefore, $F(x)=F(y)\implies F(tx)=F(ty)$ for $t>0$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q3) Are the sum and products of homogenous functions necessarily homogenous?
?
Ans) Let $f(x)$ and $g(x)$ be homogenous functions of degree $k_{1}$ and $k_{2}$ respectively, with $x=(x_{1},x_{2},\dots,x_{n})$.
For sum:
$f(tx)+g(tx)\implies t^{k_{1}}f(x)+t^{k_{2}}g(x)$.
If $k_{1}=k_{2}=k$, $t^{k}(f(x)+g(x))$ $\implies$ the sum is homogenous of degree $k$.
However, if $k_{1}\ne k_{2}$, then we cannot take $t$ fully common, therefore the sum is not homogenous.
Therefore, *the sum of two homogenous functions is not necessarily homogenous.*
For product:
$f(tx)\cdot g(tx)=t^{k_{1}}f(x)\cdot t^{k_{2}}g(x)=t^{k_{1} + k_{2}}(f(x)+g(x))$ $\implies$ the product is homogenous of degree $k_{1}+k_{2}$. Therefore, *the product of two homogenous functions is necessarily homogenous.*
.
For questions like this where you're asked to check for homogeneity, its best to just put $t$ in the argument and check if you can take $t$ common in the end.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q4) If $f(x,y)$ is homogenous of degree 1, show that $f_{11}''(x,y)f_{22}''(x,y)-(f_{12}''(x,y))^{2}=0$.
?
Ans) If $f(x,y)$ is homogenous of degree 1, then $f_{1}'$ and $f_{2}'$ are homogenous of degree $k-1=0$. Using Euler's theorem on the two first partials, we get$$\begin{align}
xf_{11}''(x,y)+yf_{12}''(x,y)=0 \\
xf_{12}''(x,y) + yf_{22}''(x,y)=0
\end{align}$$Note that $f_{12}''=f_{21}''$ by Young's Theorem. *This gives us a system of equations with which we can express $f_{11}''$ and $f_{22}''$ in terms of $f_{12}''$*. Therefore, $f_{11}''= \dfrac{{-y}}{x}f_{12}''$, $f_{22}''= \dfrac{{-x}}{y}f_{12}''$. This means we can rewrite the equation $f_{11}''f_{22}''-(f_{12}'')^{2}$ as $\left[ \dfrac{{-y}}{x}f_{12}'' \right]\cdot\left[ \dfrac{{-x}}{y}f_{12}'' \right]-(f_{12}'')^{2}=(f_{12}'')^{2}-(f_{12}'')^{2}=0$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q5) If $f$ is homogenous of degree $k$, prove that $f^{-1}$ is homogenous of degree $\dfrac{1}{k}$.
?
Ans) Let $y=f(x)$ be homogenous of degree $k$. Let $g(y)=f^{-1}$. Therefore, $g(y)=x$ $\implies f(x)=f(g(y))$. Since $f$ is homogenous, $f(tg(y))=t^{k}f(g(y))\implies f(tg(y)) = t^{k}y$. *We started with applying $f$ to $g$*, *so now we'll apply $g$ to $f$ here to invert it.* The $f$ and $g$ will cancel so $tg(y)=g(t^{k}y)$ $\implies$ $g$ is homogenous of degree $\dfrac{1}{k}$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
