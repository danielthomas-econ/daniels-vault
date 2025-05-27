---
color: var(--mk-color-base-60)
tags:
  - sem1-flashcards/stats/discrete
---
Quick access:
[[College work/Statistics for Economics/Discrete random variables/Expectation and variance#Expected value|Expected value]]
	[[College work/Statistics for Economics/Discrete random variables/Expectation and variance#Rules of expectation|Rules of expectation]]
[[College work/Statistics for Economics/Discrete random variables/Expectation and variance#Variance|Variance]]
	[[College work/Statistics for Economics/Discrete random variables/Expectation and variance#Rules of variance|Rules of variance]]

The two main characteristics of any distribution are its expected value $E(x)$ and variance $V(x)$.

## Expected value
Expected value, denoted by $E(x)$, *gives us the average value of $x$*. The formula for expectation is:$$E(x) = \sum_{x \in D}xp(x)$$
where $D$ denotes the set of all values of $x$.

$E(x)$ doesn't have to be a possible value of $x$. It simply tells us that **if the experiment was repeated infinite times, the average number of outcomes would be** $E(x)$.

### Rules of expectation
1. $E(ax)=aE(x)$ - We can take the constant out
2. $E(a)=a$ - *Expected value of a constant is the constant*
3. $E(ax+b)=aE(x)+b$ - Combining the rules above
4. $E(h(x)) = \sum\limits_{x \in D}h(x)p(x)$ - *Expected value of a function is the same as substituting the function as x.*

## Variance
Variance tells us more on how the items in a distribution are distributed, and is represented by $V(x)$. $$\begin{align}
& V(x) = E((x-\mu)^{2}) \\
 Sho&rtcut = E(x^{2})-E(x)^{2}\end{align}$$
### Rules of variance
1. $V(a)=0$ - **A constant has no variance**
2. $V(ax)=a^{2}V(x)$ - We must square the constant when we take it out
3. $\sigma_{ax}=+\sqrt{ V(ax) }=+\sqrt{ a^{2}V(x) }=|a|\sigma_{x}$ - Take the absolute value of the constant out when finding standard deviation
4. $V(ax+b) = a^{2}V(x)$ - Since a constant has no variance, $V(ax)=V(ax+b)$.
5. $V(h(x))=E(h(x)^{2})-[E(h(x))]^{2}$

