---
color: var(--mk-color-orange)
tags:
  - quantecon
---
Quick access:
- [[#What is numpy?|What is numpy?]]
- [[#Importing names directly|Importing names directly]]

## What is numpy?
`numpy` is a very popular library in Python, and is mostly used for:
- working with arrays (vectors and matrices)
- common mathematical functions like `cos` and `sqrt`
- generating random numbers
- linear algebra, etc.

After `import numpy as np` we have access to these attributes via the syntax `np.attribute`. Eg: `np.sqrt(4)`, `np.log(4)`.

## Importing names directly
Previously, we had to use any numpy attribute like this:
~~~python
import numpy as np
np.sqrt(4)
~~~

This can get tedious if we use this attribute numerous times. Therefore, a cleaner way to do this is:
~~~python
from numpy import sqrt
sqrt(4)
~~~
