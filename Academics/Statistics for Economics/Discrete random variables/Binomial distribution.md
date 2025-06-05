---
color: var(--mk-color-base-60)
tags:
  - sem1-flashcards/stats/discrete
---
Quick access:
[[Binomial distribution#Binomial experiment|Binomial experiment]]
[[Binomial distribution#Binomial distribution|Binomial distribution]]
	[[Binomial distribution#Mean and variance|Mean and variance]]
[[Binomial distribution#Bernoulli distribution|Bernoulli distribution]]

## Binomial experiment
We can only use the binomial distribution formula if we are dealing with binomial events. The conditions for a binomial event are:
1. The experiment consists of a sequence of $n$ smaller experiments called trials
2. Each trial results in either a success or a failure
3. Trials are independent of each other
4. Probability of success remains the same

## Binomial distribution
The binomial random variable $X = \text{number of successes in }n\text{ trials.}$ It is denoted by $b(x;n,p)$, where $x$ is the value of the rv $X$, $n$ is the number of trials and $p$ is the probability of success. **The binomial distribution formula is** $$b(x;n,p)= {^n}C_{r}\:p^r\:q^{n-r}$$
where $q$ is the probability of failure and $r$ is the number of successes observed.

### Mean and variance
The mean of $X\sim Bin(n,p)$ is $np$, and its variance is $npq$.

## Bernoulli distribution
This is a special case of the binomial distribution where the experiment is carried out only once, i.e. $n=1$. It works exactly like a binomial would, and its mean is $p$, and variance is $pq$.