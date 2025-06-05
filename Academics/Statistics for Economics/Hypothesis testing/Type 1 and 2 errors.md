---
color: var(--mk-color-yellow)
tags:
  - "#sem2-flashcards/stats/hypothesis_testing"
---
Quick access:
- [[#Errors|Errors]]
- [[#Alpha and beta|Alpha and beta]]

## Errors
The way we define our decision rule (and thus rejection region) can cause errors in our result. Suppose a company wants to test if their water dispenser actually dispenses 250 ml each time. If we define our rejection region to be $\bar{X} > 250$ and get a sample mean of $252$, we will end up rejecting the null hypothesis and say that the water dispenser doesn't dispense 250 ml. 

However, if in reality the water dispenser did dispense 250 ml each time, **we would be rejecting the null hypothesis when it was actually true. This is called type 1 error.** This error occurred due to *natural sample variability. The rejection region determines the probability of this error but does NOT cause it.* If we used a less strict decision rule like reject $H_{0}$ if $\bar{X} > 255$, we wouldn't encounter this error. The opposite, **failing to reject null when it is false, is called type 2 error.** 
 ![[WhatsApp Image 2025-05-26 at 13.04.34_d4c4a715.jpg]]
Due to sampling variability, it is almost impossible to create a test with no errors whatsoever. Instead, *we can focus on minimizing both these errors.* The choice of our decision rule and rejection region decides the level of type 1 and 2 errors. Note that **we usually consider type 1 errors to be more severe,** and thus try to minimize them.
 
## Alpha and beta
**The probability of a type 1 or 2 error is denoted by $\alpha$ or $\beta$ respectively.** A hypothesis test has *only one $\alpha$ but many $\beta$ values.* We can understand why this is by graphing our distribution and rejection region.
![[Pasted image 20250526141227.png]]
This is a graph of our distribution *assuming the null hypothesis is true.* The shaded area represents the rejection region. Clearly, the shaded area shows us the case where we reject null when it is true. **Therefore, the shaded region is $\alpha$**. We also call this $\alpha$ as the "level of significance" to denote the level of type 1 error we deem acceptable. This is why for a given decision rule, we can only have one $\alpha$. 

*However, $\beta$ depends on the true value of the alternative hypothesis. Therefore, for each value we consider in the alternative, we'll have a different* $\beta$. Our alternative will have a different distribution than the null. $\beta$ is the probability of failing to reject null when it is false. Since we consider null to be false here, we look at the graph of $H_{a}$. Since we fail to reject, **we consider the region to the left of the rejection area. This gives us the region for $\beta$**. Having a different $H_{a}$ will move the distribution of $H_{a}$ and will therefore change the value of $\beta$.
![[graphical-representation-of-type-1-and-type-2-errors.webp|center|400]]

### Calculating alpha and beta
To calculate $\alpha$, simply **look at the area of the rejection region when the null is true.** By definition, that is the probability of rejecting the null when it is true, so that area will be $\alpha$.

To calculate $\beta$ for a specific alternative value is a lot more complex. In some cases, you have formulae, in others, you may not. Calculating $\beta$ will be done in the respective cases of hypothesis testing, so refer to those notes instead.