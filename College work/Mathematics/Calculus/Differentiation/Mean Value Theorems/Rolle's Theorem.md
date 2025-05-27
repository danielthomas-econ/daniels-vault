---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Quick access
- [[#What is Rolle's Theorem|What is Rolle's Theorem]]
	- [[#What is Rolle's Theorem#Geometric interpretation|Geometric interpretation]]
	- [[#What is Rolle's Theorem#Alternate form of Rolle's Theorem|Alternate form of Rolle's Theorem]]
- [[#Proof of Rolle's Theorem|Proof of Rolle's Theorem]]
- [[#Proofs|Proofs]]
- [[#Flashcards|Flashcards]]


## What is Rolle's Theorem
Let $f:[a,b]\to \mathbb{R}$ s.t.
i) $f(x)$ is continuous on $[a,b]$
ii) $f(x)$ is derivable on $(a,b)$
iii) $f(a)=f(b)$
then $\exists$ at least one point $c\in(a,b)$ s.t. $f'(c)=0$

### Geometric interpretation
If the function is continuous on $[a,b]$ and derivable on $(a,b)$ and the endpoints of our interval are equal, *we will have at least one point where the tangent to the point is parallel to the x axis.*

### Alternate form of Rolle's Theorem
Let $f:[a,a+h]\to R,$ $(h>0)$ s.t.
i) $f$ is continuous on $[a,a+h]$
ii) $f$ is derivable on $(a,a+h)$
iii) $f(a)=f(a+h)$
then $\exists$ a real number $\theta\in(0,1)$ s.t. $f'(a+\theta h)=0$.

## Proof of Rolle's Theorem
**Case 1:** $f$ is a constant function
Let $f(x)=m$, then $f'(x)=0$ $\forall\:x\in(a,b)$

**Case 2:** $f$ is a non-constant function
As $f$ is continuous on $[a,b]$, it must either increase or decrease for $x>a$.
*Subcase 1:* Suppose $f$ increases when $x>a$. Since $f(a)=f(b)$, there will be a maximum point $c$, after which $f$ must start decreasing so that it reaches $(b,f(b))$.
![[Untitledcplushcminushgraph.jpg|center|300]]
Take $h$ as an integer $>0$.Then $f(c-h)-f(c)\leq 0$ and $f(c+h)-f(c)\leq 0$. **Divide by $-h$ and $h$ and we get** $\dfrac{{f(c-h)-f(c)}}{-h}\geq 0$ and $\dfrac{{f(c+h)-f(c)}}{h}\leq 0$. *This tells us that the left hand derivative is greater than zero, while the right hand derivative is less than zero.* Since $f$ is differentiable at all points, $f'(c)$ must exist. This is only possible if both sided derivatives are equal, **which only happens at zero.** Therefore, $\exists$ at least one $c\in(a,b)$ s.t. $f'(c)=0$.

*Subcase 2:* Suppose $f$ decreases when $x>a$. Since $f(a)=f(b)$, $f$ must start increasing again after a minimum point so that it reaches $(b,f(b))$. Let the minimum point be $c$. Consider an integer $h>0$. We know $f(c-h)-f(c)\geq 0$ and $f(c+h)-f(c)\geq 0$. Divide by $-h$ and $h$. We get $\dfrac{{f(c-h)-f(c)}}{-h}\leq 0$ and $\dfrac{{f(c+h)-f(c)}}{h}\geq 0$. Therefore, $Lf'(c)\leq 0$, $Rf'(c)\geq 0$. Since $f$ is differentiable in $(a,b)$, $f'(c)$ must exist. This means $Lf'(c)=Rf'(c)$, which is only possible at $0$. Therefore, $\exists$ at least one point $c\in(a,b)$ s.t. $f'(c)=0$.

## Proofs
i) **VVIMP:** If a function $f$ is s.t. its derivative is continuous on $[a,b]$ and derivable on $(a,b)$ respectively, prove that $\exists$ a point $c\in(a,b)\implies f(b)=f(a)+(b-a)f'(a)+\dfrac{(b-a)^{2}}{2}f''(c)$.
?
Ans) Define $g:[a,b]\to \mathbb{R}$.
Let $g(x)=f(b)-f(x)-(b-x)f'(x)-A(b-x)^{2}$ - *1,* where $A$ is a constant tbd by $g(a)=g(b)$.
*Note:* We get the value of $g(x)$ by shifting all the terms in the proof statement to the LHS and replacing $a$ with $x$.
.
$g(a)=f(b)-f(a)-(b-a)f'(a)-A(b-a)^{2}$.
$g(b)=f(b)-f(b)-0=0$.
Since $g(a)=g(b)$, $g(a)=0$.
Therefore, $f(b)=f(a)+(b-a)f'(a)+A(b-a)^{2}$ - *2*
.
As all the terms in $g$ are continuous on $[a,b]$ and differentiable on $(a,b)$, $g$ holds those same properties. Since $g(a)=g(b)$, it satisfies all conditions of Rolle's Theorem. Applying Rolle's Theorem to $g$ on $[a,b]$, $\exists$ at least one point $c\in(a,b)$ s.t. $g'(c)=0$.
$g'(x)=0-f'(x)+f'(x)-(b-x)f''(x)+2A(b-x)$
$\therefore g'(x)=-(b-x)f''(x)+2A(b-x)$
$\implies g'(c)=-(b-c)f''(c)+2A(b-c)=0$
$(b-c)f''(c)=2A(b-c)\implies A=\dfrac{f''(c)}{2}$.
Sub the value of $A$ in *2,*
$f(b)=f(a)+(b-a)f'(a)+\dfrac{(b-a)^{2}}{2}f''(c)$.
Hence, proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-07,3,252-->

ii) $f$ is twice differentiable on $[a,a+h]$, show $f(a+h)=f(a)+hf'(a)+\dfrac{h^{2}}{2}f''(a+\theta h)$ for $0<\theta<1$.
?
Ans) Define $g:[a,a+h]\to \mathbb{R}$
Let $g(x)=f(a+h)-f(x)-(a+h-x)f'(x)-A(a+h-x)^{2}$, where $A$ is determined by $g(a)=g(a+h)$
*Note:* Like the previous question, we get $g$ by moving all terms to the LHS. **We must also define $g(x)$ so that when we sub in $a$**, **we get something very similar to our proof statement and subbing in $a+h$ gives us zero.**
$g(a)=f(a+h)-f(a)-hf'(a)+A(h^{2})$
$g(a+h)=f(a+h)-f(a+h)-0-0=0$
Since $g(a)=g(a+h)$, $g(a)=0$.
Therefore, $f(a+h)=f(a)+hf'(a)+h^{2}A$ - *1*
.
Since all the terms of $g$ are continuous on $[a,b]$ and differentiable on $(a,b)$, $g$ is also continuous on $[a,b]$ and differentiable on $(a,b)$. We also know that $g(a)=g(a+h)=0$. Applying Rolle's Theorem on $g$ in $[a,a+h]$, $\exists$ at least one $c\in(a,a+h)$ s.t. $g'(c)=0$.
$g'(x)=0-f'(x)+f'(x)-(a+h-x)f''(x)+2A(a+h-x)$
$=-(a+h-x)f''(x)+2A(a+h-x)$
$g'(c)=-(a+h-c)f''(c)+2A(a+h-c)=0$
$\implies 2A(a+h-c)=(a+h-c)f''(c)$
Therefore, $A=\dfrac{f''(c)}{2}$
**Since $c$ lies in between $a$ and $a+h$**, **it can be expressed as $a+\theta h, \theta\in(0,1)$**. Therefore, $A=\dfrac{f''(a+\theta h)}{2}$. Sub in *1,*
$f(a+h)=f(a)+h'f(a)+\dfrac{h^{2}}{2}f''(a+\theta h)$.
Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-05,1,232-->

## Flashcards
Q1) Prove that between any two roots of the equation $e^x\cos x=1$ there exists at least one root of $e^x\sin x-1=0$.
?
Ans) $e^{x}\cos x=1 \implies \cos x=e^{-x} \implies \cos x-e^{-x}=0$. Similarly, since $e^{x}\sin x=1$, $\sin x-e^{-x}=0$.
Let $f(x)=\cos x-e^{-x},\:g(x)=\sin x-e^{-x}$. Let $\alpha$ and $\beta$ be the roots of $f(x)$. Since $f$ is continuous in $[\alpha,\beta]$ and derivable in $(\alpha,\beta)$ and $f(\alpha)=f(\beta)$, we can apply Rolle's theorem. Therefore, $\exists\:c\in(\alpha,\beta)$ s.t. $f'(c)=0$.
$f'(x)=-\sin x+e^{-x}$.
$f'(c)=e^{-c}-\sin c=0$
Therefore, $\sin c=e^{-c} \implies \sin c-e^{-c}=0$.
$\implies g(c)=0$. Therefore, there exists a root $c$ of $g(x)$ between the two roots of $f(x)$ $\alpha$ and $\beta$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,270-->

Q2) Show that there is no real number $k$ for which $x^{2}-3x+k=0$ has two distinct roots in $[0,1]$.
?
Ans) Suppose $\alpha$ and $\beta$ are distinct roots in $[0,1]$ with $\alpha <\beta$.
$f(x)=x^{2}-3x+k$ implies $f(\alpha)=f(\beta)=0$. The function $f$ is continuous in $[\alpha,\beta]$, derivable in $(\alpha,\beta)$ and $f(\alpha)=f(\beta)$. Applying Rolle's theorem on $f$ in $[\alpha,\beta]\subset[0,1]$, $\exists\:c\in(\alpha,\beta)$ s.t. $f'(c)=0$. Therefore, $2c-3=0\implies c=\dfrac{3}{2}$. However, $c \notin(0,1)$. *This is a contradiction.* This arises due to our incorrect assumption that $\alpha$ and $\beta$ are two distinct roots in $[0,1]$. Hence, proved by contradiction.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-07,4,270-->