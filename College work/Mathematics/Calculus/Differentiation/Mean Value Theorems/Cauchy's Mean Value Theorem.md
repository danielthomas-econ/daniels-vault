---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Quick access
- [[#What is CMVT|What is CMVT]]
- [[#Proof of CMVT|Proof of CMVT]]
- [[#Proofs|Proofs]]

- [[#Flashcards|Flashcards]]


## What is CMVT
Let $f$ and $g$ be defined on $[a,b]$ s.t. 
i) $f,g$ are continuous on $[a,b]$
ii) $f,g$ are derivable on $(a,b)$
iii) $g(x)\ne 0$ $\forall\:x\in(a,b)$
then $\exists\:c\in(a,b)$ s.t. $\dfrac{f'(c)}{g'(c)}=\dfrac{{f(b)-f(a)}}{g(b)-g(a)}$

*Note:* We can think of [[Lagrange's Mean Value Theorem|LMVT]] as CMVT with $g(x)=x$. Then $g'(x)=1$ and we get $\dfrac{f'(c)}{1}=\dfrac{{f(b)-f(a)}}{b-a}$. However, **we cannot derive CMVT from LMVT.**

## Proof of CMVT
Define $\phi:[a,b]\to \mathbb{R}$ s.t. $\phi(x)=f(x)+Ag(x)$, where $A$ is a constant tbd by $\phi(a)=\phi(b)$. 
This implies $f(a)+Ag(a)=f(b)+Ag(b)\implies A=-\left[ \dfrac{{f(b)-f(a)}}{g(b)-g(a)} \right]$ - *1*

From assumptions 1 and 2, $\phi(x)$ is continuous on $[a,b]$ and derivable on $(a,b)$. Since $\phi(a)=\phi(b)$, it satisfies the conditions of [[Rolle's Theorem|Rolle's Theorem.]] Applying Rolle's Theorem on $\phi$ in $[a,b]$, $\exists$ at least one $c\in(a,b)$ s.t. $\phi'(c)=0$
$\phi'(c)=f'(c)+Ag'(c)=0$
$\implies A=-\dfrac{f'(c)}{g'(c)}$ - *2*
From *1* and *2,* we get our required proof.

## Proofs
i) Let $f:[a,b]\to \mathbb{R}$ $(a>0)$ s.t. $f$ is continuous on $[a,b]$ and derivable on $(a,b)$. Prove that $\exists$ $c\in(a,b)$ s.t. $2c[f(a)-f(b)]=f'(c)(a^{2}-b^{2})$
?
Ans) We have to look at the proof statement to figure out how to define our $g(x)$. Since we have $2c$, there is probably some $c^2$ term that was differentiated. Having $a^{2}-b^{2}$ also tells us that our $g(x)$ must have some squared term.
.
Define $g(x) =x^{2}$ in $[a,b]$. $g$ is continuous in $[a,b]$ and derivable in $(a,b)$, and $g'(x)=2x\ne 0\:\forall\:x\in(a,b)$. By CMVT, $\exists$ $c\in(a,b)$ s.t. $\dfrac{f'(c)}{g'(c)}=\dfrac{{f(b)-f(a)}}{g(b)-g(a)}$. Therefore, $\dfrac{f'(c)}{2c}=\dfrac{{f(b)-f(a)}}{b^{2}-a^{2}}$. Cross multiplying gives $2c[f(b)-f(a)]=f'(c)(b^{2}-a^{2})$. Multiply by $-1$ inside to get the proof.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,272-->


## Flashcards
Q1) Verify CMVT for $f(x)=e^x$, $g(x)=e^{-x}$ in the interval $[0,1]$
?
Ans) $f(x)$ and $g(x)$ are both continuous in $[0,1]$ and derivable in $(0,1)$ and $g(x)\ne 0$ for $x\in(0,1)$. By CMVT, $\exists$ $c\in(a,b)$ s.t. $\dfrac{f'(c)}{g(c)}=\dfrac{{f(b)-f(a)}}{g(b)-g(a)}$. Therefore, $\dfrac{e^c}{-e^{-c}}=\dfrac{{e-1}}{\dfrac{1}{e}-1}=\dfrac{e({e-1})}{1-e}$
$\implies \dfrac{e^c}{-e^{-c}}=-e\implies \dfrac{e^c}{e^{-c}}=e$
$\implies e^{2c}=e$
Therefore, $2c=1\implies c=\dfrac{1}{2}$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,272-->

Q2) Show that $\dfrac{{\sin\alpha - \sin\beta}}{\cos\beta-\cos\alpha}=\cot \theta$, $0<\alpha<\theta<\beta< \dfrac{\pi}{2}$
?
Ans) Let $f(x)=\sin x,\:g(x)=\cos x$, $x\in[\alpha,\beta]$. $g'(x)=-\sin x\ne 0\:\forall\:x\in[\alpha,\beta]\subset\left( 0, \dfrac{\pi}{2} \right)$. Since both functions are continuous on $[\alpha,\beta]$ and derivable on $(\alpha,\beta)$, they satisfy the conditions of CMVT. Applying CMVT on $f(x)$ and $g(x)$ in $[\alpha,\beta]$, $\exists$ $\theta\in(\alpha,\beta)$ s.t. $\dfrac{f'(\theta)}{g'(\theta)}=\dfrac{{f(\beta)-f(\alpha)}}{g(\beta)-g(\alpha)}\implies \dfrac{{\cos \theta}}{-\sin \theta}=\dfrac{{\sin\beta-\sin\alpha}}{\cos\beta-\cos\alpha}$.
Therefore, $-\cot \theta=\dfrac{-(\sin\alpha-\sin\beta)}{\cos\beta-\cos\alpha}$. Cancel out the negative signs to get the proof.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-07,4,270-->
