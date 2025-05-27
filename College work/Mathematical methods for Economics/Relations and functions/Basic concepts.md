---
color: var(--mk-color-green)
tags:
  - sem1-flashcards/mme
---
## What is a relation?
A relation is a connection between or among things. A relation $R$ from set $A$ to $B$ is **a subset of the cartesian product of $A\times B$**. We derive this subset by describing a certain relationship between the two sets.

We can write a relation with the following notation: $f: A \to B$. Here, $f$ represents *the name of the function,* while $A$ is the *domain* and $B$ is the *codomain.*

## What is a function?
A function is a special type of relation wherein **every element of the domain set has a *unique* image in the codomain set.** In simple terms, one element of domain set points to only one element in the codomain set. We denote a function using $f(x)$. In the below picture, the first relation is a function *because each element in the input set only has one corresponding element in the output set.* The second relation is not a function since the element of 8 maps to both 10 and 0.
![[functions-vs-relations3-l.jpg|center|512]]

An real-life example of a function would be temperature ($T$) given as a function of time ($t$). This function can be written as $f(t)=T$. **At a given time, there can only be one value for temperature.** At 5pm, the temperature cannot be both 26 and 20 degrees. Therefore, each element in the domain set can only have one image in the codomain set. 

However, **a given temperature may occur at many times.** It could be 37 degrees at 1pm and 3pm. Therefore, an element in the codomain set may have more than one pre-images. This means that $f(8)$ and $f(16)$ can both equal 10; however, $f(8)$ cannot equal both 10 and 12 simultaneously.
## Image and pre-image
The *image is the output you get* when you apply the function to an element in the input set. In $f(x)=a$, we say that $a$ is the image of $x$. Since an image is the output, all images are in the codomain set. The collection of all images is called the [[Domain, range and codomain#Range|range]].