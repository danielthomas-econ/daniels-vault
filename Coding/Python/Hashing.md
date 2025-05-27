---
color: "#20bf6b"
sticker: lucide//hash
tags:
  - py-syntax
---
The `hash()` function is used to get the **hash value** of an item. This is a unique alphanumerical way to represent data securely without revealing its actual contents. `hash()` is **deterministic,** meaning the same input will always output the same hash value. However, *this is only true for one run of the program* because Python 'salts' the value for security reasons at the start of reach execution. Example:
~~~python
password = "baldy1"
password = hash(password)
print(password)
~~~
The above code sets the variable `password` equal to `baldy1` and then hashes it. This will output `-2043884907991124420`, as it is the hash value of `baldy1`. If we change `password` to equal `baldy`, our hash value becomes `8219356433346813150`. *Simply removing the 1 completely changed the hash value.* 

## Salting
While hashing is great, hackers have a set of all hash values for common passwords. Therefore, if you use a common password, *they can look up the hash value and crack your password.* To prevent this, we can use a technique called 'salting'. 

This involves adding some extra value to the hash input, which means **the hash output will be different even for identical inputs.** We can do this using
~~~python
password = "baldy1"
salt = 10221

newPassword = f"{password}{salt}" # append the salt
newPassword = hash(newPassword) # hash the lot

print(newPassword)
~~~
Although the user's password is still `baldy1`, we add a value called `salt` to the password, so the new password becomes `baldy110221`. *Now, our hash value will be completely unique even with the same input,* so looking up hash value tables will not break our encryption.

It is best to store the value of the password and salt in a dictionary to avoid confusion. We can do this using `db["david"] = {"password":newPassword, "salt": salt}` (uses a [[replit db]] key). If we use this method, we can use the following login system:
~~~python
from replit import db

ans = input("Password >") # Get the input
salt = db["david"]["salt"] # Get the salt from the database.
newPassword = f"{ans}{salt}"
newPassword = hash(newPassword) # Hash the concatenated string

if newPassword == db["david"]["password"]: #compare hash of newPassword to stored hash.
  print("Login successful")
  ~~~
This **extracts the value of `salt` from the db key and appends it to the password, then hashes it.** Now if the hash of this appended password matches the stored hash, we know they entered the right password even after the salting process.

> [!NOTE]
> Since Python uses a random salt for `hash` in each new run of the program, it is not a good option for storing passwords in a database. A better option would be the [[hashlib]] library.

