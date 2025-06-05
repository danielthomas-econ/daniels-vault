---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Quick access:
- [[#What are partial derivatives|What are partial derivatives]]
- [[#Solving partial derivatives|Solving partial derivatives]]
- [[#Second order partial derivatives|Second order partial derivatives]]
	- [[#Second order partial derivatives#Using Leibniz notation|Using Leibniz notation]]
- [[#Flashcards|Flashcards]]

## What are partial derivatives
Partial differentiation is used when *we have a function that is dependent on more than one variable.* Typically, we have a function $f(x)$. Since this only has one independent variable, we can differentiate it normally using $\dfrac{d\:f(x)}{dx}$. However, if our function is $f(x,y)$, **we cannot do this.** We must partially differentiate this with respect to either $x$ or $y$. Partial derivatives are denoted by $\dfrac{ \partial  f(x,y) }{ \partial x }$ or by $f_{x}$/$f_{y}$ The $\partial$ is called 'del'. 

## Solving partial derivatives
When solving partial derivatives wrt $x$, **we must treat the other variable like a constant.** Let's take $x^4+x^2y^2+y^4$ as an example. If we want to find $f_{x}$, we should keep $y$ as a constant. Therefore, $f_{x}$ becomes $4x^3+2xy^2$. In the same way, we have $f_{y}=4y^3+2yx^2$.

## Second order partial derivatives
We know that any given $f(x,y)$ has two first order partial derivatives: $f_{x}$ and $f_{y}$. *Each of these ones have two of their own partial derivatives.* If we partially differentiate $f_{x}$ wrt $x$, we get $f_{xx}$, and wrt $y$ gives us $f_{xy}$. Similarly, the partially differentiating $f_{y}$ gives us $f_{yy}$ and $f_{yx}$. 

$f_{xx}$ and $f_{yy}$ are normal second order partial derivatives, while $f_{xy}$ and $f_{yx}$ are called mixed partial derivatives. **In our syllabus, $f_{xy}$ and $f_{yx}$ will always be the same. However, in most cases outside the textbook, they aren't.** 

### Using Leibniz notation
We have to be a little careful if we choose to use the Leibniz notation when taking higher order partial derivatives. Here is the correct notation we should be using:
- $x$ and then $x$: $\dfrac{ \partial ^2f }{ \partial x^{2} }$
- $x$ and then $y$: $\dfrac{ \partial^{2}f }{ \partial y\partial x }$
- $y$ and then $y$: $\dfrac{ \partial^{2}f }{ \partial y^{2} }$
- $y$ and then $x$: $\dfrac{ \partial^{2}f }{ \partial x\partial y }$

Note that **if we differentiate wrt $x$ then $y$**, **our denominator shows $\partial y$ first, then $\partial x$** (written in reverse order).


## Flashcards
Q1) If $u=\log(\tan x+\tan y+\tan z)$, prove that$\sin 2x\dfrac{ \partial u }{ \partial x }+\sin 2y\dfrac{ \partial u }{ \partial y }+\sin 2z\dfrac{ \partial u }{ \partial z }=2$.
?
Ans) Differentiating $u$ wrt $x$ gives $u_{x}=\dfrac{1}{\tan x+\tan y+\tan z}\cdot \sec ^{2}x$. Multiplying this with $\sin 2x$ gives $\sin 2xu_{x}=\dfrac{{\sin 2x \cdot \sec ^{2}x}}{\tan x+\tan y+\tan z}$. Expanding the terms in the numerator, $\sin 2xu_{x}=\dfrac{{2\sin x\cos x\cdot{\dfrac{1}{\cos ^{2}x}}}}{\tan x+\tan y+\tan z}$Cancel out the $\cos$ terms, we get $\sin 2xu_{x}=\dfrac{{2 \tan x}}{\tan x+\tan y+\tan z}$. Since the equation is symmetric, it follows the same pattern for $u_{y}$ and $u_{z}$. Therefore, $\sin 2xu_{x}+\sin 2yu_{y}+\sin 2zu_{z}=\dfrac{{2(\tan x+\tan y+\tan z)}}{\tan x+\tan y+\tan z}=2$. Hence proved.
<!--SR:!2025-01-08,4,270-->

Q2) If $z=\log(x^{3}+y^{3}-x^{2}y-xy^{2})$, prove that $\dfrac{ \partial^{2}z }{ \partial x^{2} }+2\dfrac{ \partial^{2}z }{ \partial x\partial y }+\dfrac{ \partial^{2}z }{ \partial y }=\dfrac{{-4}}{(x+y)^{2}}$.
?
Ans) *We can see that our log term is very complex, so we can simplify it by factoring things out.* We can take $x^{2}$ and $y^{2}$ common to get $z=\log[x^{2}(x-y)+y^{2}(y-x)]$. We can change the sign of $y^{2}$ to get the $x^{2}-y^{2}$ identity, which gives us $z=\log[x^{2}(x-y)-y^{2}(x-y)]$. Taking $(x-y)$ common, we get $z=\log[(x-y)(x^{2}-y^{2})]=\log[(x-y)^{2}(x+y)]$. Expand the log inside and use properties to get $z=2\log(x-y)+\log(x+y)$. Now we can start differentiating.
.
You'll end up with something like this:
![[Pasted image 20241011065935.png|center|600]]
<!--SR:!2025-01-08,4,272-->


