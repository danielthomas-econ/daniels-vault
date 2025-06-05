---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Quick access
- [[#What is LMVT|What is LMVT]]
	- [[#What is LMVT#Geometric interpretation of LMVT|Geometric interpretation of LMVT]]
	- [[#What is LMVT#Proof of LMVT|Proof of LMVT]]
- [[#Alternate form of LMVT|Alternate form of LMVT]]
- [[#Proofs|Proofs]]
	- [[#Proofs#Prove a function lies in an interval|Prove a function lies in an interval]]

- [[#Flashcards|Flashcards]]

## What is LMVT
Lagrange's Mean Value Theorem, also called LMVT, is an extension of [[Rolle's Theorem|Rolle's Theorem.]] *It is called the first mean value theorem of differential calculus.* The theorem states that:
If $f:[a,b]\to \mathbb{R}$, s.t.
i) $f$ is continuous on $[a,b]$
ii) $f$ is derivable on $(a,b)$
then $\exists$ at least one point $c\in(a,b)$ s.t. $f'(c)=\dfrac{{f(b)-f(a)}}{b-a}$.

*Corollary:* When $f(a)=f(b)$, we get Rolle's theorem.

### Geometric interpretation of LMVT
Let's analyze both sides of the LMVT statement. The RHS $\dfrac{{f(b)-f(a)}}{b-a}$ is the slope formula and represents **the secant line connecting points $a$ and $b$**, which are at the ends of our interval. The LHS $f'(c)$ tells us that **there is a point $c$ where the slope of the tangent at $c$ is equal to the slope of the secant line between $a$ and $b$**.

### Proof of LMVT
Define $g:[a,b]\to \mathbb{R}$ s.t. $g(x)=f(x)+Ax$, where $A$ is a constant to be determined by $g(a)=g(b)$. *We do this so that we define $g(x)$ in such a way that it meets the conditions of Rolle's Theorem.* Therefore, we can say $f(a)+Aa=f(b)+Ab$. Rearranging, we get $A=-\left[ \dfrac{{f(b)-f(a)}}{b-a} \right]$ - *1*

Since both $f(x)$ and $Ax$ are continuous on $[a,b]$ and differentiable on $(a,b)$, $g(x)$ also fulfills the same properties as it is the sum of two derivable functions.

Applying Rolle's Theorem on $g(x)$ in $[a,b]$, $\exists$ at least one point $c\in(a,b)$ s.t. $g'(c)=0$. Therefore, $g'(c)=f'(c)+A=0\implies A=-f'(c)$ - *2*

From 1 and 2,
$f'(c)=\dfrac{{f(b)-f(a)}}{b-a}$
Hence, proved.

## Alternate form of LMVT
Let $f:[a,a+h]\to \mathbb{R}$ s.t. $f$ is continuous on $[a,a+h]$ and derivable on $(a,a+h)$, then $\exists$ a real number $0<\theta<1$ s.t.
$$hf'(a+\theta h)=f(a+h)-f(a)$$

Since $0<\theta<1$, we can say that $a<a+\theta h<a+h$. Therefore, $a+\theta h\in(a,a+h)$.

The alternate form works by shrinking the interval $[a,b]$ to a smaller interval $[a,a+h]$, where $h$ is a small number. This means that **the change in $f$ from $a$ to $a+h$ is equal to the derivative $f'$ at some point in $(a,a+h)$**, **scaled by the length of the interval $h$**.

Geometrically, this means that in a small interval $[a,a+h]$, the slope of the secant line connecting $(a,f(a))$ and $(a+h,f(a+h))$ is approximately equal to the tangent at some point $a+\theta h$. The approximation becomes better as $h$ gets smaller.


Eg: Let $[a,a+h]=[0,0.1]$ and $f(x)=\sin(x)$. Find $\sin(0.1)$.
We know that $hf'(a+\theta h)=f(a+h)-f(a)$. Therefore, $f(a+h)=hf'(a+\theta h)+f(a)$. Since $a=0,h=0.1$, we can say that $\sin(0.1)=0.1\cos(0.1\theta)+\sin(0)$. Therefore, $\sin(0.1)=0.1[\cos(0.1\theta)]$.

## Proofs
i) Let $f$ be continuous on $[a,b]$ and derivable on $(a,b)$ and $f'(x)=0\:\forall x$, then show $f$ is a constant function.

*Proof:* To prove $f$ is constant, we must prove that $f(x_{1})=f(x_{2})$ for any two $x_{1},x_{2}$ in $[a,b]$.
Let $x_{1},x_{2}$ be any two points in $[a,b]$ s.t. $[x_{1},x_{2}]\subset[a,b]$. As $f$ is continuous on $[a,b]$ and derivable on $(a,b)$, $f$ will also be continuous on $[x_{1},x_{2}]$ and derivable on $(x_{1},x_{2})$.

Applying LMVT on $f$ for $[x_{1},x_{2}]$, $\exists$ a point $c\in(x_{1},x_{2})$ s.t. $f'(c)=\dfrac{{f(x_{2})-f(x_{1})}}{x_{2}-x_{1}}$. **As $f'(x)=0$ $\forall\:x$**, **we can say that $f'(c)=0$**. Therefore, $\dfrac{{f(x_{2})-f(x_{1})}}{x_{2}-x_{1}}=0$. Therefore, $f(x_{2})-f(x_{1})=0$.

This means $f(x_{1})=f(x_{2})$ $\forall\:x_{1},x_{2} \in[a,b]$. Hence proved.
<div style="border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;"></div>

ii) If $f$ is continuous on $[a,b]$ and derivable on $(a,b)$ and $f'(x)>0\:\forall x$ then show that $x$ is strictly increasing on $[a,b]$.

*Proof:* For a function to be strictly increasing, $x_{1}<x_{2}\implies f(x_{1})<f(x_{2})$. Let $x_{1},x_{2}$ be any two points in $(a,b)$ s.t. $x_{1}<x_{2}$. Since $f$ is continuous on $[a,b]$ and derivable on $(a,b)$, $f$ is continuous on $[x_{1},x_{2}]$ and derivable on $(x_{1},x_{2})$. Applying LMVT on $f$ in $[x_{1},x_{2}]$, $\exists$ a point $c\in(x_{1},x_{2})$ s.t. $f'(c)=\dfrac{{f(x_{2})-f(x_{1})}}{x_{2}-x_{1}}$.

As $f'(x)>0$ $\forall\:x$, we can say that $f'(c)>0$. Therefore, $\dfrac{{f(x_{2})-f(x_{1})}}{x_{2}-x_{1}}>0$. Therefore, $f(x_{2})-f(x_{1})>0\implies f(x_{2})>f(x_{1})$ $\forall\:x_{2},x_{1} (x_{2}>x_{1})$. Hence, proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

iii) **Very important:** Let $f:[a-h,a+h]\to \mathbb{R}$ s.t. $f$ is continuous and derivable in the interval. Prove that there is a real number $\theta\in(0,1)$ s.t. $f(a+h)-f(a-h)=h[f'(a+\theta h)+f'(a-\theta h)]$.
?
Ans) To solve questions like this, **we have to construct a function in such a way that the derivative looks like** $f'(a+\theta h)+f'(a-\theta h)$. To do this, we define $g(x)=f(a+hx)-f(a-hx)$, $g:[0,1]\to \mathbb{R}$. *We define the domain as $[0,1]$ so that it is the same domain as theta.* Since $f(x)$ is derivable on $[a-h,a+h]$ and continuous on $(a-h,a+h)$, $g(x)$ is continuous on $[0,1]$ and derivable on $(0,1)$. Therefore, $g(x)$ satisfies the conditions of LMVT.
.
Applying LMVT to $g(x)$ on $[0,1]$, $\exists\: \theta\in(0,1)$ s.t. $g'(\theta)=\dfrac{{g(1)-g(0)}}{1-0}$. Therefore, $g'(\theta)=g(1)-g(0)=f(a+h)-f(a-h)-[f(a)-f(a)]$. Therefore, $g'(\theta)=f(a+h)-f(a-h)$ - *1*
We know $g'(x)=h[f'(a+hx)+f'(a-hx)]$. When $x=\theta$, $g'(\theta)=h[f'(a+\theta h)+f'(a-\theta h)]$ - *2*
Equate *1* and *2,*
$f(a+h)-f(a-h)=h[f'(a+\theta h)+f'(a-\theta h)]$.
Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-05,1,236-->

iv) A twice differentiable function $f$ is s.t. $f(a)=f(b)=0$ and $f(c)>0$, $a<c<b$. Prove that there is at least one value $\alpha$ between $a$ and $b$ for which $f''(\alpha)<0$ (concave down).
?
Ans) **Note: Since our proof requires $f''$**, **we will apply LMVT to $f'$ too.**
Since $f''$ exists in $[a,b]$, both $f$ and $f'$ exist and are continuous in $[a,b]$ and derivable in $(a,b)$, and hence in $[a,c]$ and $[c,b]$.
Applying LMVT on $f$ in $[a,c]$ and $[c,b]$, we get at least one point $\alpha_{1}$ in $[a,c]$ and $\alpha_{2}$ in  $[c,b]$ s.t. $f'(\alpha_{1})=\dfrac{{f(c)-f(a)}}{c-a}=\dfrac{f(c)}{c-a}$ and $f'(\alpha_{2})=\dfrac{{f(b)-f(c)}}{b-c}=-\dfrac{f(c)}{b-c}$, where $a<\alpha_{1}<c<\alpha_{2}<b$.
.
Since $f'$ is continuous in $[\alpha_{1},\alpha_{2}]$ and derivable in $(\alpha_{1},\alpha_{2})$, we can apply LMVT on $f'$ in $[\alpha_{1},\alpha_{2}]$, which tells us $\exists\:\alpha\in(\alpha_{1},\alpha_{2})\subset(a,b)$ s.t. $f''(\alpha)=\dfrac{{f'(\alpha_{2})-f'(\alpha_{1})}}{\alpha_{2}-\alpha_{1}}$ $=\dfrac{1}{\alpha_{2}-\alpha_{1}}\left[ -\dfrac{f(c)}{b-c}-\dfrac{f(c)}{c-a} \right]$ $=-\dfrac{f(c)}{\alpha_{2}-\alpha_{1}}\left[ \dfrac{1}{b-c}+\dfrac{1}{c-a} \right]$.
We know $a<\alpha_{1}<c<\alpha_{2}<b$ and that $f'(c)>0$ when $a<c<b$. From this info, we can say that $f''(\alpha)=\dfrac{{-ve}}{+ve}[+ve]=-ve$. Therefore, $f''(\alpha)<0$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,276-->

v) Prove that for any quadratic function $px^{2}+qx+r$, the value of $\theta$ in LMVT is always $\dfrac{1}{2}$ no matter what $p,q,r,a,h$ might be.
?
Ans) Let $f(x) = px^{2}+qx+r$
Since $f(x)$ is a polynomial, it is continuous and differentiable for all values of $x$. Applying LMVT to $f(x)$ in $[a,a+h]$, $\exists$ $\theta\in(0,1)$ s.t. $f'(a+\theta h)=\dfrac{{f(a+h)-f(a)}}{h}$.
$f'(x)=2px+q\implies f'(a+\theta h)=2p(a+\theta h)+q$
Therefore, $2p(a+\theta h)+q=\dfrac{{{p(a+h)^{2}}+q(a+h)+r-pa^{2}-qa-r}}{h}$.
$\implies 2pa+2p\theta h+q=\dfrac{{\cancel{pa^{2}}+ph^{2}+2ahp+\cancel{qa}+qh+\cancel{r}-\cancel{pa^{2}}-\cancel{qa}-\cancel{r}}}{h}$.
Taking $h$ common on RHS and cancelling, we get
$2pa+2p\theta h+q=ph+2ap+q$
$\implies 2p\theta h=ph\implies \theta=\dfrac{ph}{2ph}=\dfrac{1}{2}$.
Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,276-->

### Prove a function lies in an interval
There are many proof questions where you have to show a function lies between a given interval. There are two ways we can do this:
1. Using increasing and decreasing functions
2. Using LMVT

We'll go over this example using both ways.
Eg: Show that $\dfrac{x}{1+x}<\log(1+x)<x$, $x>0$.
*Proof 1: Using increasing and decreasing functions*
We have to prove that $\log(1+x) > \dfrac{x}{1+x}$ and $x>\log(1+x)$. **To do this, we use both sides of the inequality to define two different functions.** Let the first function $f(x)=\log(1+x)-\dfrac{x}{1+x}$, $x>0$.
Therefore, $f'(x)=\dfrac{1}{1+x}-\dfrac{1}{(1+x)^{2}}=\dfrac{x}{(1+x)^{2}}>0$ $(x>0)$.
$\implies f'(x)>0\:\forall x>0$. *This tells us that the function $f$ is increasing in* $x>0$. This means $f(x)>f(0)$. Therefore, $\log(1+x)-\dfrac{x}{1+x}>0\implies \log(1+x) > \dfrac{x}{1+x}$ - **1**

Lets define our second function using the second inequality. Let $g(x)=x-\log(1+x)$. $g'(x) = 1-\dfrac{1}{1+x}=\dfrac{x}{1+x}>0$ $(x>0)$. Since $g'(x)>0$, $g$ is an increasing function. Therefore, $g(x)>g(0)$. 
$\implies x - \log(1+x)>0$. Therefore, $x>\log(1+x)$ - **2**

Putting 1 and 2 together, we get our required proof.

*Proof 2: Using LMVT*
Define $f(x)=\log(1+x)$ (the middle term) on $[0,x]$. Since $f(x)$ is continuous on $[0,x]$ and derivable on $(0,x)$, we can apply LMVT. Using LMVT on $f(x)$ in $[0,x]$, $\exists$ a real number $\theta\in(0,1)$ s.t. $f'(a+\theta h)=\dfrac{{f(a+h)-f(a)}}{h}$. Here, $a=0, h=x$. Therefore, $f'(\theta x)=\dfrac{{f(x)-f(0)}}{x}\implies f'(\theta x)=\dfrac{\log(1+x)}{x}$. Taking the derivative of $f$, we get $\dfrac{1}{1+\theta x}=\dfrac{\log(1+x)}{x}\implies \dfrac{x}{1+\theta x}=\log(1+x)$ - *1*

We know $0<\theta<1$. Therefore, $1<1+\theta x<1+x\implies \dfrac{1}{1+x} < \dfrac{1}{1+\theta x} < 1\implies \dfrac{x}{1+x} < \dfrac{x}{1+\theta x} < x$. Sub *1,* and we get $\dfrac{x}{1+x} < \log(1+x) < x$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q1) Prove that $\dfrac{{v-u}}{1+v^{2}}< \tan^{-1}v-\tan^{-1}u < \dfrac{{v-u}}{1+u^{2}}$, given $0<u<v$. Also deduce that $\dfrac{\pi}{4}+\dfrac{3}{25} < \tan^{-1} \dfrac{4}{3} < \dfrac{\pi}{4}+\dfrac{1}{6}$.
?
Ans) Let $f(x)=\tan^{-1}x$ on $[u,v]$. $f(x)$ is continuous on $[u,v]$ and derivable on $(u,v)$, therefore we can apply LMVT. Using LMVT on $f(x)$ in $[u,v]$, $\exists\: \theta\in(0,1)$ s.t. $f'(a+\theta h)= \dfrac{{f(v)-f(u)}}{v-u}$. *Be careful when assigning the values of a and h.* Comparing the intervals $[a,a+h]$ and $[u,v]$, we get $a=u$, $a+h=v\implies h=v-a=v-u$.
.
Taking the derivative of $f(x)$ and substituting, we get $\dfrac{1}{1+(u+\theta(v-u))^{2}} = \dfrac{{\tan^{-1}v-\tan^{-1}u}}{v-u}$. Rearranging, we get $\dfrac{v-u}{1+(u+\theta(v-u))^{2}}=\tan^{-1}v-\tan^{-1}u$ - *1*
.
We know $0<\theta<1$. Therefore, $0<\theta(v-u)<v-u\implies u<u+\theta(v-u)<v$. Therefore, $1+u^{2}<1+(u+\theta(v-u))^{2} < 1+v^{2}$. Taking reciprocals, $\dfrac{1}{1+v^{2}} < \dfrac{1}{1+(u+\theta(v-u))^{2}} < \dfrac{1}{1+u^{2}}$. Multiply $v-u$ across the numerators and sub in *1* and we get the proof.
.
Sub $u=1, v=\dfrac{4}{3}$ to get the second part of the question.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-07,4,272-->



## Flashcards
Q1) Prove LMVT.
?
Ans) Define $g:[a,b]\to \mathbb{R}$ s.t. $g(x)=f(x)+Ax$, where $A$ is a constant to be determined by $g(a)=g(b)$. *We do this so that we define $g(x)$ in such a way that it meets the conditions of Rolle's Theorem.* Therefore, we can say $f(a)+Aa=f(b)+Ab$. Rearranging, we get $A=-\left[ \dfrac{{f(b)-f(a)}}{b-a} \right]$ - *1*
.
Since both $f(x)$ and $Ax$ are continuous on $[a,b]$ and differentiable on $(a,b)$, $g(x)$ also fulfills the same properties as it is the sum of two derivable functions.
.
Applying Rolle's Theorem on $g(x)$ in $[a,b]$, $\exists$ at least one point $c\in(a,b)$ s.t. $g'(c)=0$. Therefore, $g'(c)=f'(c)+A=0\implies A=-f'(c)$ - *2*
.
From 1 and 2,
$f'(c)=\dfrac{{f(b)-f(a)}}{b-a}$
Hence, proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-07,4,270-->

