---
color: var(--mk-color-turquoise)
tags:
  - "#sem2-flashcards/linear_alg/system_of_equations"
---
Quick access:
- [[#Concept behind Gaussian elimination|Concept behind Gaussian elimination]]
- [[#Steps involved in Gaussian elimination|Steps involved in Gaussian elimination]]
- [[#Gauss Jordan method|Gauss Jordan method]]

## Concept behind Gaussian elimination
Since [[Elementary row transformations|ERTs]] don't change the solution set, we can use these to simplify our system of equations. Once we convert a system to an augmented matrix, *our goal is to get as many zeros as possible. When we convert this back into equation form, terms with zeros as coefficients are effectively 'eliminated'.* This makes our system a lot simpler to solve.

## Steps involved in Gaussian elimination
**Step 1:** Make the entry at $(1,1)$ equal to $1$ by using the ERT $R_{1} \to \dfrac{1}{a_{11}}R_{1}$. Since we divide the whole first row by the first term, the first term is divided by itself and becomes $1.$ *If the first term is zero, swap with another row.*

**Step 2:** Make the entries at $(2,1)$, $(3,1)$,$\dots$,$(m,1)$ equal to zero by using the ERT $R_{i}\to R_{i}-a_{i1}R_{1}$. Since the first element of the first row is 1, multiply by the first element of the $i^{th}$ row and subtract that from the entire $i^{th}$ row. This makes the first element of the $i^{th}$ row zero. At this stage, you'll have something like this:
$\left[\begin{array}{cccc|c}1 & a_{12} & \dots & a_{1n} & b_{1} \\ 0  & a_{22} & \dots & a_{2n} & b_{2}\\ 0 \\ \dots \\ 0 & a_{m_{2}} & \dots & a_{mn} & b_{m}\end{array}\right]$

**Step 3:** Move to $(2,2)$ and make it equal to 1. Repeat the previous step again so that all the elements under $a_{22}$ are equal to zero.

**Step 4:** Repeat until you've got all the diagonal elements equal to 1 and all elements below them equal to zero. *If you get a row with its diagonal element equal to zero, swap it with the bottom row and continue making diagonals equal to 1.* You should end up with a [[Key vocabulary#Row echelon form|row echelon form]] of the augmented matrix.

**Step 5:** Convert the matrix back to equation form and solve for each variable to get your final solution set.
Example:
![[WhatsApp Image 2025-05-27 at 19.07.09_7417d0c3.jpg]]

## Gauss Jordan method
This method involves reducing the matrix to its *reduced row echelon form.* The benefit of this method is that the final reduced row echelon matrix **gives us our final answer in terms of free variables.** This means your solution set is right in front of you, you don't need to do any steps after reducing like we previously did in Gaussian elimination.

## Solving multiple systems together
If we have multiple systems, **we can solve them simultaneously if their coefficient matrices are the same.** In this case, we can simply attach more augmented columns and proceed as usual. If we have systems $AX_{1}=B$, $AX_{2}=C$ and $AX_{3}=D$, we can solve for $X_{1},X_{2}$ and $X_{3}$ by solving the system represented by $[A|B|C|D]$.