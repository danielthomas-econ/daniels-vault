---
color: var(--mk-color-base-60)
tags:
  - sem1-flashcards/stats/discrete
---
Quick access:
[[Hypergeometric distribution#Assumptions of hypergeometric distributions|Assumptions of hypergeometric distributions]]
[[Hypergeometric distribution#PMF of a hypergeometric distribution|PMF of a hypergeometric distribution]]
	[[Hypergeometric distribution#Conditions for the value of x|Conditions for the value of x]]
[[Hypergeometric distribution#Mean and variance of a hypergeometric distribution|Mean and variance of a hypergeometric distribution]]
	[[Hypergeometric distribution#Finite population correction factor|Finite population correction factor]]
[[Hypergeometric distribution#Approximating hypergeometric to binomial|Approximating hypergeometric to binomial]]


## Assumptions of hypergeometric distributions
1. Population sampled has $n$ elements (finite population)
2. Each individual can be characterized as a failure or a success, and there are $M$ successes in the population.
3. A sample of $n$ individuals are chosen without replacement in such a way that each subset of size $n$ is equally likely to be chosen.

## PMF of a hypergeometric distribution
This is used to give us *the exact probability model for number of successes when we sample a finite number $n$ (without replacement) from the population $N$*. It is a common distribution that we've already used many times, even if we didn't know its exact name. Eg: Probability that we get 3 spades in 3 card pulls.

The rv $X$ represents the number of $S's$ (successes) in the population. The pmf of X is represented by$$P(X=x)=\dfrac{{^MC_{x}\times{^{N-M}C_{n-x}}}}{^NC_{n}}$$
where the total population is $N$, *the total number of successes in the population is M and number of failures in the population is N-M.* 

### Conditions for the value of x
**However, there is a special condition that** $max(0,n-(N-M))\le x\le min(n,M)$. The maximum bound $min(n,M)$ tells us that *we cannot draw more successes than our sample size,* so $x\le n$. Similarly, *we cannot draw more successes than the total number of successes in the population.* This means $x\le M$. Since $x\le n$ and $x\le M$, we can say that $x\le min(n,M)$.

The minimum bound $x\ge max(0,n-(N-M))$ gives us the minimum possible number of successes. **It works by subtracting the total items drawn (n) by the total failures (N-M).** If the total items drawn is more than the number of failures, i.e. $n>N-M$, *you are guaranteed a success.* However, if it is less, the difference becomes negative so we take the minimum possible successes as $0$.

## Mean and variance of a hypergeometric distribution
The mean $E(X)$ is *essentially the same as binomial distribution,* so it is $np$. However, in a hypergeometric distribution, $p=\dfrac{{\text{Total successes in a population}}}{\text{Total items in the population}}=\dfrac{M}{N}$. Therefore, $E(X)=n\times \dfrac{M}{N}$.

Again, the variance is similar to the binomial distribution and takes the form of $npq$, which becomes $n\times \dfrac{M}{N}\times\left( 1-\dfrac{M}{N} \right)$. **However, we have to multiply another term called the 'finite population correction factor'.** This makes our variance become $V(X)=\left( \dfrac{{N-n}}{N-1} \right)\times n\times \dfrac{M}{N}\times\left( 1-\dfrac{M}{N} \right)$.

### Finite population correction factor
As seen above, this term is equal to $\left( \dfrac{{N-n}}{N-1} \right)$. We must include this value because **when sampling without replacement, each selection affects the remaining population, reducing the variability of the sample.** This means that the closer $n$ (total draws) is to $N$ (total population), the smaller the variance becomes. The finite population correction factor *accounts for this using a ratio that becomes smaller as $n$ approaches $N$*.

We only use the FPC factor when calculating variance and not expectation since the expected value doesn't change based on if we are sampling with or without replacement. Regardless of the size of $n$, the expectation is always $\mu$. Sampling from a finite population without replacement reduces the variability though, so we must use the FPC factor to account for that.

## Approximating hypergeometric to binomial
We have already seen that hypergeometric and [[Binomial distribution|binomial distributions]] have some similarities since their means and variances are very closely related. There's a rule of thumb that connects these two distributions as well.

It says that if $n\le 0.05N$,**then probability of with replacement and without replacement are very close.** This means when $n\le 0.05N$, we can use a binomial distribution to approximate a hypergeometric distribution. This approximation gets better as the population $N$ gets larger.