Q2) Let $f$ be continuous on $[a,b]$ and derivable on $(a,b)$ and $f'(x)=0\:\forall x$, then show $f$ is a constant function.
?
*Proof:* To prove $f$ is constant, we must prove that $f(x_{1})=f(x_{2})$ for any two $x_{1},x_{2}$ in $[a,b]$.
Let $x_{1},x_{2}$ be any two points in $[a,b]$ s.t. $[x_{1},x_{2}]\subset[a,b]$. As $f$ is continuous on $[a,b]$ and derivable on $(a,b)$, $f$ will also be continuous on $[x_{1},x_{2}]$ and derivable on $(x_{1},x_{2})$.
.
Applying LMVT on $f$ for $[x_{1},x_{2}]$, $\exists$ a point $c\in(x_{1},x_{2})$ s.t. $f'(c)=\dfrac{{f(x_{2})-f(x_{1})}}{x_{2}-x_{1}}$. **As $f'(x)=0$ $\forall\:x$**, **we can say that $f'(c)=0$**. Therefore, $\dfrac{{f(x_{2})-f(x_{1})}}{x_{2}-x_{1}}=0$. Therefore, $f(x_{2})-f(x_{1})=0$.
.
This means $f(x_{1})=f(x_{2})$ $\forall\:x_{1},x_{2} \in[a,b]$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-07,4,272-->

