---
color: var(--mk-color-brown)
tags:
  - sem1-flashcards/mme
---
Quick access:
[[Quadratic functions#Basics of a quadratic|Basics of a quadratic]]
[[Quadratic functions#Zeros of a quadratic|Zeros of a quadratic]]
[[Quadratic functions#Max/min of a quadratic|Max/min of a quadratic]]

## Basics of a quadratic
Functions of the form $ax^{2}+bx+c$, where $a,b,c$ are constants are $a\ne{0}$ are called quadratic functions. Their graphs are parabolas, facing upwards if $a>0$ and downwards if $a<0$.

## Zeros of a quadratic
The zeros of a quadratic are the points at which the function intersects the $x$ axis (i.e. $y=0$). A quadratic has at most two zeros. To determine the number of zeros, we use the *discriminant.*
- $b^{2}<4ac\implies$ no zeros
- $b^{2}-4ac=0\implies$ one zero
- $b^{2}-4ac>0\implies$ two zeros

The zeros to a quadratic are given by the equation $x=\dfrac{-b\pm \sqrt{ b^{2}-4ac }}{2a}$.
![[Pasted image 20241002190724.png|center|400]]

## Max/min of a quadratic
We can derive the maximum and minimum of a quadratic by manipulating the basic equation of a quadratic function.

We know that the standard form of a quadratic is $ax^{2}+bx+c$. Taking $a$ common, we get $a\left[ x^{2}+\dfrac{bx}{a} \right]+c$. *Now lets complete the square in the bracket.* We get $a\left[ x^{2}+\dfrac{bx}{a}+\left( \dfrac{b}{2a} \right)^{2}-\left( \dfrac{b}{2a} \right)^{2} \right]+c$. This gives us $a\left[ x+\left( \dfrac{b}{2a} \right) \right]^{2}-a\left( \dfrac{b}{2a} \right)^{2}+c$. Simplifying the ending, we get $a\left[ x+\left( \dfrac{b}{2a} \right) \right]^{2}-\dfrac{ab^{2}}{4a^{2}}+c$. Canceling the $a$ terms and take LCM for $c$, we get $a\left[ x+\left( \dfrac{b}{2a} \right) \right]^{2}-\dfrac{b^{2}+4ac}{4a}$.

This splits our equation into two clear parts. *Note that the second part has no $x$*, *so its value will remain constant.* Therefore, the min/max value is determined solely by the first part of the equation $a\left[ x+\left( \dfrac{b}{2a} \right) \right]^{2}$. Since we have a squared term that's always positive, the sign depends on the sign of $a$. **The lowest possible value the squared term can take is $0$, and this happens at** $x=\dfrac{-b}{2a}$. Therefore, $f\left( \dfrac{-b}{2a} \right)=\dfrac{-b^{2}+4ac}{4a}=c-\dfrac{b^{2}}{4a}$.
Depending on the sign, this is the min/max value of the quadratic.

Therefore, if $f(x)$ is a quadratic function and if $a>0$, $f(x)$ attains its minimum at $\left( \dfrac{-b}{2a},c-\dfrac{b^{2}}{4a} \right)$. If $a<0$, then $f(x)$ attains its maximum at $\left( \dfrac{-b}{2a},c-\dfrac{b^{2}}{4a} \right)$.