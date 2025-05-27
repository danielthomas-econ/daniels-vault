---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/mme
---
Quick access:
[[Set theory and logical operators#Set operations|Set operations]]
[[Set theory and logical operators#Subsets|Subsets]]
	[[Set theory and logical operators#Proving set equivalence using subsets|Proving set equivalence using subsets]]
[[Set theory and logical operators#Logical operators as set operations|Logical operators as set operations]]
[[Set theory and logical operators#Proofs|Proofs]]

## Set operations
The main set operators are:
- Union ($\cup$) - Takes all elements from both sets
- Intersection ($\cup$) - Takes elements common in both sets
- Complement ($A'$) - Takes all elements in the universal set that do not belong to $A$.
- Set difference ($\setminus$) - Takes all elements in set $A$, and removes all elements from set $B$ *(part of $A$ that doesn't overlap with $B$).*
- Symmetric difference ($\triangle$) - Takes elements in either $A$ or $B$, but not in both.
![[Pasted image 20241003183911.png]]

We can express set difference and symmetric difference using unions and intersections. **These are important since we can use them as substitutions in proofs.**
- $A\setminus B=A\cap B^{\prime}$
- $A\triangle B = (A\setminus B)\cup(B\setminus A)$
- $A\triangle B=(A\cup B)\setminus(A\cap B)$
## Subsets
Let's understand subsets in logic with an example. 
- Let $P(x):\:x^2=4$ and $A=${$x\in R\:|\:P(x)\:is\:true$}, $A=${$-2,2$}. 
- Let $Q(x):\:x=2$ and let set $B=${$x\in R\:|\:Q(x)\:is\:true$}, $B=${$2$}.

In this case, $Q(x)\implies P(x)\iff B\subset A$. $Q(x)$ is true $\implies$ $x=2$ $\implies\:P(x)$ is true. However, the opposite is not true. We cannot say that $P(x)\implies Q(x)$ since $Q(x)$ does not account for $-2$.

**We can generalize this statement accordingly:** 
If $A=${$x\in R\:|\:P(x)\:is\:true$} and $B=${$x\in R\:|\:Q(x)\:is\:true$}, then if $Q(x)\implies P(x)$ for all $x$, then $B\subseteq A$. This is true since *every element $x$ that satisfies $Q(x)$ (therefore belonging to $B$) must also satisfy $P(x)$ (therefore belonging to $A$).* 

### Proving set equivalence using subsets
We can prove that two sets $A$ and $B$ are equal by **checking if they are subsets of each other.** If $A\subset B$ and $B \subset A$, the two sets have to be equal. Therefore, $A=B$.

## Logical operators as set operations
There are three main logical operators: $and$, $or$, and $not$. *We can also represent these operators through set operations.* The logical operators relate to set operations as:
- $or$ is the same as $\cup$ 
- $and$ is the same as $\cap$
- $not$ is the same as $A^\prime$

This means we can rewrite $P(x)$ or $Q(x)$ is true as $P\cup Q$ or $P(x)$ and $Q(x)$ is true as $P\cap Q$.

## Proofs
Q1) Prove $(A\cup B)\setminus C=(A\setminus C)\cup (B\setminus C)$
?
Ans) $(A\cup B)\setminus C=(A\setminus C)\cup (B\setminus C)$ can be rewritten as $(A\cup B)\cap C^{\prime}=(A\cap C^{\prime})\cup(B\cap C^{\prime})$. This is because $X\setminus Y=X\cap Y^{\prime}$. The RHS can be rewritten as $(A\cup B)\cap C^{\prime}$ due to the distributive law. Therefore, LHS = RHS.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Prove $A\cap B\subseteq A \cup B$.
?
Ans) Suppose $x \in A\cap B$. Then $x\in A\text{ and }x\in B$ *- S1.* If $x\in A\cup B$, then $x\in A\text{ or }x\in B$. From S1, we know that $x$ is in both $A$ and B. Therefore, $x$ will certainly belong to $A$ or $B$. Therefore, any element $x$ in set $A\cap B$ will belong to the set $A\cup B$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q3) Prove $(A\cup B)\setminus(A\cap B)=(A\setminus B)\cup(B\setminus A)$.
?
Ans) $(A\cup B)\setminus(A\cap B)=(A\cup B)\cap(A\cap B)'$
$=(A\cup B)\cap(A'\cup B')$.
Expand this.
$=(A\cap A')\cup(A\cap B')\cup(B\cap A')\cup(B\cap B')$. **We know that $(A\cap A')$ and $(B\cap B')$ are null sets.** Therefore,
$=(A\cap B')\cup(B\cap A')$
$=(A\setminus B)\cup(B\setminus A)$.
Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