Q3) If $f$ is continuous on $[a,b]$ and derivable on $(a,b)$ and $f'(x)>0\:\forall x$ then show that $x$ is strictly increasing on $[a,b]$.
?
*Proof:* For a function to be strictly increasing, $x_{1}<x_{2}\implies f(x_{1})<f(x_{2})$. Let $x_{1},x_{2}$ be any two points in $(a,b)$ s.t. $x_{1}<x_{2}$. Since $f$ is continuous on $[a,b]$ and derivable on $(a,b)$, $f$ is continuous on $[x_{1},x_{2}]$ and derivable on $(x_{1},x_{2})$. Applying LMVT on $f$ in $[x_{1},x_{2}]$, $\exists$ a point $c\in(x_{1},x_{2})$ s.t. $f'(c)=\dfrac{{f(x_{2})-f(x_{1})}}{x_{2}-x_{1}}$.
.
As $f'(x)>0$ $\forall\:x$, we can say that $f'(c)>0$. Therefore, $\dfrac{{f(x_{2})-f(x_{1})}}{x_{2}-x_{1}}>0$. Therefore, $f(x_{2})-f(x_{1})>0\implies f(x_{2})>f(x_{1})$ $\forall\:x_{2},x_{1} (x_{2}>x_{1})$. Hence, proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,276-->

