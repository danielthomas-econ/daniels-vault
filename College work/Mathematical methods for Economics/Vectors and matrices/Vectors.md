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



## Lengths of vectors
If $a=(a_{1},a_{2},\dots,a_{n})$ is a vector, its length, **also called norm,** is denoted as $\lvert\lvert a \rvert\rvert$ and is equal to $\sqrt{ a\cdot a }$. Expanding this gives us $\lvert\lvert a \rvert\rvert=\sqrt{ a_{1}^{2}+a_{2}^{2}+\dots+a_{n}^{2} }$.

Therefore, the distance between two vectors becomes $\lvert\lvert a-b \rvert\rvert=\sqrt{ (a_{1}-b_{1})^{2}+\dots(a_{n}-b_{n})^{2} }$.

## Orthogonality
Two vectors are stb orthogonal if *their dot product is zero.* Geometrically, this means the vectors are **perpendicular** to each other.