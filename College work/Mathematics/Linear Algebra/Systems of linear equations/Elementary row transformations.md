---
color: var(--mk-color-turquoise)
tags:
  - "#sem2-flashcards/linear_alg/system_of_equations"
---


## Elementary row transformations
There are three types of ERTs:
1) $R_{i} \leftrightarrow R_{j}$ (swapping rows)
2) $R_{i} \to kR_{i}$ (multiplying the row by a non zero scalar)
3) $R_{i}\to R_{i}+kR_{j}$ (adding a scalar multiple of the $j^{th}$ row to the $i^{th}$ row)

ERTs are very useful as **applying these transformations to an augmented matrix does not change the solution set.**

Another property of ERTs (albeit less useful than the first) is that applying an ERT on the product of matrices $(AB)$ is the same as applying it to the prefactor $A$ and then multiplying it by $B$. Therefore, if $R$ is an ERT, $R(AB)=(R(A))B$.