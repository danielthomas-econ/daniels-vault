---
color: var(--mk-color-brown)
tags:
  - "#sem2-flashcards/linear_alg/eigenstuff"
---

## Concept
Let $A$ be a square matrix of order $n$. A real number $\lambda$ is stb an eigenvalue of $A$ iff $\exists$ a non zero eigenvector $X$, $X\ne 0$, s.t. $AX=\lambda X$.
![[WhatsApp Image 2025-05-28 at 08.10.15_dda34bd6.jpg]]

The word 'eigen' means *proper* in German. Graphically, **multiplying a matrix by its eigenvector does not change the direction of the vector, it just scales it by the eigenvalue.** In a sense, this is why its called a 'proper' vector. Note that the concept of eigenvalues and eigenvectors is *only defined for square matrices.*

## Eigenspace
Let $\lambda$ be an eigenvalue of a $m\times n$ matrix $A$. The **set of all eigenvectors of $A$ corresponding to the eigenvalue $\lambda$**, defined as $E_{\lambda} = \{X \in \mathbb{R}^{n}: AX=\lambda X\}$ is called the eigenspace of $A$ corresponding to $\lambda$.

Note that if $X$ is an eigenvector, then $cX$ ($c \in R, \ne 0$) is also an eigenvector. Therefore, *to get the set of all eigenvectors, we simply multiply each eigenvector by a non-zero scalar.* Even though an eigenvector can never be zero by definition, *we include the zero vector in every eigenspace.* This is done to ensure that the eigenspace will be a subspace, which we'll see later in properties of subspaces. 