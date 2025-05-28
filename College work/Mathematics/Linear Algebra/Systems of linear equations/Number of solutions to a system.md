---
color: var(--mk-color-turquoise)
tags:
  - "#sem2-flashcards/linear_alg/system_of_equations"
---
Quick access:
- [[#General case|General case]]
- [[#For a homogenous system|For a homogenous system]]
	- [[#For a homogenous system#Using the rank of the matrix|Using the rank of the matrix]]
- [[#Using determinants|Using determinants]]

## General case
Let $AX=B$ be a system of equations, $[A|B]$ be the augmented matrix of the system and $[C|D]$ be the reduced row echelon form of $[A|B]$. Then,
1) If the **last column of $[C|D]$ is a pivot column, the system has no solutions.** If this is the case, the last column would look like $[0\dots 0|1]$. Putting this back to equation form tells us $0x_{1}+\dots+0x_{n}=1\implies 0 = 1$, which is a contradiction. Therefore, this system has no solutions.

2) If **all the columns of $C$ are pivot columns** and 1) is not true, then the system has a unique solution.

3) If **at least one column of $C$ isn't a pivot column** and 1) isn't true, then the system has infinitely many solutions. The non pivot columns represent free variables, which can take infinitely many values, hence infinite solutions for the system.

## For a homogenous system
Let $AX=0$ be a homogenous system in $n$ variables. Then,
1) If the reduced row echelon form of $A$ has *less pivot columns than* $n$, the system has infinitely many solutions.
2) If the system has the same number of pivot positions as $n$, then the system has a unique solution (the trivial solution).

If we have a **homogenous system of $m$ equations in $n$ variables, then the system has infinite solutions if** $m<n$. Therefore, more variables than equations necessarily means infinite solutions for a homogenous system.

### Using the rank of the matrix
We can express the above criterion for homogenous systems in terms of the rank of a matrix. If $\text{rank}(A)<n$, the system has non-trivial solutions (infinitely many). If $\text{rank}(A)=n$, the system has a unique solution (trivial solution).

## Using determinants
Consider a system $AX=B$. Our matrix $A$ can either have $\det(A)\ne0$ or $\det(A)=0$. Let's look at these two cases:

Case 1 - Determinant is non-zero:
In this case, *our matrix is invertible.* Therefore, we can *premultiply both sides by the inverse.* This means $AX=B \implies (A^{-1}A)X=(A^{-1}B)\implies X=A^{-1}B$. Therefore, **this system has a unique solution** which is $A^{-1}B$. In the homogenous case, this would become zero.

Case 2 - Determinant is zero:
In this case, we can no longer invert the matrix and isolate $X$ as we did before. We know that the determinant being zero means that *there exists at least one pair of linearly dependent rows/columns.* 

This would mean that the rank is less than the number of variables. Lets say $\text{rank}(A)<n$. From the [[Kernel and Range#The dimension theorem|dimension theorem]] we know that $\text{dim }\text{Ker }A +\text{dim }\text{Range }A=\text{dim } \text{domain}$. If the system has $n$ variables, the domain is of dimension $n$. We also know that *the dimension of range is nothing but the rank,* which is less than $n$ here. Therefore, **dimension of the kernel cannot be zero.**

If the kernel has even a dimension of just 1, we can express the kernel as $\{c:c \in \mathbb{R}\}$, which is $\mathbb{R}$, which is infinitely large. Same holds for any dimension greater than 1. **Therefore, determinant being zero leads to a non-zero kernel, giving us infinite solutions.** 