---
color: var(--mk-color-yellow)
tags:
  - "#sem2-flashcards/stats/hypothesis_testing"
---
Quick access:
- [[#Criteria for decision rules|Criteria for decision rules]]
- [[#Using Z as a test statistic|Using Z as a test statistic]]

## Criteria for decision rules
Since we consider type 1 errors to be more severe, we want to minimize the chance of these errors occurring, i.e. we must minimize $\alpha$. *To do this, we start by taking a level of $\alpha$ we deem acceptable.* Suppose we consider a 5% $\alpha$ to be okay. We'll fix $\alpha=0.05$ and then continue framing our decision rule.

Think about the definition of $\alpha$. It is the probability that you reject the null when it is true. Therefore, we can express this mathematically as $P(\text{reject null | null is true})=0.05$. Consider we have a left tail test with the following info. $$\begin{align}
H_{0}&: \mu=5 \\
H_{a}&: \mu < 5 \\ 
n&=9 \\
X \sim &\:N(\mu, \sigma=4) \\
\bar{X} \sim &N\left( \mu, \dfrac{\sigma}{\sqrt{ n }}=\dfrac{4}{3} \right)
\end{align}$$
Then, this is equal to $P(\bar{X} \leq \bar{X}_{critical}\:|\:\mu =5)$. Standardizing, we get $P\left( \dfrac{{\bar{X} - 5}}{\dfrac{4}{3}} \leq \dfrac{{\bar{X}_{c}-5}}{\dfrac{4}{3}} \right)=0.05$
$\implies P\left( Z < \dfrac{{\bar{X} - 5}}{\dfrac{4}{3}} \right)=0.05$.
We know $\phi(-1.64)=0.05$. Therefore, $\dfrac{{\bar{X} - 5}}{\dfrac{4}{3}}=-1.64$, which tells us that $\bar{X} = 2.813$. **Therefore, our decision rule should be reject $H_{0}$ if $\bar{X} \leq 2.813$ if we want to keep $\alpha=0.05$**.

## Using Z as a test statistic
In the above example, we see that we standardize $\bar{X}$ first and then destandardize it again to express it in terms of our test statistic $\bar{X}$. Instead, we can simply change our test statistic to $Z$ to avoid that last step. Therefore, to keep $\alpha=0.05$, our new decision rule becomes reject $H_{0}$ if $Z_{cal}\leq -Z_{0.05} = -1.64$