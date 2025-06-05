---
color: var(--mk-color-turquoise)
tags:
  - "#sem2-flashcards/linear_alg/system_of_equations"
---

Consider a system of $m$ equations in $n$ variables.
$a_{11}x_{1}+a_{12}x_{2}+\dots+a_{1n}x_{n}=b_{1}$
$a_{21}x_{1}+a_{22}x_{2}+\dots +a_{2n}x_{n}=b_{2}$
.
.
.
$a_{m1}x_{1}+a_{m2}x_{2}+\dots+a_{mn}x_{n}=b_{m}$

This system can be written in a matrix form as $AX=B$, where $A=\begin{bmatrix}a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ . \\ . \\ . \\ a_{m_{1}} & a_{m_{2}} & \dots & a_{mn}\end{bmatrix}_{m\times n}$ , $X = \begin{bmatrix}x_{1} \\ x_{2} \\ . \\ . \\ . \\ x_{n}\end{bmatrix}_{n \times 1}$ and $B=\begin{bmatrix}b_{1} \\ b_{2} \\ . \\ . \\ . \\ b_{m}\end{bmatrix}_{m \times 1}$

$A$ is called the *coefficient matrix* of the system. If we append the column $B$ to this matrix, we get $[A|B]=\left[\begin{array}{cccc|c} a_{11} & a_{12} & \dots & a_{1n} & b_{1} \\ . \\ . \\ . \\ a_{m_{1}} & a_{m_{2}} & \dots & a_{mn} & b_{m}\end{array}\right]$, which is called the *augmented matrix* of the system.