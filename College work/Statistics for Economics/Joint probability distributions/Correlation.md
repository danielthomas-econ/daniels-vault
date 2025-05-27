---
color: var(--mk-color-teal)
tags:
  - sem1-flashcards/stats/joint_distributions
---
Quick access:
[[Correlation#Formula|Formula]]
[[Correlation#Correlation coefficient|Correlation coefficient]]
	[[Correlation#Interpreting the correlation coefficient|Interpreting the correlation coefficient]]

## Formula
The correlation coefficient $\rho$ is given by 
$$\rho_{X,Y}=\dfrac{{Cov(X,Y)}}{\sigma_{X}\cdot\sigma_{Y}}$$

## Correlation coefficient
We know that while covariance tells us how two variables are related, it has a critical flaw: [[Covariance#The problem with covariance|it is sensitive to scale.]] The idea behind correlation is to *scale the covariance so that it is no longer affected by scaling.* This gives us a **correlation coefficient,** denoted by $Corr(X,Y)$, $\rho_{X,Y}$ or $\rho$.

The correlation coefficient is **unitless and not affected by scale.** Therefore, $\rho(aX+b,cY+d)=\rho(X,Y)$.

### Interpreting the correlation coefficient
The value of the correlation coefficient is ranges from $-1$ to $1$. The distance between $\rho$ and $0$ tells us the strength of the correlation, while the sign tells us the direction.

If $\rho_{X,Y}$ is equal to:
$1$: Perfect positive linear relation
$-1$: Perfect negative linear relation
$0$: No linear relation

The below is a *general rule of thumb*
$0.7\leq \rho_{X,Y}\leq 1$ - High positive correlation
$-1\leq \rho_{X,Y}\leq -0.7$ - High negative correlation
$-0.3\leq \rho_{X,Y}\leq 0.3$ - Weak correlation


> [!warning] Be careful of the implications of $\rho=0$
> While it is true that $X,Y$ are independent $\implies \rho=0$, *the reverse implication isn't necessarily true.* Therefore, $\rho=0$ does not imply that $X,Y$ are independent.<br><br> Also, $\rho=0$ means there is no linear relationship, but $X$ and $Y$ could have a non-linear relation.



