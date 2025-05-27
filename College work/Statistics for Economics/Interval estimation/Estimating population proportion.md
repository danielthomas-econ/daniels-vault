---
color: var(--mk-color-orange)
tags:
  - sem2-flashcards/stats/interval_estimation
---
Quick access:
- [[#Deriving the confidence interval|Deriving the confidence interval]]
- [[#Score interval|Score interval]]
- [[#Traditional interval|Traditional interval]]
	- [[#Traditional interval#The problem with traditional intervals|The problem with traditional intervals]]
- [[#Sample size and width|Sample size and width]]

## Deriving the confidence interval
Let $p$ denote the proportion of success in a population. If $X$ is the number of successes in the sample, $p= \dfrac{X}{n}$. Since everything in the population is either a success or a failure and successes are independent of each other, we can say that *$X$ is a binomial variable with $E(X)=np$ and $\sigma_{X}=\sqrt{ np(1-p) }$*. If $np\geq 10, np(1-p) \geq 10$, **we can [[Normal distribution#Approximating binomial distribution|approximate binomial to normal.]]** Therefore, $X\sim N(np, \sqrt{ np(1-p) })$.

We know the point estimate for $p$ is $\hat{p}=\dfrac{X}{n}$. Since $\hat{p}$ is just a linear combination of $X$, it must also be normal. $E(\hat{p})=\dfrac{1}{n}\times np=p$ (unbiased) and $\sigma_{\hat{p}}=\sqrt{ \dfrac{1}{n^{2}}\times np(1-p) }=\sqrt{ \dfrac{p(1-p)}{n} }$. By converting $\hat{p}$ to standard normal and making a confidence interval, we get
$$P\left( -Z_{\frac{\alpha}{2}} < \dfrac{{\hat{p}-p}}{\sqrt{ \dfrac{p(1-p)}{n} }}<Z_{\frac{\alpha}{2}}\right)\approx 1-\alpha$$
This is only an approximate interval since *$\hat{p}$ is only an estimator of $p$*. **It is very difficult to create a CI from this since $p$ appears in many places, so isolating it becomes a challenge.**

## Score interval
One way to overcome that challenge is to simply take the challenge head on and simplify the equation. Since we have $-Z_{\frac{\alpha}{2}}$ and $Z_{\frac{\alpha}{2}}$ on both sides of the standardized $\hat{p}$, *we take the absolute value of the standardized $\hat{p}$ and then square it to eliminate the absolute value.* This gives us a quadratic in terms of $p$. This gives us two very tedious to memorize roots:
$$p= \dfrac{{\hat{p}+\dfrac{Z^{2}_{\frac{\alpha}{2}}}{2n}\pm Z_{\frac{\alpha}{2}}\sqrt{ {\dfrac{\hat{p}(1-\hat{p})}{n}}+ \dfrac{Z^{2}_{\frac{\alpha}{2}}}{4n^{2}}}}}{1+\dfrac{Z^{2}_{\frac{\alpha}{2}}}{n}}$$

## Traditional interval
Another way to overcome this challenge is simply to *replace $p$ by $\hat{p}$ in $se(p)$ so that $p$ only appears once in the numerator.* This gives us
$$P\left( -Z_{\frac{\alpha}{2}} < \dfrac{{\hat{p}-p}}{\sqrt{ \dfrac{\hat{p}(1-\hat{p})}{n} }}<Z_{\frac{\alpha}{2}}\right)\approx 1-\alpha$$
Now it becomes a lot easier to isolate $p$. By solving this, we get
$$P\left(  \hat{p}-Z_{\frac{\alpha}{2}}\sqrt{ {\dfrac{\hat{p}(1-\hat{p})}{n}} } <p < \hat{p}+Z_{\frac{\alpha}{2}}\sqrt{ \dfrac{{\hat{p}}(1-\hat{p})}{n} }\right)\approx 1-\alpha$$
This gives us $\hat{p}\pm Z_{\frac{\alpha}{2}}\sqrt{ {\dfrac{\hat{p}(1-\hat{p})}{n}} }$ as the traditional interval for population proportion. If you notice closely, this looks very much like the score interval minus the extra $\dfrac{Z^{2}_{\frac{\alpha}{2}}}{\text{some n term}}$ in each term. **If the sample size is very large, this extra term tends to zero. This means for large sample sizes, the traditional interval is very close to the score interval.**

### The problem with traditional intervals
Clearly the traditional intervals are a lot easier to memorize and compute. Why then, do we bother with score intervals? The reason is because **the coverage probability for this interval varies wildly depending on the value of $p$**. If your $p$ is close to 0.5, then its all good. Your 95% CI is right approx. 95% of the time. However, for values of $p$ close to $0$ or $1$, our 95% CI might only be correct about 85% of the time. *This is an issue even when n is large.*
![[WhatsApp Image 2025-04-04 at 02.40.03_57d273d1.jpg]]

Additionally, the traditional interval only holds when $np\geq 10, np(1-p) \geq 10$. If this criteria is not met, the traditional interval is useless. *However, the score interval does not depend on this.* Therefore, even though the score interval is tedious to calculate, **it is generally recommended that we use score intervals.**

## Sample size and width
We can use the traditional interval to find the width (just for simplicity's sake). This gives us $U-L=w =2Z_{\frac{\alpha}{2}}\sqrt{ \dfrac{\hat{p}(1-\hat{p})}{n} }$.

Squaring this and isolating $n$ gives us $n=\dfrac{4Z^{2}_{\frac{\alpha}{2}}(\hat{p}(1-\hat{p}))}{w^{2}}$. **This creates a circular dependency problem similar to [[Estimating the mean#When standard deviation is unknown|finding n when standard deviation is unknown.]]** We need $n$ to find $\hat{p}$, and we need $\hat{p}$ to find $n$.

The best workaround for this is to *be conservative and take the max value of $\hat{p}(1-\hat{p})$*. This turns out to be $\hat{p}=(1-\hat{p})=0.5$. Therefore, we can just sub $\hat{p}(1-\hat{p})=(0.5)(0.5)$ in the equation to solve for $n$. This is a good method since its the most conservative estimate for $n$, meaning we'll always get the required $n$ or a larger $n$. While a larger $n$ does make sampling harder, it ensures that $n$ is never underestimated.
