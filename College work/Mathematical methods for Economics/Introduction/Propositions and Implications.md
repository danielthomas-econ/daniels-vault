---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/mme
---
Quick access:
[[Propositions and Implications#Propositions|Propositions]]
- [[Propositions and Implications#Open proposition|Open proposition]]

[[Propositions and Implications#Implications|Implications]]
- [[Propositions and Implications#Truth tables|Truth tables]]
- [[Propositions and Implications#Logical equivalence|Logical equivalence]]
- [[Propositions and Implications#Necessary and sufficient conditions|Necessary and sufficient conditions]]


## Propositions
*Assertions that are either true or false are called statements or propositions.* "All individuals who breathe are alive" is an example of a true proposition, while "All individuals who breathe are healthy" is a false proposition.

### Open proposition
An open proposition is one which is **neither true nor false until we select a value for the variable.** For example, $(x+1)^{2}= 4$ is an open proposition. The statement itself is not inherently wrong, but whether or not the proposition is true depends on the value of the variable. In this case, our proposition is true only if $x=1$ and not for other values of $x$.


## Implications
Logical implications are relationships between two propositions where the **second proposition is a logical consequence of the first.** They can be written as $P(x) \implies Q(x)$. This is read as *P implies Q* or *if P then Q.* $\implies$ is called the implication arrow. For example:
- $xy = 0 \implies x=0\: or\: y=0$
- $x$ is a square $\implies$ $x$ is a rectangle

These propositions hold true since for each and every value we substitute in the first proposition, the second one is also true.

> [!tip] The inclusive $or$
> When we use the word $or$ to write implications, we use the inclusive $or$. Therefore, $P\: or \: Q$ means either $P$ or $Q$ or both can be correct. It doesn't mean that strictly only one of $P$ or $Q$ can be correct.

### Truth tables
We can visualize our implications using a truth table. This shows all 4 possibilities in a tabular form. **We can say a statement is a logical implication if we can rule out the 2nd scenario.** In this scenario, proposition $P$ is true while proposition $Q$ is false, meaning our statement is not logically implied.

![[R2aRo.png|center]]

The last two scenarios don't really matter in checking if our statement is logically implied since **the premise is wrong, therefore it cannot be a refutation of our implication.** The cases where our first proposition $P$ is false are called *vacuously true.* The word vacuous means empty; similarly, the last two scenarios are empty to us since the premise is not met anyways.

For example, let proposition $P$ be "All students in our class are B.A. Economics Honors students" and let proposition $Q$ be "All students in the class are students at St. Stephen's College." This is an obvious implication since students not belonging to our college cannot enter the classroom anyways. Now, if we pick out a student from SRCC who is not in our classroom, obviously both propositions fail here. **However, this doesn't mean that our original implication was wrong because the premise of proposition $P$ wasn't met in this example.**

### Logical equivalence
In some cases, both $P\implies Q$ and $Q\implies P$.In this case, *we can write both implications together using* $P \iff Q$.This is read as $P$ is equivalent to $Q$ or $P$ if and only if $Q$. The $\iff$ symbol is called an *equivalence arrow.* We can also abbreviate this symbol as **iff** (its also the latex command for the symbol).


### Necessary and sufficient conditions
Let us take the implication $P \implies Q$. We can write this as **$P$ is a sufficient condition for $Q$**. This is because if we know $P$ is true, that is enough/sufficient for us to know that $Q$ is also true.

We can also write it as **$Q$ is a necessary condition for $P$**. This is because if we have $P$, then we must necessarily also have $Q$, since $Q$ will logically follow from $P$ anyways.

Example: Let us take the implication that *$x$ is a square implies $x$ is a rectangle.* This can be written as:
- A necessary condition for $x$ to be a square is that $x$ is a rectangle
- A sufficient condition for $x$ to be a rectangle is that $x$ be a square.

If $P \iff Q$, then we say that $P$ is *a necessary and sufficient condition* for $Q$.

### Using equations as examples
Let's solve the equation $x+2 = \sqrt{4-x}$.

We start by squaring both sides to get $x^{2}+4x+4= 4-x$. This implies that $x^{2}+5x = 0$. This gives us $x(x+5)=0$, meaning $x = 0$ or $x = -5$. **While $x=0$ is a solution, $x=-5$ is not.** Why is that? 

This is because *squaring equations (our first step) is not a logically equivalent process.* This is because squaring doesn't necessarily work both ways. For example, $1^2$ and $-1^2$ both give $1$ as their output. Therefore, if $a^{2} = b^2$, then $a=b$ or $a=-b$. It is not always necessary that $a=b$.

All the other steps can be written as equivalences, but since our first step cannot, there is no chain of implications going in the opposite direction.