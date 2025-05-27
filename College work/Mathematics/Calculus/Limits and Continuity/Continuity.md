---
color: var(--mk-color-orange)
tags:
  - sem1-flashcards/math_ge/calc/limits_and_continuity
---
Quick access:
[[Continuity#Continuity definition|Continuity definition]]
[[Continuity#Types of discontinuity|Types of discontinuity]]

[[Continuity#Flashcards|Flashcards]]

## Continuity definition
A function $f$ is said to be continuous at a point $c$ if $\lim\limits_{x\to c^-}f(x)=\lim\limits_{x\to c^+}f(x)=f(x)$. If any one of these three values aren't equal, there is a discontinuity at $f(c)$.

## Types of discontinuity
### Jump discontinuity
![[Untitledjumpdiscontinutity.jpg|center|400]]
$f(c)$ is defined and both one sided limits exist, but aren't equal to each other. $\lim\limits_{x\to c^{-}}=a$, $\lim\limits_{x\to c^{+}}=b$. *This is called discontinuity of the first kind.*

### Infinite discontinuity
![[Untitledifniitediscontinuity.jpg|center|400]]
$f(c)$ is defined, limit doesn't exist. $\lim\limits_{x\to c}f(x)=\infty$, *both one sided limits do not exist.* This is also called **discontinuity of the second kind.**

### Removable discontinuity
![[Untitledremovablediscontinuity.jpg|center|400]]
$f(c)$ is defined, limit also exists and is equal to $a$. However, $\lim\limits_{x\to c}=a\ne f(c)=b$



## Flashcards
Q1) Examine the continuity of $f(x)=\dfrac{{e^{1/x}-e^{-1/x}}}{e^{1/x}+e^{-1/x}}$, $1$ at $x=0$.
?
Ans) We have to examine the continuity at $x=0$. *Our main goal is to get rid of $e^{1/h}$ because it tends to $\infty$*. We want our expression to be in terms of $e^{-1/h}$ because it goes to zero.
*LHL:* Let $x=0-h$
$\lim\limits_{h\to 0}f(0-h)=\lim\limits_{h\to 0}f(-h)=\lim\limits_{h\to 0}\dfrac{{e^{-1/h}-e^{1/h}}}{e^{-1/h}+e^{1/h}}$
**Directly substituting $h=0$ gives us an indeterminate form, so we take $e^{1/h}$ outside.** This gives us $\lim\limits_{h\to 0} \dfrac{{e^{1/h}(e^{-2/h}-1)}}{e^{1/h}(e^{-2/h}+1)}$. We can cancel out the $e^{1/h}$, and we know $\lim\limits_{h\to 0}e^{-2/h}=0$. Therefore, the limit simplifies to $\dfrac{-1}{1}=-1$.
*RHL:* Let $x=0+h$
$\lim\limits_{h\to 0}f(0+h)=\lim\limits_{h\to 0}f(h)=\lim\limits_{h\to 0} \dfrac{{e^{1/h}-e^{-1/h}}}{e^{1/h}+e^{-1/h}}$
$=\lim\limits_{h\to 0} \dfrac{{e^{1/h}(1-e^{-2/h})}}{e^{1/h}(1+e^{-2/h})}$ = $1$
Since $LHL\ne RHL$, the limit doesn't exist. The function has a jump discontinuity at $x=0$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,270-->

