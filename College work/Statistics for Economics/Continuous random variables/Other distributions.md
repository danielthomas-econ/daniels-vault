---
color: var(--mk-color-green)
---
Quick access:
[[Other distributions#Uniform distribution|Uniform distribution]]
[[Other distributions#Exponential distribution|Exponential distribution]]
	[[Other distributions#Memoryless property|Memoryless property]]


## Uniform distribution
A continuous rv $X$ is said to be uniformly distributed on the interval $[A,B]$ if the pdf is $f(x; A,B)= \dfrac{1}{B-A}$ for $x\in[A,B]$ and $0$ otherwise. Integrating this to get the cdf gives you
$$F(X)=\begin{cases}
0 & x\leq A \\
\dfrac{{x-A}}{B-A} & A<x<B \\
1 & x>B
\end{cases}$$
![[Pasted image 20250111141904.png|center|400]]

Since everything is uniformly distributed, *the mean lies in the middle of the distribution.* Therefore, $E(X)= \dfrac{{A+B}}{2}$. Also, the variance is $V(X)= \dfrac{(A-B)^{2}}{12}$.


## Exponential distribution
$X$ has an exponential distribution with parameter $\lambda$ ($\lambda>0$) if the pdf is $f(x;\lambda)=\lambda e^{-\lambda x}$ for $x\geq 0$.

Integrating this, we get the cdf as $F(x;\lambda)=1-e^{-\lambda x}$ for $x\geq 0$.

An exponential distribution has $\mu=\dfrac{1}{\lambda}$ and $\sigma^{2}=\dfrac{1}{\lambda^{2}}$. 
![[Pasted image 20250111141813.png|center|400]]

### Memoryless property
This is a very important property of the exponential distribution, and is a reason why its frequently used to model the distribution of component lifetimes.

Suppose the lifetime has an exponential distribution with parameter $\lambda$. If we leave it running for $t_{0}$ hours and see it still works, the probability it works for at least $t$ more hours is given by $P(x\geq t+t_{0}|x\geq t_{0})$. *Due to the memoryless property, the exponential distribution does not care about previous use of the component (no memory of it).* Therefore, $P(x\geq t+t_{0}|x\geq t_{0})=P(x\geq t)$.

The distribution of additional lifetime is exactly the same as the distribution of original life time. **This means distribution of remaining lifetime is independent of the current age.**

