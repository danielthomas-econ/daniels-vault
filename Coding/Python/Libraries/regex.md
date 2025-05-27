---
sticker: lucide//file-search
tags:
  - py-libraries
color: var(--mk-color-teal)
---
`import re` - It is a Python standard library which allows us to use **regular expressions,** which is a way to look for patterns in strings and text. This is useful to *identify certain kinds of strings,* like a phone number or email address. `regex` simplifies this search, since we can easily use this instead of numerous `if-else` statements.

Here is a useful [cheat sheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/) to help with writing `regex`.

Quick access:
[[regex#regex syntax|regex syntax]]
	[[regex#Quantifiers|Quantifiers]]
	[[regex#Anchors|Anchors]]
	[[regex#Character sets|Character sets]]
	[[regex#Special sequences|Special sequences]]
	[[regex#Logical operators|Logical operators]]
	[[regex#Lookaheads and Lookbehinds|Lookaheads and Lookbehinds]]

[[regex#Compiling a pattern|Compiling a pattern]]
[[regex#Checking for matches|Checking for matches]]
	[[regex#search vs match|search vs match]]
	[[regex#findall|findall]]

[[regex#Identifying social media accounts|Identifying social media accounts]]

## regex syntax
### Quantifiers
Quantifiers are a part of regex syntax that states *how many instances of the target should be present* for Python to consider it as a match. Examples include:

- **`*` (asterisk)** - Matches *zero or more* occurrences of the target. `a*` will match with `""`, `"a"`, `"aa"` etc.
- **`+` (plus)** - Matches *one or more* occurrences of the target. `a+` will match `"a"`, `"aa"` etc. but not `""`.
- **`?` (question mark)** - Matches *zero or one* occurrences of the target. `a?` will match `""` and `"a"`, but not `"aa"`.

- **`{n}` (exact no.)** - Matches *exactly `n`* occurrences of the target. `a{3}` will only match `"aaa"` and nothing else.
- **`{n,}` (`n` or more)** - Matches *`n` or more* occurrences of the target. `a{2,}` will match `"aa"`, `"aaa"`, `"aaaa"` but not `"a"`.
- **`{n,m}` (range)** - Matches *between `n` to `m`* occurrences of the target. `a{2,4}` will only match with `"aa"`, `"aaa"` and `"aaaa"`.

### Anchors
We can use **anchors** like `^` and `$` for the start and end of a pattern respectively. Using an *anchor specifies we want the pattern to be at the start/end of the string.* Therefore, a pattern like `^[A-Z]+$` means we want only capital letters (A-Z) from the start to the end of our string.

### Character sets
Character sets are defined using square brackets `[]`. They allow you to *match any one of several characters in a pattern.* For example, `[aeiou]` will not check for the string `"aeiou"`, but it'll check for any one vowel.

We can use character sets to *define ranges* of characters, like `[a-z]` or `[0-9]`. You can also **combine character ranges** by placing them in the same `[]`. For example, `[A-Za-z0-9]` will check for all 3 character ranges (any alphanumerical character).

Character sets also allow for **negating a set.** We can do this by placing a caret `^` at the start of our character set. `[^a-z]` will *match anything that isn't a lowercase letter.*

We can use a dot `.` to **represent all characters in `regex`** (except newline `\n`). This is used when the character is not that important. For example, `a.+b` means the string must start with `a` and end with `b`, with any character (of any number) in between. Another example would be `^.{10}$`, where the only rule is the string must be 10 characters long.

### Special sequences
Sequences starting with a backslash `\` in `regex` are called special sequences. These are usually shorter ways to define common patterns. I've put their equivalent character sets in brackets.

- `\d`: Matches any *digit* (`[0-9]`)
- `\D`: Opposite of the above (`[^0-9]`)

- `\w`: Matches any *letter, digit or underscore* (`[a-zA-Z0-9_]`)
- `\W`: Opposite of the above (`[^a-zA-Z0-9_]`)

- `\s`: Matches any *whitespace character* (`[\t\n\r\f\v]`)
- `\S`: Opposite of the above (`[^\t\n\r\f\v]`)

- `\b`: Represents the *word boundary.*  For example, `\bcat\b` will match `cat` but not `catalog`. `\b` asserts that `cat` is a standalone word.
- `\B`: Opposite of the above *(non-word boundary).* Therefore, the text should be a part of another word. `\Bcat\B` will match `catalog` but not `cat`.


### Logical operators

- `|`: Used as an *or* operator. Including `(facebook|twitter|youtube)` in our `regex` syntax means it must include *any one of* Facebook, Twitter or Youtube.

### Lookaheads and Lookbehinds
These assertions detect text if a *certain character is ahead/behind the match.* For example, if we want to detect currency values, we can use a **positive lookbehind** to only match numbers with a `$` sign before them. 

The syntax for lookahead is `?=` and lookbehind is `?< =` (no space). To use a *negative lookbehind,* use an `!` in the syntax. A negative lookahead is `?!` and lookbehind is `?! =` or `?<!`. We usually put these `regex` in parentheses to **make the criteria into a group.**

###### *Currency matching example:*
Lets try to match these values: `$9 $12 $1,000 $10,000 $3 million`

The basic lookbehind assertion to check for a dollar sign before a number is `(?<=\$)\d+`. This works for `$9` and `$12`, but not the rest. To include commas, **we can group digits and commas together with `[]`**. Our regex now becomes `(?<=\$)[\d,]+`. This matches everything except `$3 million`. To match text, we can add `( million| billion| trillion)?`.


## Compiling a pattern
`variable = re.compile("pattern")` - Assigns the defined pattern to a variable. The variable is now a `regex` object, on which we can use various methods.

## Checking for matches
`variable.search("string")` - Checks if the string matches a previously defined pattern. For example,
~~~python
pattern = re.compile("^[A-Z]+$")

print(pattern.search("Hello World"))
print(pattern.search("HELLO WORLD"))
print(pattern.search("HELLOWORLD"))
~~~
We've defined the variable `pattern` to be any string with only uppercase letters. If we run this code, we get the output:
~~~python
None
None
<re.Match object; span=(0, 10), match='HELLOWORLD'>
~~~
This shows us that *only the last string was a match,* since the first one isn't in uppercase letters, and the second one has a space.

### search vs match
`re` actually has two methods we can use for matching, `.search()` and `.match()`. The main difference is that **`.search()` looks for the pattern *anywhere* in the string, while `.match()` only looks for a pattern in the *start of the string*** (it implicitly starts with a `^` anchor).

`.search()` will *return the first occurrence of the pattern* in the string, while `.match()` will *only return if the pattern occurs at the start* of the string. Lets use an example where the pattern requires lowercase letters:
~~~python
pattern = re.compile("[a-z]+")

print(pattern.search("Hello World"))
print(pattern.match("Hello World"))
~~~
This code will output:
~~~python
<re.Match object; span=(1, 5), match='ello'>
None
~~~
There are two matches of the lowercase criteria in our string, `ello` and `orld`. **`.search()` only returns the first one.** `.match()` will return `None` since *the string starts with `H`*, which violates the pattern. Therefore, `.match()` stops its checks and doesn't return a match.

### findall
Alternatively, we can use the `.findall()` method to *find all instances of the target pattern being found.* This is a good alternative to `.search()` and `.match()`, which only returns the first match of the target pattern. We use `.findall()` if we know we'll encounter numerous instances of the pattern.


## Identifying social media accounts
There's a lot to explain here, but [this GitHub repo](https://github.com/lorey/social-media-profiles-regexs) works great for social media `regex`. It can even different between posts, accounts, channels, videos etc.
 