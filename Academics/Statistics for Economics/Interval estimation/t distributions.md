---
color: var(--mk-color-orange)
tags:
  - sem2-flashcards/stats/interval_estimation
---
Quick access:
- [[#The basis behind the t distribution|The basis behind the t distribution]]
- [[#Properties of t distributions|Properties of t distributions]]

## The basis behind the t distribution
We know that for a large $n$, we can say that $Z=\dfrac{{\bar{X}-\mu}}{\dfrac{s}{\sqrt{ n }}}$ has an approximately similar to a standard normal distribution. When $n$ is small, $s$ is no longer likely to be close to $\sigma$. *This increases the level of variability if n is small.* The $t$ distribution is a family of distributions that takes this into account.

When $\bar{X}$ is the mean of a **sample of size $n$ from a normal distribution** with mean $\mu$, the rv $T=\dfrac{{\bar{X}-\mu}}{\dfrac{s}{\sqrt{ n }} }$ has a probability distribution called the $t$ distribution with $n-1$ degrees of freedom (df).  ^36ef22

We can see that *t distributions depend on the degree of freedom.* Therefore, $X\sim t(\nu)$. $\nu$ is pronounced $new$ and represents the degrees of freedom.

## Properties of t distributions
Let $t_{\nu}$ denote the t distribution with $\nu$ df:
i) Each $t_{\nu}$ curve is bell shaped and centered at $0$
ii) Each $t_{\nu}$ curve is more spread out than the standard normal $z$ curve
iii) As $\nu$ increases, the spread of the corresponding $t_{\nu}$ curve decreases
iv) **As $\nu\to \infty$ the sequence of $t_{\nu}$ curves approaches the standard normal curve.** Sometimes the $z$ curve is called the $t$ curve with infinite degrees of freedom.

$t_{\alpha,\nu}$ is the number on the measurement axis for which the area under the $t$ curve with $\nu$ degrees of freedom *to the right of $t_{\alpha,\nu}$* is $\alpha$. *This is called the critical value.* This works very similar to how $Z_{\alpha}$ is the value on the measurement axis for which area to the left of $Z_{\alpha}=\alpha$. **However, $t$ distributions look at area to the right.** Eg: $t_{0.05,6}$ is the critical value for which we have an area of $0.05$ to the right of $t_{0.05,6}$ for a $t$ curve with $6$ df.


