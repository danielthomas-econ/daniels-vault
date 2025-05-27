---
color: var(--mk-color-orange)
tags:
  - ai-ml
---
You can load in data from any file as a `numpy` array using the `.genfromtxt` attribute. As the name suggests, it **generates an array from the text you input.** 

The syntax is `np.genfromtxt('filename', delimiter = 'the delimiter you used')`. Following `freecodecamp.org`'s tutorial, our data file looks like this:
![[Pasted image 20240711120911.png|center]]

As you  can see, *all the numbers are separated by a comma,* which is our delimiter. To convert this code into an array, we run the below code:
~~~python
data = np.genfromtxt('data.txt', delimiter = ',')

print(data.astype(int))
~~~
I've converted the datatype to `int`, since `.genfromtxt` *automatically casts data into the `float` datatype.* Our array looks like:
![[Pasted image 20240711121214.png]]
