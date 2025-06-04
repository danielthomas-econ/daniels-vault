---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/mme/vectors_and_matrices"
---
Quick access:
- [[#Process|Process]]

## Process
Cramer's rule is a method to solve $n$ equations in $n$ variables. Let the matrix of the system be denoted by $A$. First, *let's define $D_{j}$ as the determinant of $A$ but with the $j^{th}$ column replaced by the constant vector.* So if $AX=B$ is our system, $D_{j}=\begin{vmatrix} a_{11} & \dots & a_{1j-1} & b_{1} & a_{1j+1} & \dots & a_{1n} \\ . \\ . \\ . \\ a_{n1} & \dots & a_{nj-1}  & b_{j} & a_{nj+1} & \dots & a_{nn}\end{vmatrix}$

The system has a unique solution if $|A|\ne 0$. If $|A|=0$, we cannot apply Cramer's rule. Using Cramer's rule, the solution to the system is $x_{1}=\dfrac{D_{1}}{|A|},x_{2}=\dfrac{D_{2}}{|A|},\dots, x_{n}=\dfrac{D_{n}}{|A|}$.