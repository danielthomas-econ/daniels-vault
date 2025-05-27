---
color: var(--mk-color-pink)
tags:
  - sem2-flashcards/stats/point_estimates
---
Quick access:
- [[#Core concept|Core concept]]
- [[#Moments and moment estimators|Moments and moment estimators]]

## Core concept
The basic idea of this method is to *equate certain sample characteristics (like sample mean) to the population expected values(like population mean).* Then solving the equation(s) for the unknown parameter value(s) gives you their estimators.

## Moments and moment estimators
Let $X_{1},X_{2}\dots X_{n}$ be a random sample from a pmf or pdf $f(x)$. For $k=1,2,\dots$, the $k^{th}$ population moment (also called $k^{th}$ moment of the distribution) is $E(X^k)$. The $k^{th}$ sample moment is $\dfrac{1}{n}\sum\limits_{i=1}^{n}X_{i}^k$.
$$\begin{align}
k^{th} \text{ population moment} &= E(X^k) \\
k^{th} \text{ sample moment } &= \dfrac{1}{n} \sum\limits_{i=1}^{n}X_{i}^k
\end{align}$$
Let $X_{1}, X_{2},\dots X_{n}$ be a random sample from a pmf or pdf $f(x;\theta_{1}, \theta_{2},\dots \theta_{m})$, where $\theta_{1},\theta_{2},\dots \theta_{m}$ are parameters whose values are unknown. Then, the *moment estimators* $\hat{\theta}_{1},\dots,\hat{\theta}_{m}$ are obtained by **equating the first $m$ sample moments to their corresponding first $m$ population moments, and then solving for $\theta_{1},\dots \theta _m$**.
$$\begin{align}
\text{First moment: } E(X) & =\bar{X} \left( \sum \dfrac{X_{i}}{n} \right) \\
\text{Second moment: } E(X^{2}) &= \sum\limits_{i=1}^{n}X_{i}^{2} \\
\dots
\end{align}$$
For example, *if we have a pdf with two parameters, we look at the first two moments.* We get two equations, and they'll be in terms of the two parameters. Solving this system will then give us the estimator of the parameters.