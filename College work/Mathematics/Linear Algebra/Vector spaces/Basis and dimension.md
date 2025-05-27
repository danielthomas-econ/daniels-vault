---
color: var(--mk-color-base-70)
tags:
  - sem2-flashcards/linear_alg/vector_spaces
---
Quick access:
- [[#Basis|Basis]]
	- [[#Basis#Standard basis|Standard basis]]
	- [[#Basis#Ordered basis|Ordered basis]]
	- [[#Basis#Coordinate vectors|Coordinate vectors]]
- [[#Dimension|Dimension]]
- [[#Size conditions for a set to be a basis|Size conditions for a set to be a basis]]

## Basis
A subset $S$ of a vector space $V$ is stb a basis of $V$ if:
i) $S$ is linearly independent
ii) $span(S) = V$. 
This means *every element of $V$ can be uniquely expressed as a linear combination of the elements of the basis $S$*.

### Standard basis
The **standard basis** is the basis consisting of the most natural vectors from that space. Both $\{[5,7],[3,2]\}$ and $\{[1,0],[0,1]\}$ are bases of $\mathbb{R}^{2}$, but only the latter is the standard basis of $\mathbb{R}^{2}$. The standard basis of $\mathbb{R}^n$ is $\{e_{1},e_{2}\dots,e_{n}\}$ and of $\mathbb{P}_{n}$ is $\{1,x,x^{2}\dots,x^n\}$.

### Ordered basis
A basis of a vector space is *stb an ordered basis if it is an ordered set.* 

### Coordinate vectors
Let $S=\{v_{1},v_{2},\dots,v_{n}\}$ be an ordered basis of an $n$ dimensional vector space $V$. Every $v\in V$ can be **uniquely expressed** as a linear combination of elements of $S$. The coordinate vector of $v$ wrt the ordered basis $S$ is denoted by $[v]_{S}=\left[\begin{smallmatrix}c_{1} \\ c_{2} \\ \dots \\ c_{n} \end{smallmatrix}\right]$, where $c_{i}$ are the scalars used to represent $v$ uniquely as a linear combination of elements of $S$. *The entries of $[v]_{S}$ are called the coordinates of $v$ wrt $S$*.

**If the basis $S$ is the standard basis, then $[v]_{S}$ is just the coefficient of each term.** If $v=\left[\begin{smallmatrix}2 \\ 5 \\ -1 \end{smallmatrix}\right]$ and $S=\{e_{1},e_{2},e_{3}\}$, then $[v]_{S}=\left[\begin{smallmatrix}2 \\ 5 \\ -1 \end{smallmatrix}\right]$ as $S$ is the standard basis of $\mathbb{R}^3$. This is because we can write $v$ as $2e_{1}+5e_{2}-1e_{3}$, so putting the $c_{i}$ into the coordinate vector just gives you the original vector. 

## Dimension
Let $V$ be a vector space having a basis $B$. Then, the dimension of $V$, denoted by $\text{dim }V$, is *the number of elements in the basis $B$*.

## Size conditions for a set to be a basis
Let $V$ be a fdvs (finite dimension vector space).

i) Let $S$ be a finite subset of $V$ s.t. $span(S)=V$.
Then, $\text{dim }V \leq |S|$.
Also, $\text{dim }V=|S|\iff$ $S$ is a basis of $V$ (minimal spanning)

ii) Let $T$ be a linearly independent subset of $V$.
Then, $|T| \leq \text{dim }V$ and $T$ is finite
Also, $|T|=\text{dim }V\implies$ $T$ is a basis of $V$. (maximal LI)

In other words, if $\text{dim }V=n$, then:
**i) Any spanning set with $n$ vectors is LI and is a basis**
**ii) Any LI set with $n$ vectors also spans $V$ and is a basis**

Therefore, *a basis is the minimal spanning (removing a vector destroys spanning) and maximal LI (adding any vector introduces dependence) subset of $V$*.

