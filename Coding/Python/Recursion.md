---
color: "#20bf6b"
sticker: lucide//reply
tags:
  - py-syntax
---
Recursion is a type of program where *a [[Subroutine|subroutine]] calls itself.* Recursion is often used for mathematical problems. Example:
~~~python
def reverse(value):
  if value <= 0:
    print("Done!")
    return
  # This `if` provides the 'stop' condition for the program. Otherwise it would run forever.

  else: # if we're not at the stop condition.
    for i in range(value):
      print("💯", end="") # Outputs 'value' emojis
    print() # New line
    reverse(value - 2) # takes 2 off the value and calls the subroutine again with this new number. Eg if value was 7 it would call 'reverse(value)' again with value as 5.

reverse(9)
~~~
This code defines a function called `reverse()` with the parameter `value`. The goal of this function is to print an upside down triangle of emojis. 

It achieves this by using the [[Loops|for loop]] in line 8. If we enter `value = 9`, then it will start by printing 9 emojis. After that, **`reverse()` calls itself again with `reverse(value - 2)`. Now, it will have `value = 7`. Therefore, it prints 7 emojis in the next line.** This goes on until `value <= 0`. 

