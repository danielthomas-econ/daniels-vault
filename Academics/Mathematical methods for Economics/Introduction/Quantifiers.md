---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/mme
---
Quantifiers are terms used to *specify the quantity of variables that satisfy the premise.* There exists two kinds of quantifiers:
- Universal quantifier: For all, $\forall$
- Existential quantifier: There exists, $\exists$

$\forall$ implies that **every element** in the set will make $P(x)$ true, while $\exists$ implies that **at least one element** in the set will make $P(x)$ true.

## Order of quantifiers matters
We have to always pay attention to the order of quantifiers we use, as they can completely change the meaning of our statements. A common mistake we make is when defining additive inverse. Some people may write:
- $\exists x\in\mathbb{R}\:s.t.\:\forall y\in\mathbb{R},\:x+y=y+x=0$

At first glance, this may seem correct, but there's a mistake here. The problem is that the quantifier $\exists$ means *there is one value of $x$ that satisfies the additive inverse property.* This is obviously wrong, since the additive inverse is different for each number. Therefore, *we should use the quantifier $\forall$ at the start as we want to denote multiple values.* The right way to write the property is $\forall y\in\mathbb{R},\:\exists x\in\mathbb{R}\:s.t.\:x+y=y+x=0$.
