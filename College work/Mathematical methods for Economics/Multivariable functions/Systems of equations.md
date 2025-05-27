---
color: var(--mk-color-teal)
tags:
  - "#sem2-flashcards/mme/multivariable_functions"
---
Quick access:
- [[#Degrees of freedom|Degrees of freedom]]
	- [[#Degrees of freedom#Counting rule|Counting rule]]

## Degrees of freedom
Let $x_{1},x_{2},\dots,x_{n}$ be $n$ variables. If there are no restrictions on these variables, they are said to have $n$ degrees of freedom because they can be freely chosen to be whatever you want. *If these variables have to satisfy an equation $f_{1}(x_{1},x_{2},\dots,x_{n})=0$*, *then we have introduced a restriction.* The $n$ variables are restricted to be picked in such a way that it must satisfy the equation. Obviously, restriction and freedom are two opposite ideas. **Therefore, if we have one restriction, we have one less degree of freedom.** Whenever an 'independent' restriction is introduced, we reduce the degrees of freedom by one. 

### Counting rule
*In a system of $n$ equations with $m$ independent restrictions, the degrees of freedom becomes $n-m$* given that $m<n$. If $m>n$, the system has no solutions.

However, this is not always true. Consider a system with $100$ variables $x_{1},x_{2},\dots,x_{100}$. Let us impose one restriction: $x_{1}^{2}+x_{2}^{2}+\dots+x_{100}^{2}=0$. Here, we have zero degrees of freedom because all the variables must necessarily be zero.

So when is the counting rule useful? If we put this into a matrix system $Ax=b$, $A$ will be of order $m\times n$ ($m$ constraints or equations in $n$ variables). **The counting rule will be valid if the row vectors of the matrix $A$ are linearly independent,** because then $\text{rank}(A)=m$, meaning all the constraints are independent.