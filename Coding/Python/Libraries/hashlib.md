---
color: "#2d98da"
sticker: lucide//lock
tags:
  - py-libraries
---
## hashlib library
`hashlib` is an encryption library that is more useful than the default `hash()` function.



### SHA-256
`hashlib.sha256(item)` - Uses the SHA-256 encryption algorithm. It takes a **byte** string as an input and returns a hashed object. If our `item` is not a byte string, use `hashlib.sha256(item.encode())` to convert the item to a byte string. *However, this will return a long byte string, which can be difficult to work with.* To fix this, we **convert the byte string to hexadecimal.** Example:
~~~python
import hashlib

# Hash a string and get the binary result
binary_hash = hashlib.sha256(b"Hello, World!").digest()
print(binary_hash)
# Output: b'\x32\xe6\x9e\x67\xe7\x6b\x19\x1f\xed\x91\x1f\xe9\x3a\x3a\xc3\xd0\x0f\x8b\xbe\x95\x2a\x32\x5b\xbc\x39\xd4\x77\x7c\xbf\x9e\x6e\x1b\x9e'

# Hash a string and get the hexadecimal result
hex_hash = hashlib.sha256(b"Hello, World!").hexdigest()
print(hex_hash)
# Output: 32e69e67e76b191fed911fe93a3ac3d00f8bbe952a325bbbc39d4777cbf9e6e1b9e
~~~
Additionally, the *binary hash may not be printable* since not all binary characters correspond to printable characters. If you try to print a binary hash, you may get strange characters or question marks. That's why hashes are usually converted to hexadecimal before they're displayed or stored. **A hexadecimal string only uses 16 different characters (0-9 and a-f), so it can represent any byte value in a printable form**

Therefore, our final sha-256 encryption code will look like `hashlib.sha256(item.encode()).hexdigest()`.
