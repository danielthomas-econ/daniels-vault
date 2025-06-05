---
color: var(--mk-color-orange)
tags:
  - "#sem2-flashcards/mme/multivariable_optimization"
---
Quick access:
- [[#Interior and boundary points|Interior and boundary points]]
- [[#Types of sets|Types of sets]]
	- [[#Types of sets#Closed and open sets|Closed and open sets]]
	- [[#Types of sets#Bounded and unbounded sets|Bounded and unbounded sets]]
	- [[#Types of sets#Compact set|Compact set]]
- [[#Using inequalities to describe sets|Using inequalities to describe sets]]


## Interior and boundary points
Consider any point in the set. Draw a circle with an arbitrarily small radius around it. *The point is stb an interior point if all points in the circle lie in the set.* The definition of boundary point follows from this. If some points in the circle lie outside the set, then it is a boundary point.
![[WhatsApp Image 2025-05-16 at 18.53.20_22019c2c.jpg|center|250]]

## Types of sets
### Closed and open sets
**A closed set is a set that contains all its boundary points.** A set is also called closed if its complement is open. Therefore, *an open set is a set that contains none of its boundary points.* A set that contains some boundary points is neither open nor closed.
![[WhatsApp Image 2025-05-16 at 19.00.42_8dec4bdd.jpg|center|400]]

If we call the set of all interior points of $A$ as the interior of $A$, then *if $A$ is open, the interior of $A$ equals $A$ itself.* This is because an open set cannot have any boundary points, so all the points in an open set must be interior points.

### Bounded and unbounded sets
A set is called bounded if **the whole set can be contained within a sufficiently large circle.** The set $\{(x,y):x\geq 0, y\geq 0\}$ is unbounded because it is infinitely large.

### Compact set
A set that is *both closed and bounded* is called a compact set.

## Using inequalities to describe sets
Considering how loosely a set is defined, its really hard to just tell if a set is open/closed. Therefore, in optimization, we will use inequalities to define these sets. In this case, *boundary points are those points that satisfy with equality.* 

For example, the budget set $px+qy \leq m$, $x\geq 0, y\geq 0$ is an inequality that defines a set. It consists of all the points in the triangle shaded area of this inequality. Since the line $px+qy = m$ belongs to the set, the set contains all its boundary points and is closed. *To convert this into an open set, replace the weak inequalities with strict ones.* 

If $g(x_{1},x_{2},\dots,x_{n})$ is a function defined in $\mathbb{R}^n$ and $c \in \mathbb{R}$, then we can say that the sets $\{x:g(x)\geq c\}$, $\{x: g(x)\leq c\}$ and $\{x: g(x) = c\}$ are all closed sets. Replacing the inequalities with strict ones makes these sets open.
