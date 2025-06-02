---
color: var(--mk-color-base-70)
tags:
  - "#sem2-flashcards/linear_alg/vector_spaces"
---
Quick access:
- [[#Definition|Definition]]
- [[#Requirements to be a subspace|Requirements to be a subspace]]
- [[#Intersection of subspaces|Intersection of subspaces]]
- [[#Flashcards|Flashcards]]

## Definition
Let $V$ be a vector space. Then, a **subset $W$ of $V$ is stb a subspace if $W$ itself is a vector space** under the same compositions as that of $V$. Note that $\left\{0\right\}$ is a trivial subspace of $V$. Also, a subspace must contain $0$ as that is a requirement for it to be a vector space.

## Requirements to be a subspace
If $V$ is a vector space and $W \subseteq V$, then all elements of $W$ must follow the same properties as $V$. Therefore, elements of $W$ will follow commutativity, associativity, distributivity etc. **However, $W$ need not follow closure.** If we add any two elements in $W$, their sum might be in $V$ but not in $W$. *This is because since $V$ is a vector space, addition is closed under $V$*. *But that does not mean addition is closed under $W$*. 

**Therefore, a non-empty subset $W$ of a vector space $V$ is a subspace of $V$ $\iff$ $W$ is closed under vector addition and scalar multiplication.** Therefore, we must prove:
1) $W$ is non-empty $(0 \in W)$
2) $W$ is closed under vector addition
3) $W$ is closed under scalar multiplication

## Intersection of subspaces
The intersection of an arbitrary number of subspaces is always a subspace. However, *union of subspaces may not be a subspace.* 

Proof: Let $W_{1},W_{2}$ be subspaces of a vector space $V$. We have to show that $W= W_{1} \cap W_{2}$ is a subspace.

Since $0 \in W_{1},W_{2}$ (subspace must be non-empty), $0 \in W$. Therefore, $W$ is non-empty - *1*

Consider $u,v \in W=W_{1} \cap W_{2}$. Therefore, $u,v \in W_{1}$ and $u,v \in  W_{2}$.
$\implies u+v \in W_{1},u+v \in W_{2}$ (closure under addition).
$\implies u+v \in W_{1} \cap W_{2}$
$\implies u+v \in W$ 
Therefore, $W$ is closed under addition - *2*

Consider $u \in W=W_{1} \cap W_{2}$ and $c \in \mathbb{R}$. $u \in W_{1}, u \in W_{2}$.
$\implies cu \in W_{1}, cu \in W_{2}$ (closure under scalar multiplication)
$\implies cu \in W_{1} \cap W_{2}$ 
$\implies cu \in W$
Therefore, $W$ is closed under scalar multiplication - *3*

From 1,2 and 3, $W$ is a subspace of $V$. **This proof generalizes to the intersection of $n$ subspaces.** If we consider $W=W_{1} \cup W_{2}$, for $u,v \in W_{1} \cup W_{2}$, we can't tell exactly where $u+v$ will be. If $u \in W_{1}$ and $v \in W_{2}$, there's no closure property to tell us where $u+v$ is. This is why the union of subspaces isn't necessarily a subspace.




## Flashcards
Q1) Show that the intersection of two arbitrary subspaces is a subspace.
?
Proof: Let $W_{1},W_{2}$ be subspaces of a vector space $V$. We have to show that $W= W_{1} \cap W_{2}$ is a subspace.
.
Since $0 \in W_{1},W_{2}$ (subspace must be non-empty), $0 \in W$. Therefore, $W$ is non-empty - *1*
.
Consider $u,v \in W=W_{1} \cap W_{2}$. Therefore, $u,v \in W_{1}$ and $u,v \in  W_{2}$.
$\implies u+v \in W_{1},u+v \in W_{2}$ (closure under addition).
$\implies u+v \in W_{1} \cap W_{2}$
$\implies u+v \in W$ 
Therefore, $W$ is closed under addition - *2*
.
Consider $u \in W=W_{1} \cap W_{2}$ and $c \in \mathbb{R}$. $u \in W_{1}, u \in W_{2}$.
$\implies cu \in W_{1}, cu \in W_{2}$ (closure under scalar multiplication)
$\implies cu \in W_{1} \cap W_{2}$ 
$\implies cu \in W$
Therefore, $W$ is closed under scalar multiplication - *3*
.
From 1,2 and 3, $W$ is a subspace of $V$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Show that an eigenspace is a subspace of $\mathbb{R}^n$.
?
Ans) ![[WhatsApp Image 2025-06-02 at 09.21.06_774e38c5.jpg]]
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
