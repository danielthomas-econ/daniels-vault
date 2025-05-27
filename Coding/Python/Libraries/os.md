---
color: "#2d98da"
sticker: lucide//brain
---
## os library
`os` allows you to communicate instructions to the console.

Quick access:
[[os#Clear screen|Clear screen]]
[[os#List directories|List directories]]
[[os#Make a folder|Make a folder]]
[[os#Rename a file|Rename a file]]
[[os#Find the current working directory|Find the current working directory]]
[[os#Check if a file path exists|Check if a file path exists]]
[[os#Store environment variables|Store environment variables]]

### Clear screen
`os.system("clear")` clears the console every time its run (Unix)
`os.system("cls")` does the same for Windows

### List directories
`os.listdir()` lists all the files inside the current working directory. This can be directly printed with `print(os.listdir())`. We can also store its value to a variable to check if a certain file is in our current directory.
~~~python
files = os.listdir()
if "quickSave.txt" not in files:
  print("Error: Quick Save not found.")
  ~~~

### Make a folder
`os.mkdir("folder name")` will create a folder with that name. **However, it requires parent directories to already exist and will throw a `FileNotFoundError` if they don't.** Additionally, it will also create `FileExistsError` if the directory its trying to create already exists.

We can use `os.mkdirs("folder name", exist_ok = True)` to get past this. `os.makedirs()` is used to create a directory and **automatically creates all the necessary parent directories.** So if you try to create the directory `a/b/c` with `os.makedirs()`, and the directory `a/b` does not exist, `os.makedirs()` will create `a/b` for you before creating `c`.

`os.mkdirs()` also has an `exist_ok` argument. If we set it to true, then `os.mkdirs()` *will not raise an error if the directory already exists.* 

### Rename a file
`os.rename(oldname, new name)` will change a file's name. Example: `os.rename("myname.txt", "NEW.o")`.

### Find the current working directory
`os.getcwd()` - Tells you the directory from which your Python code is run

### Check if a file path exists
`os.path.exists(file_path)` - Checks if the `file_path` is a real file path. It's useful in `if-else` statements to verify a path's existence.

### Store environment variables
`os.environ['var']` - Stores an environment variable, which is useful for **storing sensitive data** like passwords or API keys.