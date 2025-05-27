---
color: var(--mk-color-orange)
tags:
  - sem2-flashcards/linear_alg/linear_transformations
---
Quick access:
- [[#Definition|Definition]]
- [[#Linear operators|Linear operators]]
	- [[#Linear operators#Types of linear operators|Types of linear operators]]
- [[#Flashcards|Flashcards]]


## Definition
Let $V,W$ be vector spaces and $f:V\to W$ be a function. Then $f$ is a linear transformation if:
i) $f(u+v)=f(u)+f(v)\:\forall\: u,v \in V$ *(additivity)*
ii) $f(cu)=cf(u)\:\forall\:c\in \mathbb{R},u \in V$ *(scalar multiplication)* 

Note that these are the same [[Linear functions#Properties of linear functions|properties]] that a linear function has, which is why such transformations are called linear.

Eg: $f: M_{m\times n}\to M_{n\times m}$ s.t. $f(A)=A^T$.
Proof: Let $u,v \in M_{m\times n}$ and $c\in \mathbb{R}$ be arbitrary.
$f(u+v)=u^{T}+v^{T}=f(u)+f(v)$
$f(cu)=(cu)^T=cu^T=cf(u)$
Therefore, $f(A)=A^T$ is a linear transformation

## Properties of a linear transformation
Let $L:V\to W$ be a LT. Then,

i) $L(0_{v})=0_{w}$ *(zero always goes to zero)*

Proof: $L(0_{v})=L(0\times0_{v})$ ($0x=0_{v}\forall\:x \in V$)
$=0L(0_{v})$ ($\because$ $L$ is a LT)
$=0_{w}$ ($\because L(0_{v})\in W$, zero times an element in $W$ gives $0_{w}$)

ii) $L(-v)=-L(v)$

iii) $L(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n})=c_{1}L(v_{1})+c_{2}L(v_{2})+\dots c_{n}L(v_{n})$ for $v_{1},v_{2},\dots,v_{n} \in V$, $c_{1},c_{2},\dots c_{n}\in \mathbb{R}$

Proof: We'll prove the result **using mathematical induction** on $n$.
For $n=2$:
$L(c_{1}v_{1}+c_{2}v_{2})=L(c_{1}v_{1})+L(c_{2}v_{2})$ ($\because L$ is a LT)
$=c_{1}L(v_{1})+c_{2}L(v_{2})$ ($\because$ L is a LT)
$\therefore$ the result holds true for $n=2$

Suppose it is true for $n=k$.
$\therefore$ $L(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{k}v_{k})=c_{1}L(v_{1})+c_{2}L(v_{2})+\dots+c_{k}L(v_{k})$.

Consider $n=k+1$
$L(c_{1}v_{1}+c_{2}v_{2}+\dots c_{k}v_{k}+c_{k+1}v_{k+1})=L(c_{1}v_{1}+c_{2}v_{2}\dots+c_{k}v_{k})+L(c_{k+1}v_{k+1})$  ($\because L$ is a LT)
$=c_{1}L(v_{1})+c_{2}L(v_{2})+\dots c_{k}L(v_{k})+c_{k+1}L(v_{k+1})$ ($\because$ inductive hypothesis)
Therefore, the result holds true for $n=k+1$
Hence proved by mathematical induction.



## Linear operators
**A linear transformation from a vector space to itself is called a linear operator.** 

### Types of linear operators
i)Identity linear operator
$f:V\to V \:\text{s.t. } f(v)=v$

ii) Zero linear operator
$f: V\to V \text{ s.t. } f(v)=0$

iii) Reflection
$f:\mathbb{R}^{2}\to \mathbb{R}^{2} \text{ s.t. } f([x,y])=[x,-y]$ (reflection through $x$ axis)
$f([x,y,z])=[x,y,-z]$ would be reflection about $xy$ plane

iv) Projection
$f: \mathbb{R}^{3}\to \mathbb{R}^{3}\text{ s.t. }f([x,y,z])=[x,y,0]$ (projection to the $xy$ plane)

v) Contraction/dilation
$f: \mathbb{R}^{2}\to \mathbb{R}^{2} \text{ s.t. }f(u)=ku, k\in \mathbb{R}$ (contraction if $|k| <1$, i.e. vector shrinks)

vi) Rotation
$f:\mathbb{R}^{2}\to \mathbb{R}^{2}\text{ s.t. }f(\left[\begin{smallmatrix}x \\ y \end{smallmatrix}\right])=\left[\begin{matrix}x\cos \theta-y\sin \theta \\ x\sin \theta+y\cos \theta \end{matrix}\right]$ (rotates by $\theta$ anticlockwise)





