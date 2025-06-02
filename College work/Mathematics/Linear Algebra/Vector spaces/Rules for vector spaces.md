---
color: var(--mk-color-base-70)
tags:
  - "#sem2-flashcards/linear_alg/vector_spaces"
---
Quick access:
- [[#Definition|Definition]]
	- [[#Definition#Non-standard operations|Non-standard operations]]
- [[#Flashcards|Flashcards]]

## Definition
A vector space is a set $V$ defined with operations called *vector addition* and *scalar multiplication.* The following properties must hold:
For every $u,v,w \in V$ and $a,b \in R$,
1) $u+v \in V$ (closure under addition)
2) $au \in V$ (closure under scalar multiplication)
3) $u+v = v+u$ (commutativity under addition)
4) $u+(v+w)=(u+v)+w$ (associativity under addition)
5) $\exists$ an element $0 \in V$ s.t. $0+u=u=u + 0$ (existence of additive identity)
6) $\exists$ an element $-u \in V$ s.t. $u+(-u)=0 + (-u)+u$ (existence of additive inverse)
7) $a(u+v)=au+av$ (distributive law)
8) $(a+b)u=au+bu$ (distributive law)
9) $(ab)u=a(bu)$ (associativity under scalar multiplication)
10) $1u=u$ (identity of scalar multiplication)

To remember this for the exam, remember that after the two closure properties, there are 4 addition properties, two distributive laws and two scalar multiplication properties.

### Non-standard operations
Note that *vector addition and scalar multiplication need not be the regular operations we use on $\mathbb{R}$*. Vector spaces can have their own unique non-standard operations defined as long as they satisfy the ten properties above. We'll denote these operators by $\oplus$ and $\odot$.

Example: $u,v \in V$, $V=\mathbb{R}^{2}$.
$u \oplus v=[u_{1}+v_{1}+1,u_{2}+v_{2}-2]$
$c \odot u=[cu_{1}+c-1,cu_{2}-2c+2]$

To find the additive identity here, we need $u \oplus 0=u$ $\forall$ $u \in V$. Let $[x,y]$ be the additive identity. Then, $u \oplus [x,y]=[u_{1}+x+1,u_{2}+y-2]=[u_{1},u_{2}]$. Therefore, $[x+1,y-2]=[0,0]$ $\implies [x,y]=[-1,2]$. Therefore, $[-1,2]$ is the additive identity. **This tells us that the zero vector is not necessarily the additive identity for every vector space. We just denote the additive identity by zero, that doesn't mean it is equal to zero.** 

To find identity of scalar multiplication, we need $c \odot u = u$ $\forall$ $u \in V$.
If $a$ denotes identity, $a \odot u=[au_{1}+a-1,au_{2}-2a+2]=[u_{1},u_{2}]$. Therefore, $[au_{1}+a-u_{1}-1,au_{2}-2a-u_{2}+2]=[0,0]$ $\implies[a(u_{1}+1)-(u_{1}+1),a(u_{2}-2)-(u_{2}-2)]=[0,0]$
$\implies[(a-1)(u_{1}+1),(a-1)(u_{2}-2)]=[0,0]$.
*The only value of $a$ that satisfies both these equations simultaneously is $a=1$*. Therefore, the identity of scalar multiplication is $1$, even if the vector space is under non-standard operations.



## Flashcards
Q1) For a vector space $V$ and $a \in \mathbb{R}$, show that $a \cdot0=0$.
?
Ans) For these seemingly obvious proofs, *a common first step is to add zero.* This doesn't change the LHS but we can manipulate the zero *to add more terms to our RHS.* This adds more opportunities to group and cancel out things, which helps a lot in our proof.
$$\begin{align}
a\cdot 0 &= a\cdot 0 + 0 \text{ (additive identity)}\\ 
&= a \cdot 0 + (a\cdot 0 + (-a\cdot 0)) \text{ (additive inverse)} \\
&= (a\cdot 0 + a\cdot 0) + (-a\cdot 0) \text{ (associativity)} \\
&= a(0+0) + (-a \cdot 0)  \text{ (distributivity)} \\
&= a \cdot 0 + (-a \cdot 0) \\
&= 0 \text{ (additive inverse}) \\
\end{align}$$<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) For a vector space $V$ with $v \in V$ and $0 \in \mathbb{R}$, show that $0v=0$.
?
Ans) $$\begin{align}
0v &= 0v + 0 \text{ ( additive identity)} \\
&= 0v + (0v + (-0v)) \text{ (additive inverse)} \\
&= (0v+0v) + (-0v) \text{ (associativity)} \\
&= (0+0)v + (-0v)  \text{ (distributivity)} \\
&= 0v + (-0v) \\
&= 0  \text{ (additive inverse)}
\end{align}$$<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q3) For a vector space $V$ with $v \in V$, show that $(-1)v=-v$.
?
Ans) $$\begin{align}
(-1)v &= (-1)v + 0 \text{ (additive identity)} \\
&= (-1)v + (v + (-v)) \text{ (additive inverse}) \\
&= ((-1)v + v) + (-v) \text{ (associativity)} \\
&=((-1)+1)v + (-v) \text{ (distributivity)} \\
&= 0v + (-v) \\
&= -v
\end{align}$$<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

