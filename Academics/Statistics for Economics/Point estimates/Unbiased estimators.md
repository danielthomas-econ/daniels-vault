---
color: var(--mk-color-pink)
tags:
  - sem2-flashcards/stats/point_estimates
---
Quick access:
- [[#Estimates and estimators|Estimates and estimators]]
- [[#Unbiased estimators|Unbiased estimators]]
	- [[#Unbiased estimators#Making biased estimators unbiased|Making biased estimators unbiased]]
- [[#Mean squared error|Mean squared error]]
- [[#Minimum variance unbiased estimators|Minimum variance unbiased estimators]]
	- [[#Minimum variance unbiased estimators#Efficiency|Efficiency]]

## Estimates and estimators
The whole point of statistical inference is almost always to draw a conclusion about one of the parameters of the population from a sample. For example, to get an idea of what $\mu$ is, we can get $\bar{x}$ from many samples and use that to estimate $\mu$. 

In general, for a population parameter $\theta$, *we want to find a single number that represents a sensible value of $\theta$*. This number is called the **point estimate.** The statistic used to obtain the estimate is called the **point estimator.** Note that the *estimator is a function,* while the *estimate is the output of the estimator function,* which means the estimate is always a value.

The symbol $\hat{\theta}$ is used to denote both the estimator of $\theta$ and the point estimate resulting from the sample. Therefore, we read $\hat{\mu}=\bar{X}$ as 'the point estimator of $\mu$ is the sample mean $\bar{X}$.'

## Unbiased estimators
A point estimator is said to be unbiased if $E(\hat{\theta})=\theta$. In other words, we can call an estimator *unbiased if its sampling distribution is always centered at the true value of the parameter.* If $\hat{\theta}$ is biased, there will be a difference between its expected value and the real value of $\theta$. Therefore, *the difference $E(\hat{\theta})-\theta$ is called the bias of $\hat{\theta}$*.

An estimator is stb **asymptotically unbiased** if the bias term goes to zero as $n\to \infty$. For example, $E(\bar{x}^{2})=\mu^{2}+\dfrac{\sigma^{2}}{n}$. Therefore, the bias is $\dfrac{\sigma^{2}}{n}$. $\lim\limits_{n\to \infty} \dfrac{\sigma^{2}}{n}=0$. Therefore, $\bar{x}^{2}$ is asymptotically unbiased.

### Making biased estimators unbiased
It is possible to algebraically manipulate biased estimators to make them unbiased. Consider the case where $E(\hat{\theta})= \dfrac{n}{n+1}\theta$. Clearly, $E(\hat{\theta})\ne \theta$. **However, we can isolate $\theta$ in the RHS by bringing the other terms inside the expectation.** Therefore, $E\left( \dfrac{(n+1)\hat{\theta}}{n} \right)=\theta$. Therefore, $\dfrac{(n+1)\hat{\theta}}{n}$ is an unbiased estimator of $\theta$.

## Mean squared error
Another way to think about measuring the bias of the estimator is to consider the squared error $(\hat{\theta}-\theta)^{2}$. If $\hat{\theta}$ a good estimator, this value will be small. Therefore, if the expected value of the squared error is small, that means $\hat{\theta}$ is a good estimator.
$$MSE=E[(\hat{\theta}-\theta)^{2}]$$
We can simplify this further.
$$\begin{align}
E[(\hat{\theta}-\theta)^{2}]=&E(\hat{\theta}^{2}+\theta^{2}-2\theta \hat{\theta}) \\
=&E(\hat{\theta}^{2})+\theta^{2}-2\theta E(\hat{\theta}) \\
=&V(\hat{\theta})+[E(\hat{\theta})]^{2}+\theta^{2}-2\theta E(\hat{\theta}) \\
=&V(\hat{\theta})+[E(\hat{\theta})-\theta]^{2} \\
=&V(\hat{\theta})+Bias^{2}
\end{align}$$
Since both variance and bias are bad for our estimator, **we want to minimize MSE to reduce both of their values.**

## Minimum variance unbiased estimators
One problem with unbiased estimators is that **if we can find two unbiased estimators, then any weighted average of the two will be an unbiased estimator.** In this case, what estimator should we pick?

The general rule is that among all unbiased $\hat{\theta}$, *pick the one with minimum variance.* The selected $\hat{\theta}$ is called the minimum variance unbiased estimator (MVUE) of $\theta$. The MVUE (in a way) is the most likely among all estimators to provide an estimate close to the true $\theta$ since its pdf is very concentrated near $\theta$ and sparse away from $\theta$. This can clearly be seen below as $\hat{\theta}_{1}$ is certainly the better estimator.
![[WhatsApp Image 2025-02-27 at 10.29.42_ab8e20e1.jpg]]

### Efficiency
$\hat{\theta}_{1}$ is stb more efficient than $\hat{\theta}_{2}$ if $V(\hat{\theta}_{1})<V(\hat{\theta}_{2})$. Therefore, an estimator with a lower variance is stb a more efficient estimator. Note that efficiency can only be used to compare two estimators. You cannot simply state $\hat{\theta}_{1}$ is efficient without comparing it to another variable.



## Flashcards
Q1) Part b)![[WhatsApp Image 2025-02-27 at 11.14.43_4a8a03c4.jpg]]
?
Ans) ![[Pasted image 20250227111552.png]]
The standard error of an estimator is *the standard deviation of the estimator.* The part I missed is that $V(X_{i})$ can be written as $n_{i}p_{i}q_{i}$ since $X_{i}$ is binomial (either they smoke filter or they don't, and the trials are independent). A lot of questions seem to use binomial variables, **so always check if we can substitute formulae for binomial variables to simplify.**
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
