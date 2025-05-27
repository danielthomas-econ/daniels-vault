---
color: var(--mk-color-pink)
tags:
  - sem2-flashcards/stats/point_estimates
---
Quick access:
- [[#Core concept|Core concept]]
- [[#Maximum likelihood estimates|Maximum likelihood estimates]]
- [[#Difficulties with MLE|Difficulties with MLE]]

## Core concept
We have a certain pmf or pdf we want to find the MLE for. Consider we have a sample size of $n$. Since we have $n$ independent pdfs, we can multiply them. Then we simplify this function, called the likelihood function $(\mathcal{L})$.

*Our goal is to maximize this likelihood function.* This can be a little tricky sometimes because of how complex these functions can get. **A simple trick is to take $\ln(\mathcal{L})$ and maximize that. Since $\mathcal{L}$ is the product of pdfs, $\ln(\mathcal{L})$ becomes a sum, making it simpler to work with.** Also, $\ln$ is a monotically increasing function. Therefore, that $p^{*}$ which maximizes $\ln(\mathcal{L})$ will also maximize $\mathcal{L}$, making it a much easier method.

## Maximum likelihood estimates
Let $X_{1},X_{2}\dots,X_{n}$ have a joint pmf or pdf $f(x_{1},x_{2},\dots,x_{n};\theta_{1},\theta_{2},\dots \theta _{m})$ where the parameters $\theta_{1}, \theta_{2}, \theta_{n}$ have unknown values. *This is called the likelihood function when $x_{1},\dots,x_{n}$ are the observed sample values and its a function of $\theta_{1},\dots \theta_{m}$*. The maximum likelihood estimates $\hat{\theta}_{1},\dots \hat{\theta}_{m}$ are those values of $\theta_{i}$ that maximize the likelihood function.

Maximizing the likelihood function *gives us the parameter values for which the observed sample is most likely to have been generated.* In other words, it gives us parameter values that most closely agree with the observed data.

When the sample size $n$ is large, the MLE of any parameter $\theta$ is approximately unbiased $(E(\hat{\theta})\approx \theta)$ and has a variance that is either as small or nearly as small as can be achieved by any estimator. Therefore, **$\hat{\theta}_{MLE}$ is approximately the minimum variance unbiased estimator (MVUE) of $\theta$** (for large $n$).

## Difficulties with MLE
Problems arise with this method when *the parameter is part of the domain of the function.* In this case, we cannot use calculus to maximize the function and we'll need graphical techniques.

Suppose we have $X \sim U(\theta,9)$. Clearly, the parameter is in the domain of the function. Let's solve this.
$f(x;\theta)= \dfrac{1}{9-\theta},\:\theta<x<9$
$\mathcal{L}=f(x_{1},x_{2},\dots x_{n};\theta)=\dfrac{1}{(9-\theta)}\times \dfrac{1}{(9-\theta)}\dots \times \dfrac{1}{(9-\theta)}=\dfrac{1}{(9-\theta)^n}$
Suppose we have a sample of $(-2,4,8, 8.2)$. **Since $\theta$ is population min, any value of $\theta>-2$ will not be possible, since population min must be less than equal to the sample min.** Therefore, we get a jump discontinuity at $\theta=-2$. Our graph will look something like this:
![[WhatsApp Image 2025-04-04 at 19.17.24_4a917be9.jpg]]
We can sub in $\theta=-5,-3,-2$ (any values $\leq -2$) with $n=4$ to arrive at those probabilities. For $\theta=-2$, the probability is $\dfrac{1}{11^4}$. However, for $\theta>-2$ the probability becomes zero. Therefore, $\theta=-2$ is the MLE for $\theta$.

