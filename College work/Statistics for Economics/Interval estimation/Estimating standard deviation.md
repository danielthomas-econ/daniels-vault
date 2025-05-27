---
color: var(--mk-color-orange)
tags:
  - sem2-flashcards/stats/interval_estimation
---
Quick access:
- [[#Chi-squared distribution|Chi-squared distribution]]
	- [[#Chi-squared distribution#Chi-squared critical value|Chi-squared critical value]]
- [[#Deriving the CI|Deriving the CI]]

## Chi-squared distribution
Let $X_{1},X_{2},\dots,X_{n}$ be a random sample from a **normal distribution** with parameters $\mu$ and $\sigma^{2}$. Then the rv $\dfrac{(n-1)S^{2}}{\sigma^{2}}$ has a chi-squared ($\chi^{2}$) probability distribution with $n-1$ degrees of freedom. This rv can also be written as $\dfrac{\sum(X_{i}-\bar{X})^{2}}{\sigma^{2}}$.

The chi-squared distribution relies on a single parameter, which is the degrees of freedom ($\nu$). It always has a positive pdf with a positive skew, *but it becomes more symmetric as $\nu$ increases.* 

### Chi-squared critical value
We will define $\chi^{2}_{\alpha,\nu}$ to be the chi-square critical value, which is the number on the horizontal axis such that **area to the right of** $\chi^{2}_{\alpha,\nu}$ on a chi-square curve with $\nu$ df is equal to $\alpha$.

## Deriving the CI
The area to the right of $\chi^{2}_{\frac{\alpha}{2},\nu}$ is $\dfrac{\alpha}{2}$, and so is the area to the left of $\chi^{2}_{1-\frac{\alpha}{2},\nu}$. Therefore, the area in the middle is $1-\alpha$. 
![[WhatsApp Image 2025-04-25 at 01.23.43_7b7c38e3.jpg]]
We get the inequality $P\left( \chi^{2}_{1-\frac{\alpha}{2},n-1} < \dfrac{(n-1)S^{2}}{\sigma^{2}} < \chi^{2}_{\frac{\alpha}{2},n-1}\right)=1-\alpha$. Isolating $\sigma^{2}$ gives us $P\left( \dfrac{(n-1)S^{2}}{\chi^{2}_{\frac{\alpha}{2},n-1}} < \sigma^{2} < \dfrac{(n-1)S^{2}}{\chi^{2}_{1-\frac{\alpha}{2},n-1}}\right)$. This is our confidence interval for $\sigma^{2}$. **We can simply take the square root of both terms of the CI to get a CI for $\sigma$**.