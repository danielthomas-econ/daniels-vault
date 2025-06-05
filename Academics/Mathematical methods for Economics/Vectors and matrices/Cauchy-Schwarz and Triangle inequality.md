---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/mme/vectors_and_matrices"
---

## Cauchy-Schwarz inequality
The Cauchy-Schwarz inequality states that:$$|a\cdot b| \leq \lvert\lvert a \rvert\rvert \cdot \lvert\lvert b \rvert\rvert $$
Proof:
$|a \cdot b| \leq \lvert\lvert a \rvert\rvert\cdot \lvert\lvert b \rvert\rvert$ $\implies$ $-(\lvert\lvert a \rvert\rvert\cdot \lvert\lvert b \rvert\rvert)\leq a\cdot b \leq \lvert\lvert a \rvert\rvert\cdot \lvert\lvert b \rvert\rvert$
$\implies -1 \leq \dfrac{a}{\lvert\lvert a \rvert\rvert} \cdot \dfrac{b}{\lvert\lvert b \rvert\rvert}\leq 1$
$\implies -1\leq p\cdot q\leq 1$, where $p$ and $q$ are unit vectors.
*To prove the Cauchy-Schwarz inequality, we need to prove that the dot product of two unit vectors lies between -1 and 1.*
Consider $(p-q)\cdot(p-q)=\lvert\lvert p-q \rvert\rvert^{2} \geq 0$.
Therefore, $\lvert\lvert p \rvert\rvert^{2}-2p\cdot q+\lvert\lvert q^{2} \rvert\rvert\geq 0$
$\implies 2-2p\cdot q \geq 0$ ($p$ and $q$ are unit vectors)
$\implies -2p\cdot q \geq -2$
$\implies p\cdot q \leq 1$ - **1**
.
Consider $(p+q)\cdot(p+q) = \lvert\lvert p+q \rvert\rvert^{2}\geq 0$
Therefore, $\lvert\lvert p \rvert\rvert^{2} +2p\cdot q+\lvert\lvert q \rvert\rvert^{2}\geq 0$
$\implies 2+2p\cdot q \geq 0$
$\implies 2p\cdot q \geq -2$
$\implies p \cdot q \geq -1$ - **2**
.
From 1 and 2, we see that $-1 \leq p \cdot q \leq 1$, so Cauchy-Schwarz inequality must hold.


## Triangle inequality
This is also called Minkowski's inequality. This inequality states that $\lvert\lvert x+y \rvert\rvert \leq \lvert\lvert  x \rvert\rvert+\lvert\lvert y \rvert\rvert$.

Proof:
$$\begin{align}
\lvert\lvert x+y \rvert\rvert ^{2} &= (x+y) \cdot (x+y) \\
&= \lvert\lvert x \rvert\rvert ^{2}+\lvert\lvert y \rvert\rvert^{2} + 2 x\cdot y \\
&\leq \lvert\lvert x \rvert\rvert^{2} + \lvert\lvert y \rvert\rvert^{2} +2 |x\cdot y| \\
&=\lvert\lvert x \rvert\rvert^{2} + \lvert\lvert y \rvert\rvert^{2} + 2\lvert\lvert x \rvert\rvert \lvert\lvert y \rvert\rvert \text{ (Cauchy-Schwarz)}  \\
&=(\lvert\lvert x \rvert\rvert +\lvert\lvert y \rvert\rvert )^{2} \\    \implies \lvert\lvert x+y \rvert\rvert ^{2} &\leq (\lvert\lvert x \rvert\rvert +\lvert\lvert y \rvert\rvert )^{2}
\end{align}$$
Since both these numbers are positive, we can say that $\lvert\lvert x+y \rvert\rvert \leq \lvert\lvert x \rvert\rvert+\lvert\lvert y \rvert\rvert$. Hence proved.









## Flashcards
Q1) State and prove Cauchy-Schwarz inequality.
?
Proof:
$|a \cdot b| \leq \lvert\lvert a \rvert\rvert\cdot \lvert\lvert b \rvert\rvert$ $\implies$ $-(\lvert\lvert a \rvert\rvert\cdot \lvert\lvert b \rvert\rvert)\leq a\cdot b \leq \lvert\lvert a \rvert\rvert\cdot \lvert\lvert b \rvert\rvert$
$\implies -1 \leq \dfrac{a}{\lvert\lvert a \rvert\rvert} \cdot \dfrac{b}{\lvert\lvert b \rvert\rvert}\leq 1$
$\implies -1\leq p\cdot q\leq 1$, where $p$ and $q$ are unit vectors.
*To prove the Cauchy-Schwarz inequality, we need to prove that the dot product of two unit vectors lies between -1 and 1.*
Consider $(p-q)\cdot(p-q)=\lvert\lvert p-q \rvert\rvert^{2} \geq 0$.
Therefore, $\lvert\lvert p \rvert\rvert^{2}-2p\cdot q+\lvert\lvert q^{2} \rvert\rvert\geq 0$
$\implies 2-2p\cdot q \geq 0$ ($p$ and $q$ are unit vectors)
$\implies -2p\cdot q \geq -2$
$\implies p\cdot q \leq 1$ - **1**
.
Consider $(p+q)\cdot(p+q) = \lvert\lvert p+q \rvert\rvert^{2}\geq 0$
Therefore, $\lvert\lvert p \rvert\rvert^{2} +2p\cdot q+\lvert\lvert q \rvert\rvert^{2}\geq 0$
$\implies 2+2p\cdot q \geq 0$
$\implies 2p\cdot q \geq -2$
$\implies p \cdot q \geq -1$ - **2**
.
From 1 and 2, we see that $-1 \leq p \cdot q \leq 1$, so Cauchy-Schwarz inequality must hold.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) Prove Minkowski's inequality.
?
Proof:
$$\begin{align}
\lvert\lvert x+y \rvert\rvert ^{2} &= (x+y) \cdot (x+y) \\
&= \lvert\lvert x \rvert\rvert ^{2}+\lvert\lvert y \rvert\rvert^{2} + 2 x\cdot y \\
&\leq \lvert\lvert x \rvert\rvert^{2} + \lvert\lvert y \rvert\rvert^{2} +2 |x\cdot y| \\
&=\lvert\lvert x \rvert\rvert^{2} + \lvert\lvert y \rvert\rvert^{2} + 2\lvert\lvert x \rvert\rvert \lvert\lvert y \rvert\rvert \text{ (Cauchy-Schwarz)}  \\
&=(\lvert\lvert x \rvert\rvert +\lvert\lvert y \rvert\rvert )^{2} \\    \implies \lvert\lvert x+y \rvert\rvert ^{2} &\leq (\lvert\lvert x \rvert\rvert +\lvert\lvert y \rvert\rvert )^{2}
\end{align}$$
Since both these numbers are positive, we can say that $\lvert\lvert x+y \rvert\rvert \leq \lvert\lvert x \rvert\rvert+\lvert\lvert y \rvert\rvert$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>