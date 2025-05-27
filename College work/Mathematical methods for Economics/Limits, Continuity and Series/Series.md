---
color: var(--mk-color-pink)
tags:
  - sem1-flashcards/mme
---
Quick access:
- [[#Finite geometric series|Finite geometric series]]
- [[#Infinite geometric series|Infinite geometric series]]
- [[#Convergence of infinite geometric series|Convergence of infinite geometric series]]
	- [[#Convergence of infinite geometric series#Ratio test|Ratio test]]

## Finite geometric series
We obtain each term in a geometric series by multiplying the previous one by a constant $k$. Therefore, the sum of a finite geometric series is represented as $$s_{n}=a+ak+ak^{2}+\dots+ak^{n-2}+ak^{n-1}$$

We can obtain $k$, the common ratio, using $\dfrac{s_{n+1}}{s_{n}}$. This ratio must remain constant for all values of $\dfrac{s_{n+1}}{s_{n}}$. **It is the same as a geometric [[Sequences|sequence]]**, **but we sum up all the terms to get a series.**

We can derive the formula for the sum of a finite geometric series by *multiplying each term of the series by $k$ and subtracting the new series from the original one.* This gives us $s_{n}-ks_{n}=a-ak^n$ (as all the other terms are common between the two series and get cancelled). This results in $s_{n}(1-k)=a(1-k^n)$. Therefore, the formula for the sum of a finite geometric series is $$s_{n}=\dfrac{a(1-k^n)}{1-k}$$
## Infinite geometric series
This is essentially a geometric series with no last term. Therefore, we can represent it as $a+ak+ak^{2}+\dots ak^{n-1}+\dots$. To get the sum of this infinite series, **we consider the sum of a finite geometric series when $n\to \infty$**. Doing this, we get 
$$s_{n}=\dfrac{a}{1-k}, |k|<1$$ ^be3ec6

If $|k|>1$, then the series diverges and has no finite sum. When $k=1$, $s_{n}=na$. This goes to $\infty$ if $a>0$ and $-\infty$ if $a<0$. If $k=-1$, $s_{n}=a$ when $n$ is odd and $0$ when $n$ is even.

## Convergence of infinite geometric series
If a series converges, *then its terms must go to $0$* (necessary condition). It is important to note that **terms going to $0$ doesn't imply convergence, but terms not going to $0$ implies the series is definitely not convergent.**  

This means that knowing the terms of a series goes to $0$ isn't sufficient to conclude a series is convergent. However, knowing that a series is convergent is sufficient to conclude its terms go to $0$. If the terms do not go to $0$, we can safely say its a divergent series. Eg: Harmonic series $a_{n}=\dfrac{1}{n}$ diverges even though the terms approach $0$.

### Ratio test
The ratio test takes $b_{n}=\dfrac{a_{{n+1}}}{a_{n}} (a_{n}\ne 0)$. If $b_{n}$ doesn't converge, then the ratio test cannot tell us anything. However, if $b_{n}\to l$:
- If $|l|<1$, then $\sum\limits_{n=1}^{\infty} a_{n}$ converges
- If $|l|>1$, then $\sum\limits_{{n=1}}^{\infty} a_{n}$ diverges
- If $|l|=1$, then the result is ambiguous

Q) Prove that the series $a_{n}=e^x$ converges.
?
Ans) $e^x=1+\dfrac{x}{1!}+\dfrac{x^{2}}{2!}+\dfrac{x^{3}}{3!}\dots \dfrac{x^n}{n!}\dots$
We can use the ratio test to check for convergence. $\dfrac{a_{{n+1}}}{a_{n}}=\dfrac{\dfrac{\dfrac{x^{n+1}}{(n+1)!}}{x^n}}{n!}=\dfrac{x}{n+1}$. *For a fixed $x$*, *this series converges* as $n\to \infty$, $\dfrac{x}{n+1}\to 0$. Therefore, $e^x$ converges for all $x$ since $\dfrac{x}{n+1}\to l$, $|l|<1$.
