---
color: var(--mk-color-turquoise)
tags:
  - "#sem2-flashcards/linear_alg/system_of_equations"
---

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
We can express the above criterion in terms of the rank of a matrix. If $\text{rank}(A)<n$, the system has non-trivial solutions (infinitely many). If $\text{rank}(A)=n$, the system has a unique solution (trivial solution).