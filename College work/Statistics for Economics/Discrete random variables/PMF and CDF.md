---
color: var(--mk-color-base-60)
tags:
  - sem1-flashcards/stats/discrete
---
Quick access:
[[College work/Statistics for Economics/Discrete random variables/PMF and CDF#Discrete random variables|Discrete random variables]]
[[College work/Statistics for Economics/Discrete random variables/PMF and CDF#Probability distribution of a discrete random variable|Probability distribution of a discrete random variable]]
[[College work/Statistics for Economics/Discrete random variables/PMF and CDF#Parameters of probability distributions|Parameters of a probability distribution]]
[[College work/Statistics for Economics/Discrete random variables/PMF and CDF#Cumulative distribution function|Cumulative distribution function]]
[[College work/Statistics for Economics/Discrete random variables/PMF and CDF#Converting between pmf and cdf|Converting between pmf and cdf]]

## Discrete random variables
We know that a random variable is a rule of association that assigns each outcome in $\mathbb{S}$ with a number. A random variable is called $discrete$ if *all of the possible values create either a finite set or a countably infinite set.* A set is called countably infinite if we can list a first, second, third value etc. (i.e. count the values) but there are an infinite number of elements. Therefore, $[10,20]$ is an infinite set but $\mathbb{N}=\{1,2,3,\dots\}$ is countably infinite.

## Probability distribution of a discrete random variable
A probability distribution tells us **how the total probability of 1 is distributed among the various X values.** It is also called a probability mass function (or pmf for short). Below is an example of a pmf:
![[Untitledprobabilitydistributionn.jpg|center|600]]

There's a special type of random variable called a **Bernoulli's variable.** This is a rv that can only take the value of $0$ or $1$ (true or false). The probability of $1$ will be $p$ and $0$ is $1-p$. Therefore, the pmf of a Bernoulli's variable only has two points: At $(0,1-p)$ and another at $(1,p)$.
![[Untitled-1bernoulllllllllli.jpg|center|600]]

## Parameters of probability distributions
A parameter is a number which $p(x)$ depends upon. *Changing the value of the parameter outputs a different probability distribution.* The collection of probability distributions for different values of the parameter is called a *family of probability distributions.* Bernoulli's variable uses the parameter $p$, since modifying $p$ gives us an entirely different probability function. 

## Cumulative distribution function
A cdf helps us *calculate the probability that the value of $X$ will be at most $x$*. It is denoted using $F(x)$ and is defined as:
$$F(x)=P(X\le x)=\sum\limits_{y:y \leq x}p(y)$$
We obtain a cdf by summing up the probability of $X$ at different possible values. Therefore, a cdf will always be increasing (since $p(x)\ge 0$). Since these are discrete rvs, they will look like a **step function.** The graph will have a jump at a possible value of $X$ and then stay flat until the next possible value of $X$. 
![[CDFDiscrete.png|center]]

## Converting between pmf and cdf
