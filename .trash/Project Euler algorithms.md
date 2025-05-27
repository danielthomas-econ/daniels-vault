---
color: var(--mk-color-turquoise)
sticker: lucide//sigma
---
Quick access:
[[Project Euler algorithms#Fibonacci sequence|Fibonacci Sequence]]
[[Project Euler algorithms#Prime factor finder|Prime factor finder]]
[[Project Euler algorithms#Prime number generator|Prime number generator]]
[[Project Euler algorithms#Finding highest common factor (HCF)|Finding highest common factor (HCF)]]
[[Project Euler algorithms#Finding lowest common multiple (LCM)|Finding lowest common multiple (LCM)]]
[[Project Euler algorithms#Number of divisors|Number of divisors]]


## Fibonacci sequence
Reference: Q2
~~~python
# sum of even valued terms in the fibonacci sequence whose values do not exceed four million

def fib(n):
    a, b = 0, 1
    sumlist = []
    for i in range(n):
        if a > 4000000:
            break
        print(a)
        if a % 2 == 0:
            sumlist.append(a)
        a, b = b, a+b # a becomes b, and b becomes a + b, i.e. next fib number
    sumcount = sum(sumlist)
    print(f"The sum of even terms in the fibonnaci sequence less than 4 million is {sumcount}")
~~~

The key to the solution is taking `a, b = 0, 1`, which initializes the first two terms of the Fibonacci sequence. **After that, we can say that `a`, the 2nd last term, becomes `b`, and `b`, the last term, becomes `a+b` (definition of the sequence).**

Eg: In `0, 1, 1, 2, 3`, we see that `a,b` goes from `0,1`, to `1,1`, to `1,2` and then `2,3`. If you observe carefully, it does match the rule we listed above.

## Prime factor finder
Reference: Q3
~~~python
def prime_factors(n):
    pfactors = []
    
    # keeps dividing by 2 to eliminate all factors of two, making it odd
    while n % 2 == 0:
        pfactors.append(2)
        n = n // 2
    
    # divides this odd number continuously by odd numbers within a range
    for i in range(3, int(n**0.5)+1, 2): # odd numbers from 3 to the sqrt of n
        while n % i == 0:
            pfactors.append(i)
            n = n // i

    return pfactors
~~~

This algorithm is broken down into two parts. First off, we continuously divide `n` by 2, until it is no longer divisible. This factors out all 2s, leaving us with an odd number.

In the next step, *we only look for prime factors till* `sqrt(n).` This is an important optimization trick. Since `n` can be expressed as $n=a\times b$, **if a is more than $\sqrt{ n }$, b is less than $\sqrt{ n }$ and vice versa.** That means each factor pair has at least one number less than $\sqrt{ n }$. Therefore, looking up to just $\sqrt{ n }$ will be enough for us. 

Again, we do the same thing we did with 2, but for all odd numbers from $3$ to $\sqrt{ n }$. We keep dividing it by `i` to completely factor `i` out of the number. This goes on for all `i in range(3, int(n**0.5+1), 2).` The end result is that we are left with $n=1$.

## Prime number generator
Reference: Q7
~~~python
primes = [2]

for i in range(3, 2000001, 2):
    is_prime = True
    for n in range(3, int(i**0.5)+1,2):
        if i % n == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)
~~~
This checks all numbers from 3 to 2 million and finds prime numbers in them. It works by **setting a flag for primes** with `is_prime=True`. Then it runs through all numbers from 3 to $\sqrt{ 2,000,000 }$ (because of the square root trick discussed above). *If any number perfectly divides `i`*, *then `i` is not a prime number.* Therefore, we change the flag and break the loop. Note that $i=n$ will never be an issue since we only loop till $n=\sqrt{ i }$.

## Finding highest common factor (HCF)
Reference:Q5

We can find the highest common factor using the Euclidean method. *Given two numbers $a$ and $b$, the HCF of $a$ and $b$ is the same as HCF of $b$ and $a(mod\:b)$*. We can use this fact and repeat this until we get $b=0$. At that point, the value of $a$ is the HCF of $a$ and $b$. To implement this in Python, we use:
~~~python
def hcf(x,y):
	while y>0:
		x,y = y, x%y
	return x
~~~

## Finding lowest common multiple (LCM)
Reference: Q5

The standard relation between HCF and LCM of two numbers is $$HCF(a,b)\times LCM(a,b)=a\times b$$
Rearranging this, we get $LCM=\dfrac{{a\times b}}{HCF}$. Therefore, we can easily define a LCM function using our HCF function.
~~~python
def lcm(x,y):
		return x*y // hcf(x,y)
~~~

## Number of divisors
Reference: Q12

The brute force approach to finding the number of divisors is extremely slow. To optimize this, *we can use a relation between prime factors and the number of divisors.* The relation says that

$$\begin{align}
& \text{If }N\text{ can be expressed as }(a^p)(b^q)(c^r)\dots \text{, then the number of divisors} \\
& \text{is given by } (p+1)(q+1)(r+1)\dots\end{align}$$

To implement this in Python, we use
~~~python
def num_divisors(num):
    if num == 0:
        return 0

    counter = 0
    divisors = 1

    while num % 2 == 0:
        counter += 1
        num = num // 2
    divisors = divisors * (counter+1)

    for i in range(3,int(num**0.5+1),2):
        counter = 0
        while num % i == 0:
            counter += 1
            num = num // i
        divisors = divisors * (counter+1)

    # check if its still a prime
    if num > 1:
        divisors = divisors * 2 # we multiply by two because now we have an additional number with exponent 1
                                # so we must multiply by 1+1 according to the formula

    return divisors
~~~
This counts the occurrence of each prime factor using the `counter` variable.  Lastly, if the number is still a prime, we multiply it by two for reasons explained above.

