---
color: var(--mk-color-yellow)
tags:
  - sem2-flashcards/macro/keynesian_macro
---

## Deriving the multiplier
The multiplier seeks to answer the question by how much will a one dollar increase in autonomous spending increase equilibrium income. To solve this question, we start by assuming there is a one dollar increase in autonomous spending.

Let's say output is also increased by a dollar to match this. **This increase in output gives rise to induced spending as consumption rises because the level of income has risen.** We know that $\$c$ will be spent on consumption out of the initial one dollar increase in income. Assume that production rises further to meet this induced spending. Therefore, output and income have increased by $\$(1+c)$. This increase in income by $1+c$ dollars will give rise to more induced spending, putting us on a nearly endless track.

![[WhatsApp Image 2025-04-25 at 15.56.01_c342aaad.jpg]]
With each round, we can see that induced spending increases the demand by $c$ in each round. The last column is the cumulative sum of all the previous rounds, so it becomes $\Delta \bar{A} + c\Delta \bar{A}+c^{2}\Delta \bar{A}+\dots$, and taking common gives us $(1+c+c^{2}\dots)\Delta \bar{A}$. **Notice that this is an infinite geometric series with the starting term as 1 and common ratio as c.** Since $c<1$, the sum converges so we use [[Academics/Mathematical methods for Economics/Limits, Continuity and Series/Series#^be3ec6|the formula]] $\dfrac{a}{1-r}$ to get the sum of this geometric series as $\dfrac{1}{1-c}$. Therefore, the total increase in income is $\left[ \dfrac{1}{1-c} \right]\Delta \bar{A}$.

$$Y_{0}=\left[ \dfrac{1}{1-c} \right]\Delta \bar{A}$$
$$\text{The multiplier: }\alpha=\dfrac{1}{1-c}$$

Since $0<c<1$, the multiplier is always a positive value greater than one. Therefore, **for an extra dollar of autonomous consumption, we have more than a dollar increase in equilibrium output.** 