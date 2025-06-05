---
color: var(--mk-color-base-60)
---
Since trig functions are still functions, they require a [[Domain, range and codomain#Domain|domain]] and a [[Domain, range and codomain#Range|range]] to be defined. We'll go over the range and domain of all 6 functions and the reasoning behind it. We can remember it in pairs: sin and cos, cosec and sec, tan and cot all have similar domains and ranges.

Quick access:
[[Domain and range of trig functions#sin|sin]]
[[Domain and range of trig functions#cos|cos]]
[[Domain and range of trig functions#cosec|cosec]]
[[Domain and range of trig functions#sec|sec]]
[[Domain and range of trig functions#tan|tan]]
[[Domain and range of trig functions#cot|cot]]

[[Domain and range of trig functions#arcsin|arcsin]]

[[Domain and range of trig functions#Periodicity of trig functions|Periodicity of trig functions]]

## sin
We know that the $sin$ value corresponds to the $y$ coordinate of a [[Unit circle and ratios|unit circle]]. Therefore, $sin$ repeats itself after every $2\pi$ (circumference of the unit circle). *$sin$ will be $0$ at the origin since at $0$ degrees, the coordinate in the unit circle will be the rightmost coordinate ($1,0$)*, and $sin=y$ coordinate. $sin$ is equal to $0$ for every $n^{th}$ multiple of $\pi$.

We can also see that the value of $sin$ is defined for all input values ($x$ values). Therefore, **the domain of $sin$ is all real numbers.** However, we can see that the output of the $sin$ function is only between $1$ and $-1$. Therefore, **the range of $sin$ is $[-1,1]$**.
![[sine-graph.svg]]

## cos
The $cos$ graph is a wave too, however, the value of $cos\:0=1$. Therefore, *the difference between $sin$ and $cos$ graph is that the $cos$ graph has $y=1$ at the origin.* Once again, $cos\:0=1$ because of the unit circle. At $0$ degrees, there is just a line to the right, i.e. the coordinates are $(1,0)$. Since $cos$ represents $x$ values, we get $cos\:0=1$.

Just like the $sin$ graph, the domain is all real numbers and the range is $[-1,1]$.
![[cosine-graph.svg]]

## cosec
We know that $csc\:\theta=\dfrac{1}{sin\:\theta}$, and its graph is very weird. Since we have $sin\:\theta$ in the denominator, **the graph of $csc\:\theta$ will not be defined if $sin\:\theta$ is zero.** Therefore, the domain of the function will be {$x\:|\:x\in R\:and\:x\ne n\pi$}.

The range of the function will be {$y\:|\:y\in R\:and\:y\ge1\:or\:y\le1$}. This is because the value of $sin\:\theta$ is restricted to $[-1,1]$, and the reciprocals of these values will always fall outside the interval. Eg: Reciprocal of $\frac{1}{2}$ is $2$, which is outside the interval.
![[unnamed.gif|center]]

## sec
$sec\:\theta$ is just like $csc\:\theta$, but it is the reciprocal of $cos\:\theta$. Therefore, its **domain will be real numbers except for where $cos\:\theta=0$**. $cos\:\theta$ is zero at $\dfrac{\pi}{2}$,and loops every $2\pi$. This means that $cos\:\theta=0$ for every $\dfrac{(2n+1)\pi}{2}$. Therefore, the domain will be 
{$x\:|\:x\in R\:and\:x\ne \dfrac{(2n+1)\pi}{2}$} and its range is the same as $csc\:\theta$, 
{$y\:|\:y\in R\:and\:y\ge1\:or\:y\le1$}.
![[Pasted image 20240901175005.png|center|350]]

## tan
The $tan$ function is the same as $\dfrac{sin\:\theta}{cos\:\theta}$. Therefore, its **domain will be all real numbers except where $cos\:\theta=0$, just like $sec$**. We can express this as {$x\:|\:x\in R\:and\:x\ne \dfrac{(2n+1)\pi}{2}$}. The graph of $tan\:\theta$ has a **range of all real numbers,** since there is no restriction on the $y$ axis.

This is the first function we've encountered that has a periodicity of $\pi$. $tan\:\theta$ repeats after $\pi$ intervals since *its value depends on the ratio of $sin$ to $cos$*, *which repeats after every $\pi$intervals.* 
![[unnamed 1.gif|center|500]]

## cot
$cot\:\theta$ is the ratio of $cos\:\theta$ and $sin\:\theta$. Since $sin$ is in the denominator, the **domain of $cot$ is all real numbers except where $sin\:\theta=0$**. This is written as {$x\:|\:x\in R\:and\:x\ne n\pi$}. Just like $tan\:\theta$, the graph has a range of all real numbers and repeats after every $\pi$ intervals.
![[Pasted image 20240901181831.png|center|500]]

## arcsin
The domain of the $arcsin$ function is $[-1,1]$. **This is because the set of all input values of $arcsin$ is the set of all output values of** $sin$. Since $sin$ is periodic and repeats after every $2\pi$, we have to restrict the range. Otherwise, we'd have multiple outputs, making $arcsin$ not a function anymore. Therefore, we restrict the range to $[\dfrac{-\pi}{2},\dfrac{\pi}{2}]$. In this interval, each input corresponds to a unique angle. *This means that $arcsin$ only exists in quadrants 1 and 4.* 
![[0-6.png]]

## Periodicity of trig functions
From the graphs, we see that $sin,\:cos,\:csc$ and $sec$ repeat their values after every $2\pi$ intervals. This means that $sin(2\pi+x)=sin(x)$ (you can replace $sin$ with the other three functions too). This also means that $sin(\pi+x)=-sin(x)$.

$tan$ and $cot$ repeat every $\pi$ intervals due to the ratio of $sin\:\theta$ and $cos\:\theta$ repeating after $\pi$ intervals. We can prove this by:$$tan\:(\pi+x)=\dfrac{sin\:(\pi+x)}{cos\:(\pi+x)}=\dfrac{-sin\:(x)}{-cos\:(x)}=\dfrac{sin\:(x)}{cos\:(x)}=tan\:(x)$$

