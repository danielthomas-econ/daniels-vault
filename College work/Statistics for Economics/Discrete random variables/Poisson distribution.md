---
color: var(--mk-color-gray)
tags:
  - sem1-flashcards/stats/discrete
---
Quick access:
[[Poisson distribution#When is it used|When is it used]]
[[Poisson distribution#PMF of the Poisson distribution|PMF of the Poisson distribution]]
[[Poisson distribution#Approximating binomial using Poisson|Approximating binomial using Poisson]]
[[Poisson distribution#Expectation and variance|Expectation and variance]]

## When is it used
The Poisson distribution is used when we have *independent events occurring at a fixed rate over time.* It is typically used to solve questions where you must **count the number of occurrences of things over a certain time period.** Usually, the probability of more than 1 event happening in a time interval is very small, and you are given the rate of occurrence.

## PMF of the Poisson distribution
The Poisson distribution of a rv $X$ has the pmf
$$p(x;\mu)= \dfrac{{e^{-\mu}\cdot \mu^{x}}}{x!}, x=0,1,2,3\dots$$
The parameter $\mu$ is the expected value of $X$. Sometimes it is also written as $\lambda$.

## Approximating binomial using Poisson
For any [[Binomial distribution#Binomial experiment|binomial experiment]] where **p is very large and n is very small,** we can use a Poisson distribution to approximate it. 
$$\begin{align}
\text{For} &\text{ a binomial pmf }b(x;n,p), \text{ if }n\to \infty \text{ and } p\to 0 \\
& \text{such that }np\to \mu, \text{then }b(x;n,p)\to p(x;\mu)
\end{align}$$
We can safely apply this rule of thumb if $n>50$ and $np<5$.

## Expectation and variance
We know that a binomial approaches Poisson, so $np\to \mu$. Since $p\to 0$, $np(1-p)=npq\to \mu$. For a binomial, $E(X)=np$ and $V(X)=npq$, therefore *for a Poisson distribution,*
$$E(X)=V(X)=\mu$$
