---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/mme
---
## What is absolute value
Let $a$ be any real number on the number line. The absolute value of $a$ is defined as *the distance from $a$ to $0$*. It is represented by $|a|$. $|a|=a,\:\geq 0$ and $-a,\:a< 0$.

## Defining intervals for absolute values
For $|x|\leq a$, the interval will be $[-a,a]$. Since it is less than $a$, $x$ must lie in between $a$ and $-a$ so that its absolute value remains less than $a$. You can also write $|x|\leq a$ as $-a\leq x\leq a$.

It is the opposite if we have $|x|\geq a$. Then, our interval becomes $(-\infty,-a]\cup[a,\infty)$. 

Q) Find the interval solution of $|3-8x|\leq 5$.
?
Ans) $-5\leq 3-8x\leq 5$.
$-8\leq-8x\leq 2$.
$-1\leq -x\leq \dfrac{1}{4}$.
Therefore, $\dfrac{-1}{4}\leq x\leq 1$. The interval will be $\left[ -\dfrac{1}{4},1 \right]$.

Q) Find the interval solution of $|x^{2}-2|\leq 1$.
?
Ans) $-1\leq x^{2}-2\leq 1$
$1\leq x^{2}\leq 3$
Therefore, $1\leq x\leq \sqrt{ 3 }$, $-\sqrt{ 3 }\leq x\leq-1$.
The interval will be $[-\sqrt{ 3 },1]\cup[1,\sqrt{ 3 }]$.


## Flashcards
Q1) Prove the triangle inequality: If $x$ and $y$ are real numbers, then $|x+y|\le|x|+|y|$.
?
Ans) We want to show that $-(|x|+|y|)\le x+y\le |x|+|y|$. *To do this, lets take $x$ and $y$ individually.*
We know $-|x|\le x\le |x|$ and $-|y|\le y \le |y|$. **Add the two inequalities component wise.** This gives us $-|x|-|y|\le x+y \le |x|+|y|$, which gives us $-(|x|+|y|)\le x+y\le |x|+|y|$. From this, we can say that $|x+y|\le |x|+|y|$.

Q2) Prove that for any real numbers $a$ and $b$, then $||a|-|b||\le|a-b|$
?
Ans) Let us consider each number individually.
*Using triangle inequality,* we know that $|a|=|(a-b)+b|\le |a-b|+|b|$. We can rearrange this to get $|a|-|b|\le |a-b|$ - **1**
-
Similarly, we can use triangle inequality to say that $|b|=|(b-a)+a|\le |b-a|+|a|$. This gives us $|b|-|a|\le |b-a|\iff |b| - |a|\le |a-b|\iff |a|-|b|\ge -(|a-b|)$ - **2**
-
Combining $1$ and $2$, we get $-(|a-b|)\le |a|-|b|\le |a-b|$. Taking absolute value of the middle term gives us $||a|-|b||\le|a-b|$. Hence proved.