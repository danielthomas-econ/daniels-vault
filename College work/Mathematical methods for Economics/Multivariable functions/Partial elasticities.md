---
color: var(--mk-color-teal)
tags:
  - "#sem2-flashcards/mme/multivariable_functions"
---
Quick access:
- [[#Partial elasticities|Partial elasticities]]
- [[#Elasticities of composite functions|Elasticities of composite functions]]
- [[#Marginal rate of substitution|Marginal rate of substitution]]
- [[#Elasticity of substitution|Elasticity of substitution]]

## Partial elasticities
We know that for regular elasticities, the elasticity of $y$ wrt $x$ can be written as $El_{x}y= \dfrac{x}{y} \times \dfrac{dy}{dx}$. This generalizes to functions of many variables too. If we have $z=f(x_{1},x_{2},\dots,x_{n})$, then *the elasticity of $z$ wrt $x_{i}$ is given by* $El_{x_{i}}z = \dfrac{x_{i}}{z} \times \dfrac{ \partial z }{ \partial x_{i} }$. Just remember we have to differentiate $z$ wrt $x_{i}$ and the other term is in the opposite order, so it becomes $x_{i}$ by $z$. *Alternatively, you can simplify this with logarithms to get* $El_{x_{i}}z = \dfrac{{d \ln z}}{d \ln x_{i}}$.

## Elasticities of composite functions
Just like differentiating composite functions, we must follow the chain rule here too. If we have $z=F(x_{1},x_{2},\dots,x_{n})$ and $x_{i}=f_{i}(t_{1},t_{2},\dots,t_{m})$, $z$ is the main variable, $x$ is the intermediate variable and $t$ is the basic variable.

In this case, elasticity of $z$ wrt $t_{j}$ is $$\begin{align}
El_{t_{j}}z &= \sum\limits_{i=1}^{n}El_{i}F(x_{1},x_{2},\dots,x_{n})El_{j}x_{i} \\
&= \sum\limits_{i=1}^{n}El_{x_{i}}z \times El_{t_{j}}x_{i}
\end{align}$$
In English, **this means we take the elasticity of $z$ wrt $x_{i}$ first, then multiply that with the elasticity of $x_{i}$ wrt $t_{j}$ to get our final result: the elasticity of $z$ wrt** $t_{j}$.

## Marginal rate of substitution
We know that the MRS is the slope of the IC curve, and [[Level curves and geometric representations#^cbbb6c|IC curves are simply level curves.]] We know the slope of a level curve is $\dfrac{{-F_{1}'(x,y)}}{F_{2}'(x,y)}$. Since the IC is downward sloping, *MRS is actually the negative slope* (we consider the absolute value since MRS being negative makes no real world sense). Equating the two and cancelling the negative sign tells us that the MRS of $y$ and $x$ is given by
$$MRS_{yx} = \dfrac{{F_{1}'(x,y)}}{F_{2}'(x,y)}$$
**Keep in mind that $MRS_{yx}\ne MRS_{xy}$ (they're negative reciprocals), so the order is very important here.** If we're taking MRS of y and x, the partial wrt x comes in the numerator.

## Elasticity of substitution
Economically, the elasticity of substitution represents how easy it is to substitute one good for another. Mathematically, the elasticity of substitution between $y$ and $x$ is denoted by
$$\sigma_{yx} = El_{MRS_{yx}}\left( \dfrac{y}{x} \right)$$
We can find this elasticity the same way we find normal elasticities. *I would strong suggest simplifying this with log to get* $\sigma_{yx} = \dfrac{{d\ln\left( \dfrac{y}{x} \right)}}{d \ln MRS_{yx}}$. This is because when you solve for MRS, most of the time you can simplify it in such a way that you get one term in $\dfrac{y}{x}$. **If you take log on both sides and isolate $\ln\left( \dfrac{y}{x} \right)$**, **you'll get $\ln \left( \dfrac{y}{x} \right)$ expressed in terms of $\ln MRS_{yx}$ and maybe some constant term.** This makes it super easy to differentiate wrt $\ln MRS_{yx}$ and solve for $\sigma_{yx}$ using the log method.