## Flashcards
Q1) Let $V$ be a n-dimensional vector space and $B$ be an ordered basis of $V$. Then, show that $f:V\to \mathbb{R}^n$ s.t. $f(v)=[v]_{B}$ is a LT.
?
Ans) Let $B=\{v_{1},v_{2}\dots,v_{n}\}$ and $u,v\in V$ be arbitrary
Since $B$ is a basis of $V$, $u,v$ can be *uniquely* expressed as a LC of elements of $B$. Let:
$u=c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}, \:c_{i}\in \mathbb{R}$
$v=d_{1}v_{1}+d_{2}v_{2}+\dots+d_{n}v_{n},\: d_{i}\in \mathbb{R}$
.
$f(u+v)=f(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}+d_{1}v_{1}+\dots+d_{n}v_{n})$
$=f((c_{1}+d_{1})v_{1}+(c_{2}+d_{2})v_{2}+\dots+(c_{n}+d_{n})v_{n})$
$=\left[\begin{smallmatrix}c_{1}+d_{1} \\ c_{2}+d_{2} \\ \dots \\ c_{n}+d_{n} \end{smallmatrix}\right]\: \text{(coordinate vectors take the coefficients of v)}$
$=\left[\begin{smallmatrix}c_{1} \\ c_{2} \\ \dots \\ c_{n} \end{smallmatrix}\right]+\left[\begin{smallmatrix}d_{1} \\ d_{2} \\ \dots \\ d_{n} \end{smallmatrix}\right]$
$=f(u)+f(v)$
.
Let $k \in \mathbb{R}$ be arbitrary.
$f(ku)=f(kc_{1}u_{1}+kc_{2}u_{2}+\dots kc_{n}v_{n})$
$=\left[\begin{smallmatrix}kc_{1} \\ kc_{2} \\ \dots \\ kc_{n} \end{smallmatrix}\right]$
$=k\left[\begin{smallmatrix}c_{1} \\ c_{2} \\ \dots \\ c_{n} \end{smallmatrix}\right]$
$=kf(u)$
.
Therefore, $f$ is a linear transformation as it satisfies both properties.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Let $f:\mathbb{R}^{2}\to \mathbb{R}^{2}$ be a LT s.t. $f([1,1])=[5,2]$ and $f([2,1])=[3,9]$. Find $f([-1,1])$.
?
Ans) Since $[1,1]$ and $[2,1]$ are LI, they form a basis of $\mathbb{R}^{2}$
$\implies \exists \:c_{1},c_{2} \in \mathbb{R} \text{ s.t. }[-1,1]=c_{1}[1,1]+c_{2}[2,1]$
$\implies c_{1}+2c_{2}=-1,c_{1}+c_{2}=1$
$\implies c_{1}=3,c_{2}=-2$
Therefore, $[-1,1]=3[1,1]-2[2,1]$. This means that $f([-1,1])=f(3[1,1]-2[2,1])$
$=3f[1,1]-2f[2,1]$
$=3[5,2]-2[3,9]$
$=[9,-12]$
Therefore, $f([-1,1])=[9,-12]$
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q3) Prove $L(0_{v})=0_{w}$ *(zero always goes to zero)*
?
Proof: $L(0_{v})=L(0\times0_{v})$ ($0x=0_{v}\forall\:x \in V$)
$=0L(0_{v})$ ($\because$ $L$ is a LT)
$=0_{w}$ ($\because L(0_{v})\in W$, zero times an element in $W$ gives $0_{w}$)
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q4)Prove $L(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n})=c_{1}L(v_{1})+c_{2}L(v_{2})+\dots c_{n}L(v_{n})$ for $v_{1},v_{2},\dots,v_{n} \in V$, $c_{1},c_{2},\dots c_{n}\in \mathbb{R}$
?
Proof: We'll prove the result **using mathematical induction** on $n$.
For $n=2$:
$L(c_{1}v_{1}+c_{2}v_{2})=L(c_{1}v_{1})+L(c_{2}v_{2})$ ($\because L$ is a LT)
$=c_{1}L(v_{1})+c_{2}L(v_{2})$ ($\because$ L is a LT)
$\therefore$ the result holds true for $n=2$
.
Suppose it is true for $n=k$.
$\therefore$ $L(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{k}v_{k})=c_{1}L(v_{1})+c_{2}L(v_{2})+\dots+c_{k}L(v_{k})$.
.
Consider $n=k+1$
$L(c_{1}v_{1}+c_{2}v_{2}+\dots c_{k}v_{k}+c_{k+1}v_{k+1})=L(c_{1}v_{1}+c_{2}v_{2}\dots+c_{k}v_{k})+L(c_{k+1}v_{k+1})$  ($\because L$ is a LT)
$=c_{1}L(v_{1})+c_{2}L(v_{2})+\dots c_{k}L(v_{k})+c_{k+1}L(v_{k+1})$ ($\because$ inductive hypothesis)
Therefore, the result holds true for $n=k+1$
Hence proved by mathematical induction.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q5) **IMP:** Prove that if $B=\{v_{1},v_{2},\dots,v_{n}\}$ is an ordered basis of $V$and $W$ is a vector space s.t. $w_{1},w_{2},\dots w_{n}\in W$, then $\exists$ a *unique linear transformation* s.t. $L(v_{i})=w_{i}, i=1,2,\dots,n$.
?
Proof: Let $v \in V$ be arbitrary. Since $B$ is a basis of $V$, $\exists\:a_{1},a_{2},\dots,a_{n}\in \mathbb{R}$ s.t. $v=a_{1}v_{1}+a_{2}v_{2}+\dots+a_{n}v_{n}$.
Define $L:V\to W$ s.t. 
$L(v)=L(a_{1}v_{1}+a_{2}v_{2}+\dots+a_{n}v_{n})$
$=a_{1}w_{1}+a_{2}w_{2}+\dots+a_{n}w_{n}$ **(we're constructing a function to satisfy $L(v_{i})=w_{i}$**)
Then, $L(v_{i})=L(0v_{1}+0v_{2}+\dots+1v_{i}+\dots+0v_{n})$
$=1w_{i}=w_{i}$
$\therefore L(v_{i})=w_{i},\forall\:i=1,2,\dots,n$.
.
We will now show $L(v_{i})$ is a LT. Let $v=a_{1}v_{1}+a_{2}v_{2}+\dots+a_{n}v_{n}$, $u=b_{1}v_{1}+b_{2}v_{2}+\dots+b_{n}v_{n} \in V$ be arbitrary.
$L(v+u)=L(a_{1}v_{1}+a_{2}v_{2}+\dots+a_{n}v_{n}+b_{1}v_{1}+\dots+b_{n}v_{n})$
$=L((a_{1}+b_{1})v_{1}+(a_{2}+b_{2})v_{2}+\dots+(a_{n}+b_{n})v_{n})$
$=(a_{1}+b_{1})w_{1}+(a_{2}+b_{2})w_{2}+\dots+(a_{n}+b_{n})w_{n}$
$=a_{1}w_{1}+a_{2}w_{2}+\dots+a_{n}w_{n}+b_{1}w_{1}+\dots+b_{n}w_{n}$
$=L(a_{1}v_{1}+a_{2}v_{2}+\dots+a_{n}v_{n})+L(b_{1}v_{1}+\dots+b_{n}v_{n})$
$=L(v)+L(u)$
.
Let $c \in \mathbb{R}$ be arbitrary.
$L(cv)=L(ca_{1}v_{1}+ca_{2}v_{2}+\dots+ca_{n}v_{n})$
$=ca_{1}w_{1}+ca_{2}w_{2}+\dots+ca_{n}w_{n}$
$=c(a_{1}w_{1}+a_{2}w_{2}+\dots+a_{n}w_{n})$
$=c(L(a_{1}v_{1}+a_{2}v_{2}+\dots+a_{n}v_{n}))$
$=cL(v)$
Therefore, $L$ is a LT.
.
Now **we must prove that $L$ is a unique LT.** Let, if possible, $\exists$ another LT $T$ s.t. $T(v_{i})=w_{i},\:i=1,2,\dots,n$
Now, $T(v)=T(a_{1}v_{1}+a_{2}v_{2}+\dots+a_{n}v_{n})$
$=a_{1}T(v_{1})+a_{2}T(v_{2})+\dots+a_{n}T(v_{n})$
$=a_{1}w_{1}+a_{2}w_{2}+\dots+a_{n}w_{n}$
$=a_{1}L(v_{1})+a_{2}L(v_{2})+\dots+a_{n}L(v_{n})$
$= L(a_{1}v_{1}+a_{2}v_{2}+\dots+a_{n}v_{n})$
$=L(v)$
$\therefore\: T(v)=L(v)$. Therefore, $L$ is a unique LT.
Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

