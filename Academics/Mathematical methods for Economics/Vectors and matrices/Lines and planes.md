---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/mme/vectors_and_matrices"
---
Quick access:
- [[#A line through n dimensional space|A line through n dimensional space]]
	- [[#A line through n dimensional space#Line moving in the same direction as a vector|Line moving in the same direction as a vector]]
- [[#Hyperplanes|Hyperplanes]]
- [[#Flashcards|Flashcards]]

## A line through n dimensional space
Dealing with lines and planes is when understanding the geometric interpretation of vectors becomes very important.

![[WhatsApp Image 2025-05-29 at 19.39.12_2f073e1a.jpg|center|400]]
Let's consider the two vectors $a$ and $b$. [[Geometric representation of vectors#Vector subtraction|We know that]] the vector $b-a$ is a vector that connects the tip of $a$ to the tip of $b$. Therefore, $a+(b-a)=b$. **Now let's scale this vector with a scalar $t$**. Now, $a+t(b-a)$ gives us a line depending on the value of $t$. Just using $b-a$ gave us the small line segment connecting the tips of $a$ and $b$, but scaling it with $t$ gives us the entire line that goes in the direction of $b-a$. We can simplify this to get:
$$\text{Equation of a line in } \mathbb{R}^{n}= (1-t)a+tb$$
This is essentially *identical to the parametric equation of a line formula* $(1-\lambda)a + \lambda b$ and I explained how we derived it above.

Example: 
![[Pasted image 20250529194835.png]]
?
Ans)![[Pasted image 20250529194905.png]]
Simply sub in the values of the vectors $a$ and $b$ in the formula $x=(1-t)a+tb$ to get the equation of the line as the vector $[1-2t,2-3t,2+2t]$. **To find where it meets the $x_{1}x_{2}$ plane, we must find where** $x_{3}=0$. This is like how to find where a function meets the $x$ axis, the opposite variable, $y$, must be set to zero. Doing this tells us $2+2t=0 \implies t=-1$. Therefore, our line meets the $x_{1}x_{2}$ plane at $(3,5,0)$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

### Line moving in the same direction as a vector
Suppose we have a point $p$ and a vector $a$ and we want to find the line that goes through $p$ in the direction of the vector $a$.  **The logic here is completely analogous to the previous case.** 
![[WhatsApp Image 2025-05-29 at 19.54.34_c160cf23.jpg|center|350]]
You can see the vector $a$ (look at the arrow). Its base is on the point $A$ ($A$ is $p$). *Just like before, we get a line if we scale it by a scalar $t$*. Therefore, the equation of a line that passes through a point in a certain direction is $x=p+ta$, where $p \in \mathbb{R}^n$ is a point, $a \in \mathbb{R}^n$ is the direction vector and $t \in \mathbb{R}$ is a scalar.

## Hyperplanes
We'll start with a regular plane in $\mathbb{R}^{3}$ and then generalize that to planes in $\mathbb{R}^n$. Suppose we have a plane $\mathcal{P}$ going through a point $a$ with a *vector $p=(p_{1},p_{2},p_{3})$ as its normal.* Now if $p$ is orthogonal to the plane, *it is orthogonal to any line in the plane.* Therefore, if we get another point $x$, we can connect $a$ and $x$ using the vector $x-a$. This means $p$ must be orthogonal to $x-a$. Therefore, $p \cdot (x-a)=0$. Expanding this, we get:
$$\text{Equation of a plane: }(p_{1},p_{2},p_{3}) \cdot (x_{1}-a_{1},x_{2}-a_{2},x_{3}-a_{3})=0$$
Generalizing this to a hyperplane in $n$ dimensions just requires taking $n$ dimensional vectors, the equation is still $p \cdot (x-a)=0$.

Example:
![[Pasted image 20250529201334.png]]
?
Ans)
![[Pasted image 20250529201402.png]]



## Flashcards
Q1)
![[Pasted image 20250529214723.png]]
?
Ans) Since the normal is orthogonal to any vector in the plane, it must be orthogonal to both $(1,2,2)$ and $(4,1,-1)$. If we consider $p=(p_{1},p_{2},p_{3})$ as the normal, we get a system of two equations in three variables. **This is fine because there are infinite normal vectors to a plane (scalar multiples).** Solving this system gives us $p_{1}$ and $p_{2}$ in terms of $p_{3}$ as $\left( \dfrac{4}{7},-\dfrac{9}{7},1 \right)$, or $(4,-9,7)$. We know a point in the plane is $(0,0,0)$. Therefore, our plane equation becomes $(p_{1},p_{2},p_{3}) \cdot (x_{1}-0,x_{2}-0,x_{3}-0)=0$ $\implies 4x_{1}-9x_{2}+7x_{3}=0$ is the equation of our plane.
.
To find the intersection with the given line, simply sub the given values of $x_{1},x_{2},x_{3}$ in the equation and solve for $t$, and then plug $t$ back to get the final line equation. The final value of $t$ is $\dfrac{38}{15}$ and the line equation is $\left( -\dfrac{8}{15}, \dfrac{61}{15}, \dfrac{83}{15} \right)$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
