---
color: var(--mk-color-yellow)
tags:
  - "#sem2-flashcards/stats/hypothesis_testing"
---
Quick access:
- [[#Case 1: Normal population with known standard deviation|Case 1: Normal population with known standard deviation]]
	- [[#Case 1: Normal population with known standard deviation#Formula for beta|Formula for beta]]
	- [[#Case 1: Normal population with known standard deviation#Sample size determination|Sample size determination]]
- [[#Case 2: Large sample test|Case 2: Large sample test]]
- [[#Case 3: Small sample test|Case 3: Small sample test]]


The general method for hypothesis testing is given below. We'll examine how to follow these steps for specific cases.
![[WhatsApp Image 2025-05-27 at 08.03.03_1a645443.jpg]]
## Case 1: Normal population with known standard deviation
This is a rather unrealistic case since we almost never know the value of $\sigma$. We use this case just to build up an intuition of how to build hypothesis tests.

Suppose we have a random variable $X$ and $X \sim N(\mu, \sigma \:(\text{known}))$. Then we can say $\bar{X} \sim N\left( \mu, \dfrac{\sigma}{\sqrt{ n }} \right)$. *We'll use the standardized value $Z$ as the test statistic.* $Z = \dfrac{{\bar{X} - \mu_{0}}}{\dfrac{\sigma}{\sqrt{ n }}} \sim SN$ expresses the distance between $\bar{X}$ and $\mu_{0}$ (the value of the mean according to the null hypothesis) in standard deviation units. If the distance is too large in the direction of the alternative, we reject the null.

If our alternative is $H_{a}:\mu > \mu_{0}$, then the rejection region based on the test statistic is of the form $z \geq c$. We choose the value of $c$ based on what level of $\alpha$ is acceptable to us. This can be easily done since $Z \sim SN$. *Therefore, the cutoff value of $c$ is the $z$ critical value that captures an area of $\alpha$ under the $z$ curve.* In other words, we can say that **the rejection region $z\geq z_{\alpha}$ has a type 1 error probability of $\alpha$**. Same logic holds if our alternative was a left tailed test.

If we had a two tailed alternative, the only difference would be that we must split the acceptable $\alpha$ between both the tails. **Therefore, each tail will have an area of** $\dfrac{\alpha}{2}$. Since the standard normal distribution is symmetric, the cutoff values will be $c$ and $-c$, or $z_{\frac{\alpha}{2}}$ and $-z_{\frac{\alpha}{2}}$. Therefore, our rejection region becomes $z \geq z_{\frac{\alpha}{2}}$ and $z \leq -z_{\frac{\alpha}{2}}$.
![[WhatsApp Image 2025-05-26 at 14.46.06_03203336.jpg]]

### Formula for beta
The $z$ test used here in case 1 is one of the few cases for which we can derive a formula for $\beta$. For a right tailed test, we know that the rejection region is $z \geq z_{\alpha}$. We can express this in terms of $\bar{X}$ as $$\begin{align}
z &\geq z_{\alpha} \\
\implies \dfrac{{\bar{X} - \mu_{0}}}{\dfrac{\sigma}{\sqrt{ n }}} &\geq z_{\alpha} \\
\implies \bar{X} - \mu_{0} &\geq z_{\alpha} \dfrac{\sigma}{\sqrt{ n }} \\
\implies \bar{X} &\geq \mu_{0} + z_{\alpha} \dfrac{\sigma}{\sqrt{ n }}
\end{align}$$
Therefore, we can say that **the rejection region $z\geq z_{\alpha}$ is equivalent to saying $\bar{X}\geq \mu_{0} +z_{\alpha} \dfrac{\sigma}{\sqrt{ n }}$**. A simple way to remember this is that *we reject the null if $\bar{X}$ is greater than the upper bound of our [[Estimating the mean#^6e1641|confidence interval.]]* 

Since $\beta = P(\text{not rejecting null when it is false})$, we consider $\bar{X} < \mu_{0} +z_{\alpha} \dfrac{\sigma}{\sqrt{ n }}$, which is when we do not reject null ($\bar{X}$ is within our confidence interval). **Remember that for a different value of the alternative hypothesis, we have a different** $\beta$. **Let us consider some $\mu'$ that exceeds the null value** $\mu_{0}$. In this case, $\bar{X} \sim N\left( \mu', \dfrac{\sigma}{\sqrt{ n }} \right)$Then we have
$$\begin{align}
\beta(\mu') &=P(H_{0}\text{ is not rejected when }\mu = \mu') \\
&=P\left( \bar{X} < \mu_{0} + z_{\alpha} \dfrac{\sigma}{\sqrt{ n }} \text{ when } \mu= \mu' \right) \\
&=P\left( \dfrac{{\bar{X}- \mu'}}{\dfrac{\sigma}{\sqrt{ n }}} < \dfrac{{\mu_{0}+z_{\alpha} \dfrac{\sigma}{\sqrt{ n }}-\mu'}}{\dfrac{\sigma}{\sqrt{ n }}} \right) \\
&=P\left( Z< z_{\alpha } + \dfrac{{\mu_{0}-\mu'}}{\dfrac{\sigma}{\sqrt{ n }}} \right) \\
&=\Phi\left( z_{\alpha} + \dfrac{{\mu_{0} - \mu'}}{\dfrac{\sigma}{\sqrt{ n }}} \right)
\end{align}$$
This is the case for a right tailed alternative. Here are the formulae for the other types of hypotheses, which are derived in the exact same manner.
![[WhatsApp Image 2025-05-27 at 09.07.08_2abd570d.jpg]]

**As we take an alternative case further from the null, $\mu'$ increases so $\mu_{0} - \mu'$ becomes more negative, making $\beta(\mu')$ smaller.** This makes sense as if we take a $\mu'$ very far from $\mu_{0}$, we get an alternative distribution centered very far away from the null distribution, meaning the *overlap region becomes very small.* A smaller overlap means that the probability of committing a type 2 error naturally becomes lower.
![[graphical-representation-of-type-1-and-type-2-errors.webp|center|400]]

### Sample size determination
Suppose we want to restrict $P(\text{type 1 error}) = \alpha$ and $\beta(\mu')=\beta$ for a given $\alpha$, $\mu'$ and $\beta$. As seen above, for an upper tailed test, we must have $\Phi\left( z_{\alpha} + \dfrac{{\mu_{0}-\mu'}}{\dfrac{\sigma}{\sqrt{ n }}} \right)=\beta$ (since $\beta(\mu')=\beta$). *If you look at the graph above, you can see that although this is an upper tailed test, when we consider the alternative distribution, $\beta$ is actually a **left tailed probability.*** Therefore, we consider a negative value to account for it being left tailed. This implies that $-z_{\beta}= z_{\alpha} + \dfrac{{\mu_{0}-\mu'}}{\dfrac{\sigma}{\sqrt{ n }}}$. **We use this to isolate $n$ and determine the sample size so that we get a set $\alpha$ and $\beta$**.
$$\begin{aligned}
-z_{\beta} &= z_{\alpha} + \dfrac{{\mu_{0} - \mu'}}{\dfrac{\sigma}{\sqrt{ n }}} \\
\implies -z_{\beta} &= \dfrac{{z_{\alpha} \dfrac{\sigma}{\sqrt{ n }}+\mu_{0} - \mu'}}{\dfrac{\sigma}{\sqrt{ n }}} \\
\implies -z_{\beta} \dfrac{\sigma}{\sqrt{ n }} &=z_{\alpha} \dfrac{\sigma}{\sqrt{ n }} + \mu_{0} - \mu' \\
\implies \dfrac{\sigma}{\sqrt{ n }}(z_{\alpha} +z_{\beta}) &=\mu'-\mu_{0} \\
\implies \dfrac{\sigma}{\sqrt{ n }} &= \dfrac{{\mu'-\mu_{0}}}{z_{\alpha}+z_{\beta}} \\
\implies \dfrac{\sqrt{ n }}{\sigma} &= \dfrac{{z_{\alpha} + z_{\beta}}}{\mu' - \mu_{0}} \\
\implies n &= \left[ \dfrac{\sigma(z_{\alpha}+z_{\beta})}{\mu'-\mu_{0}} \right]^{2}
\end{aligned}$$

This formula works for both right and left tailed tests. For a two tailed test, simply use $z_{\frac{\alpha}{2}}$ instead of $z_{\alpha}$.

## Case 2: Large sample test
When we have a large sample, we require neither normality nor the knowledge of $\sigma$. According to the rule of thumb, f we have $n>30$, we can use CLT and say $\bar{X} \approx N$, thereby removing the normality requirement. If we have $n>40$, we can say $S \approx \sigma$, so we don't need to know $\sigma$ either. The rest of the procedure follows exactly from case 1, except **now we will only have approximates everywhere instead of exact values.** We start by saying $Z = \dfrac{{\bar{X} - \mu}}{\dfrac{S}{\sqrt{ n }}} \approx SN$ and then continue the same way as we did in case 1.

## Case 3: Small sample test
If we have $n\leq 30$, we can no longer apply CLT. In this case, *we require normality or else we have a dead end.* From [[t distributions#^36ef22|t distributions,]] we know that if we have a random sample of size $n$ from a normal distribution, the variable $T= \dfrac{{\bar{X} - \mu}}{\dfrac{S}{\sqrt{ n }}}\sim t_{n-1}$. We continue with this test statistic just as we did in case 1. For an upper tail test, our rejection rejection becomes $t\geq t_{\alpha, n-1}$ instead of $z\geq z_{\alpha}$.

This is actually the same test statistic as the large sample test. We simply label it as $T$ to show it comes from a $t$ distribution with $n-1$ df instead of a standard normal distribution.