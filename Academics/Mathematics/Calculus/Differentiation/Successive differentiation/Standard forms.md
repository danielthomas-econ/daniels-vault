---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Some identities that we can use to quickly find the $n_{th}$ derivative of a given function.

Quick access:
[[Standard forms#Standard forms|Standard forms]]
- [[Standard forms#1. $y=x m$ (m is a +ve integer)|1. y = x^m]]
- [[Standard forms#2. $y=(ax+b) m$ (m is a +ve integer)|2. y = (ax+b)^m]] 
- [[Standard forms#3. $y=e {ax}$|3. y = e^ax]]
- [[Standard forms#4. $y=a x$|4. y = a^x]]
- [[Standard forms#5. $y=sin(ax+b)$|5. y = sin(ax+b)]]
- [[Standard forms#6. $y=cos(ax+b)$|6. y = cos(ax+b)]]
- [[Standard forms#7. $y= dfrac{1}{ax+b}$|7. y = 1/ax+b]]
- [[Standard forms#8. $y=log(ax+b)$|8. y = log(ax+b)]]
- [[Standard forms#9. $y=e {ax} sin(bx+c)$|9. y = e^ax sin(bx+c)]]
- [[Standard forms#10. $y=e {ax} cos(bx+c)$|10. y = e^ax cos(bx+c)]] 

[[Standard forms#Flashcards|Flashcards]]

## Standard forms

### 1. $y=x^m$ (m is a +ve integer)
$y_n=m(m-1)(m-2)...(m-(n-1))\:x^{m-n}$ if $n\le m$.
$y_n=0$ if $n>m$.

If $n=m$, the derivative will be a constant value.

### 2. $y=(ax+b)^m$ (m is a +ve integer)
It's similar to the previous one, **except we have to use the chain rule here.** Therefore, we have to include the derivative of $ax+b$, which is $a$, in our answer.

$y_n=a^n\:m(m-1)(m-2)...(m-(n-1))\:(ax+b)^{m-n}$ if $n\le m$.
$y_n=0$ if $n>m$.

### 3. $y=e^{ax}$
$y_n=a^n\:e^{ax}$ (once again, don't forget chain rule)

### 4. $y=a^x$
$y_n=a^x\:(log\:a)^n$

### 5. $y=sin(ax+b)$
We have to use a little more logic here to derive a constant pattern since continuously differentiating $sin$ will leave us with alternating $cos$ and $sin$ derivatives.

$y_{1}= a\:cos(ax+b)=a\:sin(ax+b+\frac{\pi}{2})$ {using [[Cofunctions|cofunctions]], $cos\:x=sin(x+\frac{\pi}{2})$}

$y_2=a^2\:cos(ax+b+\frac{\pi}{2})=a^2\:sin(ax+b+\frac{2\pi}{2})$. *For each next derivative, multiply $a$ and add $\frac{\pi}{2}$ to convert the $cos$ to $sin$*.

$y_n=a^n\:sin(ax+b+\frac{n\pi}{2})$.

### 6. $y=cos(ax+b)$
Exact same thing as above, but with $cos$ instead.

$y_n=a^n\:cos(ax+b+\frac{n\pi}{2})$.

### 7. $y=\dfrac{1}{ax+b}$
$y_1=\dfrac{-1\times a}{(ax+b)^2}$

$y_2=\dfrac{-1\times-2\times a^2}{(ax+b)^3}=\dfrac{(-1)^{2}\times2!\times a^2}{(ax+b)^3}$

This pattern continues, and we factor out $-1$ so that the rest can be expressed in factorial form. We generalize it as:

$y_n=\dfrac{(-1)^{n}\times n! \times a^n}{(ax+b)^{n+1}}$.

**This is a very important result that we'll be using often.**

### 8. $y=log(ax+b)$
$y_1=\dfrac{a}{ax+b}=a\times (\dfrac{1}{ax+b})$.

Notice that the 2nd term is the same as above. We've already differentiated once, so to get the $n^{th}$ derivative, we have to differentiate $n-1$ times. *Replace all $n$ terms in the above result to get this one.*

$y_n=a[\dfrac{(-1)^{n-1}\times (n-1)!\times a^{n-1}}{(ax+b)^n}]$. Taking the $a$ inside, we get:

$y_n=\dfrac{(-1)^{n-1}\times (n-1)!\times a^{n}}{(ax+b)^n}$


### 9. $y=e^{ax}\:sin(bx+c)$

$y_{1}=e^{ax}(a\:sin(bx+c)+b\:cos(bx+c))$

We must **eliminate the $cos$ part** from the $n^{th}$ derivative. We can do this by substituting $a=r\:cos\:\alpha$ and $b=r\:sin\:\alpha$. This implies $r^2=a^2+b^2$ and $tan\:\alpha=\frac{b}{a}$. Substituting, we get:

$y_1=e^{ax}(r\:cos\:\alpha\:sin\:(bx+c)+r\:sin\:\alpha\:cos\:(bx+c))$. This is of the form [[Important formulae#Sum and difference formula|sin(a+b)]], so we can simplify it as $y_1=re^{ax}(sin\:(ax+b+\alpha))$.

$y_2=r^2e^{ax}(sin\:(ax+b+2\alpha))$. The next derivative will keep multiplying $r$ and add an extra $\alpha$ inside. We get the $n^{th}$ derivative as:

$y_n=r^ne^{ax}(sin\:(ax+b+n\alpha))$. However, *we have to substitute the values of $r$ and $\alpha$ back to the original values.* Therefore, our $n^{th}$ derivative becomes:

$y_n=(a^2+b^2)^{\frac{n}{2}}e^{ax}(sin\:(bx+c+n\:arctan(\frac{b}{a}))$.


### 10. $y=e^{ax}\:cos(bx+c)$
The same as above, but with $cos$ instead of $sin$.

$y_n=(a^2+b^2)^{\frac{n}{2}}e^{ax}(cos\:(bx+c+n\:arctan(\frac{b}{a}))$.

---

## Flashcards

a) $n^{th}$ derivative of $y=x^m$
?
Ans) $y_n=m(m-1)(m-2)...(m-(n-1))x^{m-n}$ if $n\le m$
$y_n=0$ if $n>m$
<!--SR:!2025-01-08,4,270-->

b) $n^{th}$ derivative of $y=(ax+b)^m$
?
Ans) $y_n=a^{n}m(m-1)(m-2)...(m-(n-1))(ax+b)^{m-n}$ if $n\le m$
$y_n=0$ if $n>m$
<!--SR:!2025-01-09,4,280-->

c) $n^{th}$ derivative of $y=e^{ax}$
?
Ans) $y_n=a^{n}e^{ax}$
<!--SR:!2025-01-08,4,274-->

d) $n^{th}$ derivative of $y=a^x$
?
Ans) $y_n=a^x\:log(a)^n$
<!--SR:!2025-01-08,4,274-->

e) $n^{th}$ derivative of $y=sin(ax+b)$
?
Ans) $y_n=a^{n}\:sin(ax+b+\frac{n\pi}{2})$

f) $n^{th}$ derivative of $y=cos(ax+b)$
?
Ans) $y_n=a^n\:cos(ax+b+\frac{n\pi}{2})$

g) $n^{th}$ derivative of $y=\dfrac{1}{ax+b}$
?
Ans) $y_n=\dfrac{(-1)^{n}\times n!\times a^n}{(ax+b)^{n+1}}$
<!--SR:!2025-01-08,4,270-->

h) $n^{th}$ derivative of $y=log(ax+b)$
?
Ans) $y_n=\dfrac{(-1)^{n-1}\times (n-1)!\times a^{n}}{(ax+b)^{n}}$
<!--SR:!2025-01-08,4,274-->

i) $n^{th}$ derivative of $y= e^{ax}\sin(bx+c)$
?
Ans) $y_n=(a^{2}+b^{2})^{\frac{n}{2}}e^{ax}(\sin(bx+c+n\:arctan(\frac{b}{a})))$
<!--SR:!2025-01-08,4,274-->

j) $n^{th}$ derivative of $y=e^{ax}\cos(bx+c)$
?
Ans) $y_n=(a^2+b^2)^{\frac{n}{2}}\:e^{ax}(\cos(bx+c+n\:arctan(\frac{b}{a})))$
<!--SR:!2025-01-08,4,280-->

---
Q1) If $y=\dfrac{1}{x^2+4}$, find $y_n$.
?
Ans) First, break up the equation using partial fractions and factorize the bottom. Now, it becomes $y=\dfrac{A}{x-2i}+\dfrac{B}{x+2i}$. Therefore, $A(x+2i)+B(x-2i)=1$. Substituting $2$ and $-2$, we get $A=\frac{1}{4i}$ and $B=\frac{-1}{4i}$. Therefore, $y=\dfrac{1}{4i}\left[\dfrac{1}{x-2i}-\dfrac{1}{x+2i}\right]$. **Differentiating $n$ times, we get:** $y_n=\dfrac{(-1)^{n}\:n!}{4i}\left[\dfrac{1}{(x-2i)^{n+1}}-\dfrac{1}{(x+2i)^{n+1}}\right]$ - *Eq 1*
.
Now we use trig sub. Let $x=r\:cos\:\theta$, $y=2=r\:sin\:\theta$, which implies that $r^2=x^2+4$ and $tan\:\theta=\frac{2}{x}$. The first term becomes:
$\dfrac{1}{(x-2i)^{n+1}}=\dfrac{1}{r^{n+1}(cos\:\theta-i\:sin\:\theta)^{n+1}}=\dfrac{1}{r^{n+1}(cos\:(-\theta)+i\:sin\:(-\theta))^{n+1}}=$$\dfrac{1}{r^{n+1}(cos\:\theta+i\:sin\:\theta)^{-1(n+1)}}$ (by [[Important formulae#De Moivre's Theorem|De Moivre's Theorem]]). This becomes $\dfrac{(cos\:\theta+i\:sin\:\theta)^{n+1}}{r^{n+1}}$, which is
$\dfrac{1}{r^{n+1}}\left[cos\:(n+1)\theta+sin\:(n+1)\theta\right]$ - *Eq 2*
.
Similarly, $\dfrac{1}{(x+2i)^{n+1}}=\dfrac{1}{r^{n+1}}[cos\:(n+1)\theta-sin\:(n+1)\theta]$ - *Eq 3*
.
Sub $2$ and $3$ in $1$, and we get $y_n=\dfrac{(-1)^n\:n!}{4i\:r^{n+1}}[2i\:sin\:(n+1)\theta]$. Cancel $2i$ and substitute the value of $r$ and $\theta$, and we get the final answer:
$y_n=\dfrac{(-1)^n\:n!}{2(x^2+4)^{\frac{n+1}{2}}}[sin\:(n+1)\:arctan\:(\frac{2}{x})]$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,280-->

Q2) If $y=arctan\left(\dfrac{1+x}{1-x}\right)$, find $y_n$.
?
Ans) Sub $x=tan\:\theta$. Now it is in the form of [[Important formulae#Sum and difference formula|tan(a+b)]], where $a=\frac{\pi}{4}$ and $b=\theta$. Substituting gives us $arctan(tan(\frac{\pi}{4}+\theta))$, which cancels out to $\frac{\pi}{4}+\theta$, which is $\frac{\pi}{4}+arctan\:(x)$. Differentiating once gives us $y_1=\dfrac{1}{1+x^2}$. Now we can **continue with partial fractions** like the previous question, and we get $y_1=\dfrac{1}{2i}\left[\dfrac{1}{x-i}-\dfrac{1}{x+i}\right]$.
-
Since we have already differentiated once, *we must differentiate $n-1$ times to get the $n^{th}$ derivative.* Then we'll get $y_n=\dfrac{(-1)^{n-1}\:(n-1)!}{2i}\left[\dfrac{1}{(x-i)^n}-\dfrac{1}{(x+i)^n}\right]$. **Differentiate the terms inside the brackets individually** like the previous question, and you should get $\dfrac{1}{r^n}\left[cos\:n\phi\pm i\:sin\:n\phi\right]$. Substituting, we see the $cos$ terms cancel, leaving us with $y_n=\dfrac{(-1)^{n-1}(n-1)!}{2i\:r^n}\left[2isin\:n\phi\right]$. Cancel the $2i$ and sub the values of $r$ and $\phi$ (same as $\theta$ in previous question), and we get $y_n=\dfrac{(-1)^{n-1}\:(n-1)!}{(x^{2}+1)^{\frac{n}{2}}}[sin\:n\:arctan(\frac{1}{x})]$
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-05,1,240-->

Q3) $y=e^{x}cosx\:cos2x$
?
Ans) There is a trig identity which states that $2cos\:a\:cos\:b=cos(a+b)+cos(a-b)$. *Whenever we get a question of this format, with two $cos$ values being multiplied, we should use [[Important formulae#sin and cos multiplication formulae|this identity]] to simplify.* The only problem is, we only have $cos\:a\:cos\:b$. To fix this, we multiply the $cos$ terms by 2 and divide the $e^x$ term by 2. This gives us $y=\dfrac{e^x}{2}\left[2cos\:xcos\:2x\right]$, which simplifies to $y=\dfrac{1}{2}e^x[cos(3x)+cos(x)]$. We can find the $n^{th}$ derivative using the [[Standard forms#10. $y=e {ax} cos(bx+c)$|e^{ax}cos(bx+c)]]formula.
-
Therefore, $y_n=\dfrac{1}{2}[e^x\cdot10^{\frac{n}{2}}cos(3x+n\:arctan(3)+e^x\cdot2^{\frac{n}{2}}cos(x+n\:arctan(1)]$ Here, there is no coefficient for $x$ in $e^x$, therefore $a=1$. We get the final answer by taking $e^x$ outside and simplifying $n\:arctan(1)$ to $n\frac{\pi}{4}$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,280-->

Q4) Find the $n^{th}$ differential coefficient of $sin^{5}x\:cos^{3}x$.
?
Ans) If we get a product of powers of $sin$ and $cos$, we should **break them up into a sum by trigonometry.** Follow this method for all such questions.
-
Let $cos\:x+i\:sin\:x=z$, then $cos\:x-i\:sin\:x=z^{-1}$ (inverse). Therefore, $cos\:x=\dfrac{z+z^{-1}}{2}$ and $sin\:x=\dfrac{z-z^{-1}}{2i}$. For $cos\:px\pm\:i\:sin\:px$ we have the same formula but with $z^p$ and $z^{-p}$.
-
Let $y=sin^{5}x\:cos^{3}x$, then $y=\left(\dfrac{z-z^{-1}}{2i}\right)^{5}\:\left(\dfrac{z+z^{-1}}{2}\right)^3$. Take out the denominator and we get $i2^{8}y$ on LHS. We can factor the RHS as $(z-z^{-1})^{2}(z-z^{-1})^{3}(z+z^{-1})^3$. **The terms with power 3 can be simplified to** $(z^{2}-z^{-2})^3$ as $(a+b)(a-b)=a^2-b^2$. This leaves us with $(z^{2}-z^{-2})^3(z-z^{-1})^{2}$. Expand and simplify it.
-
We can then use the $sin\:x=\dfrac{z-z^{-1}}{2i}$ but as $2i\:sin\:px=z^p-z^{-p}$ to simplify all the terms. The first term will be $z^8-z^{-8}$, which simplifies to $2i\:sin\:8x$, last term is $6z^2-6z^{-2}$, which becomes $6(2i\:sin\:2x)$. We can cancel the $2i$ in LHS and RHS, and we're left with $y=\dfrac{1}{2^7}[sin\:8x-2sin\:4x-2sin\:6x+6sin\:2x]$. Differentiate $n$ times w.r.t $x$ using [[Standard forms#5. $y=sin(ax+b)$|sin(ax+b)]] and you get the final answer.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,280-->

Q5) Find the $n^{th}$ derivative of $f(x)=\dfrac{1}{1-5x+6x^{2}}$.
?
Ans) $6x^{2}-5x+1=6x^{2}-2x-3x+1=(2x-1)(3x-1)$. Therefore, we can write $f(x)$ as $\dfrac{1}{(2x-1)(3x-1)}=\dfrac{A}{2x-1}+\dfrac{B}{3x-1}$. We get $A=2,B=-3$, so $f(x)=\dfrac{2}{(2x-1)}-\dfrac{3}{3x-1}$. We know the $n^{th}$ derivative of $\dfrac{1}{ax+b}=\dfrac{{-1^{n} \cdot n! \cdot a^n}}{(ax+b)^{n+1}}$, Therefore, $f^{(n)}(x)=2\left[ \dfrac{{-1^{n} \cdot n! \cdot 2^n}}{(2x-1)^{n+1}} \right]-3\left[ \dfrac{{-1^{n} \cdot n! \cdot 3^n}}{(3x-1)^{n+1}} \right]$. Finally, multiply the $2$ and $3$ inside, so the exponent term in the numerator becomes $n+1$ for both of them.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-08,4,280-->