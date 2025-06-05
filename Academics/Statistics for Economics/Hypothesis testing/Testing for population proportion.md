---
color: var(--mk-color-yellow)
tags:
  - "#sem2-flashcards/stats/hypothesis_testing"
---
Quick access:
- [[#Large sample tests for population proportion|Large sample tests for population proportion]]

## Large sample tests for population proportion
Generally, we use the test statistic $Z = \dfrac{{\hat{\theta}-\theta_{0}}}{\sigma_{\theta}}$, where $\hat{\theta}$ is the estimator of the parameter, $\theta_{0}$ is the null value and $\sigma_{\theta}$ is the standard deviation of the parameter. We'll use this to find the test statistic for population proportion.

Let $p$ be the proportion of successes in the population. We know its estimator is $\hat{p} = \dfrac{X}{n}$. We've already derived that $\hat{p}\approx N\left( p, \sqrt{ \dfrac{p(1-p)}{n} } \right)$ when finding [[Estimating population proportion#Deriving the confidence interval|the confidence interval for population proportion.]]  *Unfortunately, we don't know the value of $p$*, *so we don't know the exact value of our parameters.* To fix this problem, let's recall that we conduct hypothesis testing by **assuming that null is true.** When null is true, $p=p_{0}$ (the null value). Now we can say that $\hat{p} \approx N\left( p_{0}, \sqrt{ \dfrac{p_{0}(1-p_{0})}{n} } \right)$. 

Standardizing gives us the test statistic $Z = \dfrac{{\hat{p} - p_{0}}}{\sqrt{ \dfrac{p_{0}(1-p_{0})}{n  } }}$. **Note that we can only use this when $np_{0}\geq 10$ and $n(1-p_{0})\geq 10$ as that was a basic assumption we used when building this formula.** 

Now that we have the test statistic, the rest of the process is same as before.