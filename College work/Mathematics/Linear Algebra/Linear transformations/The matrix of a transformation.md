---
color: var(--mk-color-orange)
tags:
  - sem2-flashcards/linear_alg/linear_transformations
---
Quick access:
- [[#The matrix|The matrix]]

## The matrix
Let $V,W$ be $n,m$ dim vector spaces. Let $B=\{v_{1},v_{2},\dots,v_{n}\}$$, $C=\{w_{1},w_{2},\dots,w_{n}\}$ be ordered bases of $V$ and $W$. Let $L:V\to W$ be a LT. Then, $\exists$ a unique matrix $A$ of order $m\times n$ (order of codomain $\times$ order of domain) s.t. $[L(v)]_{C}=A[v]_{B}$. *The columns of $A$ is the coordinate vector of $L(v_{i})$ wrt $C$*, *so each column is $[L(v_{i})]_{C}$*.

If the vector spaces are $\mathbb{R}^n$ and $\mathbb{R}^m$ and the bases are standard ordered basis, then $L(v_{i})=Av$.

Eg: Let $\mathbb{P}_{3}\to \mathbb{R}^{3}$ be a LT defined as $L(a_{3}x^{3}+a_{2}x^{2}+a_{1}x+a_{0})$$=[a_{0}+a_{1}, 2a_{2}, a_{3}-a_{0}]$. Find the matrix $A$ of $L$ wrt bases $B=\{x^{3}+x^{2},x^{2}+x,x+1,1\}$ and $C=\{[-2,1,3],[1,-3,0],[3,-6,2]\}$.
?
Ans) *We start by finding $L(v_{i})$*, *so we should apply the LT to each element of the basis $B$ (basis of the domain).*
$L(x^{3}+x^{2})=[0,2,1]$
$L(x^{2}+x)=[1,2,0]$
$L(x+1)=[2,0,-1]$
$L(1)=[1,0,-1]$
.
If $B$ and $C$ were standard bases, then we already have our coordinate vectors and we can simply put them as columns of the matrix $A$. However, since they are non standard, **we must express the above 4 vectors as a LC of elements of $C$**. Therefore, $[0,2,1]=a_{1}[-2,1,-3] + a_{2}[1,-3,0]+a_{3}[3,-6,2]$ and so on for all 4 vectors. We'll now solve the above systems.
$\left[\begin{array}{ccc|c|c|c|c} -2 & 1 & 3 & 0 & 1 & 2 & 1 \\ 1 & -3 & -6 & 2 & 2 & 0 & 0 \\ -3 & 0 & 2 & 1 & 0 & -1 & -1 \end{array}\right]$
Note that the *coefficient matrix must reduce to an identity here. Also, since $C$ is a basis, this system will always have only one solution.*
Reducing the matrix gives us $\left[\begin{array}{ccc|c|c|c|c} 1 & 0 & 0 & -1 & -10 & -15 & -9 \\ 0 & 1 & 0 & 1 & 26 & 41 & 25 \\ 0 & 0 & 1 & -1 & -15 & -23 & -14 \end{array}\right]$.
The augmented columns are the scalars used to make the linear combination, and hence each column corresponds to the [[Basis and dimension#Coordinate vectors|coordinate vector]] of the respective matrix (recall that putting the scalars used to make the LC in a vector gives the coordinate vector). Therefore, *the augmented columns form our required matrix $A$*.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

