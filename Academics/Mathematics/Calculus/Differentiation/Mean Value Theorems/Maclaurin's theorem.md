---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Maclaurin's theorem is basically [[Taylor's theorem]] when $a=0, h=x$. Therefore, Maclaurin's theorem states that:

If $f:[0,x]\to \mathbb{R}$ s.t. the $(n-1)^{th}$ derivative is continuous on $[0,x]$ and derivable on $(0,x)$, then $\exists$ a real number $\theta\in(0,1)$ s.t. $$f(x)=f(0)+xf'(0)+\dfrac{x^{2}}{2!}f''(0)\dots+\dfrac{x^{n-1}}{(n-1)!}f^{(n-1)}(0)+R_{n}$$
where $R_{n}$ can be either
*Cauchy's form of remainder:* $\dfrac{x^n(1-\theta)^{n-1}f^{(n)}(\theta x)}{(n-1)!}$
*Lagrange's form of remainder:* $\dfrac{x^n}{n!}f^{(n)}(\theta x)$
