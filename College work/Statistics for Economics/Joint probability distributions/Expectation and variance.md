---
color: var(--mk-color-teal)
tags:
  - sem1-flashcards/stats/joint_distributions
---
The rules of expectation and variance stay largely the same for joint probability distributions.

## Expectation
The expected value of $X$ is denoted by 
$$\begin{align}
E(X)&=\int \int xf(x,y)\:dx\:dy \\
&=\int xf_{X}(x)\:dx
\end{align}$$
Therefore, the expected value of $X$ is the sum of $x$ times its [[PMFs and PDFs#Marginal pmf|marginal pdf.]] 

## Variance
The variance of $X$ is given by
$$\begin{align}
V(X)&=E(x^{2})-(E(X))^{2} \\
&=\int x^{2}f_{X}(x)\:dx - \left( \int xf_{X}(x)\:dx \right)^{2}
\end{align}$$


## Flashcards
Q1) ![[Untitledoerpjavjioi34uq9a.jpg|center|400]]
?
Ans) We know the time difference between Annie and Alvie's (or Alvie and Annie's) arrival can be expressed as $|X-Y|$. Let this function be called $h(X,Y)$. The expected value is $E(h(X,Y))=\int \int h(X,Y)f(X,Y)\:dy\:dx$.
.
The problem is that *we are not given $f(X,Y)$. However, we can derive this since $X$ and $Y$ are independent.* Therefore, $f(X,Y)=f_{X}(x)\cdot f_{Y}(y)=3x^{2}\cdot 2y=6x^{2}y$. Therefore, we need to compute $E(h(X,Y))=\int\limits_{x}\int\limits_{{y}}|X-Y|6x^{2}y\:dy\:dx$.
.
The next problem is **dealing with the bounds of the limits.** This can be tricky due to the absolute value. Consider two cases: $X>Y$. Now $Y$ cannot be more than $X$, so the limit of $Y$'s integral is $0$ to $x$. If $X<Y$, $Y$ cannot be less than $X$, so the limit of $Y$'s integral is $x$ to $1$.
.
Therefore, we are left with $E(h(X,Y))=\int\limits_{0}^1\int\limits_{0}^x(x-y)6x^{2}y\:dy\:dx+\int\limits_{0}^1\int\limits_{{x}}^1(y-x)6x^{2}y\:dy\:dx$. Solving this should give you $\dfrac{1}{6}+\dfrac{1}{12}=\dfrac{1}{4}$ hours, or 15 minutes.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
