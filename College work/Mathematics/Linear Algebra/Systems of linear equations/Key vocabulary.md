---
color: var(--mk-color-turquoise)
tags:
  - "#sem2-flashcards/linear_alg/system_of_equations"
---
Quick access:
- [[#Homogenous equation|Homogenous equation]]
- [[#Homogenous system|Homogenous system]]
- [[#Consistent system|Consistent system]]
- [[#Row echelon form|Row echelon form]]
- [[#Reduced row echelon form|Reduced row echelon form]]
- [[#Pivot columns|Pivot columns]]
- [[#Basic and free variables|Basic and free variables]]


## Homogenous equation
A homogenous linear equation is a linear equation where *the constant term is zero.* Eg: $5x+2y=0$ is homogenous, $5x+2y=-1$ is not.

## Homogenous system
A system of homogenous equations is called a homogenous system. By definition, the matrix $B$ will be a zero matrix. *Such a system always has at least one solution (trivial solution).* This is because if we have $AX=B$ and $B=0$, then $X=0$ will be a solution. If it has one non-trivial solution, then it has infinitely many solutions.

## Consistent system
A system of equations with *at least one solution* is called consistent. It is called inconsistent if it has no solutions. A homogenous system is always consistent.

## Equivalent systems
Two systems of $m$ equations in $n$ variables are stb equivalent if *they have the same solution set.* Since ERTs don't change the solution set, we can also say that a matrix $C$ is equivalent to a matrix $D$ iff $D$ can be obtained from $C$ through ERTs.

## Row echelon form
A matrix is stb in row echelon form if:
1) The first non-zero entry in each row is 1 (leading entry, also called *pivot position*)
2) Each successive row has its first non-zero entry (pivot position) **to the right** of the non-zero entry above it.
3) In case there are any rows of zeros, they must be at the bottommost position.
Although we typically follow a 'standard' procedure for reducing a matrix, you can use any method to reduce a matrix as long as it ends up in row echelon form. Therefore, **a matrix can have multiple row echelon forms.** We'll call this a *REF* for simplicity.

## Reduced row echelon form
A matrix is stb in reduced row echelon form if it is *in row echelon form and every element above the leading entry is zero.* While a matrix may have multiple row echelon forms, **there is only one unique reduced row echelon form.** We'll denoted this with *RREF* for simplicity.

## Pivot columns
Columns that *contain leading entries* in a row echelon form are called pivot columns. The remaining columns are called non-pivot columns.

## Basic and free variables
Variables *associated to the pivot columns* are called basic (or dependent) variables. Those associated to non-pivot columns are called free variables. **We always express basic variables in terms of the free ones.**

## Rank of a matrix
The rank of a matrix $A$ is the *number of non-zero rows* in the reduced row echelon form of $A$. In other words, it is the number of leading entries in the reduced row echelon form.