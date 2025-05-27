---
color: var(--mk-color-orange)
---
Quick access:
- [[#Deriving the confidence interval|Deriving the confidence interval]]
	- [[#Deriving the confidence interval#With standard deviation unknown|With standard deviation unknown]]
- [[#When the population isn't normally distributed|When the population isn't normally distributed]]
	- [[#When the population isn't normally distributed#Standard deviation is known|Standard deviation is known]]
	- [[#When the population isn't normally distributed#Standard deviation is not known|Standard deviation is not known]]
- [[#Sample size and width|Sample size and width]]
	- [[#Sample size and width#When standard deviation is unknown|When standard deviation is unknown]]

## Deriving the confidence interval
Suppose we have $X \sim N(\mu,\sigma)$, with $\sigma$ unknown. In this case, we know that $\bar{X}\sim N\left( \mu, \dfrac{\sigma}{\sqrt{ n }} \right)$. Therefore, we can say that $\dfrac{{\bar{X}-\mu}}{\dfrac{\sigma}{\sqrt{ n }}} \sim \text{Standard Normal (SN)}$. Let's say we want to derive a 95% confidence interval. The area between $-1.96$ and $1.96$ is $0.95$. Therefore, $P\left( -1.96 < \dfrac{{\bar{X}-\mu}}{\dfrac{\sigma}{\sqrt{ n }}}<1.96 \right)=0.95$.

**Our main goal is to isolate $\mu$ in the middle to get an interval for only $\mu$**. Let's start by multiplying $\dfrac{\sigma}{\sqrt{ n }}$ throughout. 
$\implies P\left( -\dfrac{1.96\sigma}{\sqrt{ n }}<\bar{X}-\mu < \dfrac{1.96\sigma}{\sqrt{ n }} \right)=0.95$
Subtract $\bar{X}$ throughout and multiply by $-1$:
$\implies P\left( \bar{X}-\dfrac{1.96\sigma}{\sqrt{ n }} < \mu < \bar{X}+\dfrac{1.96\sigma}{\sqrt{ n }}\right)=0.95$

This clearly gives us an interval $\left( \bar{X}\pm \dfrac{1.96\sigma}{\sqrt{ n }} \right)$ which has a $95\%$ chance of containing the population mean.

We can generalize this as for $X\sim N(\mu,\sigma)$ and $\sigma$ unknown, the $(1-\alpha)100\%$ CI for $\mu$ is
$$\bar{X}\pm Z_{\frac{\alpha}{2}} \dfrac{\sigma}{\sqrt{ n }}$$ ^6e1641

### With standard deviation unknown
If the population is distributed normally but we don't know the standard deviation, then the previous formula becomes useless. In this case, **we use [[t distributions]]**. Just replace the $Z$ value with the $t$ value and use $s$ to approximate $\sigma$. Therefore, for $X\sim N(\mu,\sigma?)$, the $(1-\alpha)100\%$ CI for $\mu$ is $\bar{X}\pm t_{\frac{\alpha}{2}} \dfrac{s}{\sqrt{ n }}$.

## When the population isn't normally distributed
In the previous case, we could immediately build the interval since we knew the population is normal and would have a symmetric distribution. But if you don't know the distribution, you cannot use this information. We have to take a few more steps to get the confidence interval.

### Standard deviation is known
Let's consider the same case as before, but with the distribution unknown. Therefore, $X\sim\:?(\mu,\sigma)$, with $\sigma$ known. **If the sample size is large enough $(n>30)$**, **we can invoke [[Central limit theorem|the central limit theorem]] and use it to estimate the sample mean.** Using CLT tells us that $\bar{X} \approx N\left( \mu, \dfrac{\sigma}{\sqrt{ n }} \right)$. This is the exact same as before, except the inequality is replaced by an approximation. Therefore, $\dfrac{{\bar{X}-\mu}}{\dfrac{\sigma}{\sqrt{ n }}} \approx SN$, and we can continue down the same path to get the same inequality with an approximation sign. Therefore, for $X\sim\: ?(\mu,\sigma)$, a $(1-\alpha)100\%$ CI is given by $\approx\bar{X}\pm Z_{\frac{\alpha}{2}} \dfrac{\sigma}{\sqrt{ n }}$.

### Standard deviation is not known
If we know neither the mean nor the standard deviation, then *we must estimate the standard deviation.* To approximate $S$ as $\sigma$, **we need the sample size to be large enough, which is $n>40$ in this case.** The interval is the same, only difference being $\sigma$ replaced by $\sigma$. Therefore, for $X \sim\:?(\mu, \sigma?)$, a $(1-\alpha)100\%$ CI is given by $\approx \bar{X}\pm Z_{\frac{\alpha}{2}} \dfrac{s}{\sqrt{ n }}$. This is called **the large sample confidence interval for $\mu$**.


## Sample size and width
The width of a confidence interval is given by the upper limit minus the lower limit, which gives us $$w = 2Z_{\frac{\alpha}{2}} \dfrac{\sigma}{\sqrt{ n }}$$
To find the sample size necessary for a given width $w$, we can simply isolate the $n$. This gives us 
$$n=\left( 2Z_{\frac{\alpha}{2}} \dfrac{\sigma}{w} \right)^{2}$$
**We can see an inverse relation between the sample size and width.** The half width is sometimes called the *bound on error.* This is because if we allow for a maximum error of 5 (thereby bounding the error), we can go 5 above and 5 below the true mean (over and underestimating). Therefore, the width of the interval becomes 10, which is twice the bound on error.

### When standard deviation is unknown
Usually when $\sigma$ was unknown, we'd approximate it as $s$ given that $n>40$. However, an issue arises if we use this method to calculate $n$. This is because **the value of $s$ is only known after the sample is collected, i.e. after $n$ has been chosen already.** This creates an issue where we need $n$ to find $s$, and we need $s$ to find $n$.

There is one reasonable workaround to this problem. If we can get a good estimate on the range of the population, then we can say $s \approx \dfrac{{Range}}{4}$ (provided the distribution isn't too skewed). We can then sub this $s$ in place of $\sigma$ in the previous formula and solve for $n$.