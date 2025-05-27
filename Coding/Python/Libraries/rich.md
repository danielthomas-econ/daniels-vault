---
color: var(--mk-color-teal)
sticker: lucide//dollar-sign
tags:
  - py-libraries
---
`pip install rich` - Improves the readability of terminal and makes it more aesthetic.


### Inspect an element
We can also use `rich` to inspect details about elements in our code.
~~~python
from rich import inspect
x = 10
inspect(10, methods=True)
~~~
This outputs
![[Pasted image 20250311092638.png]]


### Build a tree structure to represent JSON dictionaries
~~~python
from rich import print as rprint
from rich.tree import Tree
from rich.console import Console
import requests

def build_tree(node, parent, depth=1):
    # Define a color mapping based on depth
    color_mapping = {
        1: "red",
        2: "yellow",
        3: "blue",
        4: "magenta",
        5: "orange",
    }  
    # Get the color for the current depth, default to "white" if not specified
    color = color_mapping.get(depth, "white")

    if isinstance(node, dict):
        for key, value in node.items():
            branch = parent.add(f"[bold {color}]{key}[/bold {color}]")
            build_tree(value, branch, depth + 1)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            branch = parent.add(f"[bold {color}]{i}[/bold {color}]")
            build_tree(item, branch, depth + 1)
    else:
        parent.add(f"[{color}]{str(node)}[/{color}]")

result = requests.get("https://randomuser.me/api/")
user = result.json()


console = Console()
tree = Tree("[bold green]User Data[/bold green]")
build_tree(user, tree)
console.print(tree)
~~~
Honestly, I have no idea how this code works, I just asked Copilot to write some code which displays [[json]] data in a tree like structure. Just copy paste this code and replace the API link in line 18. Our output will look like:
![[Pasted image 20240617131603.png]]
The tree format and colors help us clearly see the structure of the dictionary and it weeds out any confusion. **I have added this code into Coding projects/useful_functions/jsontree.py.** To import this function, we use:
~~~python
import sys
sys.path.append('./useful_functions')
from jsontree import visualize_json
~~~
The `sys.path.append` is needed to tell python to look in the `useful functions` directory to find the `jsontree` module. To run the `visualize_json` module, we use to print a tree structure of the variable `data`. 
~~~python
result = requests.get(url)
data = result.json()

visualize_json(data)
~~~
