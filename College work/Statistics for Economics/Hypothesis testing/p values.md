---
color: var(--mk-color-yellow)
tags:
  - "#sem2-flashcards/stats/hypothesis_testing"
---

## What is a p value
The $P$-value is the probability, calculated assuming null is true, of *obtaining a value of the test statistic at least as contradictory to $H_{0}$* as the value calculated from the available sample.
![[p-value.jpg|center|500]]
The $p$ value is the *area under the curve towards the direction away from the mean from the critical point.* As we can see, the critical point above is marked in red. The direction away from the mean is to the right, so the $p$ value is the area to the right of the critical point. This is because any value is this area is at least as contradictory to the null (mean) as the critical point.

The benefit of using a $p$ value is that **you do not need to specify any level of $\alpha$**. You simply report the $p$ value and let the reader decide what level of significance they want to choose and whether they should reject or accept the claim based on the $p$ value. 

## Decision rule
**We reject $H_{0}$ if $p \leq \alpha$ in every case.** This is because if $p \leq \alpha$, then area under the curve with critical value $p$ is less than with critical value $\alpha$. *This means that $p$ is further from the mean than $\alpha$*. This simply tells us that $p$ is in the rejection region as it is less likely to occur than $\alpha$. This graph shows us that *the rejection region method and $p$ value method are identical.* $p \leq \alpha$ simply means that the $p$ value is in the rejection region, so we reject $H_{0}$.
![[Significance-level-and-p-value.png]]
A smaller $p$ means there is less area under the curve at $p$, which means $p$ is further from the mean. This tells us that **the smaller the $p$ value, the more evidence there is against the null.** Therefore, we are more likely to reject null with a smaller $p$.

### Observed significance level
Suppose we have a $p$ value of $0.03$. If we take $\alpha=0.1$, we reject the null. Same goes for $\alpha=0.05$. However, we fail to reject null if $\alpha=0.01$. *What is the smallest level of $\alpha$ for which we reject the null? It is $\alpha=0.03 = p$*. Since the $p$ value is the smallest significance level at which we can reject the null, **we also call the $p$ value the observed significance level (OSL).**  

We call data significant if we use it to reject the null. *The $p$ value must therefore be the smallest level at which the data is considered 'significant'.*

## Calculating p values
The below figure shows us the $p$ values for all three test cases.
![[WhatsApp Image 2025-05-27 at 12.29.55_054e07d4.jpg|center|500]]

Since $p$ value is simply the shaded region, it becomes pretty clear that the $p$ value can be calculated by
$$\text{P value: } p= \begin{cases}
\Phi(z) \text{ for a left tailed test} \\
1-\Phi(z) \text{ for a right tailed test} \\
2[1-\Phi(|z|)] \text{ for a two tailed test}
\end{cases}$$

*The idea remains the same for a t test, although we can't use $\Phi$ for t tests.* Simply calculate the area under the curve to the corresponding direction using t tables to get the $p$ value.