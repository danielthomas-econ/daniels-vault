---
color: var(--mk-color-orange)
tags:
  - sem1-flashcards/math_ge/calc/limits_and_continuity
---
A one sided limit **refers to the value that a function approaches as $x$ approaches a value from either the left or the right side.** Think of a number line; the left side has negative values while the right side has positive values. Similarly, the left hand limit is denoted by $a^-$ while the right hand limit is denoted by $a^+$.

Left hand limits are written as $\lim\limits_{x\to a^-}f(x)$ and right hand limits are written as $\lim\limits_{x\to a^+}f(x)$. LHLs are used when we have values less than $a$, and RHLs are used when our value is greater than $a$.

One-sided limits are *most useful when a function behaves differently on two sides of a point.* For example, step functions, piecewise functions and discontinuities.

Example: $$ f(x) = \begin{cases} 2x + 1 & \text{if } x < 1 \\ x^2 & \text{if } x \geq 1 \end{cases}$$
LHL $(x\to 1^-)$:
When we are on the left side of the function, $x<1$, therefore $f(x)=2x+1$. Substituting $x=1$, we get the limit 3.

RHL $(x\to 1^+)$:
On the right side, $x\ge1$, so $f(x)=x^2$, and substituting gives us the limit as 1.  

## Existence of a limit
If our LHL and RHL are not equal, **the limit does not exist.** The limit may exist at one side of the point given (either $x\to a^-$ or $x\to a^+$), but not at the point itself, *i.e. there will not be a limit at $x\to a$*, which is what our questions usually ask us. Graphically, it looks like this:
![[Pasted image 20240831193120.png]]
