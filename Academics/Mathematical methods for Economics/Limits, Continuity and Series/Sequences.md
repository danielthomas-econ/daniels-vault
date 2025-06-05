---
color: var(--mk-color-pink)
tags:
  - sem1-flashcards/mme
---
Quick access:
[[Sequences#Sequences|Sequences]]
[[Sequences#Convergence of sequences|Convergence of sequences]]
	[[Sequences#Sandwich/Squeeze theorem|Sandwich/Squeeze theorem]]
[[Sequences#Divergence of sequences|Divergence of sequences]]

## Sequences
In general, a function whose domain is the entire set of *positive integers* is called an infinite sequence. If $s$ is an infinite sequence, its terms are denoted as $s_{1}, s_{2},s_{3}$ etc. The sequence itself is denoted by $\{s_{n}\}$.

## Convergence of sequences
In general, a sequence $\{s_{n}\}$ is said to converge to $\alpha$ if $s_{n}$ is arbitrarily close to $\alpha$ for all $n$ sufficiently large. This means $$\lim\limits_{n\to \infty}s_{n}=\alpha$$
Eg: $\{s_{n}\}=\dfrac{1}{n}$ converges to $0$ as when $n\to \infty$, $\dfrac{1}{n} \to 0$.

**We can also write this more mathematically.** A sequence $\{x_{n}\}$ is said to converge to the limit $\lim\limits_{{n\to \infty}}x_{n}=l$, $l\in \mathbb{R}$ if $\forall \:\varepsilon>0$, $\exists \:N\:s.t.\forall\:n\ge N$, $|x_{n}-l|<\varepsilon\iff l-\varepsilon\le x\le l+\varepsilon$. In simple terms, this means *a number l is the limit of a sequence if after a certain value N, all the terms in the sequence lie within a small distance from l.* That small distance is given by $\varepsilon$. This means that all terms after $N$ lie within the bound $l-\varepsilon$ and $l+\varepsilon$.
![[Pasted image 20241106170016.png]]
The image above shows us that after $M$, all values of $a_{n}$ lie within the range formed by $l\pm \varepsilon$.

> [!NOTE] Convergence of bounded sequences
> Any *monotonically increasing (decreasing)* function with an upper bound (lower bound) converges to its supremum (infimum). Eg: $1+\dfrac{1}{n}$ converges to $1$, its infimum (infimum since $1+\dfrac{1}{n}$ is a decreasing function)<br><br> Supremum = least upper bound, Infimum = greatest lower bound.

### Sandwich/Squeeze theorem
*Claim:* $\forall n\ge N_{0}$, if $x_{n}\le y_{n}\le z_{n}$, if $x_{n}\to l$ and $z_{n}\to l$, then $y_{n}\to l$.

*Proof:* Given any $\varepsilon>0, \exists \:n\ge N_{1}$ s.t. $\forall\:x_{n,\:}l-\varepsilon<x_{n}<l+\varepsilon$. Similarly, $\exists \:n>N_{2}$ s.t. $\forall\:z_{n},\:l-\varepsilon<z_{n}<l+\varepsilon$.
Let $N_{0}$ be a real number s.t. $x_{n}\le y_{n}\le z_{n}$ holds $\forall\:n\ge N_{0}$.
Define $N=max(N_{0},N_{1},N_{2})$. This implies $\exists \:N$ s.t. $\forall\:n\ge N$, $l-\varepsilon<x_{n}\le y_{n}\le z_{n}<l+\varepsilon$. This is because $N>N_{0},N_{1},N_{2}$. Since $y_{n}$ lies between $l\pm \varepsilon$ $\forall\:n\ge N$, $y_{n}\to l$ as $n\to \infty$.

Q) Does $a_{n} = \dfrac{\sin(n)}{n}$ converge?
?
Ans) Yes it does, and we can prove it using the sandwich theorem. **We already know the range of $\sin(n)$ is -1 to 1.** Therefore, $-1\le \sin(n)\le 1$. Divide both sides by $n$ to get the $a_{n}$ term in the middle. This gives us $-\dfrac{1}{n}\le \dfrac{\sin(n)}{n}\le \dfrac{1}{n}$. We know that $\lim\limits_{n\to \infty}-\dfrac{1}{n}=\lim\limits_{n\to \infty} \dfrac{1}{n}=0$. By sandwich theorem, this means that $\lim\limits_{n\to \infty} \dfrac{\sin(n)}{n}=0$. Therefore, this sequence converges to $0$.

## Divergence of sequences
If a sequence doesn't converge to any real number, it diverges. For example, $100\cdot(1.08)^{n-1}$ diverges since it approaches $\infty$ as $n\to \infty$. *All unbounded sequences are divergent, but the converse isn't true.* It isn't necessary that a divergent sequence must be unbounded. For example, an oscillating sequence is divergent but it is also bounded.






## Flashcards
Q1) Does the sequence $a_{n}=\dfrac{8n}{3n-5}$ converge?
?
Ans) Yes, it does. **For rational functions, take the highest degree of the variable common and cancel.** Once you do that, you can compute the limit. Therefore, $\lim\limits_{n\to \infty} \dfrac{8n}{3n-5}=\lim\limits_{n\to \infty} \dfrac{8}{3-\dfrac{5}{n}}$. As $n\to \infty$, we know that $\dfrac{5}{n}\to 0$. Therefore, the value of the limit is $\dfrac{8}{3}$. This means *the sequences converges to $\dfrac{8}{3}$*.

Q2) Does the sequence $a_{n}=\cos \dfrac{1}{n}$ converge?
?
Ans) Yes, it does. Taking the limit of $a_{n}$, we get $\lim\limits_{n\to \infty} \cos \dfrac{1}{n}=\cos 0=1$. Therefore, the sequence converges to $1$.