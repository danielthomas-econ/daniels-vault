---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/mme/vectors_and_matrices"
---
Quick access:

- [[#What are vectors?|What are vectors?]]
- [[#Operations on two vectors|Operations on two vectors]]
	- [[#Operations on two vectors#Equality|Equality]]
	- [[#Operations on two vectors#Addition|Addition]]
	- [[#Operations on two vectors#Subtraction|Subtraction]]
	- [[#Operations on two vectors#Scalar multiplication|Scalar multiplication]]
	- [[#Operations on two vectors#Dot product|Dot product]]
- [[#Geometric representation of vectors|Geometric representation of vectors]]
	- [[#Geometric representation of vectors#Vector addition|Vector addition]]
	- [[#Geometric representation of vectors#Vector subtraction|Vector subtraction]]
	- [[#Geometric representation of vectors#Scalar multiplication|Scalar multiplication]]
- [[#Lengths of vectors|Lengths of vectors]]
- [[#Orthogonality|Orthogonality]]



## What are vectors?
An ordered set of numbers, distinguished not only by the elements it contains but also the order in which they appear, is called a vector. We can have either row vectors like $a=\begin{bmatrix}a_{1} & a_{2} & \dots & a_{n}\end{bmatrix}$ or column vectors like $b=\begin{bmatrix}b_{1} \\ b_{2} \\ \dots \\ b_{n}\end{bmatrix}$. The numbers $a_{1},a_{2},\dots,a_{n}$ are called the *components or coordinates* of the vector. $a_{i}$ is the $i^{th}$ component of the vector. If a vector has $n$ components, we say that is has dimension $n$.


## Operations on two vectors
### Equality
Two vectors $a$ and $b$ are said to be equal if all their corresponding components are equal. Note that equality is only possible if both $a$ and $b$ share the same dimension.

### Addition
The sum of two vectors, denoted by $a+b$, is *the sum of corresponding components.* Therefore, $a+b=(a_{1}+b_{1}, a_{2}+b_{2},\dots,a_{n}+b_{n})$. 

### Subtraction
Subtraction works the same as addition. You subtract the corresponding components to get $a-b$. We often define subtraction as $a+(-1)b$. While it is the same as $a-b$, writing $a+(-1)b$ helps us get a better visual intuition of the operation.

### Scalar multiplication
If $a$ is a vector and $k \in \mathbb{R}$, $ka=(ka_{1},ka_{2},\dots ,ka_{n})$. In other words, we *multiply the scalar with every component* of the vector to get its scalar multiple.


These operations follow these basic rules, which are pretty intuitive and practically the same as for standard real number operations.
![[WhatsApp Image 2025-05-28 at 12.58.08_8915f52e.jpg|center|400]]

### Dot product
The dot product of two vectors $a$ and $b$ is given by $a_{1}b_{1}+a_{2}b_{2}+\dots+a_{n}b_{n}$. Note that **the dot product takes two vectors and outputs just one number.** It is represented by $a \cdot b$. The dot product also follows some basic rules, which are mostly the same as in real numbers.
![[WhatsApp Image 2025-05-28 at 13.27.15_f30827df.jpg|center|400]]
One interesting property of the dot product is that *the dot product of a vector with itself gives us the distance of the vector squared.* Consider the vector $[3,4]$. From the Pythagorean theorem, we know that the line connecting $[3,4]$ to the origin must have a length of $5$. Taking the dot product of $[3,4]$ with itself gives us $3^{2}+4^{2}=25=5^{2}$.


## Geometric representation of vectors
A vector is represented by an arrow that starts at point $P$ and ends at point $Q$. *Two vectors with the same length and direction are stb equal.* Therefore, the start and end points don't matter at all. For this reason, we generally consider vectors to have their base at the origin and tip at a point $(x_{1},x_{2},\dots,x_{n})$. Since there is only one unique arrow going from the origin to $(x_{1},x_{2},\dots,x_{n})$, **we can simply represent the vector using its end point for notation purposes.** Ex: The vector $[3,4]$ represents the arrow going from $(0,0)$ to $(3,4)$.

### Vector addition
Adding two vectors $[a_{1},a_{2}]$ and $[b_{1},b_{2}]$ gives us $[a_{1}+b_{1},a_{2}+b_{2}]$. Geometrically, this is equivalent to *placing the base of vector $b$ on the tip of vector $a$*, *with the new tip giving us $a+b$*. You could also do it in reverse by placing $a$ on $b$. Plotting $a$, $b$ and the both ways to get $a+b$ gives us a parallelogram with corner points $(0,0)$, $(a_{1},a_{2})$, $(b_{1},b_{2})$ and $(a_{1}+b_{1},a_{2}+b_{2})$. Since the desired sum is $(a_{1}+b_{1},a_{2}+b_{2})$, we can draw a point to it from the origin to get the sum of the two vectors. **Geometrically, the vector representing the sum is the diagonal of the parallelogram with sides $a$ and $b$**.
![[WhatsApp Image 2025-05-28 at 13.06.15_8eb1315e.jpg]]
From 12.4, we see that triangles $OSR$ and $PTQ$ are congruent.
Proof: $OS=b_{1}=PT$
$\angle S = \angle T$ (both are right angles)
$SR=b_{2}=QT$
Therefore, the two triangles are congruent by SAS congruency.

This tells us that $OR$ and $PQ$ are parallel and have the same length. Therefore, $OPQR$ is a parallelogram and $a+b$ is its diagonal. This is called *the parallelogram law.* 

### Vector subtraction
We know that adding $(a-b)$ to $b$ will give us $a$. We've already seen how vector addition works. Therefore, if we place the base of $(a-b)$ on the tip of $b$, it will give us $a$, so it must reach the tip of $a$. **Therefore, the difference of two vectors is geometrically represented by a vector connecting their tips.** If the vector points towards $a$, it is $a-b$. If it points to $b$, it is $b-a$. 
![[WhatsApp Image 2025-05-28 at 13.17.54_c7c69221.jpg|center|350]]

### Scalar multiplication
If $k>1$, then $ka$ will be a new vector that *points in the same direction as $k$*, *but its length will be longer* $k$ times the length of $a$. If $k \in (0,1)$, then the vector will point in the same direction but be shorter. Its length is $k$ times the length of $a$, which is less than the length of $a$ since $k$ is in the interval $(0,1)$.

These same results hold **if $k$ is negative, except the vector will point in the exact opposite direction.**

## Lengths of vectors
If $a=(a_{1},a_{2},\dots,a_{n})$ is a vector, its length, **also called norm,** is denoted as $\lvert\lvert a \rvert\rvert$ and is equal to $\sqrt{ a\cdot a }$. Expanding this gives us $\lvert\lvert a \rvert\rvert=\sqrt{ a_{1}^{2}+a_{2}^{2}+\dots+a_{n}^{2} }$.

Therefore, the distance between two vectors becomes $\lvert\lvert a-b \rvert\rvert=\sqrt{ (a_{1}-b_{1})^{2}+\dots(a_{n}-b_{n})^{2} }$.

## Orthogonality
Two vectors are stb orthogonal if *their dot product is zero.* Geometrically, this means the vectors are **perpendicular** to each other.