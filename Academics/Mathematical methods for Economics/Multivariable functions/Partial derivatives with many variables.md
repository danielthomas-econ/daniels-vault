---
color: var(--mk-color-teal)
tags:
  - "#sem2-flashcards/mme/multivariable_functions"
---
Quick access:
- [[#Young's theorem|Young's theorem]]
- [[#Hessian matrix|Hessian matrix]]

## Young's theorem
Suppose two $m^{th}$ order partials of the function $f(x_{1},x_{2},\dots,x_{n})$ *involve the same number of differentiations wrt each variable and are both continuous* in an open set $S$. Then, we can say that **the two partials are necessarily equal at all points in $S$**. 

A very useful implication of Young's theorem is that if we have $f_{12}''$ and $f_{21}''$ and both are continuous, we can see that both involve the same number of differentiations (both $x$ and $y$ are differentiated once). **Therefore, $f_{12}''$ and $f_{21}''$ are equal in this case.**

## Hessian matrix
If $z=f(x_{1},x_{2},\dots,x_{n})$, then $\dfrac{ \partial f }{ \partial x_{i} }$ is the derivative of $f$ wrt $x_{i}$ keeping all other variables constant. **For each of the $n$ first order partials, we have $n$ second order partials.** $\dfrac{ \partial f }{ \partial x_{j} }\left( \dfrac{ \partial f }{ \partial x_{i} } \right)= \dfrac{ \partial^{2} f }{ \partial x_{i}x_{j} }=z_{ij}''$. **Therefore, the total number of second order partials is** $n^{2}$. Since there are $n^{2}$ second order partials, we can put them all into a square matrix of order $n$. *The matrix of second order partials is called the Hessian.* It looks like:
![[Pasted image 20250530131423.png|center|400]]

The $(i,j)^{th}$ entry of the Hessian is $\dfrac{ \partial^{2} f }{ \partial x_{i}x_{j} }$. From Young's theorem, we know that $f_{ij}''=f_{ji}''$ if they're continuous. Therefore, *when the second partials are continuous, the Hessian is symmetric and has at most $\dfrac{n(n+1)}{2}$ unique entries.* 


