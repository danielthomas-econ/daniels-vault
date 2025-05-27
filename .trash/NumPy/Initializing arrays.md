---
color: var(--mk-color-orange)
tags:
  - ai-ml
---
Initializing arrays with NumPy refers to **creating arrays with specific shapes, sizes and values.** These are usually standard arrays that are commonly used. Instead of defining them with `np.array` each time, we can create them using certain commands. These commands usually follow the structure of `np.command(shape of array)`.

### Common methods to initialize arrays
- `np.zeros((2,3))` - Creates a *zero matrix* of the defined shape.
- `np.ones((3,4))` - Creates a *matrix of ones.*
- `np.full((2,2), 7)` - Creates a *matrix of one number.* We can replace the shape argument with `array.shape` of an existing array.
- `np.eye(3)` - Creates an *identity matrix* of the defined order.
- `np.random.random((2,2))` - Creates a *matrix of random floats* from `0` to `1`.
- `np.random.randint(1,7, size = (3,3))` - Creates a *matrix of random integers* from `1` to `7` (ending is exclusive) of size `(3,3)`.
- `np.arange(1, 10)` - Creates a *vector of numbers in a range.*
- `np.linspace(0,1,5)` - Creates a *vector of equally spaced values* between a start and stop value, with the last argument being number of elements in the vector.
- `np.repeat(array,3,axis = 0/1)` - *Repeats an existing array* the number of times specified (`3` here). Axis `0` means horizontal, axis `1` is vertical.

- `np.anycommand.astype(int)` - *Converts an array's values to integers.* Can be used alongside other commands that output float values by default, like `np.eye()`.
- `array2 = array1.copy()` - The *safe way to create a copy of an array.* Just like we do with lists, we must use `.copy()` to create a copy of an array, otherwise any changes in `array2` will also reflect in `array1`.


