---
color: var(--mk-color-brown)
tags:
  - "#sem2-flashcards/linear_alg/eigenstuff"
  - "#sem2-flashcards/mme/eigenstuff"
---
Quick access:
- [[#Concept|Concept]]
- [[#Eigenspace|Eigenspace]]
- [[#Finding eigenvalues and vectors|Finding eigenvalues and vectors]]
	- [[#Finding eigenvalues and vectors#Characteristic polynomial|Characteristic polynomial]]
	- [[#Finding eigenvalues and vectors#Solving for eigenvectors|Solving for eigenvectors]]
	- [[#Finding eigenvalues and vectors#Getting the eigenspace|Getting the eigenspace]]
	- [[#Finding eigenvalues and vectors#Basic example|Basic example]]
	- [[#Finding eigenvalues and vectors#Example with special case of eigenspace|Example with special case of eigenspace]]
- [[#Useful properties of eigenvalues|Useful properties of eigenvalues]]
	- [[#Useful properties of eigenvalues#Determinant and trace|Determinant and trace]]
	- [[#Useful properties of eigenvalues#Triangular matrices|Triangular matrices]]
	- [[#Useful properties of eigenvalues#Symmetric matrices|Symmetric matrices]]

## Concept
Let $A$ be a square matrix of order $n$. A real number $\lambda$ is stb an eigenvalue of $A$ iff $\exists$ a non zero eigenvector $X$, $X\ne 0$, s.t. $AX=\lambda X$.
![[WhatsApp Image 2025-05-28 at 08.10.15_dda34bd6.jpg]]

The word 'eigen' means *proper* in German. Graphically, **multiplying a matrix by its eigenvector does not change the direction of the vector, it just scales it by the eigenvalue.** In a sense, this is why its called a 'proper' vector. Note that the concept of eigenvalues and eigenvectors is *only defined for square matrices.*

## Eigenspace
Let $\lambda$ be an eigenvalue of a $m\times n$ matrix $A$. The **set of all eigenvectors of $A$ corresponding to the eigenvalue $\lambda$**, defined as $E_{\lambda} = \{X \in \mathbb{R}^{n}: AX=\lambda X\}$ is called the eigenspace of $A$ corresponding to $\lambda$.

Note that if $X$ is an eigenvector, then $cX$ ($c \in R, \ne 0$) is also an eigenvector. Therefore, *to get the set of all eigenvectors, we simply multiply each eigenvector by a non-zero scalar.* Even though an eigenvector can never be zero by definition, *we include the zero vector in every eigenspace.* This is done to ensure that the eigenspace will be a [[Subspaces|subspace.]]

## Finding eigenvalues and vectors
If $X$ is an eigenvector of $A$ corresponding to an eigenvalue $\lambda$, then by definition we know $AX=\lambda X$. We can simplify this as
$$\begin{align}
AX&=\lambda X \\
\implies \lambda IX-AX&=0 \\
\implies(\lambda I-A)X&=0 \\ 
\implies \det(\lambda I-A)\cdot &\det X=0
\end{align}$$
We know that $X\ne 0$ by definition, so its determinant isn't zero. This means $\det(\lambda I-A)=0$. If this wasn't zero, premultiplying both sides by $(\lambda I-A)^{-1}$ would give us $X=0$, a contradiction. Note that this holds true for $\det(A-\lambda I)$ too, just use what you prefer.

This condition we found is actually an iff condition. *Therefore, we must have $\det(\lambda I-A)=0$ to have an eigenvalue.* Since a square matrix of order $n$ gives you a determinant in the form of an $n^{th}$ order equation, *we can have at most $n$ eigenvalues.* 

### Characteristic polynomial
Since you're taking $\det(\lambda I-A)$, your determinant will be an $n^{th}$ order polynomial expressed in terms of $\lambda$. This is called the **characteristic polynomial.** Formally, it is defined as $p_{A}(x)=|\lambda I-A|$. You can also write $|xI-A|$ if you want to solve the polynomial in $x$ like we usually do, its your choice. **The roots of the characteristic polynomial are the eigenvalues of the matrix.** For our course, we're gonna stick to the real roots only.

### Solving for eigenvectors
Once you have your eigenvalues, you must find the eigenvector corresponding to each eigenvalue. Start by letting $X$, a $n^{th}$ order column vector, be your eigenvector. Then for the eigenvalue $\lambda_{1}$, we know that $AX=\lambda_{1}X$.

Sub the value of $\lambda_{1}$ and solve the equation. **I'd recommend moving all terms to one side to make the RHS zero.** Solve the system and express the basic variables in terms of the free ones. For example, if you have a matrix of order 2, $x_{1}=4x_{2}$. This would give you the eigenvector $X=\begin{bmatrix}x_{1} \\ x_{2}\end{bmatrix}=\begin{bmatrix}4x_{2} \\ x_{2}\end{bmatrix}$. Then sub any value of $x_{2}$ you want. *Don't leave the eigenvector in its general form.* So if we set $x_{2}=5$, then $X=\begin{bmatrix}20 \\ 5\end{bmatrix}$.

### Getting the eigenspace
Once you have the eigenvector corresponding its eigenvalue $\lambda_{1}$, the eigenspace $E_{\lambda_{1}}$ is simply $\{cX:c\in \mathbb{R}\}$, where $X$ is the eigenvector. In our above example: $E_{\lambda_{1}}=\left\{c \begin{bmatrix}20 \\ 5\end{bmatrix}:c \in \mathbb{R}\right\}$.

Sometimes, **you may have one basic variable expressed in terms of two free variables.** This usually happens when you have repeated eigenvalues. For example, $x_{1}=4x_{2}-7x_{3}$, while $x_{2}=x_{2}$ and $x_{3}=x_{3}$. Our eigenvector $X$ becomes $\begin{bmatrix}4x_{2}-7x_{3} \\ x_{2} \\ x_{3}\end{bmatrix}$. Sub values and get a specific eigenvector as usual. *But when you write the eigenspace for this, we must express this as a linear combination of two vectors.* Therefore, we rewrite this as $\begin{bmatrix}4x_{2} \\ x_{2} \\ 0\end{bmatrix}+\begin{bmatrix}-7x_{3} \\ 0 \\ x_{3}\end{bmatrix}$. Our eigenspace can then be written as $E_{\lambda}=\left\{x_{2}\begin{bmatrix}4 \\ 1 \\ 0\end{bmatrix}+x_{3}\begin{bmatrix}-7 \\ 0 \\ 1\end{bmatrix}:x_{2},x_{3} \in \mathbb{R}\right\}$. ^e35ca8

This is done because the eigenspace is a vector space, so we're basically expressing it as the span of its [[Basis and dimension#Basis|basis.]] We don't know the dimension of the eigenspace for sure, so its safer to write it in this form. For example, if the eigenspace is a plane in $\mathbb{R}^{3}$, it is two dimensional, so its basis must have two elements. Only using one element in the eigenspace restricts it to a line and doesn't capture the entire eigenspace.

### Basic example
![[WhatsApp Image 2025-05-28 at 09.03.52_5ce29978.jpg|center|600]]
![[WhatsApp Image 2025-05-28 at 09.03.53_2269b733.jpg|center|600]]

### Example with special case of eigenspace
![[WhatsApp Image 2025-05-28 at 09.14.43_5cd80452.jpg|center|600]]
![[WhatsApp Image 2025-05-28 at 09.14.44_9722c171.jpg|center|600]]
![[WhatsApp Image 2025-05-28 at 09.14.44_8cd3b80f.jpg|center|600]]

## Useful properties of eigenvalues
### Determinant and trace
The **product of eigenvalues is given by the determinant and the sum of eigenvalues is the trace** (sum of diagonal elements) of the matrix. This is very useful in rechecking your work and in some proof questions. This result also tells us that *zero is an eigenvalue iff determinant is zero,* as determinant being zero means the product of eigenvalues is zero, which means at least one eigenvalue must necessarily be zero.

### Triangular matrices
**The eigenvalues of a triangular matrix as its diagonal elements.** This is true because when finding $\det(\lambda I-A)$, most of the terms will become zero (because a triangular matrix has many zeros), leaving us with just the diagonal elements as roots.

### Symmetric matrices
If $A$ is a symmetric matrix, then the characteristic polynomial of $A$ has only real roots. **Therefore, all eigenvalues are real.** Also, if $x_{1}$ and $x_{2}$ are two eigenvectors associated with different eigenvalues $\lambda_{1}$ and $\lambda_{2}$, then **the eigenvectors are orthogonal.** 

