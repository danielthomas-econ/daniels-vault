---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/mme/vectors_and_matrices"
---
Quick access:
- [[#Geometric representation of a vector|Geometric representation of a vector]]
	- [[#Geometric representation of a vector#Vector addition|Vector addition]]
	- [[#Geometric representation of a vector#Vector subtraction|Vector subtraction]]
	- [[#Geometric representation of a vector#Scalar multiplication|Scalar multiplication]]

## Geometric representation of a vector
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