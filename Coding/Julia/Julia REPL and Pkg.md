---
color: var(--mk-color-purple)
sticker: lucide//terminal
---
Quick access
- [[#The REPL|The REPL]]
	- [[#The REPL#Common repl commands|Common repl commands]]
- [[#The package manager|The package manager]]
	- [[#The package manager#Installing packages|Installing packages]]

## The REPL
The Julia REPL is the terminal in which we run Julia. It looks like this by default. Just search `Julia` in the Windows search bar and you'll find it.![[Pasted image 20250121141005.png]]

We can open this in **VS Code** using `Alt+J & Alt+O`. This opens the Julia REPL in the bottom of your screen. To run code in this repl, we can click anywhere outside the repl and hit `Alt+Enter`.

You can also open Julia in the **terminal** by just opening command prompt and typing in `julia`.

## The package manager
To use the Julia package manager, we type `using Pkg` and then continue with the relevant `Pkg` command. *The shorter way is to hit `]` to enter `Pkg` mode in the repl, and use `backspace` to exit it.* 

### Installing packages
Once you've used `using Pkg`, you can type `Pkg.add("package_name")` to download a package. If you are already in `Pkg` mode, just type `add package_name`.
![[Pasted image 20250121141911.png]]