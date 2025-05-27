---
sticker: lucide//binary
color: var(--mk-color-green)
tags:
  - py-syntax
---
## Syntax

Input:
```python
varName = "abc"
print(varName)
```

Output:
`abc`

Variables store data that the user inputs. It can be a string (seen above), a number or the value from the [[Input statement|input]] command. *When printing variable names, do not use quotes.* If we use `print("varName")`, our output will be `varName`.

### Rules for naming variables:
You can give a variable any name you want, but **you can't use spaces**. You can use:
- underscores_between_words
- camelCaseToMakeItEasierToRead


### [[Errors#2. SyntaxError|SyntaxError]]
Input:
```python
my variable = input("WHO GOES THERE? ")
print(my variable)
```

Output:
```python
 File "main.py", line 1
    my variable = input("WHO GOES THERE? ")
       ^
SyntaxError: invalid syntax
```

SyntaxError pops up as we *accidently left a space* while naming the variable.


