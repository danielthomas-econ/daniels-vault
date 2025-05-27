---
color: var(--mk-color-orange)
tags:
  - sem2-flashcards/linear_alg/linear_transformations
---

## Definitions
Let $T: V\to W$ be a LT. *T is stb 1-1 if:*
$T(u)=T(v) \implies u = v\:\forall\:u,v \in V$. We can also say that for every $w \in W$, $\exists$ **at most one** $v \in V$ s.t. $T(v)=w$ (every element in the codomain has at most one preimage)

*T is stb onto if:*
For every $w \in W$, $\exists$ **at least one** $v \in V$ s.t. $T(v)=w$ (every element in the codomain has at least one preimage).

## Relation to dimension
From the definition of 1-1 and onto LTs, we can say:
i) $T$ is 1-1 $\implies \text{dim }V\leq \text{dim }W$
ii) $T$ is onto $\implies \text{dim }V \geq \text{dim }W$
iii) If $\text{dim }A>\text{dim }B$ (strictly), then $T$ *cannot be 1-1*
iv) If $\text{dim }A< \text{dim } B$ (strictly), then $T$ *cannot be onto*

Note that these results hold for set cardinality, when the function is defined from one set to another. For vector spaces like $\mathbb{R}^3$ and $\mathbb{R}^2$, both share infinite cardinality. Therefore, we use dimension to tell us which vector space has a larger infinite cardinality. 

## Important theorems
Let $T:V\to W$ be a LT. Then,
$$1)\:T \text{ is 1-1} \iff\text{Ker }T=\{0\} (\text{dim }\text{Ker }T=0)$$
Proof: Let $T$ be 1-1, and let $v \in \text{Ker }T$ be arbitrary.
$T(v)=0$ ($\because v \in \text{Ker }T$)
$=T(0)$ ($\because T$ is a LT and zero goes to zero)
Since $T$ is 1-1, $T(v)=T(0)\implies v=0$.
Since $v$ is an arbitrary element of $\text{Ker }T$, all elements of $\text{Ker }T$ are zero. Therefore, $\text{Ker }T=\{0\}$.

Suppose $\text{Ker }T=\{0\}$.
Consider $T(u),T(v) \in \text{Ker }T$, $u,v \in V$ be arbitrary.
$T(u)=T(v)$ ($\because$ both equal zero)
$\implies T(u)-T(v)=0$
$\implies T(u-v)=0$ ($\because$ T is a LT)
$\implies u-v = 0$ ($\because T$ is a LT, zero goes to zero)
$\implies u=v$
$\therefore$ $T(u)= T(v) \implies u=v$
$\therefore T$ is 1-1.
We have proven the implication both ways.

$$2)\: \text{If } W \text{ is fdvs, } T \text{ is onto} \iff \text{Range }T=W(\text{dim }\text{Range }T=\text{dim } W)$$
Proof: Let $T$ be onto.
$\text{Range } T$ contains all $T(v)$, $v \in V$.
$\therefore w \in \text{Range } T$, $\forall\: w \in W$
$\implies W \subseteq \text{Range }T$
But we know that $\text{Range }T \subseteq W$ (codomain).
$\therefore \text{Range }T=W$, $\text{dim }\text{Range }T=\text{dim } W$

Suppose $\text{dim }\text{Range }T=\text{dim }W$
Since $\text{Range }T \subseteq W$, $\text{Range }T=W$. *This is because if $A$ is a subspace of $B$ but $\text{dim }A=\text{dim }B$*, *then $A=B$*.
$\therefore T$ is onto
We have proven the implication both ways

**The most important use of these two results is that if we want to check for 1-1 and onto, we can simply find the kernel and range of the LT and check for the respective conditions.** This makes the process much simpler.

## Important behaviors of 1-1 and onto functions
Let $T:V\to W$ be a LT. Let $S$ be any LI subset of $V$. Then,
$$\begin{align}
\text{i) If }T \text{ is 1-1},
\text{ then } T(S) = \{T(S):s \in S\}\text{ is also LI in } W
\end{align} $$
In other words, **a 1-1 LT takes a LI set in V to a LI set in W.**

Now consider $S$ to be a spanning set of $V$.
$$\text{ii) If } T \text{ is onto, then } T(S) \text{ spans }W $$
*Therefore, an onto LT takes a spanning set in V to a spanning set in W.*

Proof i)
Given: $T: V\to W$ is a 1-1 LT, $S$ is a LI subset of $V$.
To prove: $T(S)$ is also LI in $W$
Consider some arbitrary finite subset of $S=\{v_{1},v_{2},\dots,v_{n}\}$ and also $T(S)$ $\{T(v_{1}),T(v_{2}),\dots,T(v_{n})\}$. *We take an arb finite subset as we don't know if $S$ is infinite.*
Consider $c_{1}T(v_{1})+c_{2}T(v_{2})+\dots+c_{n}T(v_{n})=0$ (check for $T(S)$ being LI)
$\implies T(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n})=0$
$=T(0)$ ($\because$ $T$ is a LT and zero goes to zero).
$\implies c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}=0$
$\implies c_{1},c_{2},\dots,c_{n}=0$ ($\because$ $v_{i}\in S$ are LI, so the scalars must be zero)
$\implies T(v_{1}), T(v_{2}),\dots,T(v_{n})$ are LI
$\implies$ any arbitrary subset of $T(S)$ is LI
$\implies$ $T(S)$ is LI.
Hence proved.

