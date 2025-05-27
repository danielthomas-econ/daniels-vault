---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Solving implicit partial derivatives follows a very similar process to [[Implicit differentiation|regular implicit differentiation.]] If we have $z(x,y)$ and $z$ is in our equation, lets take $xz$ for example, *then we must use the product rule.* $xz=\dfrac{ \partial x }{ \partial x }z+x \dfrac{ \partial z }{ \partial x }=z+x\dfrac{ \partial z }{ \partial x }$.

Eg: Find $f_{x}$ of $x^{2}y+xz+yz^{2}=8$.
?
Ans) Take the partial derivative on both sides.
$\dfrac{ \partial [x^{2}y+xz+yz^{2}] }{ \partial x }=\dfrac{ \partial \:8 }{ \partial x }$. This gives $2xy+\dfrac{ \partial x }{ \partial x }z+x \dfrac{ \partial z }{ \partial x }+y\cdot 2z \dfrac{ \partial z }{ \partial x }=0$. Taking common factors out, we have $\dfrac{ \partial z }{ \partial x }[x+2zy]=-(2xy+z)$. Therefore, $f_{x}=\dfrac{{-(2xy+z)}}{x+2yz}$.
<!--SR:!2025-01-08,4,274-->




## Flashcards
Q1) If $x^x+y^y+z^z=c$, show that $\dfrac{ \partial z^{2} }{ \partial x\partial y }= -(x\log ex)^{-1}$ at $x=y=z$.
?
Ans) We must first notice that this is an implicit expression we are given here, *so we must treat $z$ as a function of $x$ and $y$*. **Also, reading the Leibniz notation tells us that we should differentiate wrt $y$ first.** To simplify the equation, lets take $\log$ on both sides. This gives us $x\log x+y\log y+z\log z=\log c$. Differentiating partially wrt $y$ gives $\log y+1+z_{y}\log z+z\cdot \dfrac{1}{z}\cdot z_{y}=0$ (we treat $z$ as implicit). Therefore, $z_{y}=\dfrac{-(\log y+1)}{(\log z+1)}$. Since the function is symmetric, we also have $z_{x}=\dfrac{{-(\log x+1)}}{(\log z+1)}$.
-
Differentiating $z_{y}$ wrt x gives $z_{yx}=\dfrac{{0\times(\log z+1)+(\log y+1)\left( \dfrac{1}{z} \cdot z_{x}\right)}}{(\log z+1)^{2}}$. Simplify and sub $z_{x}$, we have $z_{yx}=\dfrac{{(\log y+1)(-(\log x+1))}}{z(\log z+1)^{3}}$. Substitute the condition $x=y=z$, we have $z_{yx}=\dfrac{{-(\log x+1)^{2}}}{x(\log x+1)^{3}}$. Cancelling powers gives $z_{yx}=-(x(\log x+1))^{-1}$. **We can rewrite $1$ as $\log e$ and then we know $\log e+\log x=\log ex$**. Therefore, $z_{yx}=-(x\log ex)^{-1}$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,274-->

Q2) If $V=r^m$, where $r^{2}=x^{2}+y^{2}+z^{2}$, show that $\dfrac{ \partial V }{ \partial x^{2} }+\dfrac{ \partial V }{ \partial y^{2} }+\dfrac{ \partial V }{ \partial z^{2} }=m(m+1)r^{m-2}$.
?
Ans) $r=(x^{2}+y^{2}+z^{2})^{\frac{1}{2}}$. Therefore, $V=(x^{2}+y^{2}+z^{2})^{\frac{m}{2}}$. Differentiating wrt x, $\dfrac{ \partial V }{ \partial x }=\dfrac{m}{2}(x^{2}+y^{2}+z^{2})^{\frac{m-2}{2}}\times2x$. Therefore, $\dfrac{ \partial V }{ \partial x }=mx(x^{2}+y^{2}+z^{2})^{\frac{m-2}{2}}=mxr^{m-2}$.
.
Differentiate again wrt x,
$\dfrac{ \partial V }{ \partial x^{2} }=m\left( r^{m-2}+x(m-2)r^{m-3}\times \dfrac{ \partial r }{ \partial x } \right)$ **don't forget to take** $\dfrac{ \partial r }{ \partial x }$, which we know is $\dfrac{x}{r}$ here. Substituting, we get $\dfrac{ \partial V }{ \partial x^{2} }=m(r^{m-2}+x^{2}(m-2)r^{m-4})$. Since $r$ is symmetric, it'll be the same for $y$ and $z$.
.
Therefore, $\dfrac{ \partial V }{ \partial x^{2} }+\dfrac{ \partial V }{ \partial y^{2} }+\dfrac{ \partial V }{ \partial z^{2} }$$=3mr^{m-2}+mx^{2}(m-2)r^{m-4}+my^{2}(m-2)r^{m-4}+mz^{2}(m-2)r^{m-4}$
$=m(3r^{m-2}+(x^{2}+y^{2}+z^{2})(m-2)r^{m-4})$. **Take $r^{m-2}$ common.** This makes $r^{m-4}=r^{m-4-(m-2)}=r^{-2}$. Also sub $(x^{2}+y^{2}+z^{2})=r^2$. Therefore, we get $mr^{m-2}(3+r^{2}\times r^{-2}\times(m-2))$. **The $r$ terms cancel out,** leaving us with $mr^{m-2}(3+m-2)$, giving us our final answer $m(m+1)r^{m-2}$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,270-->

Q3) If $u=\dfrac{1}{\sqrt{ x^{2}+y^{2}+z^{2} }}$, prove that $\dfrac{ \partial u^{2} }{ \partial x^{2} }+\dfrac{ \partial u^{2} }{ \partial y^{2} }+\dfrac{ \partial u^{2} }{ \partial z^{2} }=0$.
?
Ans) $u=(x^{2}+y^{2}+z^{2})^{-1/2}$
$\dfrac{ \partial u }{ \partial x }=-\dfrac{1}{2}(x^{2}+y^{2}+z^{2})^{\frac{-3}{2}}\cdot 2x=-x(x^{2}+y^{2}+z^{2})^{-3/2}$.
$\dfrac{ \partial u^{2} }{ \partial x^{2} }=-(x^{2}+y^{2}+z^{2})^{-3/2}-x\left( -\dfrac{3}{2} \right)(x^{2}+y^{2}+z^{2})^{\frac{-5}{2}}\cdot2x$
$=3x^{2}(x^{2}+y^{2}+z^{2})^\frac{-5}{2}-(x^{2}+y^{2}+z^{2})^{-3/2}$
Similarly for $\dfrac{ \partial u^{2} }{ \partial y^{2} }$ and $\dfrac{ \partial u^{2} }{ \partial z^{2} }$. Adding all of them together,
$\dfrac{ \partial u^{2} }{ \partial x^{2} }+\dfrac{ \partial u^{2} }{ \partial y^{2} }+\dfrac{ \partial u^{2} }{ \partial z^{2} }=3(x^{2}+y^{2}+z^{2})^{-5/2}[x^{2}+y^{2}+z^{2}]-3(x^{2}+y^{2}+z^{2})^{-3/2}$
$=3(x^{2}+y^{2}+z^{2})^{-3/2}-3(x^{2}+y^{2}+z^{2})^{-3/2}=0$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,270-->

