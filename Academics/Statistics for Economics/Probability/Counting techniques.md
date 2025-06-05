---
color: var(--mk-color-turquoise)
tags:
  - sem1-flashcards/stats/probability
---
Quick access:
[[Counting techniques#Product rule|Product rule]]
	[[Counting techniques#Ordered pairs|Ordered pairs]]
	[[Counting techniques#k-tuples|k-tuples]]
[[Counting techniques#Permutations and combinations|Permutations and combinations]]

When the events in our sample space are equally likely, we can simply say $P(A)=\dfrac{N(A)}{N}$. However, in cases where our outcomes aren't equally likely or $N$ is very large, we can use certain counting techniques to simplify the process of finding these probabilities.

## Product rule
### Ordered pairs
We use this when we have an event with ordered pairs and we wish to count the number of ordered pairs. *If the first element can be selected in $n_1$ ways, and for each of the $n_1$ ways the second element can be chosen in $n_2$ ways, then the number of pairs is $n_1n_2$*.

For example, let's say you are renovating your house. There are 12 plumbers are 9 electricians nearby. In how many possible ways can they be chosen? With $n_1=12$ and $n_2=9$, the product rule says there are $108$ different ways of choosing them. **This works because we had the same number of choices of the second element for each first element.**

### k-tuples
This is an extension of the product rule for ordered pairs. In many cases, we'll have far more than just two ordered events. In this case, we use $k-tuples$. *An ordered collection of $k$ objects is called a* $k-tuple$. Therefore, a collection of $3$ items is a $3-tuple$.

For a $k-tuple$, if there are $n_1$ possible ways to pick the first element; for each choice of the first element there are $n_2$ choices of the second element; for each possible choice of the $k-1^{th}$ element there are $n_k$ choices of the $k^{th}$ element. Then there are $n_1n_2n_{3}....n_k$ possible $k-tuples$.

## Permutations and combinations
Permutations are *an ordered subset.* The number of ways in which a permutation of $r$ objects can be formed from $n$ objects is denoted by $^nP_{r}$ or $P_{{r,n}}=\dfrac{n!}{(n-r)!}$. **This changes if we have repeated objects.** Since repeated objects do not form unique permutations, we must divide them away. The formula becomes $^{n}P_{r}= \dfrac{n!}{(n-r)!\:k_{1}!\:k_{2}!\dots\:k_{n}!}$, where $k_{1,2\dots n}$ tells us how many times the $n^{th}$ object was repeated.

Eg: A, B, C, D. If we want to arrange them in a permutation of 3 out of 4, then $n=4,\:r=3$. Therefore, number of permutations will be $\dfrac{4!}{(4-3)!}=4!$.

Combinations are *an unordered subset.* Therefore, ABC = CAB. The number of ways in which a combination of $r$ items can be formed from $n$ items is denoted by $^nC_{r}$, $C_{{r,n}}$ or $n\choose r$$=\dfrac{n!}{r!(n-r)!}$.

Eg: From an committee of 25 SYs, 10 will be chosen for TY posts. To find the number of possible combinations, we set $n=25,\:r=10$ and apply the combination formula (since order doesn't matter here). Doing that, we get $^{25}C_{10}=\dfrac{25!}{10!15!}$.


## Flashcards
Q1) Solve part b)
![[UntitledMNZVRAIOEWAFIJP.jpg|center|500]]
?
Ans) $P(\text{At least one C})=\dfrac{{2\cdot P(\text{one C})}+P(\text{two C})}{\text{Total outcomes}}=\dfrac{{2(^1C_{1}\cdot{^3C_{1})}+(^2C_{2})}}{^5C_{2}}=\dfrac{{2(3)+1}}{10}=\dfrac{7}{10}$

Q2) If there are 5 different catalysts we can use in an experiment and we run this experiment 5 times, what is the probability that we use different catalysts each time?
?
Ans) $P(\text{Different catalysts})=\dfrac{{5\times 4\times 3\times 2\times 1}}{5\times 5\times 5 \times 5 \times 5}$. The numerator is $5!$ because *once you pick a certain catalyst, it cannot be picked again,* reducing the total catalysts available to 4. This goes on an on, *giving us $5!$*. The denominator isn't subject to the same restriction, so it is simply $5^5$.


Q3) ![[UntitledOORQ3FJI2RH3.jpg|center|500]]
?
Ans) a) Number of ways = $^{20}C_{3}=1140$ ways
-
b) There are two ways:
i) Since we are excluding the best machinist, *now we only have 19 total machinists to choose from.* This means the total ways are $^{19}C_{3}=969$ ways.
ii) We can take Ways without best machinist = Total ways - Ways with best machinist. To find ways with best machinist, *we consider the first slot to be fixed (with the best machinist), leaving only two slots left for 19 machinists.* This gives us $1140- ^{19}C_{3}= 1140-171=969$ ways.
-
c) We use the complement method here. Ways with at least one of the 10 best = Total ways - Ways without any of the 10 best. To find the ways without any of the best 10, we only have 10 machinists to fill up 3 slots. Therefore, it becomes $1140-^{10}C_{3}=1140-120=1020$ ways.
-
d) Sub the values we already have to get $\dfrac{969}{1140}=0.85$.

Q4) ![[UntitlednjrvnjnjnijopkopkokpjinjbuFW.jpg|center|500]]
?
Ans)![[Pasted image 20241006131247.png|center|600]]![[Pasted image 20241006131327.png|center|600]]

