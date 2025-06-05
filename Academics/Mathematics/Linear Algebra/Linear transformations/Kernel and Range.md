---
color: var(--mk-color-orange)
tags:
  - sem2-flashcards/linear_alg/linear_transformations
---
Quick access:
- [[#Kernel of a LT|Kernel of a LT]]
- [[#Range of a LT|Range of a LT]]
- [[#Viewed as columns of a matrix|Viewed as columns of a matrix]]
- [[#The dimension theorem|The dimension theorem]]
- [[#Flashcards|Flashcards]]

## Kernel of a LT
Let $T: V\to W$ be a linear transformation. The kernel of $T$, denoted by $\text{Ker }T$, is defined as $\text{Ker } T=\{v \in V: T(v)=0\}$. *It is the set of all elements in the domain that make the function equal to zero.* The dimension of the kernel is also called the *nullity* of the transformation.

Note:
i) $\text{Ker }T$ is a subset of $V$.
ii) $\text{Ker } T \ne \phi\:(\because T(0_{v})=0_{w} \text{ by properties of LT})$
iii) $\text{Ker } T$ is a subspace of $V$.

## Range of a LT
Let $T:V \to W$ be a linear transformation. Then $\text{Range } T$ is defined as $\{T(v):v \in V\}$. It is the set of all outputs of the function.

Note:
i) $\text{Range } T$ is a subset of $W$
ii) $\text{Range } T \ne \phi$ ($\because V$ is a vector space, so $V \ne \phi$)
iii) $\text{Range } T$ is a subspace of $W$

Eg: Find the kernel and range of $T:\mathbb{R}^{3} \to \mathbb{R}^{3}, T([x,y,z]) =[0,y,0]$. Also find the dimension of both kernel and range.
?
Ans) By definition, $\text{Ker } T=\{v \in V: T(v)=0\}$
$= \{v \in V: [0,y,0]= [0,0,0]\}$
$=\{[x,y,z]:y=0\}$
$=\{[x,0,z]: x,z \in \mathbb{R}\}$
$=\{x[1,0,0]+z[0,0,1]: x,z \in \mathbb{R}\}$
$=\text{span}(\{[1,0,0], [0,0,1]\})$
$\implies \text{dim }\text{Ker }T=2$ as it is a basis of $\text{Ker } T$ (spans $\text{Ker } T$ and is LI)
.
$\text{Range } T=\{T(v): v \in V\}$
$=\{[0,y,0]:y \in \mathbb{R}\}$
$=\{y[0,1,0]:y \in \mathbb{R}\}$
$=\text{span}(\{[0,1,0]\})$
$\implies \text{dim } \text{Range } T=1$ as it is a basis of $\text{Range } T$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

## Viewed as columns of a matrix
Suppose $T$ is a LT, $T: \mathbb{R}^{n}\to \mathbb{R}^m$ s.t. $T(x)=Ax$, where $A$ is the matrix of the LT. 

**i) Kernel:**
$\text{Ker } T=\{x \in \mathbb{R}^{n}: T(x)=0\}$
$=\{x \in \mathbb{R}^{n}: Ax=0\}$
$\therefore$ $\text{Ker } T$ is the solution set of $Ax=0$.
We know the *number of vectors that span the solution set is the same as the number of free variables in an echelon form,* which is the same as the number of non-pivot columns in an echelon form of $A$. Therefore, we can say
$$\text{dim } \text{Ker } T=\text{no. of non-pivot columns in an echleon form of A}$$

**ii) Range:**
$\text{Range }T=\{T(x):x \in \mathbb{R}^n\}$
$=\{Ax: x \in \mathbb{R}^n\}$
$=\{x_{1}a_{1}+x_{2}a_{2}+\dots+x_{n}a_{n}: x = \left[\begin{smallmatrix}x_{1} \\ x_{2} \\ \dots \\ x_{n} \end{smallmatrix}\right], A=[a_{1},a_{2},\dots,a_{n}]\}$ ($a_{i}$ are the columns of the matrix $A$).
$=\text{span}(\{a_{1},a_{2},\dots,a_{n}\})$
$=\text{span}(\{\text{linearly independent }a_{i}\})$ ($\because$ LD vectors don't add to span)
Since the linearly independent columns of $A$ correspond to its pivot columns, we can say
$$\text{dim }\text{Range }T=\text{no. of pivot columns in an echelon form of A}$$
This is why $\text{Range }T$ is *equal to $\text{rank}(A)$*.

## The dimension theorem
Let $T: V\to W$ be a LT and $V$ be a fdvs. Then,
$$\text{dim V = dim Ker T + dim Range T}$$

This follows directly from viewing the kernel and range as non-pivot and pivot columns of a matrix. If $\text{dim } \text{Ker }$equals the dimension of the non-pivot columns and $\text{dim }\text{Range }$equals the dimension of the pivot columns, their sum will be the dimension of all columns of the matrix, which is the dimension of the domain (no. of columns = $\text{dim }$domain, no. of rows = $\text{dim }$codomain).





## Flashcards
Q1) Prove that $\text{Ker } T$ is a subspace of the domain $V$.
?
Ans) Since $0 \in \text{Ker } T$, $\text{Ker } T \ne \phi$. 
Let $u,v \in \text{Ker }T$ be arbitrary $\implies T(u) = T(v)=0$
$T(u+v)=T(u)+T(v)$
$=0+0$
$=0$
$\therefore T(u+v) \in \text{Ker } T$.
For $c \in \mathbb{R}$,
$T(cu)=cT(u)$
$=c(0)$
$=0$
$\therefore T(cu) \in \text{Ker } T$.
Therefore, $\text{Ker } T$ is a subspace of $V$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Prove that $\text{Range } T$ is a subspace of the codomain $W$.
?
Ans) Since $T(0_{v})=0_{w}$, $\text{Range } T\ne \phi$
Let $w_{1},w_{2} \in \text{Range } T$ be arbitrary.
$\implies \exists\: v_{1},v_{2} \in V$ s.t. $T(v_{1})=w_{1}, T(v_{2})=w_{2}$.
Since $v_{1},v_{2} \in V$, $v_{1}+v_{2} \in V$ ($\because V$ is a vector space)
$\implies T(v_{1}+v_{2})\in \text{Range } T$
$\implies T(v_{1})+T(v_{2}) \in \text{Range } T$ ($\because T$ is a LT)
$\implies w_{1}+w_{2} \in \text{Range } T\: \forall\:w_{1},w_{2} \in \text{Range } T$
.
For $c  \in \mathbb{R}$, $v_{1} \in V$,
$cv_{1} \in V$ ($\because V$ is a vector space)
$\implies T(cv_{1}) \in \text{Range } T$
$\implies cT(v_{1}) \in \text{Range } T$ ($\because T$ is a LT)
$\implies cw_{1} \in \text{Range } T$.
Therefore, $\text{Range } T$ is a subspace of $W$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q3) Find the kernel and range and their dimensions for the LT $T: \mathbb{R}^{2} \to \mathbb{R}^{2},$ $T\left(\left[\begin{matrix}x \\ y \end{matrix}\right]\right)=\begin{bmatrix}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{bmatrix}\left[\begin{matrix}x \\ y \end{matrix}\right]$ for a fixed $\theta$.
?
Ans) $\text{Ker } T=\left\{\begin{bmatrix}x \\ y\end{bmatrix} \in \mathbb{R}^{2} : \begin{bmatrix}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{bmatrix}\begin{bmatrix}x \\ y\end{bmatrix}=0\right\}$
$\begin{vmatrix}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{vmatrix}=\cos ^{2} \theta + \sin ^{2} \theta=1$
Since $\det \ne 0$, $A^{-1}$ exists. 
We know $AX=0$
$\implies(A^{-1}A)X=A^{-1}(0)$
$\implies X=0$
$\implies X=0$ is the only solution.
$\therefore \text{Ker } T=\left\{\begin{bmatrix}0 \\ 0 \end{bmatrix}\right\}$ 
$\implies \text{dim } \text{Ker } T=0$ (basis of trivial vs is $\phi \implies \text{dim } =0$)
.
$\text{Range } T=\{T(v):v \in V\}$
$=\left\{\begin{bmatrix}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}\begin{bmatrix}x \\ y\end{bmatrix}:\begin{bmatrix}x \\ y\end{bmatrix} \in \mathbb{R}^{2}\right\}$
$=\left\{x\begin{bmatrix} \cos \theta \\ \sin \theta \end{bmatrix} + y\begin{bmatrix}-\sin \theta \\ \cos \theta\end{bmatrix}:x,y \in \mathbb{R}\right\}$
$=\text{span}\left(\left\{\begin{bmatrix}\cos \theta \\ \sin \theta \end{bmatrix}, \begin{bmatrix}-\sin \theta \\ \cos \theta\end{bmatrix}\right\}\right)$ - *1*
**If we can show this is a basis of $\text{Range } T$**, **we can say range has a dimension of two.** We have already shown it spans $\text{Range } T$, now we have to prove they are LI.
Consider $c_{1}\begin{bmatrix}\cos \theta \\ \sin \theta\end{bmatrix} + c_{2} \begin{bmatrix}-\sin \theta \\ \cos \theta\end{bmatrix}=0$
$\implies \begin{bmatrix}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta\end{bmatrix}\begin{bmatrix}c_{1} \\ c_{2}\end{bmatrix}=0$
Since determinant of the matrix is 1, the system must have a unique solution. Since the system is homogenous, that unique solution is $\begin{bmatrix}0 \\ 0\end{bmatrix}$. Therefore, $\begin{bmatrix} c_{1} \\ c_{2}\end{bmatrix}=\begin{bmatrix}0 \\ 0\end{bmatrix} \implies$ they are LI. 
Therefore, *1* is a basis of $\text{Range } T$, so $\text{dim }\text{Range }T=2$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q4) Let $A$ be any matrix. Prove $\text{rank}(A)=\text{rank}(A^T)$.
?
Ans) Let $A$ be a $m\times n$ matrix. 
Let us define a LT $T:\mathbb{R}^n\to \mathbb{R}^m$, $T(x)=Ax$. Therefore, $A$ is the matrix of $T$.
We know $\text{dim }\text{Range }T=$ number of LI columns = $\text{rank}(A)$ - *1*
$\text{Range }T=\{T(x):x \in \mathbb{R}^n\}$
$=\{Ax: x \in \mathbb{R}^n\}$
$=\left\{x_{1}a_{1}+x_{2}a_{2}+\dots+x_{n}a_{n}: x = \left[\begin{smallmatrix}x_{1} \\ x_{2} \\ \dots \\ x_{n} \end{smallmatrix}\right], A=[a_{1},a_{2},\dots,a_{n}]\right\}$
$=\text{span}(\{a_{1},a_{2},\dots,a_{n}\})$
$=\text{span}(\text{LI columns of }A)$ ($\because$ LD columns don't change span)
$=\text{span}(\text{LI rows of }A^T)$
$\therefore$ $\text{dim }\text{Range }T=\text{dim}(\text{span}(\text{LI rows of }A^T))$
$=\text{rank}(A^T)$ - *2*
From *1 and 2,* we get $\text{rank}(A)=\text{rank}(A^T)$.
Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q5) Let $L:\mathbb{R}^{n}\to \mathbb{R}$ be any non-zero LT. Find $\text{dim }\text{Ker }L$.
?
Ans) We know that $\text{Range }L \subseteq \mathbb{R}$ by definition. Therefore, $\text{dim }\text{Range }L \leq \text{dim }\mathbb{R}=1$. **However, if $\text{dim }\text{Range }L=0$, then $L$ is the zero LT as all the elements of $\mathbb{R}^n$ will go to zero.** We are told $L$ is not the zero LT. $\therefore$ $\text{dim }\text{Range }L=1$.
From the dimension theorem, $\text{dim }\mathbb{R}^{n}= \text{dim }\text{Ker }L+\text{dim }\text{Range }L$
$\implies n=\text{dim }\text{Ker }L+1$
$\implies \text{dim }\text{Ker }L=n-1$
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
