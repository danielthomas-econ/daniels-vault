---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/mme/vectors_and_matrices"
---
Quick access:
- [[#Definition|Definition]]
- [[#Finding rank using minors|Finding rank using minors]]
- [[#Finding rank using ERTs|Finding rank using ERTs]]
- [[#Applications to systems of linear equations|Applications to systems of linear equations]]
	- [[#Applications to systems of linear equations#Number of solutions|Number of solutions]]
	- [[#Applications to systems of linear equations#Superfluous equations|Superfluous equations]]
	- [[#Applications to systems of linear equations#Degrees of freedom|Degrees of freedom]]
- [[#Flashcards|Flashcards]]


## Definition
The rank of a matrix is *the maximum number of linearly independent vectors* in the matrix. If we have a matrix of order $m \times n$, then the rank of the matrix can be at most $\text{min}(m,n)$.

## Finding rank using minors
The rank of a matrix is *the order of the largest minor of A that is different from zero.* If all possible minors of order $n$ are equal to zero, then the $\text{rank}(A) < n$. If there exists at least one non-zero minor for a minor of order $m$, but all minors with order $> m$ are zero, then the matrix has rank $m$.

Remember that we get minors by eliminating rows and columns in such a way that we get a determinant of order $n$. You must consider **every single minor** of order $n$ by using different permutations of row or column deletions.
![[WhatsApp Image 2025-05-29 at 19.00.12_cbce4bc1.jpg|center|400]]

## Finding rank using ERTs
It is far simpler to find the rank of a matrix using [[Elementary row transformations|ERTs.]] We simply *reduce the matrix to its RREF and count the number of non-zero rows.* 


## Applications to systems of linear equations
Since we can express systems of linear equations as matrices, the rank of the matrix that represents a system can give us certain information about that system.

### Number of solutions
A *necessary and sufficient* condition for a system to be consistent (have at least one solution) is that **the rank of the coefficient matrix must be equal to the rank of the augmented matrix.** Since the augmented matrix adds just one more column to the coefficient matrix, the difference of their ranks is at most 1. Since it has all the columns of the coefficient matrix, its rank cannot be less than the coefficient matrix. *Therefore, we only have two cases: $\text{rank}(A|B)>\text{rank}(A)$ and $\text{rank}(A|B)=\text{rank}(A)$*.

If $\text{rank}(A|B)>\text{rank}(A)$, you end up with a contradiction and a system with no solutions. Consider a $3\times 3$ matrix $A$. If the $\text{rank}(A)=2$, the last row in the RREF must be all zero. If $\text{rank}(A|B)=3$, the only way this is possible would be for the last entry of the augmented column to be non-zero. An example would be the matrix $\left[\begin{array}{ccc|c}1 & 0 & 0 & 5 \\ 0 & 1 & 0 & 6 \\ 0 & 0 & 0 & 2\end{array}\right]$. **When $\text{rank}(A|B)>\text{rank}(A)$**, **clearly the last row of the RREF tells us that zero equals a non-zero number. This is impossible, so the system has no solutions.** 
If $\text{rank}(A|B)=\text{rank}(A)=n$, where $n$ is the number of variables, then *you're left with a RREF that has no free variables. Therefore, the system has a unique solution.* If $\text{rank}(A|B)=\text{rank}(A) <n$, you'll have free variables, so you'll have infinite solutions. This is why $AX=B$ has a solution $\iff$ $\text{rank}(A)=\text{rank}(A|B)$.

Summary:
$$\text{Number of solutions: }\begin{cases}
\text{rank}(A|B) > \text{rank}(A) \implies \text{contradiction, no soln} \\
\text{rank}(A|B) = \text{rank}(A) = n
 \implies \text{unique soln} \\
\text{rank}(A|B) = \text{rank}(A) < n \implies \text{infinite solns}\end{cases}$$

### Superfluous equations
Superfluous equations are *equations which are redundant as they're simply linear combinations of other equations in the system.* This means they do not provide any new information. They're kind of like the previous equations repackaged into another equation, this equation doesn't add anything new to the system. *These equations can be ignored when solving the system.*

From this definition, it follows that **rows corresponding to rows of zeros in RREF are rows that represent superfluous equations.** Any row that becomes all zero in an RREF represent rows that are linear combinations of other rows, which is exactly the definition of a superfluous equation.

It doesn't make sense to talk about redundant equations if the whole system is redundant (inconsistent), so let's restrict ourselves to the case $\text{rank}(A)=\text{rank}(A|B)$. **If $\text{rank}(A)=\text{rank}(B)=k \leq m$**, **where $m$ is the number of equations, then there exist $m-k$ superfluous equations.** 

This is pretty intuitive. If $\text{rank}(A)=\text{rank}(A|B)=k$, then we have $k$ linearly independent equations in the system. Superfluous equations are linearly dependent. *If we have a system of $m$ equations and $k$ are linearly independent, $m-k$ must be linearly dependent.* 

### Degrees of freedom
Once again, we'll restrict ourselves to talking about consistent systems, i.e. $\text{rank}(A)=\text{rank}(A|B)$. Let $\text{rank}(A)=\text{rank}(A|B)=k$.

*If there are $n$ variables and $\text{rank}(A)=k$*, *then we effectively have a system of $k$ equations in $n$ variables,* since the other $m-k$ are superfluous and don't add anything to the system. $k$ must be less than equal to $n$. If they're equal, we know the system can have at most one solution. If $n>k$, we know the system can have infinite solutions.

This is because of degrees of freedom. *If $n>k$*, *then there exists variable(s) which can be chosen freely. The value of this variable does not affect the system.* Since this variable can take on any value (and hence an infinite number of values), the solution set to the system is infinite when $n>k$. If $n=k$, every variable impacts the system in some way. Therefore, there can only be a fixed value for each variable, so we have a unique solutions.

**The number of free variables, i.e. the degrees of freedom, is given by** $n-k$. If we have a system of $k$ equations in $n$ variables, then $n-k$ variables do not affect the system, so they are free variables. The other $k$ variables are uniquely determined by the system.

Summary:
$$\begin{align}
\text{If }&\text{rank}(A)=\text{rank}(A|B)=k \text{ for a system with }m \text{ equations in }n \text{ variables,} \\
 \\
&\text{We can say that the }\begin{cases}
\text{Number of superfluous equations } = m-k \\
\text{Degrees of freedom } = n-k
\end{cases}
\end{align}$$






## Flashcards
Q1) ![[e3de7cb1-1489-4688-8824-f0ebf6e92c13.png]]
?
Ans) Since the rank of a matrix is the number of linearly independent rows/columns, **we can see under what conditions will one row become fully zero (i.e. dependent).** If we use the ERTs $R_{2}\to R_{2}-2R_{1},R_{3}\to R_{3}-4R_{1}$ and then $R_{3} \to R_{3} +\left( \dfrac{2}{5} \right)R_{2}$, we get the matrix $\begin{bmatrix}1 & 3 & 1 & 1 \\ 0 & p-6 & 5 & q-2 \\ 0 & -10+\left( \dfrac{2}{5} \right)(p-6) & 0 & -1 + \left( \dfrac{2}{5} \right)(q-2)\end{bmatrix}$. Since the last row must be zero, set both the terms to zero and you get $p=31,q=\dfrac{9}{2}$. Therefore, *the rank is less than three if BOTH these conditions are met. In any other case, rank is three.* For rank to be less than 2, the second row must be all zeros. But if $p=31,q=\dfrac{9}{2}$, this is clearly impossible. Therefore, the rank of the matrix must be two when $p=31,q=\dfrac{9}{2}$ and three in any other case.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>