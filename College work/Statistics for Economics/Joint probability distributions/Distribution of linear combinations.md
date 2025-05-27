---
color: var(--mk-color-teal)
tags:
  - sem2-flashcards/stats/joint_distributions
---


## Rules
i) $E(a_{1}X_{1}+a_{2}X_{2}+\dots+a_{n}X_{n})=a_{1}E(X_{1})+a_{2}E(X_{2})+\dots+a_{n}E(X_{n})$
$= a_{1}\mu_{1}+a_{2}\mu_{2}+\dots+a_{n}\mu_{n}$. 
ii) $V(a_{1}X_{1}+a_{2}X_{2}+\dots+a_{n}X_{n})=\sum\limits_{i=1}^n\sum\limits_{j=1}^na_{i}a_{j}Cov(X_{i},X_{j})$ - This is for finding variance if $X_{i}$'s aren't independent.
iii) $V(a_{1}X_{1}+a_{2}X_{2}+\dots+a_{n}X_{n})=a_{1}^{2}\sigma_{1}^{2}+a_{2}^{2}\sigma_{2}^{2}+\dots+a_{n}^{2}\sigma_{n}^{2}$

The *expected value of a linear combination is the same as the linear combination of the expected values.* An important thing to note is that $V(X_{1}-X_{2})=V(X_{1})+V(X_{2})$. Therefore, **variance of the difference of two rvs is the sum of two variances.** This is because $V(-1X_{2})=(-1)^{2}V(X_{2})=+V(X_{2})$.

In rule ii), we get the variance terms when $i=j$ as $Cov(X_{i},X_{i})=V(X_{i})$. For $i\ne j$, we get $Cov(X_{i},X_{j})$.


## Flashcards
Q1) Part d and e
![[WhatsApp Image 2025-02-26 at 16.06.05_6fceaa78.jpg|center|400]]
?
Ans)![[Pasted image 20250226160428.png]]
There is no direct formula for $V(XY)$, and it is not equal to $V(X)V(Y)$. Therefore, we find $E(B^{2})$ and sub it in $V(B)=E(B^{2})-E(B)$ to get the variance.
![[Pasted image 20250226160724.png]]
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Prove that $Cov(X,Y+Z)=Cov(X,Y)+Cov(X,Z)$
?
Ans) We know $Cov(A,B)=E(AB)-E(A)E(B)$
$\implies Cov(X,Y+Z)=E(XY+XZ)-E(X)E(Y+Z)$
$=E(XY)+E(XZ)-E(X)E(Y)-E(X)E(Z)=E(XY)-E(X)E(Y)+E(XZ)-E(X)E(Z)$
$=Cov(X,Y)+Cov(X,Z)$
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q3) ![[WhatsApp Image 2025-02-26 at 17.28.48_790b3b54.jpg|center|400]]
?
Ans) The key to this question is realizing that *both X and Y follow a binomial distribution.* A tree can either survive or not survive (two outcomes) and the trials are independent of each other. Therefore, each tree is a binomial experiment. We're also given $n=50$ and $p=0.7,0.6$, which should've been a giveaway that its binomial. Once we know that, find expectation and standard deviation of $X$ and $Y$. **Lastly, use rules of expectation and variance to find the expectation and standard deviation of $X-Y$**. Use that to normalize the probability and solve.![[Pasted image 20250226173145.png]]
