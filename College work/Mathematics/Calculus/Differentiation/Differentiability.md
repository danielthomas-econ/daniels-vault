---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
While the test for continuity tells us if $f(x)$ is continuous, *differentiability tells us if $f^\prime(x)$ is continuous.* Any time we see a **smooth graph, we know it is differentiable.** This is because the smoothness of the graph tells us that the **derivative does not radically change at any point.** Therefore, we can say that $f(x)$ and $f^\prime(x)$ are both continuous from $(a,b)$ for the below graph.
![[Pasted image 20240902192437.png|center|350]]

$f(x)=|x|$ is a good example of a function that is *continuous, but not differentiable.* We can see that there are no breakpoints on this graph, so it is clearly continuous. However, we can see that the slope of the left side is $-1$, while the slope of the right side is $+1$. Therefore, **there is a sudden change in the slope of the function.** 
![[Pasted image 20240902192747.png|center|400]]
If we plot the graph of the derivative, it will look like the graph below. We can clearly see that it is discontinuous at $x=0$ because the left hand and right hand derivatives are different. To check left hand and right hand derivative, we can use [[College work/Mathematics/Calculus/Differentiation/Basic concepts#First principle|first principle]] with $\lim\limits_{x\to a^-}$ and $\lim\limits_{x\to a^+}$. **Since the graph of the derivative is discontinuous, we can say the function is not differentiable.** 
![[Pasted image 20240902193433.png]]

> [!tip] Continuity is a pre-requisite for differentiability
> A function can be differentiable only if it is continuous (LHL = RHL). If we see that a function is not continuous, we immediately know that it is also not differentiable. *However, a function being continuous is not a guarantee it is differentiable.* Once we know a function is continuous, we have to check the left and right hand derivative to determine its differentiability.

This function is a good example of being continuous, but not differentiable. Since it is in piecewise form, we don't need to use first principle to find the left and right hand derivative. We can see that the value of $f^{\prime}(x)$ suddenly jumps from $1$ at $\lim\limits_{x\to1^-}$ to $3$ at $\lim\limits_{x\to1^+}$. *This instantaneous change in the value of $f^{\prime}(x)$ tells us that $f(x)$ is continuous, but not differentiable at $x=1$*.
![[Pasted image 20240902195611.png]]