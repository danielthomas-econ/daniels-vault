---
color: var(--mk-color-turquoise)
tags:
  - sem1-flashcards/stats/probability
---
Quick access
- [[#Conditions for independence|Conditions for independence]]
- [[#Flashcards|Flashcards]]


## Conditions for independence
It is not necessary that the probability of event $A$ changes if event $B$ occurs. In this case, $A$ and $B$ are *independent events since the occurrence of one doesn't affect the occurrence of the other.* Mathematically, we'd write it as $P(A|B)=P(A)$.

**If two events are mutually exclusive, they cannot be independent.** Let $A=\text{\{head}\}$ and $B=\text{\{tail\}}$. If we get a tail, we cannot possibly get a head too. Therefore, these events are mutually exclusive. This means that $P(A|B)=0\ne P(A)$. Therefore, mutually exclusive events can never be independent.

By substituting the definition of independent events into the [[Academics/Statistics for Economics/Probability/Conditional probability#Multiplication rule|multiplication rule,]] we get $P(A\cap B)=P(A)\cdot P(B)$. To calculate independence of more than 2 events, simply use $P(A_{1}\cap A_{2}\dots \cap A_{k})=P(A_{1})P(A_{2})\dots P(A_{k})$. **Multiple events can be pairwise independent, but that doesn't imply that they are all mutually independent.**

---
Example: It is known that $30\%$ of washing machines under warranty and $10\%$ of dryers under warranty made by a certain company require servicing. What is the probability that both machines will need warranty service?
?
Ans) The probability that a washing machine and a dryer will need service are independent of one another. *The washing machine requiring service does not increase or decrease the chance that a dryer will need service.* Therefore, $P(A\cap B)= P(A)\cdot P(B)=(0.3)(0.1)=3\%$.

---

## Flashcards
Q1) ![[Untitledvvvvv3qfifh4w90f.jpg|center|500]]
?
Ans) a) Since $A$ and $B$ are two independent events, *they do not affect each other in any way.* Therefore, $P(\text{Europe is unsuccessful})=1-0.7=0.3$.
-
b) $P(A\cup B)=P(A)+P(B)-P(A\cap B)=0.4+0.7-(0.4)(0.7)=0.82$. The key here is that **since they are independent events, we know that $P(A\cap B)=P(A)P(B)$**.
-
c) We are asked to find $P(A\cap B'|A\cup B)$. This simplifies to $\dfrac{{P((A\cap B')\cap(A\cup B))}}{P(A\cup B)}$. If you sketch out a Venn diagram, you'll see that $A\cap B'$ **is a subset of** $A\cup B$. Therefore, ${{P((A\cap B')\cap(A\cup B))}}=P(A\cap B')$. We know that since they are independent events, $P(A\cap B')=P(A)P(B')$. We also know $P(A\cup B)=0.82$ from above. Substituting, we get $\dfrac{{(0.4)(0.3)}}{0.82}=0.146$.


Q2) If $A$ and $B$ are two independent events, prove $A'$ and $B$ are also independent.
?
Ans) To prove that, we need to arrive at the conclusion that $P(A'\cap B)=P(A')P(B)$. We'll write $P(A'\cap B)$ as $P(B)-P(A\cap B)$. Since $A$ and $B$ are independent, we have $P(A'\cap B)=P(B)-P(A)P(B)$. *Take $P(B)$ common.* We end up with $P(A'\cap B)=P(B)[1-P(A)]$. **Notice the second term is in complementary form. Sub with its complement.** We are left with $P(A'\cap B)=P(B)P(A')$, which is the condition for independence. Hence proved.