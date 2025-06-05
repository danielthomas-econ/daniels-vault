---
color: var(--mk-color-gray)
tags:
  - sem1-flashcards/stats/discrete
---
Quick access
- [[#What is a geometric distribution|What is a geometric distribution]]
- [[#Expectation and variance|Expectation and variance]]

## What is a geometric distribution
Geometric distributions are a special case of the negative binomial distribution. It is a **binomial distribution where $X\to \text{no. of trials before }r^{th}\text{ success}$**. **If $r=1$**, **we call it a geometric distribution.** Therefore, $X$ represents the number of trials to get one success. This means that $X=1,2,3\dots$. We can also take $X$ as the number of failures to get one success, so $X=0,1,2\dots$. 

When we take $X$ as the number of failures to get one success, we get the PMF as $(1-p)^xp$.

## Expectation and variance
When $X$ is taken to be number of failures to get a success, we get $E(X)=\dfrac{{1-p}}{p}$ and $V(X)=\dfrac{{1-p}}{p^2}$.

If we take $Y$ as the number of trials to get one success, then $Y=X+1$. This makes $E(Y)=\dfrac{{1-p}}{p}+1=\dfrac{1}{p}$, and $V(Y)=V(X+1)=V(X)=\dfrac{{1-p}}{p^{2}}$.