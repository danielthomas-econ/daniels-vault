---
tag: sem1-flashcards/math_ge/calc/differentiation
color: "#f7b731"
---
If the variable of x and y are connected so that it is not possible to express y as a function of x, then it is said that y is an implicit function of x. Typically we differentiate functions w.r.t x. *This creates a problem when there is a y variable.* If we differentiate y w.r.t x, we get $\dfrac {dy}{dx}$, which is change in y divided by change in x. 
*Eg:* Differentiate y<sup>2</sup>:
$\dfrac {d(y^2)}{dx} = 2y * \dfrac {dy}{dx}$
We get this result by applying chain rule. The derivate of y<sup>2</sup> is 2y and the derivative of y is $\dfrac{dy}{dx}$.

Example question:![[Pasted image 20230804171822.png]]
**Steps to solve:**
First differentiate each part of the equation. Keep in mind that *when you have a y term, you must also differentiate for y (derivate of y w.r.t x is not 1!).* Then expand all the brackets. Then move any term that doesn't have $\dfrac {dy}{dx}$ to RHS. Next, take $\dfrac {dy}{dx}$ common from all the LHS terms. Finally, move all the LHS terms to the denominator of the RHS.



## Flashcards

Q)![[Pasted image 20230804172917.png]]

Ans)![[Pasted image 20230804173028.png]]
Look for what you are being asked to prove. In the final answer, $e^{x+y}$ is not there, so we must eliminate it. We can do that by substituting $e^{x}+e^{y}=e^{x+y}$ to eliminate that term. Last step is just divide the two exponents by subtracting and you'll get the final answer.

Q) ![[Pasted image 20230804173649.png]]

Ans) ![[Pasted image 20230804173714.png]]
It might seem very complex at first, but its very simple. Since the $\sqrt {log\:x}$ continues until $\infty$, even if we remove one $\sqrt {log\:x}$  from the equation, **it is still equivalent to y**.
$\therefore$ The equation can be represented as $y = \sqrt {log\:x + y}$, where y equals the long infinite series. Again, look at what you are asked to solve. You need a y in the final proof, *so square both sides* (since the derivative of $y^2$ has a y term, it becomes easier to solve). From here, its pretty straightforward. 
<!--SR:!2023-08-28,2,150-->

Q) ![[Pasted image 20230805101701.png]]

Ans) ![[UntitledafAFAWF.jpg]]
![[Untitled-1tshjrh.jpg]]
Taking common outside makes this a much easier question. If you see that you can take common/cancel terms, always try to do it (don't make mistakes when taking common tho)

Q) ![[Pasted image 20230805102907.png]]

Ans) ![[Pasted image 20230805102930.png]]
You can also open the bracket on RHS and then move the $\dfrac {dy}{dx}$ terms together. Then take $3x+2y$ as denominator on both sides, then equate the numerator and you'll get the same answer.
<!--SR:!2023-11-30,30,170-->

Q) ![[Pasted image 20230805104159.png]]

Ans) ![[Pasted image 20230805104216.png]]
You can apply the property of log to simplify the equation, but the equation isn't too hard even without simplification. Just be careful when taking common terms, especially in regards to signs.

Q) ![[Pasted image 20230805104648.png]]

Ans) ![[Pasted image 20230805104701.png]]
**ALWAYS LOOK FOR WHAT YOU ARE ASKED TO PROVE.** We can see that in the required proof, there is no $x$ term. So we should isolate $x$, which will remove the $x$ term completely when differentiating it. So we transpose $y^3$ to get the equation $x = \dfrac {1}{y^3}$. Solving from there is very straightforward. Just remember to always frame your solution as per the required proof.

Q) ![[Pasted image 20230805120432.png]]

Ans) ![[Pasted image 20230805120453.png]]
Its a very complex problem but you can solve half of it easily. Start by squaring both sides and *remember to use the $(a+b)^2$ formula.* Then differentiate normally, there is no specific step you need to take. Once you get the derivative, **rationalize to eliminate the root in the denominator.** This will leave you with just $x^2$ in the denominator. *You can cancel out the negative in the denominator* to make it easier, or continue without doing that. Split the numerator into two and divide each by $x^2$. The $x$ terms will cancel out leaving you with $\dfrac {y}{x} - \dfrac{\sqrt{y^2-x^2}}{x}$. We have the first part of the proof, but the second part doesn't have $x$ in the denominator. So we should move the $x$ into the root, and in doing so $x$ becomes $x^2$ (because $\sqrt{x^{2}}= x$). Then split the numerator into two again and you get the final answer.

Q) ![[Pasted image 20230805123021.png]]

Ans) ![[Untitledsdcawc.jpg]]
This is a pretty simple question, just remember that $x^{\frac{-1}{3}}$ is equal to $\dfrac{1}{\sqrt[3]{x}}$ and then its a very simple question.

Q) ![[Pasted image 20230807123932.png]]

Ans) ![[Untitledyfhj.jpg]]
![[Untitled-1saef.jpg]]
When there is no $y$ in the value of $\dfrac{dy}{dx}$, it means you must find a way to isolate that $y$ by cancelling terms or transposition. Once you isolate the $y$ on LHS, the LHS directly becomes $\dfrac{dy}{dx}$, and you'll mostly get close to your solution.


Q) ![[Pasted image 20231115200849.png]]

Ans) b) $\frac{-2}{5}$
**Mistake:** I forgot to differentiate 7 as 0, I only differentiated LHS. Besides that, it's simple. Differentiate both sides and group terms, you'll get $\dfrac{dy}{dx}(2y+x)+y=0$. Sub in $x=1, y=1$ and solve for $\frac{dy}{dx}$.

Q) ![[Pasted image 20231122234136.png]]

Ans) ![[1190613_1332502_ans_3a1e9fe23c674beda1d064aa661dea8c.jpg]]
**Mistake made:** I messed up the simplification of $\dfrac{1}{2\sqrt x}-\dfrac{1}{2(\sqrt x)^3}$. I put the numerator as $2x-1$ instead of $x-1$. *To get $2(\sqrt x)^3$ from $2\sqrt x$ we need to multiply by $(\sqrt x)^2=x$* and that becomes the numerator. Other than that, simplification is straightforward and you'll get LHS=RHS.   