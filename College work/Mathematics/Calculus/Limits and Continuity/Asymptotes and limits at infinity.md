---
color: var(--mk-color-orange)
tags:
  - sem1-flashcards/math_ge/calc/limits_and_continuity
---
Quick access:
[[Asymptotes and limits at infinity#Basics of infinite limits|Basics of infinite limits]]
[[Asymptotes and limits at infinity#Asymptotic behavior|Asymptotic behavior]]
	[[Asymptotes and limits at infinity#Vertical asymptote|Vertical asymptote]]
	[[Asymptotes and limits at infinity#Horizontal asymptote|Horizontal asymptote]]
[[Asymptotes and limits at infinity#Limit of $x n$|Limit of x^n]]
	[[Asymptotes and limits at infinity#Behavior of polynomials|Behavior of polynomials]]
[[Asymptotes and limits at infinity#Rational limits|Rational limits]]
 
## Basics of infinite limits
Although $\infty$ isn't in $\mathbb{R}$, we can extended the concept of limits to $\infty$ and $-\infty$. While we can take $\lim\limits_{n\to \pm\infty}$, if the value of a limit itself is $\pm \infty$, then the limit does not exist. While we can leave it at DNE, $\pm \infty$ is a more specific answer.

Eg: $\lim\limits_{x\to 1} \dfrac{1}{(x-1)^{2}}$ has LHL = $\infty$ and RHL = $\infty$. While we can write that $\lim\limits_{x\to 1}$ DNE, writing $\infty$ is more specific.


## Asymptotic behavior
There are 4 types of asymptotes: Vertical, Horizontal, Oblique and Curvilinear. We will focus on vertical and horizontal asymptotes for now.

### Vertical asymptote
A vertical asymptote is any straight line that a function approaches, but never touches. As seen in the below graph of $y=\dfrac{1}{(x-1)^{2}}$, *as we approach $x=1$*, *the graph goes vertically upward but never touches the line $x=1$*. Therefore, we can say that as $x$ approaches $1$, the value of the function approaches infinity.

$$
\text{This tells us that a line } x=a \text{ is a vertical asymptote if}\lim\limits_{x\to a}=\pm \infty$$
![[Pasted image 20241117161358.png]]

### Horizontal asymptote
From the same graph above, we can see that the function approaches $0$ as $x$ goes to $\pm \infty$. Since a horizontal asymptote is parallel to the $x$ axis, we must move $x$ to the extremes of the axis to find the horizontal asymptote.
$$\text{Therefore, the line }y=b \text{ is said to be a horizontal asymptote if}\lim\limits_{x\to \pm \infty}=b$$

## Limit of $x^n$
Think about the graph of $x^n$. When $x>0$, this will always give us +ve values. However, things get a little trickier when $x<0$. If $x$ is negative, then *even powers of x will give a positive value, while odd powers of x will retain the same negative value.* Thinking about this in terms of limits to infinity,
$$\lim\limits_{x\to \infty}x^{n}= \infty,\:\lim\limits_{x\to -\infty}=\begin{cases}
-\infty\text{, n is odd} \\
\infty\:\:\:\text{, n is even}
\end{cases}$$

### Behavior of polynomials
Knowing the $\lim\limits_{x\to \infty}x^n$ is very useful when it comes to finding polynomial limits at infinity. This is because **the end behavior of a polynomial matches with the end behavior of its highest term.** This is because the term with the highest power grows so much faster than the rest, that the other terms have zero impact on the limit as $x$ goes to $\pm \infty$.
Eg: $\lim\limits_{x\to -\infty}(7x^5-4x^3+2x-9)=7\times \lim\limits_{x\to-\infty}x^5=-\infty$

## Rational limits
When we have rational limits of the form $\lim\limits_{x\to \pm\infty} \dfrac{f(x)}{g(x)}$, there are three possible cases based on the degree of $f(x)$ and $g(x)$.

### Degrees are the same
When the degrees are the same, *we check the value of the coefficients.* Eg: $\lim\limits_{x\to \infty} \dfrac{{3x+5}}{6x-8}$ will be $\dfrac{3}{6}=\dfrac{1}{2}$ from the coefficients. If you want to do it the long way, take $x$ common and cancel, you'll be left with $\lim\limits_{x\to \infty} \dfrac{{3+0}}{6-0}=\dfrac{1}{2}$.

### Degree of the denominator is greater
If the denominator has a greater degree, *then the limit to infinity is always zero.* This is because the term in the denominator will certainly outgrow the one in the numerator. This means the term in the denominator will gradually increase wrt the numerator, leading to the limit of the function being zero.

Mathematically speaking, take the highest power out and cancel. *We'll be left with $x^{n-m},\:n>m$ in the denominator as the highest power $x$ term left.* Since we know that the highest power determines the limit and $\lim\limits_{x\to \infty}\dfrac{1}{x^q}=0$, $(q=n-m)$ the limit of any rational function with the higher degree in the denominator will be zero.

### Degree of the numerator is greater
If the numerator has a greater degree, *then the limit will always be $\pm \infty$*. In this case, **the sign of the limit depends on the sign of the coefficients.** Eg: $\lim\limits_{x\to \infty} \dfrac{{5x^{3}-2x^{2}-1}}{1-3x}$. This is equal to $\lim\limits_{x\to \infty} x^{2} \dfrac{{5-\dfrac{2}{x}+\dfrac{1}{x^{3}}}}{-3+\dfrac{1}{x}}=\lim\limits_{x\to \infty} x^{2} \cdot \lim\limits_{x\to \infty} \dfrac{5}{-3}=\infty \cdot -\dfrac{5}{3}=-\infty$. Therefore, multiply infinity by the sign of the coefficients to get the final limit.


## Flashcards
Q1) Evaluate $\lim\limits_{x\to-\infty}(-4x^8+17x^3-5x+1)$
?
Ans) $=-4\times\lim\limits_{x\to -\infty}x^8$ (only the highest power matters)
$=-4\times \infty$ $= -\infty$
<!--SR:!2025-01-09,4,270-->
