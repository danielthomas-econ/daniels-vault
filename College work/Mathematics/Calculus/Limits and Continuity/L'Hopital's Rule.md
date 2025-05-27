---
color: var(--mk-color-orange)
tags:
  - sem1-flashcards/math_ge/calc/limits_and_continuity
---



## Statement of L'Hopital's rule
If $\lim\limits_{x\to c}f(x)=\lim\limits_{x\to c}g(x)=0$ or $\pm \infty$, and if $\lim\limits_{x\to c} \dfrac{f'(x)}{g'(x)}$ exists, then we can say that $\lim\limits_{x\to c} \dfrac{f(x)}{g(x)}=\lim\limits_{x\to c} \dfrac{f'(x)}{g'(x)}$. This is usually used *to transform indeterminate forms into limits that can be solved.*
If the limit of the derivatives still gives an indeterminate form, **we can continue applying L'Hopital's however many times we want until we get a real value.** 

Eg: $\lim\limits_{x\to 0} \dfrac{{a^x-b^x}}{x}$
?
Ans) Directly substituting in the limit gives us $\left( \dfrac{0}{0} \right)$, an indeterminate form. This means we have to use L'Hopital's rule and differentiate the numerator and the denominator.
.
This gives us $\lim\limits_{x\to 0} \dfrac{{a^x\log a-b^x\log b}}{1}=\log a-\log b=\log\left( \dfrac{a}{b} \right)$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,270-->










## Flashcards
Q1) $\lim\limits_{x\to 0} \left[ \dfrac{{x\cos x-\sin x}}{x^{2}\sin x} \right]$
?
Ans) Whenever we see a limit of $x\to 0$ and $\sin x$, **we should immediately think of applying** $\lim\limits_{x\to 0} \dfrac{{\sin x}}{x}=1$. We can rewrite this limit as $\lim\limits_{x\to 0}\left[ \dfrac{{x\left( \cos x-\dfrac{{\sin x}}{x} \right)}}{x^2\cdot x\cdot \dfrac{{\sin x}}{x}} \right]$. The two $\dfrac{{\sin x}}{x}$ become $1$ and $x$ cancels in the numerator and denominator. This leaves us with $\lim\limits_{x\to 0}\left[ \dfrac{{\cos x-1}}{x^{2}} \right]\left( \dfrac{0}{0} \right)$. Applying L'Hopital's rule, we have $\lim\limits_{x\to 0}\left[ \dfrac{{-\sin x}}{2x} \right]\left( \dfrac{0}{0} \right)=\lim\limits_{x\to 0}\left[ \dfrac{{-\cos x}}{2} \right]=-\dfrac{1}{2}$.
<!--SR:!2025-01-09,4,274-->

<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

Q2) $\lim\limits_{x\to 0} \dfrac{{\ln x}}{\csc x}$
?
Ans) $L=-\infty(0)$, which is indeterminate.
By L'Hopital's, $L=\lim\limits_{x\to 0}\dfrac{1}{x(-\csc x\cot x)}= \dfrac{{\sin x\sin x}}{-x\cos x}=\left( \dfrac{{\sin x}}{-x} \right)\tan x$
$=-1(0)=0$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-06,1,230-->

Q3) $\lim\limits_{x\to 0} x\ln x$
?
Ans) $L=-\infty(0)$. We can rewrite it as $L=\lim\limits_{x\to 0}\dfrac{{\ln x}}{\dfrac{1}{x}}$. Using L'Hopital's, $L=\lim\limits_{x\to 0} \dfrac{{\dfrac{1}{x}}}{{-\dfrac{1}{x^{2}}}}=\lim\limits_{x\to 0}-x=0$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,274-->

Q4) $\lim\limits_{x\to 0} {\dfrac{\sqrt{ (1+x)-1- \dfrac{x}{2} }}{x^{2}}}$
?
Ans) We can simplify this expression to be $\lim\limits_{x\to 0} {\dfrac{\sqrt{ \dfrac{x}{2} }}{x^{2}}}$. Taking $\sqrt{ 2 }$ out, we get $\dfrac{1}{\sqrt{ 2 }} \lim\limits_{x\to 0}{\dfrac{\sqrt{ x }}{x}}=\dfrac{1}{\sqrt{ 2 }}\lim\limits_{x\to 0} x^{\frac{-3}{2}}$. **Negative powers will tend to infinity as x tends to zero, and tend to zero as x tends to infinity.** Therefore, the limit will go to $\infty$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,270-->

Q5) $\lim\limits_{x\to \infty}(x^5-x^4)^\left( \frac{1}{5} \right)-x$
?
Ans) Directly applying the limit gives us $\infty-\infty$, which is indeterminate. To simplify, *take x common out of the raised to the power 1/5 term.* Now we have $\lim\limits_{x\to \infty}x\left( 1-\dfrac{1}{x} \right)^{1/5}-x$. Taking $x$ common again gives us $\lim\limits_{x\to \infty}x\left[ \left( 1-\dfrac{1}{x} \right)^{1/5}-1 \right]=\lim\limits_{x\to \infty} \dfrac{{\left( 1-\dfrac{1}{x} \right)^{1/5}-1}}{\frac{1}{x}}$. Applying L'Hopital's rule, we get $\lim\limits_{x\to \infty} \dfrac{{\dfrac{1}{5}\left( 1-\dfrac{1}{x} \right)^{-4/5}\left( \dfrac{1}{x^{2}} \right)}}{-\dfrac{1}{x^{2}}}$. The $x^{2}$ terms cancel and leave us with $-\dfrac{1}{5}$ as our answer.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-09,4,270-->
