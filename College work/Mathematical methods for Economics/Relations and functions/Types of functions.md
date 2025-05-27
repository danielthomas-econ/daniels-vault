---
color: var(--mk-color-green)
tags:
  - sem1-flashcards/mme
---
## Surjective functions (onto)
A function is said to be surjective if for every $y\in Y$ there exists at least one $x\in X$ such that $f(x)=y$. In simple terms, this means that *every element of the codomain set has at LEAST one pre-image.* This implies that the range will be equal to the codomain for surjective functions.
![[Pasted image 20240831200425.png|center|256]]
The function above is surjective since all elements in set $Y$ have a pre-image in set $X$. However, if we add an extra element 'E' to set $Y$, it is no longer surjective since no element in $X$ maps to 'E'.

## Injective function (one-to-one)
A function is called injective when for every $y\in Y$, there exists at MOST one $x\in X$ such that $f(x)=y$. This means that *every element in set $Y$ has either 1 or no pre-image, but it can never have two or three pre-images.* 

We can graphically check if a function is one-to-one **if it passes the horizontal line test.** In this test, we draw horizontal lines on the same plane as the function. We can say the function is one-to-one if *the line only touches one point on the function.*
![[Pasted image 20240901083352.png|center|512]]
The above linear function is injective since any horizontal line we draw will only touch one point on $f(x)$. However, the parabolic function below is not injective, since any horizontal line drawn above the vertex will intersect two points, meaning it fails the horizontal line test.
![[Pasted image 20240901083657.png|center|512]]