Q4) Show that $\dfrac{x}{1+x}<\log(1+x)<x$, $x>0$.
*Proof 1: Using increasing and decreasing functions*
We have to prove that $\log(1+x) > \dfrac{x}{1+x}$ and $x>\log(1+x)$. **To do this, we use both sides of the inequality to define two different functions.** Let the first function $f(x)=\log(1+x)-\dfrac{x}{1+x}$, $x>0$.
Therefore, $f'(x)=\dfrac{1}{1+x}-\dfrac{1}{(1+x)^{2}}=\dfrac{x}{(1+x)^{2}}>0$ $(x>0)$.
$\implies f'(x)>0\:\forall x>0$. *This tells us that the function $f$ is increasing in* $x>0$. This means $f(x)>f(0)$. Therefore, $\log(1+x)-\dfrac{x}{1+x}>0\implies \log(1+x) > \dfrac{x}{1+x}$ - **1**
-
Lets define our second function using the second inequality. Let $g(x)=x-\log(1+x)$. $g'(x) = 1-\dfrac{1}{1+x}=\dfrac{x}{1+x}>0$ $(x>0)$. Since $g'(x)>0$, $g$ is an increasing function. Therefore, $g(x)>g(0)$. 
$\implies x - \log(1+x)>0$. Therefore, $x>\log(1+x)$ - **2**
-
Putting 1 and 2 together, we get our required proof.
-
*Proof 2: Using LMVT*
Define $f(x)=\log(1+x)$ (the middle term) on $[0,x]$. Since $f(x)$ is continuous on $[0,x]$ and derivable on $(0,x)$, we can apply LMVT. Using LMVT on $f(x)$ in $[0,x]$, $\exists$ a real number $\theta\in(0,1)$ s.t. $f'(a+\theta h)=\dfrac{{f(a+h)-f(a)}}{h}$. Here, $a=0, h=x$. Therefore, $f'(\theta x)=\dfrac{{f(x)-f(0)}}{x}\implies f'(\theta x)=\dfrac{\log(1+x)}{x}$. Taking the derivative of $f$, we get $\dfrac{1}{1+\theta x}=\dfrac{\log(1+x)}{x}\implies \dfrac{x}{1+\theta x}=\log(1+x)$ - *1*
-
We know $0<\theta<1$. Therefore, $1<1+\theta x<1+x\implies \dfrac{1}{1+x} < \dfrac{1}{1+\theta x} < 1\implies \dfrac{x}{1+x} < \dfrac{x}{1+\theta x} < x$. Sub *1,* and we get $\dfrac{x}{1+x} < \log(1+x) < x$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>


