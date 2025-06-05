---
color: var(--mk-color-orange)
tags:
  - sem1-flashcards/math_ge/calc/limits_and_continuity
---
Quick access:
[[Solving limits#Direct substitution|Direct substitution]]
[[Solving limits#Factorizing|Factorizing]]
[[Solving limits#Radical limits|Radical limits]]

## Direct substitution
This method involves *plugging in the value of the limit, or values that are very close but not equal to our limit* and gradually moving that close number towards the value of the limit. We can then observe the trend of our answers and determine what is the limit.

Example 1: $\lim\limits_{x\to 3}(2x+1)$
Here, we can directly substitute $x=3$ and we get the value of the limit as 7.

Example: $\lim\limits_{x\to 2}\dfrac{x^2-4}{x-2}$
In this case, *substituting the value of the limit gives us $\frac{0}{0}$, which is not defined.* In this case, we should use the 2nd method, and substitute values that are close to our limit. Substituting $x=2.1$ gives us 4.1 as the limit's value. **Now we should move the value of $x$ even closer to 2.** Taking $x=2.01$ gives us 4.01 as the limit's value. We can observe that *as $x$ approaches 2, our limit approaches 4.* Therefore, the limit is equal to 4. 

## Factorizing
The above method in case 2 is often time consuming and not worth it. One other method to find limits is to factorize the limit to its simplest terms. **Identify the reason why direct substitution gives us an undefined answer, and then eliminate that.** 

In the above example, the denominator of $x-2$ gives us $0$ when we substitute $x=2$. To eliminate that, *we factorize the numerator as* $x^2-4=(x+2)(x-2)$. Now, we can *cancel out the denominator* and we're left with $\lim\limits_{x\to 2}(x+2)$. **This lets us use direct substitution** with no problems. Substituting $x=2$ gives us the same value as before, 4.

Question: $\lim\limits_{x\to 3}\dfrac{x^3-27}{x-3}$
?
Direct substitution will not work here since the denominator becomes $0$. We can factorize the numerator with the difference of cubes formula $a^3-b^3=(a-b)(a^2+ab+b^2)$. Cancelling the $x-3$ gives us $\lim\limits_{x\to 3}(x^2+3x+9)$. Now we can directly substitute, and get the limit's value as 27.
<!--SR:!2025-01-09,4,270-->

Question 2:
![[Pasted image 20240831185545.png]]
?
![[Pasted image 20240831185521.png]]
When we face complex fractions, **we should multiply the numerator and denominator by the LCM of the complex portion.** Here, the LCM of the numerator is $3x$. Multiplying and cancelling $3x$ in the numerator and denominator gives us $\lim\limits_{x\to 3}\dfrac{3-x}{3x(x-3)}$. We can factor out $-1$ in the numerator and cancel the $x-3$ terms. Now, we can directly substitute and get the value of the limit.
<!--SR:!2025-01-09,4,270-->

## Radical limits
Whenever we face radicals in our limits, *try to multiply the numerator and denominator by the conjugate of the radical.* For example, with $\lim\limits_{x\to4}\dfrac{\sqrt{x}-2}{x-4}$, the conjugate is $\sqrt{x}+2$. The numerator gets simplified thanks to the identity $(a+b)(a-b)=a^2-b^2$, leaving us with $\lim\limits_{x\to4}\dfrac{(x-4)}{(x-4)(\sqrt{x}+2)}$. All that is left to do is cancel the $(x-4)$ and substitute $x=4$, and we get the value of our limit as $\frac{1}{4}$.

## Absolute values
For limits with absolute values in them, we can either directly substitute to get the answer or *use [[One sided limits|one sided limits]] to find our answer.* The value of $\lim\limits_{x\to3}|x-3|$ can be directly obtained through direct substitution as $0$ since there's nothing stopping us from substituting. 

For $\lim\limits_{x\to0}\dfrac{|x|}{x}$, we cannot directly substitute. In this case, we take the LHL and RHL. $\lim\limits_{x\to0^-}\dfrac{|x|}{x}=\dfrac{|-0.1|}{-0.1}=\dfrac{0.1}{-0.1}=-1$. Doing the same thing for RHL using $x=0.1$ gives us the value of the limit as 1. Since LHL $\ne$ RHL, *the limit does not exist.* 