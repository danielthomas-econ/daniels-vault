---
color: var(--mk-color-base-70)
tags:
  - "#sem2-flashcards/linear_alg/vector_spaces"
  - "#sem2-flashcards/mme/vectors_and_matrices"
---
Quick access:
- [[#Definition|Definition]]
- [[#Properties of linear independence|Properties of linear independence]]
- [[#Steps to check for linear independence|Steps to check for linear independence]]
- [[#Linear independence of infinite sets|Linear independence of infinite sets]]
- [[#Flashcards|Flashcards]]

## Definition
Let $S=\left\{v_{1},v_{2},\dots,v_{n}\right\}$ be a finite non-empty subset of a vector space $V$. Then, $S$ is stb linearly independent (LI) if $\exists$ $c_{1},c_{2},\dots,c_{n} \in \mathbb{R}$ s.t. $c_{1}v_{1}+c_{2}v_{2}+\dots + c_{n}v_{n}=0$ $\implies$ **$c_{i}=0$ is the only solution for** $i=1,2,\dots,n$.

$S$ is linearly dependent (LD) if its not linearly independent. Therefore, we can write $c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}=0$ where not all $c_{i}$ are zero.

## Properties of linear independence
1) *A singleton $\left\{v\right\}$ is LI* $\iff$ $v\ne 0$.
Proof: Let $cv=0$ (to check for LI)
If $v\ne 0$, then $c=0$ is the only solution $\implies$ $\left\{v\right\}$ is LI
If $v=0$, then any $c$ satisfies this equation $\implies$ not all $c$ are zero $\implies$ $\left\{v\right\}$ is LD
Reverse implication is done in a nearly identical way.

2) *Two vectors are LD $\iff$* $v_{1}=cv_{2}$.
Proof: Let $c_{1}v_{1}+c_{2}v_{2}=0$.
If $v_{1},v_{2}$ are LD, at least one of $c_{1},c_{2}$ is not zero. WLOG, assume $c_{1}$ is not zero.
Then, $v_{1}= \dfrac{{-c_{2}}}{c_{1}}v_{2}$ (valid since $c_{1}\ne 0$)
$\implies v_{1}=cv_{2}, c\in \mathbb{R}$.
Reverse implication:
Let $v_{1}=cv_{2}$.
$\implies v_{1}-cv_{2}=0$. Here the scalars are $1$ and $-c$. Clearly, $1 \ne 0$ so all scalars aren't zero $\implies$ they are LD.

3) *Any set containing the zero vector is LD.*
Proof: Let $S=\left\{0,v_{2},v_{3},\dots,v_{n}\right\}$
Therefore, $c_{1}0+c_{2}v_{2}+\dots+c_{n}v_{n} = 0$. This equation holds true for all $c_{1} \in \mathbb{R}$ if all other $c_{i}=0$. Therefore, not all scalars are zero, so $S$ must be LD.

4) $n+1$ *or more vectors in $\mathbb{R}^n$ are always LD.*
Reason: $n$ independent vectors in $\mathbb{R}^n$ span $\mathbb{R}^n$. Therefore, adding any extra vector from $\mathbb{R}^n$ $\implies$ it belongs to $\text{span}(S)$ $\implies$ it is a linear combination of the $n$ vectors $\implies$ $n+1$ vectors are LD.

If $n$ vectors don't span $\mathbb{R}^n$, one of them must be linearly dependent $\implies$ adding another vector still keeps the set LD.

5) **Every subset of a LI set is always LI.**
Reason: If $n$ vectors in $S$ are LI, then $k$ vectors in $S_{1}$, $S_{1} \subseteq S$ and $k \leq n$ must also be LI since the $k$ vectors in $S_{1}$ are in $S$ and if $S$ is LI, then the $k$ vectors in $S_{1}$ must be LI, so $S_{1}$ is LI

6) **Superset of a LI set may not be LI.**
Reason: If we add a vector that's a linear combination of vectors already in $S$, then the set becomes LD. Adding elements doesn't guarantee that the new set retains independence.

7) **Subset of a LD set may not be LD.**
Reason: It is possible to take a subset $S_{1}$ of $S$ (where $S$ is LD) where the elements of $S_{1}$ are mutually independent. The most obvious example would be to pick any non-zero element of $S$ and make it a singleton set. Since it is a non-zero singleton, it is LI.

8) **Superset of a LD set is always LD.**
Reason: Adding more elements to a LD set does not change the fact that one vector can be expressed as a LC of other vectors in the set. Simply put the scalars of the new vectors to zero, then nothing has changed in the LC. If previously $v=c_{1}v_{1}+c_{2}v_{2}+\dots+c_{k}v_{k}$ but the superset has $n$ elements, we can rewrite this as $v=c_{1}v_{1}+c_{2}v_{2} +\dots+ c_{k}v_{k}+0v_{k+1}+\dots+0v_{n}$, which is the same as the previous LC.

9) $\varnothing$ *is LI.*
Reason: $\varnothing$ is always a subset of any set, so it is always the subset of a LI set. Since all subsets of LI sets are LI, $\varnothing$ must also be LI.


## Steps to check for linear independence
The condition for linear independence basically gives us a system. Consider $S=\left\{[p_{1},p_{2},p_{3}],[q_{1},q_{2},q_{3}],[r_{1},r_{2},r_{3}]\right\}$. The condition for linear independence tells us that $c_{1}P+c_{2}Q+c_{3}R=0$ for $c_{i} \in \mathbb{R}$. This means $c_{1}(p_{1}+q_{1}+r_{1})=0$, and the same system holds for the second and third index. *Therefore, we can express this system in a matrix and check for linear independence in the matrix,* which means we must not get a row of zeros when reducing it.

