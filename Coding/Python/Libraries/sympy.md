---
sticker: lucide//superscript
color: var(--mk-color-teal)
---
`sympy` stands for Symbolic Python. It allows you to **do algebra and calculus symbolically, meaning it doesn't find the numerical value.** 

Quick access:
[[sympy#symbols|symbols]]
[[sympy#lambdify|lambdify]]
[[sympy#diff|diff]]

### symbols
`from sympy import symbols` - Allows you to assign symbolic variables. For example, 
~~~python
from sympy import symbols

x = symbols('x')
y = symbols('y')

print(x**2 + y)
~~~
This keeps the expression in variable form instead of trying to find the numerical value of `x**2 + y`.

We can assign multiple symbols using `x, y = symbols('x y')`.

### lambdify
`from sympy import lambdify` - Allows you to *convert `sympy` expressions into a numerical form* so that it can be evaluated.
~~~python
from sympy import symbols, lambdify, sin
x = symbols('x')
expr = sin(x)

fn = lambdify(x, expr)

print(fn(0))
~~~
The syntax is `lambdify(symbol, function)`. It puts the symbol into the function and evaluates it numerically. Therefore, the above function takes the value of `sin` at `0`, since the function is now evaluated at `0`. This returns `0.0`.

We can also use `lambdify` to evaluate using [[Numpy|numpy.]] This is especially useful if *we want to use the output of `lambdify` to graph a function.* To do this, we simply add an extra argument `"numpy"` at the end of the `lambdify` function.

~~~python
taylor_func = lambdify(x, taylor_exp, "numpy")
~~~
`lambdify` outputs a **callable function `taylor_func`**. This helps us **calculate the value of `taylor_exp` over an array of values,** which is crucial for plotting graphs.

### diff
`from sympy import diff` - It calculates the symbolic derivative of a function wrt a variable.
~~~python
from sympy import symbols, sin, diff
x = symbols('x')

expr = 3*x**2 + sin(x)

derivative = diff(expr, x, 2)
print(derivative)
~~~
Here we take the expression as $3x^{2}+\sin x$. We use the syntax `diff(function, variable to differentiate wrt, order of derivative)`. Here, our function is `expr` and our variable is `x` as the function is being differentiated wrt `x`. The final output is the 2nd derivative of the given function.
~~~python
6 - sin(x)
~~~

We can use `diff.evalf` to evaluate the derivative at a point. This gives us a float as `evalf` stands for `evaluate to floating-point`. `evalf` takes `subs` as an argument, **which uses a dictionary to substitute the value of the variable and then evaluate.** Therefore, it'll look something like `eval.(subs={'var':value})`. For example, if we replaced the derivative line with this in the code above,
~~~python
derivative = diff(expr, x, 2).evalf(subs={'x': 0})
~~~
we'd get `6.00000000000000` as the output. This is because the 2nd derivative is `6-sin(x)`, which evaluates to `6` (in float) at `0` because `sin(0) = 0`.