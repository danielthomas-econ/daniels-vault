---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/stats/two_sample_inferences"
---
Quick access:
- [[#Notation|Notation]]
- [[#Hypothesis testing|Hypothesis testing]]
- [[#Confidence interval|Confidence interval]]


### Notation
Proportion of successes in population:
1 - $p_{1}$
2 - $p_{2}$

Proportion of successes in sample:
1 - $X$
2 - Y

Sample size:
1 - $m$
2 - $n$

## Hypothesis testing
Consider two independent samples. **This would mean $X$ and $Y$ are independent too.** If the samples are relatively small compared to their populations, then $X\sim B(m, p_{1})$ and $Y\sim B(n,p_{2})$. **We don't know $p_{1},p_{2}$**, **but their natural estimators are** $\hat{p}_{1},\hat{p}_{2}=\dfrac{X}{m}, \dfrac{Y}{n}$.

We start with the null hypothesis that they're the same. $$\begin{align}
H_{0}&: p_{1}-p_{2}=0 \\
H_{a}&: p_{1}-p_{2} \ne 0
\end{align}$$
Since we assume null to be true, let $p_{1}=p_{2}=p_{0}$. Since both are binomial, we can [[Normal distribution#Approximating binomial distribution|approximate binomial to normal]] if $mp_{0} \geq 10, m(1-p_{0}) \geq 10$ (same for $n$). This would mean $X \approx N(mp_{0}, \sqrt{ mp_{0}(1-p_{0}) })$. Therefore, $\dfrac{X}{m}\approx N\left( p_{0}, \sqrt{ \dfrac{p_{0}(1-p_{0})}{m} } \right)$ (and the same goes for $\dfrac{Y}{n}$).

Therefore, $\hat{p}_{1}-\hat{p}_{2} \approx N\left( 0,\sqrt{ p_{0}(1-p_{0})\left( \dfrac{1}{m}+\dfrac{1}{n} \right) } \right)$. *To get the standard deviation, first add the variances then square root, don't directly add standard deviations.* Standardizing gives us the test statistic $Z = \dfrac{{(\hat{p}_{1}-\hat{p}_{2}) - 0}}{\sqrt{ p_{0}(1-p_{0})\left( \dfrac{1}{m}+\dfrac{1}{n} \right) }} \approx SN$.

However, **we cannot use this test statistic since $p_{0}$ is unknown.** We've simply assumed the values to be equal under null, but we haven't specified what that value is. $p_{0}$ is the proportion of successes in both the samples. Therefore, **the natural estimator of $p_{0}$ would be the the weighted average of successes in the samples.** We can also say that the total successes in the samples is $X+Y$ and the total size is $m+n$ and use this to get an estimator for $p_{0}$. Both these approaches are equivalent.
$$\hat{p}_{0} = \dfrac{{m\hat{p}_{1} + n\hat{p}_{2}}}{m+n}= \dfrac{{m \dfrac{X}{m}+ n \dfrac{Y}{n}}}{m+n}= \dfrac{{X+Y}}{m+n}$$

Therefore, our final test statistic becomes $$Z = \dfrac{{(\hat{p}_{1} - \hat{p}_{2})}}{\sqrt{ \hat{p}_{0}(1-\hat{p}_{0})\left( \dfrac{1}{m} + \dfrac{1}{n} \right) }} \approx SN$$
We proceed as usual. *Since we had to approximate binomial to normal at the start, this test is only used if* $m\hat{p}_{1}\geq 10, m(1-\hat{p}_{1}) \geq 10, n\hat{p}_{2} \geq 10$ *and* $n(1-\hat{p}_{2}) \geq 10$.

## Confidence interval
We know $P\left( -Z_{\frac{\alpha}{2}} < Z < Z_{\frac{\alpha}{2}} \right) = 1-\alpha$. We can replace $Z$ with our approximate standard normal test statistic we derived earlier and isolate $p_{1}-p_{2}$. Alternatively, we also know the confidence interval when using Z scores is generally of the form $\text{estimator } \pm Z_{\frac{\alpha}{2}} \times \text{standard deviation}$.

Both these methods will give us the *approximate* $(1-\alpha)100\%$ CI for $p_{1}-p_{2}$
$$(\hat{p}_{1}-\hat{p}_{2}) \pm Z_{\frac{\alpha}{2}}\sqrt{\dfrac{\hat{p}_{1}(1-\hat{p}_{1})}{m} + \dfrac{\hat{p}_{2}(1-\hat{p}_{2})}{n}}$$
When forming our confidence interval, **we do not assume $p_{1}=p_{2}$**. **This is why the variance term here takes the individual variances and sums them up instead of pooling using some common $p_{0}$**.