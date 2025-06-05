---
color: var(--mk-color-turquoise)
tags:
  - "#sem2-flashcards/linear_alg/system_of_equations"
---
Quick access:
- [[#What is row space?|What is row space?]]
- [[#Checking if a vector belongs to the row space|Checking if a vector belongs to the row space]]
	- [[#Checking if a vector belongs to the row space#For equivalent matrices|For equivalent matrices]]

## What is row space?
The row space of a matrix $A$ is simply the *linear combination of all the rows of $A$*. If $A$ is a $m \times n$ matrix, then $A=\begin{bmatrix}k_{1} \\ k_{2} \\ \dots \\ k_{m}\end{bmatrix}$, the row space can be expressed as $c_{1}k_{1}+c_{2}k_{2}+\dots +c_{m}k_{m}$, $c_{i} \in \mathbb{R}$.

## Checking if a vector belongs to the row space
To check if a vector belongs to the row space of a matrix, by definition we **check if the vector can be expressed as a linear combination of the rows of the matrix.** Let's illustrate this with an example. We'll check if $[5,17,-20]$ belongs to the row space of $A=\begin{bmatrix}3 & 1 & -2 \\ 4 & 0 & 1 \\ -2 & 4 & -3\end{bmatrix}$.

Being in the row space means $[5,17,-20]=c_{1}[3,1,-2]+c_{2}[4,0,1]+c_{3}[-2,4,-3]$. We have a system of three equations in three variables. The augmented matrix of this system becomes $\left[\begin{array}{ccc|c}3 & 4 & -2 & 5 \\ 1 & 0 & 4 & 17 \\ -2 & 1& -3 & -20\end{array}\right]$. Solving this gives us $\left[\begin{array}{ccc|c}1 & 0 & 0 & 5 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 3\end{array}\right]$. This means we have $c_{1},c_{2},c_{3}=5,-1,3$. Therefore, $[5,17,-20]$ does belong to the row space of $A$. **Notice that we simply put the row vectors are columns and then reduce the matrix.** Therefore, we can say that$$u \in \text{row space of }A\text{ if }[A^{T}|u]\text{ has a solution}$$
### For equivalent matrices
The row space of two equivalent matrices are the same. This is because equivalent matrices $A$ and $B$ just means that $B$ is $A$ with some ERTs applied to it. *Therefore, the row vectors of $B$ are linear combinations of row vectors of* $A$. Therefore, their row spaces will be the same.