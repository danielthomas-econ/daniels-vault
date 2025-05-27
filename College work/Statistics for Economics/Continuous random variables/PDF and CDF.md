---
color: var(--mk-color-green)
---
Quick access:
[[PDF and CDF#Probability density function|Probability density function]]
[[PDF and CDF#Cumulative distribution function|Cumulative distribution function]]

## Probability density function
The PDF of a continuous random variable is just like the [[PMF and CDF#Probability distribution of a discrete random variable|pmf]] of a discrete random variable. The difference is that the *PDF is a density function, so it measures total area in an interval.* Since we have to calculate the area bounded by a function over an interval, we have to use integration. Therefore, the PDF of $X$ is denoted by $f(x)$ s.t. for any two numbers $a,b$, $a\leq b$,
$$P(a\leq X\leq b)=\int_{a}^{b}f(x)dx$$

Therefore, the probability that $X$ takes a value in the interval $[a,b]$ is the area bounded within this interval by the density function $f(x)$.

For $f(x)$ to be a legitimate PDF, it must satisfy two conditions:
i) $f(x)\geq 0$ for all $x$
ii) $\int_{-\infty}^{\infty} f(x) \, dx=1$ (area under the whole graph)


## Cumulative distribution function
Once again, the continuous CDF is very similar to the [[PMF and CDF#Cumulative distribution function|discrete cdf.]] The CDF for a continuous rv $X$ is defined for every $x$ by
$$F(x)=P(X\leq x)=\int_{-\infty}^{x}f(y)dy$$
To satisfy the properties of a CDF, $F(x)$ must also have $\lim\limits_{x\to -\infty}F(x)=0$ and $\lim\limits_{x\to \infty}F(x)=1$.