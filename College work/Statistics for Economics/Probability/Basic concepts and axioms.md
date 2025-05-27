---
color: var(--mk-color-turquoise)
tags:
  - sem1-flashcards/stats/probability
---
Quick access:
[[Basic concepts and axioms#Events and sample space|Events and sample space]]
[[Basic concepts and axioms#Sets and probability|Sets and probability]]
[[Basic concepts and axioms#Axioms of probability|Axioms of probability]]

## Events and sample space
Probability is based on observing the results of certain 'experiments'. Like scientific experiments, here we use the word **experiments to refer to any event whose outcome is uncertain.** Since the outcome of an experiment is uncertain, we cannot guarantee only one outcome. Therefore, there are **multiple outcomes for any experiment, called the sample space.** We typically denote the sample space as $\mathbb{S}$.

*Any subset of the outcomes in the sample space is called an event.* In simple terms, the outcomes that we observe are called events. An event is called simple if it consists of exactly one outcome and compound if it has multiple elements.

## Sets and probability
In probability, we'll often use the language of set theory to study our events. Previously, we stated that for any event $A$, we can say $A\subseteq \mathbb{S}$. We'll use some more operations to create and define new events.

*The complement of an event $A$ is $A^{\prime}$ and it denotes all outcomes not in $A$*. If $\mathbb{S}=\{1,2,3,4,5\}$ and $A=\{2,3\}$, then we know that $A^{\prime}\{1,4,5\}$.

The union of two events $A\cup B$ means *A or B.* This includes events that happen in at least one of the sets. The intersection of two events $A\cap B$ means *A and B.* This requires the event to be both in $A$ and in $B$ to qualify as $A\cap B$.

Applying this to probability, $P(A\cup B)=P(A)+P(B)-P(A\cap B)$. If we have three different events, $P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(A\cap B)-P(A\cap C)-P(B\cap C)$$+P(A\cap B\cap C)$.

## Axioms of probability
There are three main axioms in probability. These are results that we all intuitively know are true and don't need to prove. 

1. For any event $A$, $P(A)>0$.
2. $P(\mathbb{S})=1$
3. If $A_1,A_2,A_{3}...$ is an infinite collection of disjoint sets, then $P(A_{1}\cup A_{2}\cup A_{3}\cup...)=\sum\limits_{i=1}^{\infty}P(A_i)$.

From these axioms, we can also derive other statements. For example, $P(A)+P(A^{\prime})=1$. This is very useful since in some cases, finding the probability of the complement of the event is a lot more straightforward.