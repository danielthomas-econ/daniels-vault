---
color: var(--mk-color-turquoise)
sticker: lucide//sigma
tags:
  - project_euler
---

## Permutations
~~~python
def permutations(n):
    # base case: when the length is one, just return the item itself cause there arent any permutations of it
    if len(n) == 1:
        return [n]
    perms = []
    for i in range(len(n)):
        rest = n[:i] + n[i+1:] # puts every number other than the ith number in this variable called rest
        for p in permutations(rest): # generates all permutations of the remaining digits recursively
            perms.append(n[i]+p) # adds each possible permutation to the ith digit
    return perms
~~~