Steps:
1) Create a matrix $A$ with columns as the vectors of $S$
2) Reduce it to row echelon form (RREF is unnecessary but still works)
3) If there are no free variables, $S$ is LI. If $\exists$ at least one free variable, then $S$ is LD.

Example: $S=\left\{[3,1,-1],[-5,-2,2],[2,2,-1]\right\}$. Is $S$ LI?
?
Ans) Putting the vectors in $S$ as columns of a matrix $A$ gives us $A=\begin{bmatrix}3 & -5 & 2 \\ 1 & -2 & 2 \\ -1 & 2 & -1\end{bmatrix}$. Reducing it to row echelon form gives $A \sim \begin{bmatrix}1 & -2 & 2 \\ 0 & 1 & -4 \\ 0 & 0 & 1\end{bmatrix}$. *Since there are no free variables, $S$ is LI.* 

## Linear independence of infinite sets
Unfortunately, our previous criteria of checking if all scalars are zero doesn't work when there are infinitely many elements in the set. In this case, an infinite subset $S$ of a vector space $V$ is stb *LI if all finite subsets of $S$ are LI.* If $\exists$ even one finite subset of $S$ which is LD, then $S$ is LD.








## Flashcards
Q1) Let $S$ be a finite subset of a vector space $V$ having at least two vectors. Then show that $S$ is LD $\iff$ some vector in $S$ can be expressed as a LC of other vectors in $S$.
?
Ans) Let $S=\left\{v_{1},v_{2},\dots,v_{n}\right\}$ be LD.
$\implies$ $\exists$ $c_{1},c_{2},\dots,c_{n} \in \mathbb{R}$ not all zero s.t. $c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}=0$. WLOG, suppose $c_{1}$ is not zero.
Then we have $v_{1}= \dfrac{{-c_{2}}}{c_{1}}v_{2} - \dfrac{c_{3}}{c_{1}}v_{3}\dots \dfrac{{-c_{n}}}{c_{1}}v_{n}$
$\implies$ $S$ is LD as some vector can be written as a LC of other vectors in $S$.
Conversely, suppose $v_{1}$ can be expressed as a LC of $v_{2},v_{3},\dots, v_{n}$.
$\implies$ $\exists$ $c_{2},c_{3},\dots,c_{n} \in \mathbb{R}$ s.t. $v_{1}=c_{2}v_{2}+c_{3}v_{3}+\dots+c_{n}v_{n}$
$\implies v_{1}-c_{2}v_{2}-\dots-c_{n}v_{n}=0$
Clearly, not all scalars are zero since the scalar of $v_{1}$ is $1 \ne 0$.
$\implies$ S is LD.
Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Let $S$ be a finite subset of $V$. Then, $S$ is LI $\iff$ every vector $v \in \text{span}(S)$ can be expressed **uniquely** as a LC of elements of $S$.
?
Ans) Let $S=\left\{v_{1},v_{2},\dots,v_{n}\right\}$ be LI.
Suppose $\exists$ $v \in \text{span}(S)$ s.t. $v=a_{1}v_{1}+a_{2}v_{2}+\dots+a_{n}v_{n}$ and $v=b_{1}v_{1}+b_{2}v_{2}+\dots+b_{n}v_{n}$, $a_{i},b_{i} \in \mathbb{R}$. Subtracting the second equation from the first, $(a_{1}-b_{1})v_{1}+(a_{2}-b_{2})v_{2}+\dots+(a_{n}-b_{n})v_{n}=0$. **Since $S$ is LI, every scalar must be equal to zero.** Therefore, $a_{i}=b_{i}$ for $i=1,\dots,n$ $\implies v \in \text{span}(S)$ only has one unique representation.
.
Conversely, suppose every $v \in \text{span}(S)$ can be expressed uniquely as a LC of elements of $S$.
Consider $c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}=0$.
Since $0 \in \text{span}(S)$, there must be only one unique representation of zero. *Since this is a homogenous system, the only way to get a unique representation is if all the scalars are zero. If there exists one non-trivial expression, there will be infinite such expressions.* Therefore, we have $0v_{1}+0v_{2}+\dots+0v_{n}=0$ $\implies$ all $c_{i}=0$ is the only solution $\implies$ $S$ is LI.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q3) Show that the infinite set $S=\left\{1,1+x,1+x+x^{2},\dots\right\}$ is LI.
?
Ans) Let $T=\left\{v_{1},v_{2},\dots,v_{n}\right\}$ be any arbitrary finite subset of $S$.
**We'll start by ordering $T$ in ascending order of polynomial degree.** WLOG, suppose degree $v_{i}$ $\leq$ degree $v_{j}$ for $i <j$ and $i,j \in \left\{1,2,\dots ,n\right\}$.
Consider $c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}=0$. *Suppose that T is LD. Then, WLOG, let some $c_{i}\ne 0$* *and let $v_{k}$ be the last non-zero term.* Since we have arranged the set in ascending order, **$v_{k}$ must be the term with the highest degree.**
Then, $c_{1}v_{1}+c_{2}v_{2}+\dots+c_{k}v_{k}=0$.
$\implies v_{k}= \dfrac{{-c_{1}}}{c_{k}}v_{1}-\dots \dfrac{{-c_{k-1}}}{c_{k}}v_{k-1}$.
Degree of LHS > Degree of RHS. This is a contradiction. Therefore, our assumption that $T$ is LD was wrong.
Therefore, $T$ is LI.
Since any arbitrary finite subset of $S$ is LI, $S$ is LI.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

