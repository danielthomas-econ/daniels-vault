---
color: var(--mk-color-base-70)
tags:
  - "#sem2-flashcards/linear_alg/vector_spaces"
---
Quick access:
- [[#Definition|Definition]]
- [[#Span|Span]]
	- [[#Span#Properties of span|Properties of span]]
	- [[#Span#Finding span|Finding span]]

## Definition
Let $S$ be a non-empty subset of a vector space $V$. $v \in V$ is stb a linear combination of elements of $S$ if $\exists$ $v_{1},v_{2},\dots,v_{n} \in S$ and $c_{1},c_{2},\dots,c_{n} \in \mathbb{R}$ s.t. $v=c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}$.

Example: Let $V=\mathbb{R}^{3}$. $S=\left\{[1,0,0], [1,1,0]\right\}$. Then, $v=[3,1,0]\in V$ is a linear combination of $S$ as $\exists$ $c_{1} = 2,c_{2}=1 \in \mathbb{R}$ s.t. $[3,1,0]=2[1,0,0]+1[1,1,0]$. 

## Span
Let $S$ be any non-empty subset of a vector space $V$. Span of $S$ is denoted by $\text{span}(S)$ and *is the set of all linear combinations of the elements of $S$*. Therefore, $\text{span}(S)=\left\{c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}:v_{i} \in S, c_{i}\in \mathbb{R}\right\}$.

Example: Let $S=\left\{[1,0],[0,1]\right\}\subset \mathbb{R}^{2}$. Then, $\text{span}(S)=\left\{c_{1}[1,0]+ c_{2}[0,1]:c_{1},c_{2} \in \mathbb{R}\right\}$ $=\left\{[c_{1},c_{2}]:c_{1},c_{2} \in \mathbb{R}\right\}$ $= \mathbb{R}^{2}$.

### Properties of span
1) $\text{span}(S)$ is a **subspace** of $V$. If all scalars are zero, then zero belongs to $\text{span}(S)$. The sum of two elements of $\text{span}(S)$ is another linear combination of elements of $S$, so it must belong to $\text{span}(S)$. Same logic for scalar multiplication.

2) If $W$ is a subspace of $V$ and $S \subseteq W$, then $\text{span}(S)\subseteq W$. This is true because $W$ is closed under addition and scalar multiplication, so all linear combinations of $S$ must be in $W

3) $S \subseteq \text{span}(S)$. *Each $v_{i} \in S$ can be written as a linear combination* by taking its corresponding $c_{i}=1$ and all other scalars equal to zero.

4) **$\text{span}(S)$ is the smallest subspace of $V$ containing** $S$. Any subspace containing $S$ must contain all the linear combinations of $S$ since subspaces are closed under addition and scalar multiplication. Therefore, the smallest subspace containing $S$ is the subspace which contains only the linear combinations of $S$ and nothing more, which is $\text{span}(S)$.

5) $\text{span}(\varnothing)=\left\{0\right\}$. An empty linear combination (lc with no vectors) is defined to be $\left\{0\right\}$ by convention so that $\text{span}(S)$ is always a subspace (vector space must contain $0$).

6) The spanning set of an eigenspace is a set containing its corresponding eigenvector(s).

### Finding span
While we can use scalars $c_{1},c_{2}\dots,c_{n} \in \mathbb{R}$ to find span, it can get complicated if there are a lot of vectors. **The best method to find span is to put the vectors as rows in a matrix and find the row space of the matrix.** Since the [[Row space of a matrix|row space]] is the set of all linear combinations of the rows of a matrix, it is equivalent to span.

Another benefit with putting the vectors in a matrix is that *we can reduce the matrix to RREF to get many zeros. This does not change the row space.* Therefore, we end up with a much simpler expression of the span since most elements have become zeros.

Example:![[WhatsApp Image 2025-06-02 at 10.40.48_73050db9.jpg]]
**Be careful if your original set is not from $\mathbb{R}^n$**. Suppose our set $S$ is from $P_{3}$. **$\mathbb{R}^4$ is isomorphic to $P_{3}$**, **but the spaces aren't equal.** Therefore, take the coefficients from $S$ and reduce the matrix to its RREF = $B$. *You can't directly write $\text{row space}(B)=\text{span}(S)$*. Once you get $\text{row space}(B)$, you must mention that these are the coefficients and you'll rewrite it in $P_{3}$. Only then can you say it is equal to $\text{span}(S)$.