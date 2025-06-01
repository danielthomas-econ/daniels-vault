---
color: var(--mk-color-orange)
tags:
  - "#sem2-flashcards/mme/multivariable_optimization"
---
Quick access:
- [[#Definition|Definition]]
- [[#Mathematical definition|Mathematical definition]]
- [[#Intersection of convex sets|Intersection of convex sets]]
- [[#An economic application|An economic application]]

## Definition
A set of points $S$ in a plane is called convex if *each pair of points in $S$ can be joined by a line segment entirely within $S$*. Geometrically, it looks like:
![[WhatsApp Image 2025-05-30 at 09.31.31_d50edde3.jpg]]

## Mathematical definition
We know the parametric equation of a line is $(1-\lambda)x + \lambda y$, for $\lambda \in [0,1]$. We can apply the above definition again, but mathematically this time. **A set $S \in \mathbb{R}^n$ is convex if $x,y \in S$ and $\lambda \in [0,1]$** $\implies (1-\lambda)x + \lambda y \in S$.

## Intersection of convex sets
If $S_{1}$ and $S_{2}$ are two convex sets, *their intersection must be convex.* The proof of this is extremely simple. If $x,y \in S_{1} \cap S_{2}$, then $x,y \in S_{1}$ and $x,y \in S_{2}$. Since both are convex sets, the line connecting $x$ and $y$ lies in $S_{1}$ and also in $S_{2}$. Therefore, the line connecting the two points lies in $S_{1} \cap S_{2}$. *This generalizes to $n$ convex sets, so $S_{1} \cap S_{2} \cap \dots \cap S_{n}$ is also convex if each $S_{i}$ is convex.*

## An economic application
We know that indifference curves are always convex. So let's define the set $S=\left\{x:U(x) \geq c\right\}$. This gives us all the values of $x$ that make the utility function greater than or equal to the IC's level of satisfaction $c$. *This is called an upper level set.* 
![[WhatsApp Image 2025-05-30 at 09.44.06_c607faff.jpg|center|300]]
As you can see, *connecting any two points in the upper level set of the IC lies within the set.* Therefore, the upper level curve of an IC is a convex set.

