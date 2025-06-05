---
color: var(--mk-color-green)
tags:
  - sem1-flashcards/math_ge/calc/series
---



## The idea behind Maclaurin's series
From [[Maclaurin's theorem|Maclaurin's theorem,]] we know that $f(x)$ can be expressed as $S_{n}+R_{n}$, where $S_{n}$ is the sum of the first $n$ terms. **If we can show that $\lim\limits_{n\to \infty}R_{n}=0$, then that means $f(x)=\lim\limits_{n\to \infty}S_{n}$**. This means that if the remainder becomes $0$ as $n$ gets larger, then after that point, $f(x)$ can be expressed as $S_{n}+0$, which is just $S_{n}$. **Therefore, we can express the function as a sum of infinite terms if we can prove that the remainder will go to zero.**

If $f:[0,x]\to \mathbb{R}$ s.t.
i) $f^{(n)}$ exists $\forall\:n$
ii) $R_{n}\to 0$ as $n\to \infty$
then $f(x)=f(0)+xf'(0)+\dfrac{x^{2}}{2!}f''(0)\dots$ is called Maclaurin's series expansion for $f(x)$.

## Standard Maclaurin series expansions






## Flashcards
Q1) Assuming the validity of the expansion, show that $\sin\left( \dfrac{\pi}{4}+\theta \right)=\dfrac{1}{\sqrt{ 2 }}\left[ 1+\theta-\dfrac{\theta^{2}}{2!} -\dfrac{\theta^{3}}{3!}\dots\right]$
?
Ans) According to Taylor series, $f(a+h)=f(a)+hf'(a)+\dfrac{h^{2}}{2}f''(a)\dots$
**We must take $a=\dfrac{\pi}{4}$, $h=\theta$  and $f(x)=\sin x$ to match the question to this form.** This gives us $\sin\left( \dfrac{\pi}{4}+\theta \right)=\sin\left( \dfrac{\pi}{4} \right)+\theta \cos\left( \dfrac{\pi}{4} \right)+\dfrac{\theta^{2}}{2!}\left( -\sin\left( \dfrac{\pi}{4} \right) \right)+\dfrac{\theta^{3}}{3!}\left( -\cos\left( \dfrac{\pi}{4} \right) \right)\dots$
$=\dfrac{1}{\sqrt{ 2 }}+\dfrac{\theta}{\sqrt{ 2 }}-\dfrac{\theta^{2}}{2!\sqrt{ 2 }}-\dfrac{\theta^{3}}{3!\sqrt{ 2 }}\dots$
$=\dfrac{1}{\sqrt{ 2 }}\left[ 1+\theta-\dfrac{\theta^{2}}{2} -\dfrac{\theta^{3}}{3}\dots\right]$. Hence proved.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,270-->

Q2) Assuming the validity of the expansion, show that $\sin x=1-\dfrac{\left( x-\dfrac{\pi}{2} \right)^{2}}{2!}+\dfrac{\left( x-\dfrac{\pi}{2} \right)^4}{4!}\dots$.
?
Ans) Looking at the question, we must immediately be able to tell that *the series is centered at $\dfrac{\pi}{2}$*. Therefore, we take $f(x)=\sin x, a=\dfrac{\pi}{2}, h=x-\dfrac{\pi}{2}$. We take $a=\dfrac{\pi}{2}$ as that is the center and $h=x-\dfrac{\pi}{2}$ so that $f(a+h)$ will give us $f(x)$, which is what we need considering we have $\sin(x)$ in the question.
.
By Taylor Series, $f(x)=f(a)+hf'(a)+\dfrac{h^{2}}{2!}f''(a)\dots$
$\small\implies \sin x=\sin \dfrac{\pi}{2}+\left( x-\dfrac{\pi}{2} \right)\left( \cos\left( \dfrac{\pi}{2} \right) \right)+\dfrac{\left( x-\dfrac{\pi}{2} \right)^{2}}{2!}\left( -\sin\left( \dfrac{\pi}{2} \right) \right)$
$\small+\dfrac{\left( x-\dfrac{\pi}{2} \right)^{3}}{3!}\left( -\cos\left( \dfrac{\pi}{2} \right) \right)+\dfrac{\left( x-\dfrac{\pi}{2} \right)^4}{4!}\left( \sin\left( \dfrac{\pi}{2} \right) \right)\dots$
.
Since $\cos\left( \dfrac{\pi}{2} \right)=0$, all those terms cancel out and we get our required proof.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,270-->

Q3) Verify $e^{i\theta}=\cos \theta+i\sin \theta$
?
Ans) $e^{i\theta}=\sum\limits_{{n=0}}^{\infty} \dfrac{(i\theta)^n}{n!}$. **We know that the value of $i$ cycles with changes in powers, as** $i^0=1,i^1=i,i^2=-1,i^3=-i,i^4=1$ etc.
Therefore, for even values of $n$, $i$ alternates between $1$ and $-1$. For odd values, it alternates between $i$ and $-i$. Therefore, we can split up the summation into $\sum\limits_{{n=0}}^{\infty} \dfrac{(i\theta)^n}{n!}=$ $\sum\limits_{{n=0}}^{\infty} \dfrac{{(-1)}^{n}(\theta)^{2n}}{(2n)!} + i\sum\limits_{{n=0}}^{\infty} \dfrac{(-1)^{n-1}(\theta)^{2n-1}}{(2n-1)!}$. *The first term expresses even values of $n$ using $2n$*, *while the second term shows odd values of $n$ using $2n-1$*, and therefore it has an $i$ term outside. This sum simplifies into $\cos \theta+i\sin \theta$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,270-->
