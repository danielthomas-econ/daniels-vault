---
color: var(--mk-color-orange)
tags:
  - sem2-flashcards/stats/interval_estimation
---
Quick access:
- [[#Basics|Basics]]
- [[#Interpretation of CIs|Interpretation of CIs]]


## Basics
The interval method of estimation will give you a range and tell you how likely it is that this interval is an accurate estimate. For example: A 95% CI for $\mu$ is $(8.3,9.9)$.

We arrive at our confidence level through a graphical representation. As we can see, a 95% confidence interval is simply where 95% of the population lies in the first place. In general, we can say that **for a $(1-\alpha)100\%$ confidence interval, the area in the middle is $(1-\alpha)$ while the area on each tail is $\dfrac{\alpha}{2}$**.
![[2.webp]]

We can also have one sided intervals. Conceptually, they work the same. The only difference is that since we only have one tail outside the interval, the area of the tail is $\alpha$. In a regular interval, the area of each tail was $\dfrac{\alpha}{2}$ since the area was split between two tails on either end.
![[BtAsX.png|center|400]]

## Interpretation of CIs
It is very important that you can interpret these intervals correctly. Consider the above example of 95% CI for $\mu$ being $(8.3,9.9)$. The correct interpretation is that *there is a 95% chance that the interval contains the mean.*

Often, we might say that there is a 95% chance the mean is in the interval. However, this is wrong. This is because **the interval is a random variable, while the mean is not.** We can only make probability statements about random variables. Since the interval will change from sample to sample (this interval is dependent on $\bar{x}$ as we'll see later), we make a probability statement about it, not a constant like $\mu$.