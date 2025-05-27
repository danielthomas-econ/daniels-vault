---
color: var(--mk-color-teal)
tags:
  - sem1-flashcards/stats/joint_distributions
---
Quick access:
- [[#Basic idea|Basic idea]]
- [[#Formula|Formula]]
- [[#The problem with covariance|The problem with covariance]]

## Basic idea
Using the formula for [[College work/Statistics for Economics/Joint probability distributions/Independence|independence,]] we can tell if $X$ and $Y$ are independent or not. If they are, that means they share no relation at all. But if they aren't, we are faced with a question: *How closely related are $X$ and $Y$*? This question is answered (for linear functions) with covariance.

If the two are closely related, then a very high value of $X$ will result in a high value of $Y$, and the same goes for lower values. If you use the mean of $x$ and $y$ to divide the graph into four quadrants, **a positive covariance means you'll see the points in quadrants 1 and 3 and in quadrants 2 and 4 for negative covariance.** 
![[UntitledwfFE4Fergea.jpg|center|500]]

## Formula
The covariance between two random variables $X$ and $Y$ is
$$\begin{align}
Cov(X,Y)&=E[(X-\mu_{X})(Y-\mu_{Y})] \\
&=\int\limits_{{-\infty}}^{\infty} \int\limits_{{-\infty}}^{\infty} (x-\mu_{X})(y-\mu_{Y})f(x,y) \, dx  \, dy  \\
\end{align}$$
Replace $\int\limits_{{-\infty}}^{\infty}  \,$ with $\sum$ to get the formula for discrete. However, this complex formula can be simplified to $$Cov(x,y)=E(XY)-E(X)E(Y)$$
From the 1st formula, we can understand why positive covariance means we have points in the 1st and 3rd quadrant. When the points are in these quadrants, $E[(X-\mu_{X})(Y-\mu_{Y})]$ will always be positive, as both values are either positive (greater than mean in Q1) or negative (less than mean in Q3). Therefore, the product will always be positive.

## The problem with covariance
One limitation of covariance is that it *only tells us about linear relationships.* However, a more serious defect is that **covariance is sensitive to scale.** Therefore, the scale of units used play a large role in determining the final value of covariance.

This means that the *only use of covariance is to tell us the direction of the relationship,* whether its a positive or negative one. This is because a covariance of $132,000$ might mean the same as a covariance of $6$. Despite the issue in scaling, we know for certain that these variables exhibit a positive relationship, since both covariance values are positive (and sign isn't impacted by scale).
