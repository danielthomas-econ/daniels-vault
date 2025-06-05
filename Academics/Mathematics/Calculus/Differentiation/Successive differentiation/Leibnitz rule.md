---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
## Leibnitz rule
Leibnitz rule states that if $u$ and $v$ are 2 functions of $x$ which are $n$ times differentiable, then $y_n={^{n}C_{0}\:\cdot u_{n}v+{^{n}C_{1}\:\cdot\:}u_{n-1}v_1+{^{n}C_{2}}\:\cdot\:}u_{n-2}v_2$ ..... ${^{n}C_{n}uv_n}$.   

**Always choose the function that differentiates to zero as** $v$. This makes things a lot easier since that term will become $0$ eventually, ending the series right there. For example, to find the $n^{th}$ derivative of $x^2\:sin\:x$, we take $sin\:x=u$ and $x^2=v$. You would then solve it like this:
![[Pasted image 20240913192814.png]]

> [!NOTE] Write the full Leibnitz rule in the paper
> Ma'am said we'll get one q before Leibnitz and one q after Leibnitz for sure in the paper. When solving a question that involves using the Leibnitz rule, *we must mention the statement plus the formula* in the paper to get step marks.

## Flashcards
Q1) If $y=\log(x+\sqrt{ 1+x^{2} })$, prove that $(1+x^{2})y_{n+2}+(2n+1)xy_{n+1}+n^{2}y_{n}=0$.
?
Ans) Differentiating $y$, we get $y_{1}=\dfrac{1}{x+\sqrt{ 1+x^{2} }}\left( 1+\dfrac{1}{2\sqrt{ 1+x^{2} }}*2x \right)$. Taking LCM in the brackets gives $y_{1}=\dfrac{1}{x+\sqrt{ 1+x^{2} }}\left( \dfrac{{\sqrt{ 1+x^{2} }+x}}{\sqrt{ 1+x^{2} }} \right)$. Therefore, we end up with $y_{1}=\dfrac{1}{\sqrt{ 1+x^{2} }}$.=
<!--SR:!2025-01-08,4,270-->