---
tag: sem1-flashcards/math_ge/calc/differentiation
color: "#f7b731"
---
![[Pasted image 20230804174326.png]]
### When should we use logarithmic differentiation?

Logarithmic differentiation is used primarily in cases where:
i) If there are **more than 2 functions in multiplication or division**
ii) If the **base and exponent are both variables.**

> [!NOTE] $log\:e=1$
> The value of $log\:e$ is 1. So if you ever encounter $log\:e$ in a question, just cancel the term since it is equal to 1.

*Example question:* ![[Pasted image 20230804175331.png]]

![[Pasted image 20230804175443.png]]
Steps for logarithmic differentiation when the terms are multiplied/divided:
1) Set y = given equation
2) Log both sides
3) Apply properties of log. *Add instead of multiplication and subtract instead of division. Bring exponents to the front.*
4) **Differentiate both sides, including the side with y**
5) Once you complete differentiation, **move the $\dfrac {1}{y}$ from the LHS to RHS.** It will just become y when transposed to RHS.
6) **Sub y = whatever the equation is.** Basically just put whatever you put in step 1 in place of y. 
7) That's it. That's the final answer.

*Example question:*![[Pasted image 20230804181240.png]]
![[Pasted image 20230804181323.png]]
Steps for logarithmic differentiation *when the terms are added/subtracted:*
1) Set $y = u \pm v$, where u and v are the terms being added/subtracted (we must differentiate separately).
2) **Set u = first term and then log both sides**
3) Differentiate both sides normally
4) **Shift the $\dfrac {1}{u}$ to the other side so it becomes u * whatever was there before**
5) Sub u = first term
6) Now you have $\dfrac {du}{dx}$ alone in LHS, and that is your answer for derivative of first term
7) **Repeat steps 2-6 to find $\dfrac {dv}{dx}$** 
8) Finally, in the equation $\dfrac {dy}{dx} = \dfrac {du}{dx} + \dfrac {dv}{dx}$, replace $\dfrac {du}{dx}$ and $\dfrac {dv}{dx}$ with the two values you just solved for.
9) That's the final answer.



## Flashcards

Q) ![[Pasted image 20230805154834.png]]

Ans) ![[Pasted image 20230805154855.png]]
Just be careful when doing functions that have a lot of $log\:x$ values, it can get tricky.

Q) ![[Pasted image 20230805155239.png]]

Ans) ![[Pasted image 20230805155318.png]]

Q) ![[Pasted image 20230805160147.png]]

Ans) ![[Pasted image 20230805160222.png]]
First, simplify the value to eliminate $e$. Then differentiate the equation. Then take $y$ common and split the RHS into two, and since the denominator is $x^2$, both the denominators in the split equations will be $x$. **REMEMBER TO ALWAYS LOOK FOR SUBSTITUTIONS IN PROOF QUESTIONS.** One of the split equations will be $\dfrac{y}{x}$. In the start, we got the equation $log\:x = \dfrac {x}{y}$, therefore, $\dfrac {y}{x} = \dfrac{1}{log\:x}$. Substitute the value and multiply the split equations to get the final answer.

Q) ![[Pasted image 20230805161654.png]]

Ans) ![[Pasted image 20230805161716.png]]
You can observe that the answer does not have any y term. So *move all the y terms to one side, take y common and then differentiate.* We get $(log\:x+1)^2$ in our denominator but we need $(log\:xe)^{2}$ in our denominator. We can sub $log\:e=1$ and get $(log\:x+log\:e)^2$ in our denominator. We know if two log arguments are added, we can multiply them and take log common. Therefore, our denominator becomes $(log\:xe)^2$ and we reach the final proof. 

Q) ![[Pasted image 20230805163257.png]]

Ans) ![[Pasted image 20230805163328.png]]
Start off by differentiating normally after taking log. Then open the brackets on the RHS and cross multiply. Then you can take $\dfrac{dy}{dx}$ common outside on the LHS. Then cross multiply to get the value of $\dfrac{dy}{dx}$ isolated. Then cancel out terms until you get $\dfrac{2y}{x}$, which is the required proof.

Q) ![[Pasted image 20230806220344.png]]

Ans) ![[Pasted image 20230806220408.png]]
**REMEMBER:** $log\:(a+b) \ne log\:a+log\:b$ 
When you get a problem like this, split the terms and differentiate each individually, then add them all up.

Q) ![[Pasted image 20230807115246.png]]

Ans) ![[Untitledjfj.jpg]]Even though there aren't any variables in the exponents, using log here makes the question a lot easier.
<!--SR:!2023-11-30,30,130-->


Q) ![[Pasted image 20231122232451.png]]

Ans) Just use quotient rule, idk why I didn't think of that. Final answer will be $\dfrac{2}{x(1-log\:x)^2}$. 

Q)
![[Pasted image 20240420092402.png]]

Ans) ![[Pasted image 20240420092328.png]]
Here we should use the change of base formula since $log$ has base $3$. The formula is: $log_{a}b = \dfrac{log\:b}{log\:a}$. Therefore we convert $log_3(log_3\:x)$ to $\dfrac{log(log_3\:x)}{log\:3}$.   Take the denominator out as it is a constant and *repeat the base change* for the numerator. We get $\dfrac{1}{log_3}[log(\dfrac{log\:x}{log\:3})]$. Now we have **removed all the log bases** and can differentiate normally. Use properties of $log$ to simplify and then you get the answer. 