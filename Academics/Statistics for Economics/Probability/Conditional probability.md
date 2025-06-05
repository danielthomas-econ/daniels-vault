---
color: var(--mk-color-turquoise)
tags:
  - sem1-flashcards/stats/probability
---
Quick access:
[[Academics/Statistics for Economics/Probability/Conditional probability#What is conditional probability|What is conditional probability]]
[[Academics/Statistics for Economics/Probability/Conditional probability#Finding conditional probability|Finding conditional probability]]
	[[Academics/Statistics for Economics/Probability/Conditional probability#Multiplication rule|Multiplication rule]]
[[Academics/Statistics for Economics/Probability/Conditional probability#Law of total probability|Law of total probability]]
[[Academics/Statistics for Economics/Probability/Conditional probability#Bayes' Theorem|Bayes' Theorem]]

## What is conditional probability
Conditional probability is used to measure cases where *the occurrence of an event B changes the probability of event A occurring.* For example, let's assume that the probability of a random person having a given disease is 5%. If we are provided with the extra information that this person has taken a test for the disease which came out negative, we can say that this person has a less than 5% chance of having the disease. Here, *the probability of event A (being sick) has reduced due to the occurrence of event B (testing negative).*

## Finding conditional probability
**Conditional probability reduces our sample space.** Given that B has occurred, the relevant sample space goes from $\mathbb{S}$ to $B$. *Then, the event $A$ only occurs only if one of the outcomes in $A \cap B$ has occurred.* This also means that $P(A|B)+P(A^{\prime}|B)=1$ once $B$ has occurred. Since the total possible outcomes is now $P(B)$  and a successful event is $P(A \cap B)$, we can say that:

For any two events $A$ and $B$ with $P(B)>0$, the conditional probability of $A$ given that $B$ has occurred is defined by$$P(A|B)=\dfrac{P(A\cap B)}{P(B)}$$
If $P(A|B)>P(A)$, then $A$ and $B$ are said to be **attractive events,** since $B$ occurring increases the probability that $A$ occurs. On the other hand, if $P(A|B)<P(B)$, then they are **repellent events.**

### Multiplication rule
From the above equation, we can derive the multiplication rule for $P(A\cap B)$ by *multiplying both sides by* $P(B)$. This gives us$$P(A\cap B)=P(B)\cdot P(A|B)$$

We can generalize this rule further. $$P(A \cap B \cap C)=P(A)\cdot P(B|A)\cdot P(C|A\cap B)$$
To remember this, first take the probability of $A$. Now that $A$ has happened, we find the probability of $B$ (i.e. $P(B|A)$). Now that both $A$ and $B$ have already happened, the probability of $C$ happening is $P(C|A\cap B)$. Multiply all three to get $P(A\cap B\cap C)$.

## Law of total probability
Let $A_{1},A_{2},A_{3}\dots A_{k}$ be mutually exclusive and exhaustive events, then for any other event $B$, the probability of $B$ is 
$$\begin{align} P(B) &= P(A_{1})P(B|A_{1}) + P(A_{2})P(B|A_{2}) + \dots + P(A_{k})P(B|A_{k}) \\ &= \sum_{i=1}^{k}P(A_{i})P(B|A_{i}) \end{align}
$$
We can better understand this with an example.
A person has 3 email accounts. 70% of her mails go to account 1, 20% to account 2 and 10% to account 3. 1% of the mails on account 1 are spam, 2% are spam for account 2 and 5% for account 3. What is the probability that a randomly selected message is spam?
?
Ans) Let $A=\text{\{message is from account i\} for i = 1, 2, 3}$ and let $B=\text{\{message is spam\}}$. From the given percentages, we have that $P(A_{1})=0.7,\:P(A_{2})=0.2,\:P(A_{3})=0.1$. We also have that $P(B|A_{1})=0.01,P(B|A_{2})=0.02,P(B|A_{3})=0.05$. **Now we just substitute these values in the total probability formula.** Therefore, we have $P(B)=(0.7)(0.01)+(0.2)(0.02)+(0.1)(0.05)=0.16$. The probability that this person gets a spam mail is $1.6\%$.


## Bayes' Theorem
Let $A_{1}, A_{2},A_{3}\dots A_{k}$ be disjoint and exhaustive events. Then for any event B, $P(B)>0$, $$P(A_{j}|B)=\dfrac{P(A_{j}\cap B)}{P(B)}=\dfrac{P(A_{j})P(B|A_{j})}{\sum\limits_{i=1}^{k}P(A_{i})P(B|A_{i})}$$
**We've used the multiplication rule in the numerator and law of total probability in the denominator.** We'll use an example once again to better understand Bayes' Theorem.

> [!tip] One term in the denominator must always be in the numerator
> The Bayes' Theorem essentially *picks out one item from the sum used to find total probability* and puts that in the numerator. To make sure you're on the right path, check if one of the terms you've added in the denominator is also in the numerator.

Let's conduct an experiment where we observe the orders in SSC cafe. Let $A_{1}$ = Maggi, $A_{2}$ = Sandwich and $A_{3}$ = Mince. We are given that $P(A_{1})=0.2, P(A_{2})=0.3, P(A_{3})=0.5$. Let $B$ be the event that the student also buys a cold beverage. We are given $P(B|A_{1})=0.7,P(B|A_{2})=0.4$ and $P(B|A_{3})=0.9$. Find $P(\text{cold beverage})$ and $P(\text{Mince | Cold Beverage})$.
?
Ans) $P(\text{cold beverage})$ can be found through the *law of total probability.* Substituting the values, we get $(0.2)(0.7)+(0.3)(0.4)+(0.5)(0.9)=0.71$.
-
$P(\text{Mince | Cold beverage})$ requires the Bayes' Theorem. This is equal to $\dfrac{P(\text{Mince})P(\text{Cold beverage | Mince})}{P(\text{Cold beverage})}$. This is $\dfrac{{(0.5)(0.9)}}{0.71}=0.63$. **You can see that the $(0.5)(0.9)$ term is both in the numerator and used to calculate the denominator.**