Proof ii)
Given: $T:V\to W$ is onto, $S$ is a spanning set of $V$.
To prove: $T(S)$ is a spanning set of $W$.
We know that since $T$ is onto, $\forall\: w\in W$, $\exists\:v \in V$ s.t. $T(v)=w$.
We also know that since $S$ is a spanning set of $V$, $\forall \: v \in V$, $\exists\: v_{1},v_{2},\dots,v_{n} \in S$ and $c_{1},c_{2},\dots,c_{n} \in \mathbb{R}$ s.t. $c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}=0$
$\therefore\: T(v)=T(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n})$
$\implies w = T(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n})$
$\implies w = c_{1}T(v_{1})+c_{2}T(v_{2})+\dots+c_{n}T(v_{n})$
$\implies W \subseteq \text{span}(T(S))$
But we know that $\text{span}(T(S)) \subseteq W$ since $W$ is the codomain.
Therefore, $W=\text{span}(T(S))$.











## Flashcards
Q1) Prove $T$ is 1-1 $\iff$ $\text{Ker }T=\{0\}$ ($\text{dim }\text{Ker }T=0$)
?
Proof: Let $T$ be 1-1, and let $v \in \text{Ker }T$ be arbitrary.
$T(v)=0$ ($\because v \in \text{Ker }T$)
$=T(0)$ ($\because T$ is a LT and zero goes to zero)
Since $T$ is 1-1, $T(v)=T(0)\implies v=0$.
Since $v$ is an arbitrary element of $\text{Ker }T$, all elements of $\text{Ker }T$ are zero. Therefore, $\text{Ker }T=\{0\}$.
.
Suppose $\text{Ker }T=\{0\}$.
Consider $T(u),T(v) \in \text{Ker }T$, $u,v \in V$ be arbitrary.
$T(u)=T(v)$ ($\because$ both equal zero)
$\implies T(u)-T(v)=0$
$\implies T(u-v)=0$ ($\because$ T is a LT)
$\implies u-v = 0$ ($\because text{Ker }T=\{0\}$)
$\implies u=v$
$\therefore$ $T(u)= T(v) \implies u=v$
$\therefore T$ is 1-1.
We have proven the implication both ways.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Prove that $\text{If } W \text{ is fdvs, } T \text{ is onto} \iff \text{Range }T=W(\text{dim }\text{Range }T=\text{dim } W)$
?
Proof: Let $T$ be onto.
$\text{Range } T$ contains all $T(v)$, $v \in V$.
$\therefore w \in \text{Range } T$, $\forall\: w \in W$
$\implies W \subseteq \text{Range }T$
But we know that $\text{Range }T \subseteq W$ (codomain).
$\therefore \text{Range }T=W$, $\text{dim }\text{Range }T=\text{dim } W$
.
Suppose $\text{dim }\text{Range }T=\text{dim }W$
Since $\text{Range }T \subseteq W$, $\text{Range }T=W$. *This is because if $A$ is a subspace of $B$ but $\text{dim }A=\text{dim }B$*, *then $A=B$*.
$\therefore T$ is onto
We have proven the implication both ways.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q3) Prove that if $S$ is a LI subset of $V$ and $\text{if }T \text{ is 1-1},\text{ then } T(S) = \{T(S):s \in S\}\text{ is also LI in } W$.
?
Proof: Given: $T: V\to W$ is a 1-1 LT, $S$ is a LI subset of $V$.
To prove: $T(S)$ is also LI in $W$
Consider some arbitrary finite subset of $S=\{v_{1},v_{2},\dots,v_{n}\}$ and also $T(S)$ $\{T(v_{1}),T(v_{2}),\dots,T(v_{n})\}$. *We take an arb finite subset as we don't know if $S$ is infinite.*
Consider $c_{1}T(v_{1})+c_{2}T(v_{2})+\dots+c_{n}T(v_{n})=0$ (check for $T(S)$ being LI)
$\implies T(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n})=0$
$=T(0)$ ($\because$ $T$ is a LT and zero goes to zero).
$\implies c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}=0$
$\implies c_{1},c_{2},\dots,c_{n}=0$ ($\because$ $v_{i}\in S$ are LI, so the scalars must be zero)
$\implies T(v_{1}), T(v_{2}),\dots,T(v_{n})$ are LI
$\implies$ any arbitrary subset of $T(S)$ is LI
$\implies$ $T(S)$ is LI.
Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q4) Prove that if $S$ is a spanning set of $V$, and $\text{if } T \text{ is onto, then } T(S) \text{ spans }W$.
?
Proof: Given: $T:V\to W$ is onto, $S$ is a spanning set of $V$.
To prove: $T(S)$ is a spanning set of $W$.
We know that since $T$ is onto, $\forall\: w\in W$, $\exists\:v \in V$ s.t. $T(v)=w$.
We also know that since $S$ is a spanning set of $V$, $\forall \: v \in V$, $\exists\: v_{1},v_{2},\dots,v_{n} \in S$ and $c_{1},c_{2},\dots,c_{n} \in \mathbb{R}$ s.t. $c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n}=v$
$\therefore\: T(v)=T(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n})$
$\implies w = T(c_{1}v_{1}+c_{2}v_{2}+\dots+c_{n}v_{n})$
$\implies w = c_{1}T(v_{1})+c_{2}T(v_{2})+\dots+c_{n}T(v_{n})$
$\implies W \subseteq \text{span}(T(S))$
But we know that $\text{span}(T(S)) \subseteq W$ since $W$ is the codomain.
Therefore, $W=\text{span}(T(S))$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>