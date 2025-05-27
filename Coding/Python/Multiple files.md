---
sticker: lucide//git-fork
color: "#20bf6b"
tags:
  - py-syntax
---
Instead of scrolling for ages to find a specific bit of code, we can split our code up into different files and name them according to what they do. *This makes finding code easier.* When you use this method, **the main file will always run first.** The other files will be imported in (just like importing a library) and then run. 

Start by adding code to a certain file. Let's call it `test.py`. If you want to run `test.py`, just add `import test` (.py isn't required) to the main file. You can also use nicknames to shorten the file's name, like `import test as tt`.

## Running the code using subroutines
The problem with simply importing our code is that **it runs as soon as we import it.** If our `test.py` had a counter to $10$ and our `main.py` file was
~~~python
import test

print("Countdown")
~~~
then, Python would count to $10$ then print "Countdown". To fix this, we must write our code in `test.py` using [[Subroutine|subroutines]], just like calling a specific function from a library. Let's assume we put our entire countdown code in `test.py` under a subroutine called `countdown()`. If we want to run the countdown code now, we can use `test.countdown()` after our print statement. *This way we can control when we want to execute the code.* If you imported `test` as `tt`, then you should use `tt.countdown()` as now Python thinks the file name is `tt` and not `test`.
