---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/stats/two_sample_inferences"
---
Quick access:
- [[#F distribution|F distribution]]
- [[#Hypothesis testing|Hypothesis testing]]
	- [[#Hypothesis testing#Computing F values|Computing F values]]
	- [[#Hypothesis testing#Rejection region|Rejection region]]
	- [[#Hypothesis testing#p values for F tests|p values for F tests]]
- [[#Confidence interval|Confidence interval]]


## F distribution
The F distribution has two parameters $\nu_{1}$ and $\nu_{2}$, which are numerator and denominator degrees of freedom. We have the term numerator and denominator here because **a F variable is the ratio of chi-square variables divided by their respective degrees of freedom.** [[Estimating standard deviation#Chi-squared distribution|Recall]] that the rv $\dfrac{(n-1)s_{2}}{\sigma^{2}}\sim \chi^{2}_{n-1}$. Therefore, if $\chi_{\nu_{1}}^{2}$, $\chi_{\nu_{2}}^{2}$ are independent chi-square variables with $\nu_{1}$ and $\nu_{2}$ levels of freedom, then we can say
$$F = \dfrac{{\chi^{2}_{\nu_{1}}/\nu_{1}}}{\chi^{2}_{\nu_{2}}/\nu_{2}}
= \dfrac{\dfrac{(m-1)s_{1}^{2}}{\sigma_{1}^{2}(m-1)}}{\dfrac{(n-1)s_{2}^{2}}{\sigma_{2}^{2}(n-1)}} = \dfrac{{{s_{1}^{2}}/{\sigma_{1}^{2}}}}{{s_{2}^{2}}/{\sigma_{2}^{2}}}
$$

Therefore, the random variable $\dfrac{{{s_{1}^{2}}/{\sigma_{1}^{2}}}}{{s_{2}^{2}}/{\sigma_{2}^{2}}}\sim F_{m-1, n-1}$.

## Hypothesis testing
Since the $F$ variable involves a *ratio, not difference,* the test statistic is also a ratio. The claim that the variances are equal is **rejected if the ratio differs too much from 1.** Therefore, our null hypothesis becomes $\sigma_{1}^{2}=\sigma_{2}^{2}$. Since we start by assuming our null hypothesis is true, our $F$ variable reduces to $\dfrac{s_{1}^{2}}{s_{2}^{2}}$, **the ratio of sample variances,** as the $\sigma^{2}$ terms cancel out. Therefore, the key points to remember are:
$$\begin{align}
H_{0}: \sigma_{1}^{2}=\sigma_{2}^{2} \\
\text{Test statistic: } \dfrac{s_{1}^{2}}{s_{2}^{2}}
\end{align}
$$
### Computing F values
The F distribution is positively skewed, but tends to normal as $\nu_{1},\nu_{2} \to \infty$. Since we have to use a F distribution, we can no longer use Z or t tables as before. 
![[f14.png]]
*The F distribution isn't symmetric, so we have to calculate upper and lower tail values separately.* Fortunately, we have a useful property that can simplify our calculations.
$$F_{1-\alpha,\nu_{1},\nu_{2}}=\dfrac{1}{F_{\alpha,\nu_{2},\nu_{1}}}$$
**Note that the degrees of freedom are swapped.** Since we have very few values of $\alpha$ in the table, we can use this formula to calculate $F$ values for values of $1-\alpha$ too. **Observe that all the values in the table are greater than 1. If you are given a critical value less than 1, that's a sign you should use this formula** to find what is asked in the question. *It is also useful to find lower critical values when forming the rejection region.*

### Rejection region
We have to be careful when specifying rejection regions for hypothesis tests when using the F distribution. This is because **the F distribution isn't symmetric, so you can't simply use $F_{\alpha}$ and $-F_{\alpha}$ for right and left tailed tests.** 

In the exam, **I'd STRONGLY RECOMMEND drawing diagrams** for any F distribution question (to be honest, draw diagrams for most questions to make sure you don't go wrong).
![[Pasted image 20250529083835.png]]
We want the rejection region to have an area of $\alpha$ to keep type 1 error under control. For a *right tail test, this means area to the right of $F_{critical}$ must be $\alpha$*, *so we use $F_{\alpha}$* (by definition) to define the critical point. For a left tail test, area to the left must be $\alpha$, so the area to the right must be $1-\alpha$, therefore our critical point is $F_{1-\alpha}$.

For a two tail test, area to the right is $\dfrac{\alpha}{2}$ $\implies$ **right side critical point is $F_{\frac{\alpha}{2}}$**, and area to the left is also $\dfrac{\alpha}{2}$ $\implies$ area to the right is $1-\dfrac{\alpha}{2}$ $\implies$ **left side critical point is** $F_{1-\frac{\alpha}{2}}$. Therefore, our rejection rejection is $F_{cal} \geq F_{\alpha}$ or $F_{cal} \leq F_{1-\frac{\alpha}{2}}$. Here is a table showing all possible cases of rejection regions:
![[WhatsApp Image 2025-05-29 at 08.36.05_401a1503.jpg]]

### p values for F tests
Our F tables only give values for some $\nu_{1}$ and $\nu_{2}$ for areas $0.001,0.01,0.05$ and $0.1$. *We can only get exact p values if our critical value is exactly equal to a value in the table. If its not in the table, we can merely obtain an interval for our p value.*

For example, lets consider $\nu_{1}=7,\nu_{2}=9$.
![[Pasted image 20250529092804.png|center]]
If our calculated test statistic was $3.29$, then for an upper tail test, area to the right is $0.05$ (which is what the table tells us), so the p value is exactly $0.05$. **However, if we take $4.28$**, **graphically its to the right of $3.29$ but to the left of $5.61$**. **So the area to the right of $4.28$ is less than $0.05$ but more than $0.01$**. **Therefore, the p value for $4.28$ will be between $0.01$ and $0.05$**. We follow similar procedures for left tail and two tailed tests based on their respective rejection regions.

## Confidence interval
From the graph of the rejection rejection, we know the area between $F_{1-\frac{\alpha}{2}}$ and $F_{\frac{\alpha}{2}}$ is $1-\alpha$. Using this, we can derive a confidence interval for $\dfrac{\sigma_{1}^{2}}{\sigma_{2}^{2}}$.
$$\begin{align}
1-\alpha &= P\left( F_{1-\frac{\alpha}{2}}< F < F_{\frac{\alpha}{2}}\right) \\
&=P\left( F_{1-\frac{\alpha}{2}} < \dfrac{{s_{1}^{2}/\sigma_{1}^{2}}}{s_{2}^{2}/{\sigma_{2}^{2}} }  \\
< F_{\frac{\alpha}{2}}\right) \\
&=P\left( F_{1-\frac{\alpha}{2}} < \dfrac{s_{1}^{2}}{s_{2}^{2}} \cdot \dfrac{\sigma_{2}^{2}}{\sigma_{1}^{2}} < F_{\frac{\alpha}{2}} \right) \\
&= P\left( \dfrac{1}{F_{\frac{\alpha}{2}}} < \dfrac{s_{2}^{2}}{s_{1}^{2}} \cdot \dfrac{\sigma_{1}^{2}}{\sigma_{2}^{2}} < \dfrac{1}{F_{1-\frac{\alpha}{2}}} \right) \\
&=P\left( \dfrac{s_{1}^{2}/s_{2}^{2}}{F_{\frac{\alpha}{2}}} < \dfrac{\sigma_{1}^{2}}{\sigma_{2}^{2}} < \dfrac{s_{1}^{2}/s_{2}^{2}}{F_{1-\frac{\alpha}{2}}} \right)
\end{align}$$
Therefore, the $(1-\alpha)100\%$ CI for ratio of variances is $\left( \dfrac{s_{1}^{2}/s_{2}^{2}}{F_{\frac{\alpha}{2}}}, \dfrac{s_{1}^{2}/s_{2}^{2}}{F_{1-\frac{\alpha}{2}}} \right)$.
