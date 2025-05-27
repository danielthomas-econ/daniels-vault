---
tag: sem1-flashcards/math_ge/calc/differentiation
color: "#f7b731"
---
When x and y are connected with some other variable, then x and y are parametric functions of each other. *Eg:* $x = f(t)$ and $y = f(t)$ Here, t is the parameter and x and y are both parametric functions. In such cases, we can find the derivative by:
$\dfrac {dy}{dx} = \dfrac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}}$ or $\dfrac {dy}{dx} = \dfrac {dy}{dt} * \dfrac {dt}{dx}$. In both cases, $dt$ cancels out leaving you with $\dfrac {dy}{dx}$.

*Example question:* ![[Pasted image 20230804184802.png]]
![[Pasted image 20230804184840.png]]
In these questions, our goal is to find $\dfrac {dy}{dx}$. To do that, the steps are:
1) Find $\dfrac {dx}{dt}$
2) Find $\dfrac {dy}{dt}$ 
3) Then use the parametric differentiation formula: $\dfrac {dy}{dx} = \dfrac{\dfrac{dy}{dt}}{\dfrac{dx}{dt}}$ or $\dfrac {dy}{dx} = \dfrac {dy}{dt} * \dfrac {dt}{dx}$.
4) That's it.



## Flashcards
Q) ![[Pasted image 20230804185520.png]]

Ans)![[Pasted image 20230804191412.png]]
To find $\dfrac {dx}{dt}$, do a * $\dfrac {1}{2\sqrt{whatever}}$ * derivative of whatever. In this case, we have to use quotient rule which is why it is very long. **REMEMBER:** You can take the $\sqrt {t^2+1}$ on top, which simplifies calculation. Do the same thing to find $\dfrac {dy}{dx}$. However, this time, *there is an extra t in the equation.* It becomes a * t * whatever, so you need to use product rule to find the answer.
![[Pasted image 20230804191821.png]]
This is just the continuation of the answer. The top part shows the final value of $\dfrac {dy}{dt}$ and then finally shows the answer of $\dfrac {dy}{dx}$ by using the parametric formula.

Q) ![[Pasted image 20230804192057.png]]

Ans) ![[Pasted image 20230804192128.png]]
To solve these questions where you are asked to derivative w.r.t another function, let function 1 = y and function 2 = z. Now y and z are parametric functions with x being the parameter. So differentiate both equations w.r.t x. To solve this, we need to find $\dfrac {dy}{dz}$ which can be found using parametric formula.
<!--SR:!2023-08-28,2,150-->

Q) ![[Pasted image 20230804192741.png]]

Ans) ![[Pasted image 20230804192808.png]]
Do function 1 = y and function 2 = x, then differentiate both individually and find $\dfrac {dy}{dz}$ to solve this problem.

Q) ![[Pasted image 20230806224954.png]]

Ans) ![[Pasted image 20230806225018.png]]
Just be careful with quotient rule and *remember to take common out and cancel if possible.* 
<!--SR:!2023-08-28,2,150-->

Q) ![[Pasted image 20231117115218.png]]

Ans) ![[Pasted image 20231117115328.png]]
Final answer is $\dfrac{d^2y}{dx^2}=\dfrac{3}{16at}$.
**Mistake:** I forgot to take the derivative of $\dfrac{dy}{dx}$ when finding second derivative, I directly multiplied it by $\dfrac{dt}{dx}$. To find second order derivative of a parametric function, *you should multiply the derivative of the first order derivative with reciprocal of derivative of x.*