---
color: var(--mk-color-pink)
tags:
  - sem1-flashcards/math_ge/calc/polar
---
## Polar to rectangular coordinates
When we graph out our $P(r,\theta)$ coordinates, we notice that *by creating a triangle, we can also represent $(x,y)$ coordinates.* As seen below, the base of this triangle is the same as the $x$ distance in the cartesian system, and the height is equal to $y$. By applying trig ratios, we get the equations in the image. Multiplying both sides by $r$ gives us:
$$x=r\cos\theta,\:y=r\sin\theta$$
![[Pasted image 20240915131500.png|center|500]]

Example: Convert $P(4,\frac{3\pi}{2})$ to $(x,y)$.
![[Pasted image 20240915132941.png|center]]

## Rectangular to polar coordinates
Converting rectangular to polar is a little more complicated since **we have to keep quadrants in mind too.** The basic conversion equations are given below. The first one is derived with trig ratios, while the second one was derived using the Pythagorean Theorem.
![[Pasted image 20240915132320.png|center]]

The problem here is that **$arctan$ only gives an output in the 1st and 4th quadrants.** Therefore, if our $(x,y)$ coordinate is in the 2nd or 3rd quadrant, we need to *add $\pi$ to $\theta$ to get the right quadrant.* If our angle is in the 4th quadrant, $arctan$ gives us a negative angle. If you want a positive angle, just add $2\pi$ to $\theta$ and we'll get the exact same point as a positive angle.

Example: Convert $(-3,3)$ to $P(r,\theta)$.
![[Pasted image 20240915135731.png]]