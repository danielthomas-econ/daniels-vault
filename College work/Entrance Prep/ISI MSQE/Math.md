---
color: var(--mk-color-green)
tags:
  - "#isi_msqe"
---
Q1) If $u=\phi(x-y,y-z,z-x)$, find $\dfrac{ \partial u }{ \partial x }+\dfrac{ \partial u }{ \partial y }+\dfrac{ \partial u }{ \partial z }$. $\text{(MSQE PEA 2006 Q2)}$
?
Ans) For simplicity, lets consider $u=\phi(a,b,c)$.
By chain rule,
$\dfrac{ \partial u }{ \partial x }=\dfrac{ \partial \phi }{ \partial a }\times \dfrac{ \partial a }{ \partial x }+\dfrac{ \partial \phi }{ \partial b }\times \dfrac{ \partial b }{ \partial x }+\dfrac{ \partial \phi }{ \partial c }\times \dfrac{ \partial c }{ \partial x }$.
$=\dfrac{ \partial \phi }{ \partial a }(1)+\dfrac{ \partial \phi }{ \partial c }(-1)$.
$=\dfrac{ \partial \phi }{ \partial a }-\dfrac{ \partial \phi }{ \partial c }$
Similarly, $\dfrac{ \partial u }{ \partial y }=\dfrac{ \partial \phi }{ \partial b }-\dfrac{ \partial \phi }{ \partial a }$, $\dfrac{ \partial u }{ \partial z }=\dfrac{ \partial \phi }{ \partial c }-\dfrac{ \partial \phi }{ \partial b }$.
Adding them all up, we get zero.
**When we have functions with inputs like this, remember to apply the chain rule to solve.**
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
