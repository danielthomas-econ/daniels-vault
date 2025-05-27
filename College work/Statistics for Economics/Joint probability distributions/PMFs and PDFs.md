---
color: var(--mk-color-teal)
tags:
  - sem1-flashcards/stats/joint_distributions
---
Quick access
- [[#PMF of two discrete rvs|PMF of two discrete rvs]]
	- [[#PMF of two discrete rvs#Marginal pmf|Marginal pmf]]
- [[#PDF of two continuous rvs|PDF of two continuous rvs]]
	- [[#PDF of two continuous rvs#Marginal pdfs|Marginal pdfs]]
- [[#Conditional pdfs/pmfs|Conditional pdfs/pmfs]]


When we deal with joint probability distributions, we have two or more variables to handle. Therefore, all the PDF and PMF stuff is slightly different, and some more additional concepts will be introduced.
## PMF of two discrete rvs
Let $X$ and $Y$ be two discrete rvs, then the *joint probability mass function* $p(x,y)$ is defined for each pair of $(x,y)$ as $p(x,y)=P(X=x\:and \:Y=y)$. For this to be valid, it has to satisfy:
i) $p(x,y)\geq 0$
ii) $\sum\limits_{x}\sum\limits_{y}p(x,y)=1$
### Marginal pmf
The marginal pmf of $X$, denoted by $p_{x}(x)$, is given by$$p_{x}(x)=\sum_{y:p(x,y)>0}p(x,y)\text{   for each value of x}$$
This means we *hold $x$ fixed and sum over the joint pmf over all $y$*. Eg 5.2: We have only two possible $X$ values: $100$ and $250$. We take two cases, one where $x=100$ and one where $x=250$, and sum over all possible values of $y$ in each case. This gives us $p_{x}(100)=p(100,0)+p(100,100)+p(100,200)=0.5$ and $p_{x}(250)=p(250,0)+p(250,100)+p(250,200)=0.5$. **Now we have to combine these results into a single pmf like we've done before.**
Therefore, the marginal pmf of $x$ becomes:
$$
p_{x}(x) =
\begin{cases}
0.5 && x=100,250 \\
0 && \text{otherwise}
\end{cases}
$$
## PDF of two continuous rvs
The joint probability density function of two continuous rvs $X$ and $Y$ is given by $\int\limits_{y}\int \limits_{x}f(x,y)dx\:dy$. To find the probability that $X$ and $Y$ lie between two numbers, we use $P(a\leq X\leq b,c\leq Y\leq d)=\int\limits_{c}^{d}\int\limits_{{a}}^{b}f(x,y)dx\:dy$.

### Marginal pdfs
The marginal pdf of $x$ is given by $f_{X}(x)= \int\limits_{{-\infty}}^{\infty}f(x,y)dy$, for $-\infty\leq x\leq \infty$. This holds the value of $x$ constant and sums up over all $y$.


## Conditional pdfs/pmfs
Once again, we take the outcome we want in the numerator, and use the denominator to shrink the sample size to what has already happened. Therefore,
$$f_{Y|X}(y|x)= \dfrac{f(x,y)}{f_{x}(x)}$$