---
color: var(--mk-color-teal)
tags:
  - "#sem2-flashcards/mme/multivariable_functions"
---
Quick access:
- [[#Linear approximation|Linear approximation]]
- [[#Differentials|Differentials]]
	- [[#Differentials#Rules for differentials|Rules for differentials]]
	- [[#Differentials#Invariance of the differential|Invariance of the differential]]
- [[#Finding partial derivatives from differentials|Finding partial derivatives from differentials]]

## Linear approximation
A linear approximation of a function through a point is simply the tangent of the function at that point. Recall that the equation for the tangent plane to $z=f(x,y)$ at $(a,b,f(a,b))$ is 
$$z-f(a,b)=f_{1}'(a,b)(x-a)+f_{2}'(a,b)(y-b)$$

Therefore, *the linear approximation of $f(x,y)$ at $(a,b)$ is:*
$$f(x,y)\approx f(a+b)+f_{1}'(a,b)(x-a)+f_{2}'(a,b)(y-b)$$

## Differentials
If our function $z=f(x,y)$ changes by $dx$ and $dy$, then the overall change must be the rate of change of $x$ times the actual change in $x$ (which is $dx$) plus the same for $y$. This approach will give us a linear approximation of the change in the function value. Therefore, *the differential of $z$*, *denoted by $dz$*, *is given by:*
$$dz=f_{1}'(x,y)dx +f_{2}'(x,y)dy$$

If we want the exact change in the value of the function instead of a linear approximation, consider $x \to x+dx$ and $y \to y+dy$. Then **the actual change, called the increment, is given by:**
$$\Delta z = f(x+dx,y+dy)-f(x,y)$$

If $dx$ and $dy$ are really small, then *the increment can be approximated by the differential.* This gives us:
$$\Delta z \approx dz =f_{1}'(x,y)dx +f_{2}'(x,y)dy$$

**All the above formulae can easily be generalized to $n$ variables.**

### Rules for differentials
Differentials are linear transformations, and require the product and quotient rule. Therefore, the rules for differentials are:
$$\begin{align}
d(af+bg) &= adf+bdg \\
d(f \cdot g)  & = gdf + fdg \\
d\left( \dfrac{f}{g} \right) & = \dfrac{{gdf -fdg}}{g^{2}}
\end{align}$$

The *chain rule also applies to differentials.* This means that if $z=g(f(x,y))$, then $dz = g'(f(x,y))df$.

### Invariance of the differential
This is a rule which states that **the form of the differential remains the same whether $x$ and $y$ are free variables or dependent variables.** 

Let us prove this property to get a better understanding of it. Suppose $z=F(x,y),x=f(t,s),y=g(t,s)$. *Although $z$ depends on $x$ and $y$*, *both $x$ and $y$ depend on $t$ and $s$*, *so $z$ itself must depend on both $t$ and $s$*. Then the differential of $z$ wrt $dt$ and $ds$ becomes $dz=z_{t}'dt+z_{s}'ds$. We can expand $z_{t}'$ and $z_{s}'$ to get:
$$\begin{align}
dz&= [F_{x}'(x,y)x_{t}'+F_{y}'(x,y)y_{t}']dt + [F_{x}'(x,y)x_{s}'+F_{y}'(x,y)y_{s}']ds \\
&=F_{x}'(x,y)[x_{t}'+x_{s}'] + F_{y}'(x,y)[y_{t}' + y_{s}'] \\
&=F_{x}'(x,y)dx +F_{y}'(x,y)dy \\
&=z_{x}' dx +z_{y}'dy
\end{align}$$
Clearly, the differential remains of the same form even though $x$ and $y$ are dependent variables.

## Finding partial derivatives from differentials
If we are given a system of equations, we can use differentials to find out the partial derivatives. Suppose we have a system $u^{2} + v=xy$, $uv = -x^{2}+y^{2}$. Finding the differentials gives us another system of differentials. *We can use elimination to reduce the number of variables in the system until it becomes an equation in one variable.* Then it becomes straightforward to isolate the variable and then differentiate partially to find its partial derivative.
![[WhatsApp Image 2025-05-18 at 16.17.55_30358be9.jpg|center|500]]

We can repeat the same steps for $v$ if we eliminate $u$ from the system of equations.