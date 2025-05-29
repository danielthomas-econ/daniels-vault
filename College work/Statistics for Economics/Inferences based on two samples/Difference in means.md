---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/stats/two_sample_inferences"
---
Quick access:
- [[#Hypothesis testing|Hypothesis testing]]
	- [[#Hypothesis testing#Case 1: Normal distribution with known standard deviation|Case 1: Normal distribution with known standard deviation]]
	- [[#Hypothesis testing#Case 2: Unknown distribution and unknown standard deviation|Case 2: Unknown distribution and unknown standard deviation]]
	- [[#Hypothesis testing#Case 3: One of the samples has a small sample size (two sample t-test)|Case 3: One of the samples has a small sample size (two sample t-test)]]
	- [[#Hypothesis testing#Case 4: t-test with equal variances (pooled t-test)|Case 4: t-test with equal variances (pooled t-test)]]
- [[#Confidence intervals|Confidence intervals]]


For the rest of the note, we'll rely on the assumptions:
1) $X_{1},X_{2}\dots,X_{m}$ is a random sample with mean $\mu_{1}$ and with variance $\sigma_{1}^{2}$
2) $Y_{1},Y_{2},\dots,Y_{n}$ is a random sample with mean $\mu_{2}$ and with variance $\sigma_{2}^{2}$
3) The **samples are independent of each other.**

## Hypothesis testing
### Case 1: Normal distribution with known standard deviation
Let's start with the same way we did hypothesis testing earlier, assuming we've sample from a population that is distributed normally with known $\sigma$.

Let $X\sim N(\mu_{1},\sigma_{1}\text{ known})$, $Y \sim N(\mu_{2}, \sigma_{2}\text{ known})$. Since we want to look at $\mu_{1}-\mu_{2}$, the most natural estimator would be $\bar{X}-\bar{Y}$.
We know $\bar{X} \sim N\left( \mu_{1}, \dfrac{\sigma_{1}}{\sqrt{ m }} \right)$, $\bar{Y} \sim N\left( \mu_{2}, \dfrac{\sigma_{2}}{\sqrt{ n }} \right)$.

$E(\bar{X}-\bar{Y})=\mu_{1} - \mu_{2}$
$V(\bar{X} - \bar{Y})=V(\bar{X})+V(\bar{Y})=\dfrac{\sigma_{1}^{2}}{m}+\dfrac{\sigma_{2}^{2}}{n}$
Therefore, $\sigma_{\bar{X}-\bar{Y}}=\sqrt{ \dfrac{\sigma_{1}^{2}}{m}+\dfrac{\sigma_{2}^{2}}{n} }$
**This tells us that $\bar{X}-\bar{Y} \sim N\left( \mu_{1}-\mu_{2},\sqrt{ \dfrac{\sigma_{1}^{2}}{m}+\dfrac{\sigma_{2}^{2}}{n} } \right)$**.

Standardizing this, we get the test statistic $Z= \dfrac{{(\bar{X}-\bar{Y})-(\mu_{1}-\mu_{2})}}{\sqrt{ \dfrac{\sigma_{1}^{2}}{m}+\dfrac{\sigma_{2}^{2}}{n} }} \sim SN$

Then we have the normal procedure. Calculate the value of the test statistic and use the decision rule to reject or fail to reject $H_{0}$.

### Case 2: Unknown distribution and unknown standard deviation
If $X\sim\:?(\mu_{1}, \sigma_{1}?)$, $Y\sim\:?(\mu_{2}, \sigma_{2}?)$, **we must use CLT to approximate the distribution and standard deviation of $\bar{X}$**. If $n>30,$ $\bar{X} \approx N$ and if $n>40$, then $\sigma_{1} \approx s_{1}$. You end up getting the same test statistic but with $s$ instead of $\sigma$ and the statistic is *approximately standard normal, not exactly.* The rest of the procedure remains the same. 

One thing to keep in mind is that **although standard deviations are unknown, they must NOT be the same.** In that case, we must use a different test. To make sure they're not the same, we must [[Ratio of variances|test for ratio of standard deviations.]]

### Case 3: One of the samples has a small sample size (two sample t-test)
If either $m,n$ are small and the variances are unknown, then we have to use a two sample t test. The test statistic is the same as the previous case. We have $T= \dfrac{{(\bar{X}-\bar{Y}) - (\mu_{1}-\mu_{2})}}{\sqrt{ \dfrac{\sigma_{1}^{2}}{m}+\dfrac{\sigma_{2}^{2}}{n} }}\sim t_{\nu}$.

The degrees of freedom is given by the formula
$$\nu = \dfrac{{\left( \dfrac{s_{1}^{2}}{m}+\dfrac{s_{2}^{2}}{n} \right)^{2}}}{\dfrac{\left( \dfrac{s_{1}^{2}}{m} \right)^{2}}{m-1}+\dfrac{\left( \dfrac{s_{2}^{2}}{n} \right)^{2}}{n-1}} = \dfrac{(se_{1}^{2}+se_{2}^{2})^{2}}{\dfrac{(se_{1})^{4}}{m-1}+\dfrac{(se_{2})^{4}}{n-1}}$$
where $se_{1} = \dfrac{s_{1}}{\sqrt{ m }}$, $se_{2} = \dfrac{s_{2}}{\sqrt{ n }}$. Note that **the value of $\nu$ must be ROUNDED DOWN to the nearest integer** and then used as df.

### Case 4: t-test with equal variances (pooled t-test)
This test should only be used when there is *strong evidence that $\sigma_{1}^{2}=\sigma_{2}^{2}=\sigma^{2}$*. If you feel the sample variances are quite close, you could conduct a hypothesis test for the [[Ratio of variances#Hypothesis testing|ratio of variances.]] If you end up accepting the null ($\sigma_{1}^{2}=\sigma_{2}^{2}$), then proceed with this method, otherwise conduct a normal t test.

Now that the variances are same, our test statistic becomes $T= \dfrac{{(\bar{X}- \bar{Y}) - (\mu_{1}-\mu_{2})}}{\sqrt{ \hat{\sigma}^{2}\left( \dfrac{1}{m}+\dfrac{1}{n} \right) }}\sim t$. **Since we don't know $\sigma^{2}$**, **we have to use an estimator for it, which is why the test statistic has a $\hat{\sigma}^{2}$ instead of $\sigma^{2}$**.

It's pretty obvious that combining the sample variances would be a better estimate for variance than taking either of the two sample variances. We can't directly take an average of the two sample variances however, as that would fail to account for sample size differences. *Therefore, our variance estimator is the weighted average of the sample variances, where the weights are the degrees of freedom of each sample.* Therefore, $S_{p}^{2}= \dfrac{{df_{1}s_{1}^{2} + df_{2}s_{2}^{2}}}{df_{1}+df_{2}}= \dfrac{{(m-1)s_{1}^{2}+(n-1)s_{2}^{2}}}{m+n-2}$.

Replacing this as our estimate for sample variance gives us the test statistic $T= \dfrac{{(\bar{X}-\bar{Y})-(\mu_{1} - \mu_{2})}}{\sqrt{ S_{p}^{2}\left( \dfrac{1}{m}+\dfrac{1}{n} \right) }}\sim t_{m+n-2}$.

Continue testing the hypothesis using this as your test statistic.

## Confidence intervals
From deriving confidence intervals previously, we know that the area under the $z$ curve between $-z_{\frac{\alpha}{2}}$ and $z_{\frac{\alpha}{2}}$ is $1-\alpha$. We also know that $X,Y\sim N \implies \bar{X},\bar{Y} \sim N \implies \bar{X}-\bar{Y} \sim N \implies \dfrac{{(\bar{X}-\bar{Y}) - (\mu_{1}-\mu_{2}) }}{\sqrt{ \dfrac{\sigma_{1}^{2}}{m}+\dfrac{\sigma_{2}^{2}}{n} }}\sim SN$

Therefore, $P\left( -z_{\frac{\alpha}{2}} < \dfrac{{(\bar{X}-\bar{Y}) - (\mu_{1}-\mu_{2}) }}{\sqrt{ \dfrac{\sigma_{1}^{2}}{m}+\dfrac{\sigma_{2}^{2}}{n} }} < z_{\frac{\alpha}{2}} \right) = 1-\alpha$

Isolating $\mu_{1}-\mu_{2}$ tells us the $100(1-\alpha)\%$ CI for the difference of means is given by $$(\bar{X} - \bar{Y}) \pm z_{\frac{\alpha}{2}}\sqrt{ \dfrac{\sigma_{1}^{2}}{m}+\dfrac{\sigma_{2}^{2}}{n} }$$If $X$ and $Y$ aren't normal, we can use CLT to get an approximate confidence interval. If $\sigma$ is unknown, approximate it using $s$ if the sample size is large enough. *If you're using a t-test, simply replace $z_{\frac{\alpha}{2}}$ by $t_{\frac{\alpha}{2}, \nu}$*.