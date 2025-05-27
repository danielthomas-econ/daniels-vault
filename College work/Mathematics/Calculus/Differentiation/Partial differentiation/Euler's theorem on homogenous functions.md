---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Quick access:
[[Euler's theorem on homogenous functions#Converting to homogenous functions|Converting to homogenous functions]]
[[Euler's theorem on homogenous functions#Euler's theorem|Euler's theorem]]
	[[Euler's theorem on homogenous functions#Corollary of Euler's theorem|Corollary of Euler's theorem]]


## Converting to homogenous functions
We know that a homogenous function is a function in which all the terms share the same power. *To prove a function is homogenous, we need to write it in the form $u=x^nf(\frac{y}{x})$*. Let's go through the steps of converting with an example.

Eg: Prove $u=\log \left( \dfrac{{x^{2}+y^{2}}}{\sqrt{ x }+\sqrt{ y }} \right)$ is a homogenous function.
?
Ans) Let's *first isolate the term in parentheses.* This gives us $e^{u}=\dfrac{{x^{2}+y^{2}}}{\sqrt{ x }+\sqrt{ y }}$. Next, **we take out the highest power in both the numerator and the denominator.** This gives us $e^{u}=\dfrac{{x^{2}}}{x^{\frac{1}{2}}}\: \dfrac{{1+\left( \dfrac{y}{x} \right)^{2}}}{1+\left( \dfrac{y}{x} \right)^{\frac{1}{2}}}$. Now we must *simplify the $x$ term to get it in the form $x^n$*. This gives us $e^{u}=x^{\frac{3}{2}} \dfrac{{1+\left( \dfrac{y}{x} \right)^{2}}}{1+\left( \dfrac{y}{x} \right)^{\frac{1}{2}}}$.
.
Now we're done. This is a homogenous equation of degree $\dfrac{3}{2}$ (exponent of $x$) since we've expressed the brackets in the form of $f\left( \dfrac{y}{x} \right)$.
<!--SR:!2025-01-08,4,270-->

## Euler's theorem
Euler's Theorem states that if $f(x,y)$ is a homogenous function of degree $n$, then:$$xf_{x}+yf_{y}=nf$$
### Corollary of Euler's theorem
If $u$ is a homogenous function of degree $n$ dependent on $x$ and $y$, then:$$\begin{align}
&1)\:xu_{xx}+yu_{xy}=(n-1)u_{x} \\
&2)\:yu_{yy}+xu_{xy}=(n-1)u_{y} \\
&3)\:x^{2}u_{xx}+2xyu_{xy}+y^{2}u_{yy}=n(n-1)u
\end{align}$$



## Flashcards
Q1) ![[Pasted image 20241012115603.png]]
?
Ans) i) We can see that $\tan u$ can be expressed as $x^{\frac{1}{6}}f\left( \dfrac{y}{x} \right)$. Therefore, $\tan u$ is a homogenous equation of degree $\frac{1}{6}$. Applying Euler's theorem, we get $x\dfrac{ \partial \tan u }{ \partial x }+y\dfrac{ \partial \tan u }{ \partial y }=\dfrac{1}{6}\tan u$. We know the derivative of $\tan u$ is $\sec ^{2}u$. Therefore, this equation simplifies to $x\sec ^{2}u\dfrac{ \partial u }{ \partial x }+y\sec ^{2}u\dfrac{ \partial u }{ \partial y }=\dfrac{1}{6}\tan u$. *Divide both sides by $\sec ^{2}u$ so that the LHS matches the form in our proof.* Therefore, $x\dfrac{ \partial u }{ \partial x }+y\dfrac{ \partial u }{ \partial y }=\dfrac{1}{6} \dfrac{{\tan u}}{\sec ^{2}u}$. Simplifying the RHS, we get $x\dfrac{ \partial u }{ \partial x }+y\dfrac{ \partial u }{ \partial y }=\dfrac{1}{6} \dfrac{{\sin u}}{\cos u} \cos ^{2}u$. The RHS becomes $\dfrac{1}{6}\sin u\cos u$. *Our proof needs the RHS in the form $\sin 2u$*, *so we multiply and divide by 2.* Therefore, $\dfrac{1}{6\times 2}\: 2\sin u\cos u=\dfrac{1}{12}\sin 2u$.
-
ii)![[Untitlediiiiiiafjiofsintrigoproof.jpg|center|450x400]]
Not the neatest, but you probably get the idea.
<!--SR:!2025-01-08,4,270-->
