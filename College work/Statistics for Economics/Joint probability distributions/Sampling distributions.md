---
color: var(--mk-color-teal)
tags:
  - sem2-flashcards/stats/joint_distributions
---
Quick access:
- [[#Statistics and their distributions|Statistics and their distributions]]
- [[#Random sample|Random sample]]
- [[#How is the sample mean distributed?|How is the sample mean distributed?]]
	- [[#How is the sample mean distributed?#For the total sum of the population|For the total sum of the population]]

## Statistics and their distributions
A statistic is *any quantity whose value can be calculated from sample data.* Before we obtain a sample, there is uncertainty as to what the value of a statistic will be. Therefore, statistics are also random variables. 

Since statistics are random variables, they will have their own probability distributions. *The probability distribution of a statistic is called a sampling distribution.*

## Random sample
The rvs $X_{1}, X_{2},\dots,X_{n}$ are said to form a random sample if:
i) the $X_{i}$'s are independent rvs
ii) every $X_{i}$ has the same probability distribution

This can be simplified to saying that the $X_{i}$'s are **independent and identically distributed (iid).** 

## How is the sample mean distributed?
If $X_{1},X_{2},\dots,X_{n}$ is a random sample from a population with a mean $\mu$ and standard deviation $\sigma$, then
i) $E(\bar{X})=\mu$
ii) $V(\bar{X})= \dfrac{\sigma^{2}}{n}$

This tells us that the sampling distribution of the mean is centered exactly at the population mean. Also, *the distribution becomes more concentrated at $\mu$ as the sample size increases (since variance $\dfrac{\sigma^{2}}{n}$ will fall).* 

The standard deviation of the distribution of the mean is $\dfrac{\sigma}{\sqrt{ n }}$, and is called **the standard error of mean** as it tells us how far we'd expect the sample mean to be from the population mean. **Note that SEM is always $\dfrac{\sigma}{\sqrt{ n }}$ and not $\dfrac{\sigma^{2}}{n}$**, **which is the variance, not standard error, of mean.** 

### For the total sum of the population
If we get the value of $E(\bar{X})$ and $V(\bar{X})$, we can easily get the values for $T_{0}$ (sum of all $X_{i}$). We know $\bar{x}= \dfrac{{x_{1}+x_{2}+\dots+x_{n}}}{n}$. The numerator here is simply $T_{0}$. Therefore, $T_{0}=n\bar{X}$. Sub that into the previous results and use rules of expectation and variance. 

i) $E(T_{0})=E(n\bar{X})=nE(\bar{X})=n\mu$
ii) $V(T_{0})=V(n\bar{X})=n^{2}V(\bar{X})=n^{2} \dfrac{\sigma^{2}}{n}=n\sigma^{2}$

