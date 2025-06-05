---
color: var(--mk-color-teal)
tags:
  - "#sem2-flashcards/mme/multivariable_functions"
---
Quick access:
- [[#Expressing in matrix form|Expressing in matrix form]]
- [[#Definiteness of a quadratic form|Definiteness of a quadratic form]]
	- [[#Definiteness of a quadratic form#Quadratic forms with linear constraints|Quadratic forms with linear constraints]]
- [[#Quadratic forms in many variables|Quadratic forms in many variables]]
- [[#Definiteness of a quadratic form in many variables|Definiteness of a quadratic form in many variables]]
	- [[#Definiteness of a quadratic form in many variables#Using eigenvalues|Using eigenvalues]]
	- [[#Definiteness of a quadratic form in many variables#Using principal minors|Using principal minors]]


## Expressing in matrix form
A quadratic form of a function in two variables is $f(x,y)=ax^{2}+2bxy+cy^{2}$. Writing this in matrix notation, we get $f(x,y)=[x,y] \begin{bmatrix}a & b \\ b & c\end{bmatrix} \begin{bmatrix}x \\ y\end{bmatrix}$. By obtaining the second partials, we can see that *the [[Partial derivatives with many variables#Hessian matrix|Hessian]] of the quadratic form is* $2\begin{bmatrix}a & b \\ b & c\end{bmatrix}$.

## Definiteness of a quadratic form
The quadratic form $f(x,y)=ax^{2} + 2bxy + cy^{2}$ is stb *positive definite* if $f(x,y)>0$ for all $(x,y)\ne (0,0)$. Replace this with a weak inequality for positive semidefinite. Flip the inequality for negative (semi)definite. It is stb *indefinite* when the function is positive for some values of $(x,y)$ and negative for other values of $(x,y)$.

Expressing this condition in terms of the matrix equation shows us **the definiteness of the function depends entirely on the coefficients $a,b$ and $c$**.
![[WhatsApp Image 2025-05-30 at 12.59.04_80fe2240.jpg]]
**We consider the sign of the determinant [[Partial derivatives with many variables#Hessian matrix|Hessian]]** $2\begin{bmatrix}a & b \\ b & c\end{bmatrix}$, but the $2$ doesn't change the inequalities in any way, so we only consider $\begin{bmatrix}a & b \\ b & c\end{bmatrix}$.

If the determinant of the Hessian is negative, we know the function is indefinite. *Positive/Negative (semi)definiteness depends non the sign of $a$ and $c$ when the determinant of the Hessian is positive.* The conditions are quite straightforward: positive definite means $a,c >0$. Semidefinite means weak inequality. Negative definite means $a,c < 0$.

### Quadratic forms with linear constraints
If we have a quadratic form $Q=ax^{2}+2bxy+cy^{2}$ with its variables **subject to the constraint $px+qy=0$**, then we can say that this function is positive definite iff
$$-\begin{vmatrix}
0 & p & q \\
p & a & b \\
q & b & c
\end{vmatrix} >0$$
Change the inequality to get different forms of definiteness. Note that *this is in the same form as a [[Quasi concavity and convexity#Bordered Hessian matrix|bordered Hessian matrix.]]* You have the Hessian (or half the Hessian) surrounded by the first order partials of the constraints, with zero in the corner. This is an easy way to remember this formula.

## Quadratic forms in many variables
The general quadratic form of a function in $n$ variables is given by the double sum $$\begin{align}
Q &= \sum\limits_{i=1}^n
 \sum \limits_{j=1}^{n} a_{ij}x_{i}x_{j} \\
&=a_{11}x_{1}^{2}+a_{12}x_{1}x_{2}+\dots+a_{ij}x_{i}x_{j}+\dots+a_{nn}x_{n}^{2}\end{align}$$
If we have $x= \begin{bmatrix}x_{1} \\ x_{2} \\ \dots \\ x_{n}\end{bmatrix}$ and $A=\begin{bmatrix}a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \dots \\ a_{n 1} & a_{n 2} & \dots & a_{nn}\end{bmatrix}$, then we can express the quadratic form as $Q=x'Ax$.

Since multiplication is commutative, $x_{i}x_{j}=x_{j}x_{i}$. Therefore, $a_{ij}x_{i}x_{j}+a_{ji}x_{j}x_{i}=(a_{ij}+a_{ji})x_{i}x_{j}$. **If we replace $a_{ij}$ and $a_{ji}$ by $\dfrac{1}{2}(a_{ij}+a_{ji})$**, **we can turn $A$ into a symmetric matrix without changing $Q$**. Therefore, when you have a quadratic form in many variables, *replace $a_{ij}$ and $a_{ji}$ by their average and then proceed. It makes the next steps a lot easier.* 

## Definiteness of a quadratic form in many variables
Just like the two variable case where the function value was greater than zero for all $(x,y)\ne 0$ for positive definite, here we need $Q(x_{1},x_{2}\dots,x_{n})=x'Ax > 0$ $\forall$ $(x_{1},x_{2},\dots,x_{n}) \ne (0,0,\dots,0)$. 

### Using eigenvalues
**It becomes a lot easier to check for definiteness using [[Eigenvalues and eigenvectors#Concept|eigenvalues]] if we have a symmetric matrix.** Therefore, first convert $A$ to a symmetric matrix and then apply the condition:
![[WhatsApp Image 2025-05-30 at 13.40.24_ae2f8a4b.jpg]]

### Using principal minors
Alternatively, we can check certain minors, called leading principal minors, to determine definiteness. If $A$ is a matrix of order $n$, then the *leading principal minors of $A$ are determinants obtained by crossing out the last $n-k$ rows and columns.* We can denote this mathematically as $D_{k}=\begin{vmatrix}a_{11} & a_{12}  &  \dots & a_{1k} \\ a_{21} & a_{22} & \dots & a_{2k} \\ \dots \\ a_{k_{1}} & a_{k_{2}} & \dots & a_{kk}\end{vmatrix}$, $k=1,\dots,n$. It's called **leading** principal minors because we remove the **last** $n-k$ rows to get this minor.

If $A$ is a symmetric matrix with leading principal minors $D_{k}$ (with $k=1,\dots,n$), then$$\begin{align}
A \text{ is positive definite } & \iff D_{k} >0 \:\forall\:k=1,\dots,n \\
A \text{ is negative definite } & \iff (-1)^{k}D_{k} > 0 \: \forall \: k=1,\dots,n
\end{align}$$
**Note that the semidefinite case is not simply using a weak inequality here.** To check for semidefiniteness, we must *consider all principal minors,* which are just some arbitrary minor of order $(n-r) \times (n-r)$. This means we don't have to necessarily cross out the last $n$ rows, *we can remove any $n$ rows.* The matrix is positive semidefinite if all the principal minors are $\geq 0$. It is **negative semidefinite if all the principal minors of order $k$ have the same sign as $(-1)^{k}$**.  ^b3a207