---
color: "#20bf6b"
tags:
  - py-syntax
sticker: lucide//box
---
Quick access:
- [[#Syntax|Syntax]]
	- [[#Syntax#self|self]]
- [[#Classes|Classes]]
	- [[#Classes#Instantiation|Instantiation]]
- [[#Methods|Methods]]
- [[#Inheritance|Inheritance]]


Object oriented programming (OOP) is a method of programming wherein we use **classes and objects,** which store their data and behaviors inside them. *Classes are like templates,* a cookie cutter which has pre-defined characteristics. *Objects are the cookies created with the cutter.* They're all similar, but we can customize each one of them individually.

## Syntax
~~~python
class Consumer:
    def __init__(self,w):
        # initialize consumer with w dollars of wealth
        self.wealth = w

    def earn(self, y):
        # this consumer earns y dollars
        self.wealth += y

    def spend(self, x):
        # this consumer spends x dollars if feasible
        new_wealth = self.wealth-x
        if new_wealth < 0:
            print("Insufficient funds")
        else:
            self.wealth = new_wealth
~~~

- `class` - Indicates we are building a class
- *Instance data* - The data that will automatically be created with each instance of the class. In our example, it is `wealth`.
- *Constructor method* - `__init__` is called the constructor method as it is automatically called when an instance of a class is created.
### self
You'll see the word `self` a lot when looking at OOP code. The rules for using `self` in creating a class are:
1. *Instance data should be prepended with `self`*. The above `earn` method uses `self.wealth` instead of just `wealth` since `wealth` is instance data
2. Any **method defined within the code that defines the class** should have `self` as the first argument. All the methods defined above (`earn`, `spend`) are defined inside the `Consumer` class. Therefore, their first argument should be `self`.
3. Any method referenced within the class should be called `self.method_name`.


## Classes
Classes are templates which contain **variables that define different characteristics** items in this class may have. For example, if we want to make a class for animals, we can use:
~~~python
class animal:
  species = None
  name = None
  sound = None
~~~

Next, we use the `__init__` subroutine.  `init` is short for 'initialisation'. *It tells the class what to do* when it is used to create an animal. `__init__()` must be indented within the class we want to use it in.

### Instantiation
This is the process of **using the template (class) to make an object.** We use `var_name = class(arg1, arg2, arg3.....)` to instantiate an object. For example, `dog = animal("Brian", "Canine", "Woof")`. 

In our `__init__` subroutine, we ordered the variables as `(name, species, sound)` and *we must follow the same pattern when instantiating an object.* We can use `print(dog.name)`, and it will print `Brian`. This is because after `self`, the first variable in `__init__` was `name`, and the first variable when we defined the animal `dog` was `Brian`. Therefore, Python sets `dog.name = Brian`.


## Methods
[[Subroutine|Subroutines]] inside an object are called methods. To do this, we *indent a subroutine under a class.* An example of a method would be:
~~~python
  def talk(self):
    print((f"{self.name} says {self.sound}")) 
~~~
Since we have already defined the object `dog` under the animal class, we can use it in the `talk` subroutine since `talk` is also under the animal class. Therefore, we can run the function `dog.talk()`. This will output `Brian says Woof.`

## Inheritance
Inheritance is the process of **breaking a class into sub-classes.** Sub-classes use all attributes and methods of their parent class, but have their own unique attributes. When creating a sub-class, you must use the name of the parent class as a parameter. Eg:
~~~python
class bird(animal):

  def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
~~~
Here, we have created a class called `bird` using the parent class `animal` as a parameter. **Therefore, `bird` has all the properties of `animal`, but we've given `bird` its own `__init__` function.** According to this function, every time we create an object under the `bird` class, its `name, species` and `sound` are fixed to `Bird, Avian` and `Tweet` respectively. We can define an object under `bird` using `var_name = bird()`.

We can use unique parameters for subclasses. Here is an example of creating a `bird` class with the parameter `color`, which doesn't exist in the `animal` class.
~~~python
class bird(animal):
  def __init__(self, color):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color # Only applies to the bird sub class

polly = bird("Green") # Sets polly's colour to 'Green'
polly.talk()
print(polly.color) # Prints polly's color
~~~
Now our `__init__` function has the extra parameter `color`, unique to the `bird` sub-class. If we define `polly = bird("Green")`, Python sets `polly`'s color to green because that is the first parameter after `self`.  Therefore, printing `polly`'s color outputs green.

However, **inheritance only flows one way.** Therefore, the parameter `color` will only apply to the `bird` sub-class and not to the entire `animal` class. While `bird` can take its attributes from `animal`, `animal` cannot take any attributes from `bird.` **Only the sub-class can inherit attributes, the parent class only passes its attributes downstream.**

> [!NOTE]
>Inheritance is useful to *create a generic class and then divide it into different types.* For example, we can create a class for all characters in a game. These characters can have their own sub-classes for different types, like the player, enemies, boss etc.


