---
color: var(--mk-color-orange)
tags:
  - quantecon
---
Quick access:
- [[#Attributes|Attributes]]
	- [[#Attributes#shape|shape]]

- [[#Creating arrays|Creating arrays]]
	- [[#Creating arrays#Empty array|Empty array]]
	- [[#Creating arrays#Array of zeros or ones|Array of zeros or ones]]
	- [[#Creating arrays#Evenly spaced elements|Evenly spaced elements]]
	- [[#Creating arrays#Identity matrix|Identity matrix]]

- [[#Arithmetic operators|Arithmetic operators]]
	- [[#Arithmetic operators#Basic elementwise operators|Basic elementwise operators]]
	- [[#Arithmetic operators#Adding/multiplying whole arrays|Adding/multiplying whole arrays]]

- [[#Tricks|Tricks]]
	- [[#Tricks#Using `bool` to extract elements|Using `bool` to extract elements]]
	- [[#Tricks#Using an array to extract elements|Using an array to extract elements]]
	- [[#Tricks#Set all values in an array equal to a new value|Set all values in an array equal to a new value]]
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

## Attributes
### shape
~~~python
arrayname.shape
~~~
This gives us the shape of an array. The `shape` attribute is a [[Tuples|tuple]] of the form `(rows, columns)`. 
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

## Methods
- `arrayname.sort()` - Sorts the array in ascending order. It only sorts the array and does not create a new one.
- `arrayname.sum()` - Adds the elements in the array
- `arrayname.mean()` - Finds the mean of the array
- `arrayname.max()` - Finds the max element in an array
- `arrayname.argmax()` - Returns the index of the max element
- `arrayname.cumsum()` - Returns an array with the cumulative sum of elements
- `arrayname.cumprod()` - Returns an array with the cumulative product of elements
- `arrayname.var()` - Finds the variance of the elements
- `arrayname.std()` - Finds the standard deviance of the elements
- `arrayname.transpose()` - Returns the transpose of the array. You can also use `arrayname.T`
- `arrayname.searchsorted(n)` - Returns the index of the first element greater than or equal to `n`

~~~python
a = np.array([7,5,2,8,3,1])

a.sort()
print(f"sort = {a}")
print(f"sum = {a.sum()}")
print(f"mean = {a.mean()}")
print(f"max = {a.max()}")
print(f"argmax = {a.argmax()}")
print(f"cumsum = {a.cumsum()}")
print(f"cumprod = {a.cumprod()}")
print(f"var = {a.var()}")
print(f"std = {a.std()}")
print(f"transpose (T) = {a.transpose()}")
print(f"searchsorted = {a.searchsorted(5.5)}")
~~~
Output:
~~~python
sort = [1 2 3 5 7 8]
sum = 26
mean = 4.333333333333333
max = 8
argmax = 5
cumsum = [ 1  3  6 11 18 26]
cumprod = [   1    2    6   30  210 1680]
var = 6.5555555555555545
std = 2.5603819159562025
transpose (T) = [1 2 3 5 7 8]
searchsorted = 4
~~~
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

## Creating arrays
### Empty array
~~~python
np.empty(shape, dtype=)
~~~
Eg: `np.empty(t+1)` creates an empty array that is of length `t+1`.

### Array of zeros or ones
~~~python
np.zeros(shape, dtype=)
np.ones(shape, dtype=)
~~~
### Array of length n filled with element m
~~~python
np.full(length, number)
~~~
Creates an array of length `length` and each element of this array is `number`.
### Evenly spaced elements
~~~python
np.linspace(start, end, no. of elements)
~~~
This creates an evenly spaced list of elements from the start to the end element, **including both the start and end element.** For example, `np.linspace(2,4,5)` creates an array of 5 evenly spaced numbers between 2 and 4. This outputs `array([2. , 2.5, 3. , 3.5, 4. ])`.

### Identity matrix
~~~python
np.identity(order)
np.eye(order)
~~~
Creates an identity matrix of order `order`.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

## Arithmetic operators
### Basic elementwise operators
The operators `+, -, *, /, **` all **act elementwise** on arrays.
~~~python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
a + b
~~~
This will output an array that adds each corresponding element of `a` and `b`.
~~~python
array([ 6,  8, 10, 12])
~~~
### Adding/multiplying whole arrays
You can add/multiply a number to every element in an array by using `arrayname + number` or `arrayname * number`.
~~~python
a = np.array([7,5,2,8,3,1])
print(a + 10)
print(a * 10)
~~~
This will output:
~~~python
[17 15 12 18 13 11]
[70 50 20 80 30 10]
~~~


<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>

## Tricks
### Using `bool` to extract elements
~~~python
z = np.linspace(2,4,5)
d = np.array([0,1,1,0,0], dtype = bool)
z[d]
~~~
Array `z` is `array([2. , 2.5, 3. , 3.5, 4. ])`, while `d` is `array([False,  True,  True, False, False])`. Using `z[d]` will overlap the two lists and *only output the numbers corresponding to `True` values.* Therefore, `z[d]` is `array([2.5, 3. ])`.

### Using an array to extract elements
We can do the same thing as above but with `indices = np.array((0,2,3))`. Using `z[indices]` will output the values from `z` corresponding to index numbers `0,2,3`. This will output `array([2. , 3. , 3.5])`.

### Set all values in an array equal to a new value
We can do this with **slice notation.** Suppose we have `z = array([2. , 3. , 3.5])`. We can slice this with `z[:]`. *This does not specify a start or end, so this represents the entire array for `numpy`*. `z[:] = 42` gives us `array([42., 42., 42.])`.





## **Past Economic Shocks in Argentina**

Argentina has experienced multiple episodes of radical economic reform aimed at stabilizing its economy through rapid liberalization. Two of the most significant instances of economic "shock therapy" occurred under the leadership of José Alfredo Martínez de Hoz during the military dictatorship (1976–1981) and under Carlos Menem in the 1990s, with Domingo Cavallo spearheading reforms. While both attempts sought to impose free-market principles to combat inflation and economic stagnation, their ultimate failures provide critical insights into the risks of rapid liberalization.

### **Martínez de Hoz and Adolfo Diz: Financial Deregulation and Debt Crisis (1976–1981)**

Following the 1976 military coup that overthrew Isabel Perón, the new government appointed José Alfredo Martínez de Hoz as Minister of Economy. His economic strategy, influenced by the Chicago School and Austrian economics, particularly through the involvement of Adolfo Diz, the President of the Central Bank, aimed to curb Argentina's chronic inflation and integrate the country into the global financial system (Dornbusch & de Pablo, 1987).

Central to this reform effort was a shift toward trade liberalization, which involved a drastic reduction in import tariffs. While intended to increase efficiency and competitiveness, this policy ultimately exposed domestic industries to overwhelming foreign competition, leading to widespread industrial decline. Financial deregulation followed, allowing interest rates to be freely determined by the market. This resulted in a surge of foreign capital inflows, driving short-term economic stability but increasing vulnerability to external shocks. Additionally, the administration implemented a pre-announced exchange rate devaluation schedule, known as the *Tablita* policy, which aimed to control inflation while simultaneously attracting foreign investment. However, the overvaluation of the peso rendered Argentine exports uncompetitive, exacerbating trade deficits and leading to capital flight.

To sustain economic stability, the government turned to extensive borrowing from international markets. While this strategy provided temporary relief, it ultimately contributed to an unsustainable debt burden. By 1981, the economy had entered a state of crisis, with rising unemployment, industrial collapse, and a failing banking system (Heymann, 2000). The abandonment of the *Tablita* policy and Martínez de Hoz’s eventual removal marked the failure of this experiment in economic liberalization, as Argentina plunged into a deep recession (Dornbusch & de Pablo, 1987).

### **Carlos Menem and Domingo Cavallo: The Convertibility Plan and Its Collapse (1991–2001)**

By the late 1980s, Argentina was once again in economic turmoil, with hyperinflation exceeding 2,000% annually. Carlos Menem, elected in 1989, initially aligned with Peronist interventionist policies but soon shifted toward neoliberal reforms. Under the guidance of Domingo Cavallo, appointed Minister of Economy in 1991, the government introduced the Convertibility Plan, a bold strategy to restore monetary stability (Fanelli & Frenkel, 1996).

The centerpiece of this reform was the pegging of the Argentine peso to the U.S. dollar at a one-to-one ratio. This policy effectively eliminated inflation and restored investor confidence by providing monetary stability. In parallel, the government undertook an extensive privatization program, selling off state-owned enterprises in sectors such as telecommunications, oil, and utilities to foreign investors. These measures were accompanied by labor market deregulation, which sought to attract investment by reducing worker protections and increasing labor flexibility.

Initially, the Convertibility Plan achieved its intended goals, stabilizing prices and fostering economic growth. However, its rigid exchange rate system created structural vulnerabilities. With an overvalued peso, Argentine exports became increasingly uncompetitive, leading to persistent trade deficits. Meanwhile, privatization, while generating immediate revenue, failed to produce long-term economic development, as foreign capital largely focused on financial speculation rather than industrial investment (Sturzenegger & Zettelmeyer, 2006). The reliance on external borrowing to finance fiscal deficits further deepened Argentina’s financial dependence.

By the late 1990s, external shocks, particularly the 1999 Brazilian currency devaluation, severely impacted Argentine exports, pushing the economy into recession. The inflexibility of the currency peg, coupled with mounting debt, led to a rapid loss of investor confidence. By 2001, Argentina faced a full-blown financial crisis, with massive capital flight, rising social unrest, and an inability to service its external debt obligations. The subsequent sovereign default on $100 billion—the largest in history at the time—marked the collapse of the Convertibility Plan (Gerchunoff & Llach, 2018). The peso was ultimately devalued in early 2002, triggering widespread economic and social upheaval.

### **Conclusion**

Both the Martínez de Hoz and Menem-Cavallo shock therapy experiments failed due to underlying structural weaknesses in the Argentine economy. The reliance on financial liberalization and foreign debt under Martínez de Hoz led to industrial collapse and an unsustainable debt crisis. Similarly, the Convertibility Plan under Menem created short-term stability but ultimately proved unsustainable due to its rigid exchange rate system and dependence on external capital. These cases illustrate the risks associated with rapid economic liberalization when implemented without the necessary institutional safeguards and productive economic restructuring.

---

This version maintains an academic tone and presents the content in a structured, research-oriented manner. Let me know if you want any refinements!