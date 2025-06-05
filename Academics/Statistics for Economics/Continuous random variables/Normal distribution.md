---
color: var(--mk-color-green)
---
Quick access:
[[Normal distribution#Basic properties|Basic properties]]
[[Normal distribution#PDF of a normal distribution|PDF of a normal distribution]]
[[Normal distribution#CDF of a normal distribution|CDF of a normal distribution]]
[[Normal distribution#68-95-99.7 rule|68-95-99.7 rule]]
[[Normal distribution#Expectation and variance|Expectation and variance]]

[[Normal distribution#Standard normal distribution|Standard normal distribution]]
	[[Normal distribution#Reading the cdf|Reading the cdf]]
[[Normal distribution#Standardization|Standardization]]

[[Normal distribution#Approximating binomial distribution|Approximating the binomial distribution]]
	[[Normal distribution#Continuity correction factor|Continuity correction factor]]


## Basic properties
A normal distribution, also called a Gaussian distribution, is a unique and important distribution with the following properties:
i) The function is bell shaped
ii) It is symmetrical
iii) It has two points of inflexion
iv) It has a kurtosis of 3

## PDF of a normal distribution
The pdf of $X \sim N(\mu,\sigma)$ is given by
$$f(x)=\dfrac{1}{\sqrt{ 2\pi\sigma^{2} }}e^{\frac{{-1}}{2}(\frac{{x-\mu}}{\sigma})^{2}}$$
where $\sigma>0$.

## CDF of a normal distribution
We could integrate the pdf and get a cdf for a normal distribution. But instead of doing that, *we simply use normal distribution tables.* For finding $P(a\leq x\leq b)$, we find $F(b)-F(a)$ using the table.

## 68-95-99.7 rule
This rule states that if the population distribution of a variable is approximately normal, then we can say that roughly
$$\begin{align}
&68\%\text{ of values are within }1\sigma \text{ of the mean} \\
&95\%\text{ of values are within }2\sigma \text{ of the mean} \\
&99.7\%\text{ of values are within }3\sigma \text{ of the mean}
\end{align}$$
Since the normal distribution is symmetric, we know the areas will be something like![[013-normal-pct-all-stds.png|center|500]]
## Expectation and variance
For $X\sim N(\mu,\sigma)$,
$E(X)=\mu$ (or the midpoint of the distribution)
$V(X)=\sigma^{2}$

## Standard normal distribution
The specific normal distribution $X\sim N(0,1)$ is the most commonly used normal distribution. It has a special rv denoted by $Z\sim N(0,1)$. 

Its pdf is given by $f(z)=\dfrac{1}{\sqrt{ 2\pi }}e^{\frac{-1}{2}(z)^{2}}$. Its cdf is denoted by $\phi (z)$. Therefore, $\phi(3)=P(z\leq 3)$. Since it has $\mu=0$ and $\sigma=1$, it has $E(Z)=0$ and $V(Z)=1$.

### Reading the cdf
Being able to use the cdf of a standard normal distribution is crucial, since it simplifies everything about normal distributions.
Since the pdf is symmetric about the mean, a *standard normal distribution is symmetric around zero.*
![[standard-normal-PDF.png|center]]
Therefore, $P(Z\leq -c)=P(Z\geq c)$. If we look at the distribution above, we can tell the areas $P(Z\leq -1)=P(Z\geq 1)$. Since $\phi(z)=P(Z\leq c)$, $\phi(-c)=1-\phi(c)$. Rearranging, we get 
$$\phi(c)=1-\phi(-c)$$

This is a useful simplification trick when we have to solve for areas. Since the distribution is symmetric, *we can also use this to calculate areas if we have the table given for only the left/right side.*

## Standardization
While standard normal distributions and their tables are very useful, we have a big problem: Most of our distributions aren't distributed as $N(0,1)$. To fix this, *we use standardization to convert any normal distribution to a standard normal one.* This is done using the formula
$$Z= \dfrac{{x-\mu}}{\sigma}$$
This gives us the standardized form of $X$. Now that we have $X$ standardized in the form of $Z$, we can say that:
$P\left(  \dfrac{{x-\mu}}{\sigma}< \dfrac{{a-\mu}}{\sigma} \right)=P\left( Z< \dfrac{{a-\mu}}{\sigma} \right)$. This can be read off the standard normal table using $\phi\left( \dfrac{{a-\mu}}{\sigma} \right)$.

## Approximating binomial distribution
As long as a [[Binomial distribution|binomial distribution]] isn't too skewed, *binomial probabilities can be approximated well using normal curve areas.* The binomial distribution is perfectly symmetric if $p=0.5$, and it gets more skewed the greater the difference between $p$ and $0.5$ is. To avoid using this approximation for skewed distributions, **we have the general rule of thumb: use this if $np\geq 10$ and $nq \geq 10$**.

### Continuity correction factor
Using a continuous distribution to approximate a discrete one has one small issue.
![[Pasted image 20250111152520.png|center|500]]
Look at the graph below for $X\sim Bin(75,0.6)$. The shaded region shows us $P(X\geq 52)$. Now look what happens when we superimpose a normal curve on this and shade $P(X\geq 52)$.
![[Pasted image 20250111152722.png|center|500]]
**We can observe that half of the bar representing 52 is not being captured by the normal distribution.** This is because in discrete distributions, the bar goes from $x-0.5$ to $x+0.5$. However, in a continuous distribution, it starts at $x$ itself. Therefore, *when we use normal to approximate binomial, it will fail to account for one of $x\pm 0.5$*. This leads to over/underestimation, meaning our probability approximation will be slightly off.

Therefore, we must ensure that in our case, $52$ can take all values between $51.5$ and $52.5$. In this case, we should start at $51.5$ to get the best approximation. Generalizing, we can say
$$P(X\leq x)=Bin(n,p)\approx \phi\left( \dfrac{{x+0.5-np}}{\sqrt{ npq }} \right)$$
where $\mu=np,\sigma=\sqrt{ npq }$ (from the formulae of binomial distribution).