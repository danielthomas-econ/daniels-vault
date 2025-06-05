---
color: var(--mk-color-brown)
tags:
  - "#sem2-flashcards/linear_alg/eigenstuff"
  - "#sem2-flashcards/mme/eigenstuff"
---
Quick access:
- [[#Similar matrices|Similar matrices]]
- [[#Diagonalizable matrices|Diagonalizable matrices]]
	- [[#Diagonalizable matrices#Condition for diagonalizability|Condition for diagonalizability]]
	- [[#Diagonalizable matrices#Higher power of matrices|Higher power of matrices]]
- [[#Spectral theorem|Spectral theorem]]

## Similar matrices
A square matrix $A$ is stb similar to a square matrix $B$ if $\exists$ an invertible matrix $P$ s.t. $A=P^{-1}BP$. **If $A$ is similar to $B$, then $B$ is similar to** $A$, so we can also say that $B=P^{-1}AP$. Similar matrices also **have the same determinants, characteristic polynomial, and therefore eigenvalues.** 

## Diagonalizable matrices
Diagonalizable matrices is a special case of similar matrices when a *matrix is similar to a diagonal matrix.* Therefore, $A$ is stb diagonalizable if it is similar to a diagonal matrix $D$, or $A=P^{-1}DP$. 

Finding the matrix $P$ is straightforward. Just *put the eigenvectors of $A$ as column vectors of a matrix and you'll get $P$*. Find $P^{-1}$ accordingly. The corresponding matrix $D$ will be a diagonal matrix, with its diagonal elements being the eigenvalues corresponding to the order of the eigenvectors in $P$. 

Example:
![[WhatsApp Image 2025-05-28 at 09.49.04_7a4aa71b.jpg|center|500]]

### Condition for diagonalizability
A matrix is diagonalizable if **all its eigenvalues are distinct.** If we have a matrix of order $n$ with $n$ distinct eigenvalues, we have $n$ eigenvectors, so we can put these $n$ eigenvectors as columns of a matrix to get $P$. 

**If eigenvalues are repeated, the eigenspace must be a linear combination of independent vectors** for the matrix to be diagonalizable. For a matrix of order $n$, we have less than $n$ distinct eigenvalues if there are repeated eigenvalues. This would mean that we have less than $n$ eigenvectors, so we don't have enough to form a matrix $P$ of order $n$. But if we have an eigenspace that is a linear combination of independent vectors [[Eigenvalues and eigenvectors#^e35ca8|(special case of eigenspace),]] we may still be able to get $n$ vectors. *If the sum of the linearly independent vectors in each eigenspace (includes eigenvectors themselves) is equal to $n$*, then we can diagonalize the matrix.

### Higher power of matrices
It is very easy to find $A^{n}$ using diagonalization, since if $A$ can be diagonalized as $P^{-1}DP$, $A^{n}= P^{-1}D^{n}P$. **Now, we only have to raise a diagonal matrix to a power, which is just the power of the individual elements.** 

Also, if you are asked to find $A^{n}X$, where $X$ is an eigenvector, you can use the formula $A^{n}X=\lambda^{n}X$.

## Spectral theorem
Suppose $A$ is a symmetric matrix. Then, there exists an orthogonal matrix $U$ ($U^{-1}=U'$) s.t. $$U^{-1}AU=\text{diag}(\lambda_{1},\lambda_{2},\dots ,\lambda_{n})$$
To find $U$, we must make use some properties of symmetric matrices, specifically that [[Eigenvalues and eigenvectors#Symmetric matrices|symmetric matrices have orthogonal eigenvectors.]] If $x_{1},x_{2},\dots,x_{n}$ are eigenvectors corresponding to distinct eigenvalues, then they're mutually orthogonal. *Make the eigenvectors of length 1 by normalizing them.* Put these normalized eigenvectors into a matrix. That gives us the required matrix $U$.