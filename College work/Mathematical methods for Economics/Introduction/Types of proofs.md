---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/mme
---
We'll use the proof that the sum of all consecutive integers is odd as an example for all the types of proofs. If any number $n$ can be expressed as $2k$, $n$ is even, and if $n$ can be expressed as $2k+1$, $n$ is odd (where $k$ is an integer). We also define two integers $a$ and $b$ such that $b=a+1$. These definitions are necessary to carry forward with our proofs.

Quick access:
[[Types of proofs#Direct proof|Direct proof]]
[[Types of proofs#Proof by contrapositive|Proof by contrapositive]]
[[Types of proofs#Proof by contradiction|Proof by contradiction]]
[[Types of proofs#Proof by induction|Proof by induction]]

## Direct proof
The basic idea of a direct proof that $P\implies Q$ is that we start with the assumption that $P$ is true, and then use that to show $Q$ must also be true.

Proof: Assume $a,\:b$ are consecutive integers.
We know that $b=a+1$. Therefore, $a+b = a+(a+1)$.
**This can be expressed as $2a+1$, which is of the form** $2k+1$. Therefore, the sum of $a$ and $b$ is an odd number.

## Proof by contrapositive
We know that a [[Types of implications#Contrapositive|contrapositive]] statement is $\sim Q\implies \sim P$, and is logically equivalent to $P\implies Q$. Therefore, *if we prove the contrapositive of an implication is true, then the original implication must also be true.* 

Proof: The contrapositive statement would be "If $a+b$ is not odd, then $a$ and $b$ are not consecutive integers".

Assuming $a+b$ is not odd, **there does not exist an integer $k$**, such that $a+b=2k+1$. We can rewrite $2k+1$ as $k+(k+1)$. Therefore, $a+b$ cannot equal $k+(k+1)$. **Notice that the terms $k$ and $k+1$ are consecutive.** Therefore, $a+b$ cannot be consecutive.

We have proved that $\sim Q\implies\sim P$. Therefore, $P\implies Q$ by contrapositive. 

## Proof by contradiction
The idea here is that a proposition is either true or false, it cannot be both. We get a contradiction if *we can show a statement as both true and false* (i.e. a paradox). This implies that our original assumptions were wrong. We prove $P\implies Q$ by **assuming that $P$ and $\sim Q$ are true, which leads to a contradiction.**

Proof: Assume $a,\:b$ are consecutive integers.
Assume $(a+b)$ is **not odd.** (assuming $\sim Q$)
If $(a+b)$ is not odd, there exists no integer $k$ such that $a+b=2k+1$.

We know that $a+b=a+(a+1)=2a+1$. This means that *we cannot express $a+b$ as $2k+1$, but at the same time, we can express it as $2a+1$*. This is a clear logical contradiction which arises from our assumption that $a+b$ is not odd. Therefore, we can conclude that $a+b$ must be odd.

## Proof by induction
Proof by induction aims to prove an infinite number of facts by showing that specific cases hold true. It assumes that if the proposition is true for some value $n$, then it also holds true for $n+1$. 

The first step of induction is to **prove a base case.** Then, we assume $P(n)$ is true for some $n$, and show that this also implies $P(n+1)$ is true. Induction proves that our statement $P(x)$ must be true for all $n$ greater than or equal to the base case.

Proof: Let $P(x)$ be true if $x+(x+1)$ is odd.

*Base case:* Consider $P(1)$. $1 +(1+1)=3$. We know $3$ is odd since it can be written in the form $2k+1$, where $k=1$.

Assume that $P(x)$ is true for some value of $x$. Therefore, $x+(x+1)$ is odd. *Let's add $1$ to each term.* Notice that $(x+1)+(x+1+1)=P(x+1)$. We know that $x+(x+1)$ is odd. **Therefore, adding $2$ to it will result in the new expression also being odd.** Since we get $P(x+1)$ after adding $2$, $P(x+1)$ must also hold true if $P(x)$ is true. 