---
tag: sem1-flashcards/math_ge/calc/differentiation
color: "#f7b731"
---
![[Pasted image 20230805074748.png]]
The derivative of a derivative is called *second order derivative.* Finding the derivative of a derivative n times gives the n<sup>th</sup> order derivative.

*Example question:* ![[Pasted image 20230805075410.png]]
![[Pasted image 20230805075425.png]]
First differentiate $x^{2}*e^{2x}$ using product rule. Take $e^{2x}$ common to make the next step easier. Now find the derivative of $y_1$. Again, take $e^{2x}$ common, although it isn't necessary here. Either way, the simplified form of $y_2$ is your final answer.

## Proof questions
![[Pasted image 20230805081608.png]]
![[Pasted image 20230805081647.png]]![[Pasted image 20230805081818.png]]
Steps to follow in proof questions:
1) Find $y_1$.
2) *Always look at what y equals in the question and see if it can be substituted at any step.* In the example solution, y can be subbed in after step 3, simplifying our solution.
3) If you have a root, square it since there are **no roots** in our required proof
4) Once you get the most simplified version of $y_1$, differentiate it again to get $y_2$.
5) **REMEMBER:** To find derivative of ${y_1}^2$, first use power rule then differentiate $y_1$ to get $2y_1.y_2$ 
6) **ALWAYS TRY TO CANCEL COMMON TERMS.** Usually once you cancel the common terms you'll either get your final answer or a rearranged form of it.
7) Move the terms around to get what you are asked to prove for.

> [!success] Key point
> ***ALWAYS LOOK FOR WHAT YOU ARE ASKED TO PROVE.***
> In the above example, the required proof has a $(x^2-1)$ term and a $\dfrac {1}{4}$ term. To get this, we switch the position of $\sqrt{x^2-1}$ and 2 after step 4. Now if we square our new equation, we get $(x^2-1)$ and $\dfrac {1}{4}$ in our new equation, making it much closer to our required proof.








## Flashcards
Q) Find second order derivative of  ![[Pasted image 20230805075410.png]]

Ans)![[Pasted image 20230805075425.png]]

Q) Find second order derivative of ![[Pasted image 20230805080319.png]]

Ans) ![[Pasted image 20230805080352.png]]
First simplify the base expression, because in its current state its very complex. Simplify using the properties of log. Then find the derivative of it, and find the derivative of it again.

Q) ![[Pasted image 20230807130151.png]]

Ans) ![[Untitledwafsg.jpg]]Although there are variables in the exponents, its very easy to simplify this because of $e$. $\dfrac{d(3e^{2x})}{dx} = 3e^{2x} * 2 = 6e^{2x}$ (chain rule). Do the same for $2e^{3x}$ and then onwards its very simple to solve it. Just find $y_1$ and $y_2$ and sub in the equation, all terms cancel out. 

Q) ![[Pasted image 20230807225545.png]]
Find second order derivative.

Ans) ![[Pasted image 20230807225618.png]]
Be careful when taking LCM.

Q) ![[Pasted image 20230807225958.png]]

Ans) ![[Pasted image 20230807230021.png]]
**REMEMBER:** Even if there is a variable in the exponent, there is no need to take $log$ if the base of the variable exponent is $e$. If you remember that, this because very easy to solve.
<!--SR:!2023-08-27,1,130-->

Q) ![[Pasted image 20230808110319.png]]

Ans) ![[Pasted image 20230808110346.png]]
First find $y_1$. In the required proof, we can see there are no $x$ terms, so we must isolate $x$ along with constants so its eliminated with differentiation. Then fine $y_2$. This is where it gets complicated. You need to do a lot of manipulation to get $\dfrac{a^{2}y^{2}+b^{2}x^{2}}{a^2b^2}$, which is just the original equation but with LCM, so that entire expression is equal to 1. Once you get that value inside the brackets, the value outside the brackets will be $\dfrac{-b^4}{a^2y^2}$. Bring the y from the other side and you get the final value.

Q)![[Pasted image 20230808112306.png]]

Ans) ![[Pasted image 20230808112333.png]]
Mistake made: I got the value of $y_1$, but I did not look for what we are asked to prove. In the required proof, *there are no $t$ terms.* Therefore, you must express $y_1$ in terms of $x$ and $y$ only, not in terms of $t$. Once you do that, its very easy to solve.
<!--SR:!2023-08-27,1,130-->


Q) ![[Pasted image 20231117121434.png]]

Ans) ![[WhatsApp Image 2023-11-17 at 12.13.35 PM.jpeg]]
![[WhatsApp Image 2023-11-17 at 12.13.34 PM.jpeg]]
**Mistake:** I kept forgetting to differentiate the $x^2+a^2$ within the root. I did the log differentiation and root differentiation and forgot to differentiate within the root. If you remember to do that, it's a pretty easy question.

Q) ![[Pasted image 20231123103718.png]]

Ans) The differentiation part is pretty straightforward. In the end, you'll get $\dfrac{d^2y}{dx^2}=25ae^{5x}+25be^{-5x}$. Take $25$ common, and then you'll get $25[ae^{5x}+be^{-5x}]$. The part in square brackets is equivalent to $y$, so the final answer is $\dfrac{d^2y}{dx^2}=25y$. *Always check to see if you can sub $y$ back into the answer.* 
