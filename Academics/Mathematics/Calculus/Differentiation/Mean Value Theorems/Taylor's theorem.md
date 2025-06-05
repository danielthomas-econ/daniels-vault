---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Quick access:
- [[#Taylor's theorem|Taylor's theorem]]
- [[#Taylor's remainder|Taylor's remainder]]
	- [[#Taylor's remainder#Cauchy's remainder after n terms|Cauchy's remainder after n terms]]
	- [[#Taylor's remainder#Lagrange's remainder after n terms|Lagrange's remainder after n terms]]
- [[#Proof of Taylor's theorem|Proof of Taylor's theorem]]
- [[#Interval proofs|Interval proofs]]
- [[#Flashcards|Flashcards]]



## Taylor's theorem
Let $f[a:a+h]\to \mathbb{R}$ s.t. the $(n-1)^{th}$ derivatives of $f$ are continuous on $[a,a+h]$ and derivable on $(a,a+h)$, then $\exists$ at least one $\theta\in(0,1)$ s.t. 
$$\small f(a+h)=f(a)+hf'(a)+\dfrac{h^{2}}{2!}f''(a)\dots \dfrac{h^{n-1}}{(n-1)!}f^{(n-1)}(a)+\dfrac{h^n(1-\theta)^{n-p}}{p(n-1)!}f^n(a+\theta h)$$
where $p$ is a positive integer

## Taylor's remainder
The term which occurs after $n$ terms is called the Taylor's remainder after $n$ terms. Therefore, $f(a+h)=\text{n terms + Taylor's remainder}$. *This remainder works as an error term.* As we have a finite number of terms, we cannot exactly derive the value of $f(a+h)$. The Taylor's remainder/error terms after $n$ terms helps us adjust the inaccuracy that occurs due to our limited number of terms.
$$R_{n}=\dfrac{{h^n(1-\theta)^{n-p}}}{p(n-1)!}f^{(n)}(a+\theta h)$$

### Cauchy's remainder after n terms
When $p=1$, the remainder term is said to be Cauchy's form of remainder and is given by
$$R_{n}=\dfrac{{h^n(1-\theta)^{n-1}}}{(n-1)!}f^{(n)}(a+\theta h)$$

### Lagrange's remainder after n terms
When $p=n$, the remainder term is called Lagrange's form of remainder and is given by
$$R_{n}=\dfrac{{h^n}}{n!}f^{(n)}(a+\theta h)$$

## Proof of Taylor's theorem
Define $\phi:[a,a+h]\to \mathbb{R}$ s.t. $\small\phi(x)=f(x)+(a+h-x)f'(x)+\dfrac{(a+h-x)^{2}}{2!}f''(x)\dots \dfrac{(a+h-x)^{n-1}}{(n-1)!}f^{(n-1)}(x)+k(a+h-x)^p$
where $k$ is a constant determined by $\phi(a+h)=\phi(a)$.

$\implies f(a+h)=f(a)+hf'(a)+\dfrac{h^{2}}{2!}f''(a)\dots \dfrac{h^{n-1}}{(n-1)!}f^{(n-1)}(a)+kh^p$  - *1*

$\phi$ is continuous on $[a,a+h]$ and derivable on $(a,a+h)$ as $f,f',f''$ are continuous on $[a,a+h]$ and derivable on $(a,a+h)$. *We also assumed that $\phi(a)=\phi(a+h)$ to get the value of k.* This means that $\phi$ satisfies all the conditions of [[Rolle's Theorem#Alternate form of Rolle's Theorem|Rolle's theorem.]]
Applying Rolle's theorem to $\phi$ on $(a,a+h)$, $\exists$ at least one real number $\theta\in(0,1)$ s.t. $\phi'(a+\theta h)=0$.
$\phi'(x)={f'(x)}-{f'(x)}+{(a+h-x)f''(x)}-{(a+h-x)f''(x)}\dots$
$\dfrac{(a+h-x)^{n-1}}{(n-1)!}f^{(n)}(x)-pk(a+h-x)^{p-1}$

**All the terms of the derivative cancel out except the last two.** Therefore, $\phi'(x)=\dfrac{(a+h-x)^{n-1}f^{(n)}(x)}{(n-1)!}-pk(a+h-x)^{p-1}$
$\phi'(a+\theta h)=0=\dfrac{(a+h-a-\theta h)^{n-1}f^{(n)}(a+\theta h)}{(n-1)!}-pk(a+h-a-\theta h)^{p-1}$
$=\dfrac{(h-\theta h)^{n-1}f^{(n)}(a+\theta h)}{(n-1)!f}-pk(h-\theta h)^{p-1}$
$\implies \dfrac{(h-\theta h)^{n-1}f^{(n)}(a+\theta h)}{(n-1)!}=pk(h-\theta h)^{p-1}$
*Isolating k, we get:*
$k = \dfrac{(h-\theta h)^{n-1}f^{(n)}(a+\theta h)}{p(h-\theta h)^{p-1}(n-1)!}= \dfrac{(h-\theta h)^{n-p}f^{(n)}(a+\theta h)}{p(n-1)!}$.

Taking $h$ common,
$k= \dfrac{h^{n-p}(1-\theta)^{n-p}}{p(n-1)!}f^{(n)}(a+\theta h)$

*Sub this into 1.* The $h^{n-p}$ and $h^p$ terms will give us $h^n$ and then we have Taylor's remainder as our last term. Hence proved.

## Interval proofs
Q1) Using Taylor's theorem, show that $1-\dfrac{x^{2}}{2!}\leq \cos x\leq 1-\dfrac{x^{2}}{2!}+\dfrac{x^4}{4!}$
?
Ans)
*Case 1:* $x=0$
The inequality is trivially true as $1\leq 1\leq 1$
.
*Case 2:* $x>0$
Let $f(x)=\cos x$. Apply Taylor's theorem to $f(x)$ with Lagrange's remainder **after two terms.** $f(x)=f(0)+xf'(0)+\dfrac{x^{2}}{2!}f''(\theta x),\:0<\theta<1$.
$\implies \cos x=1-\dfrac{x^{2}}{2!}\cos \theta x$ - **1**
As $\cos \theta x\leq 1$, $\dfrac{x^{2}}{2!}\cos \theta x\leq \dfrac{x^{2}}{2!}$. Multiply both sides by $-1$,
$-\dfrac{x^{2}}{2!}\cos \theta x \geq -\dfrac{x^{2}}{2!}$. $\therefore\:1-\dfrac{x^{2}}{2!}\cos \theta x\geq 1-\dfrac{x^{2}}{2!}$. From **1,** we can say that $\cos x\geq 1-\dfrac{x^{2}}{2!}$ - **2**
.
Applying Taylor's theorem with Lagrange's remainder **after 4 terms,** we get $f(x)=f(0)+xf'(0)+\dfrac{x^{2}}{2}f''(0)+\dfrac{x^{3}}{3!}f'''(0)+\dfrac{x^4}{4!}f^{(4)}(\theta x)$, for $\theta\in(0,1)$. This implies $\cos x=1-\dfrac{x^{2}}{2!}+\dfrac{x^4}{4!}\cos(\theta x)$ - **3**
.
Since $\cos \theta x\leq 1$, $\dfrac{x^4}{4!}$$\cos \theta x \leq \dfrac{x^4}{4!}$$\implies 1-\dfrac{x^{2}}{2!}+\dfrac{x^4}{4!}\cos(\theta x)\leq 1-\dfrac{x^{2}}{2!}+\dfrac{x^4}{4!}$ **4**
From **2** and **4,** we get our required inequality.
.
*Case 3:* $x<0$
Let $x=-y$. From *case 2,* $1-\dfrac{y^{2}}{2!}\leq \cos y\leq 1-\dfrac{y^{2}}{2!}+\dfrac{y^4}{4!}$. Sub $y=-x$ and we get $1-\dfrac{x^{2}}{2!}\leq \cos x \leq 1-\dfrac{x^{2}}{2!}+\dfrac{x^4}{4!}$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,272-->



## Flashcards
Q1) If $f(x)=(1-x)^{5/2}$, find the value of $c$ as $x\to 1$ s.t. $f(x)=f(0)+xf'(0)+\dfrac{x^{2}}{2!}f''(cx)$.
?
Ans) $f(0)=1$
$f'(x)=-\dfrac{5}{2}(1-x)^{\frac{3}{2}} \implies f'(0)=-\dfrac{5}{2}$
$f''(x)=\left( -\dfrac{5}{2} \right)\left( -\dfrac{3}{2} \right)(1-x)^{\frac{1}{2}} \implies f''(cx)= \dfrac{15}{4}(1-cx)^{1/2}$
Sub in the equation. Therefore, $(1-x)^{5/2}=1-\dfrac{5}{2}x+\dfrac{15}{4}x^{2}(1-cx)^{1/2}$.
Taking $\lim\limits_{x\to 1}$, LHS = $0$. Therefore, $\lim\limits_{x\to 1} RHS=0$. Taking the dominant term in the RHS, $\lim\limits_{x\to 1}\dfrac{15}{4}x^{2}(1-cx)^{1/2}=0$. **This can only happen at $c=1$**, **as it makes the $(1-cx)^{1/2}$ term equal to zero.** Therefore, $c=1$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-07,4,270-->

Q2) Prove Taylor's theorem.
?
Ans) Define $\phi:[a,a+h]\to \mathbb{R}$ s.t. $\small\phi(x)=f(x)+(a+h-x)f'(x)+\dfrac{(a+h-x)^{2}}{2!}f''(x)\dots \dfrac{(a+h-x)^{n-1}}{(n-1)!}f^{(n-1)}(x)+k(a+h-x)^p$
where $k$ is a constant determined by $\phi(a+h)=\phi(a)$.
$\implies f(a+h)=f(a)+hf'(a)+\dfrac{h^{2}}{2!}f''(a)\dots \dfrac{h^{n-1}}{(n-1)!}f^{(n-1)}(a)+kh^p$  - *1*
.
$\phi$ is continuous on $[a,a+h]$ and derivable on $(a,a+h)$ as $f,f',f''$ are continuous on $[a,a+h]$ and derivable on $(a,a+h)$. *We also assumed that $\phi(a)=\phi(a+h)$ to get the value of k.* This means that $\phi$ satisfies all the conditions of [[Rolle's Theorem#Alternate form of Rolle's Theorem|Rolle's theorem.]]
Applying Rolle's theorem to $\phi$ on $(a,a+h)$, $\exists$ at least one real number $\theta\in(0,1)$ s.t. $\phi'(a+\theta h)=0$.
$\phi'(x)={f'(x)}-{f'(x)}+{(a+h-x)f''(x)}-{(a+h-x)f''(x)}\dots$
$\dfrac{(a+h-x)^{n-1}}{(n-1)!}f^{(n)}(x)-pk(a+h-x)^{p-1}$
.
**All the terms of the derivative cancel out except the last two.** Therefore, $\phi'(x)=\dfrac{(a+h-x)^{n-1}f^{(n)}(x)}{(n-1)!}-pk(a+h-x)^{p-1}$
$\phi'(a+\theta h)=0=\dfrac{(a+h-a-\theta h)^{n-1}f^{(n)}(a+\theta h)}{(n-1)!}-pk(a+h-a-\theta h)^{p-1}$
$=\dfrac{(h-\theta h)^{n-1}f^{(n)}(a+\theta h)}{(n-1)!f}-pk(h-\theta h)^{p-1}$
$\implies \dfrac{(h-\theta h)^{n-1}f^{(n)}(a+\theta h)}{(n-1)!}=pk(h-\theta h)^{p-1}$
*Isolating k, we get:*
$k = \dfrac{(h-\theta h)^{n-1}f^{(n)}(a+\theta h)}{p(h-\theta h)^{p-1}(n-1)!}= \dfrac{(h-\theta h)^{n-p}f^{(n)}(a+\theta h)}{p(n-1)!}$.
Taking $h$ common,
$k= \dfrac{h^{n-p}(1-\theta)^{n-p}}{p(n-1)!}f^{(n)}(a+\theta h)$
*Sub this into 1.* The $h^{n-p}$ and $h^p$ terms will give us $h^n$ and then we have Taylor's remainder as our last term. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-05,1,232-->