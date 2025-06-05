---
color: var(--mk-color-pink)
tags:
  - sem1-flashcards/mme
---
Quick access:
[[Investments#Present discounted value and future value|Present discounted value and future value]]
	[[Investments#Future value|Future value]]
	[[Investments#Present discounted value|Present discounted value]]
[[Investments#Perpetuity|Perpetuity]]
[[Investments#EMI|EMI]]

## Present discounted value and future value
### Future value
Assume you have $\$1$ today and an interest rate of $r\%$. In a year, that becomes $\$1( 1+r)$. In two years, it becomes $\$1(1+r)(1+r)$. This means in $t$ years, your $\$1$ becomes $\$1(1+r)^t$. *This is called the future value of a dollar.* In general, we can write the future value as $a(1+r)^t$, where $1+r$ is the growth rate and $a$ is the initial value. **If we are told interest is compounded continuously, $FV=ae^{rt}$ as the growth rate is $e^r$**.

You would prefer $\$1$ today over anything less than $\$1(1+r)$ in a year. This is because $\$1$ today = $\$1(1+r)$ in a year. If you know you'd get $\$1(1+r)$ in a year, why would you accept anything less than that? Similarly, you'd prefer anything more than $\$1(1+r)$ over $\$1$ today.

### Present discounted value
Present value tells us *how much money we should have today to be indifferent with a certain amount at a point $t$ in the future.* It is given by the formula $PV=\dfrac{a}{(1+r)^t}$ or $\dfrac{a}{e^{rt}}$. Let's use this with our previous example of $\$1$ today = $\$1(1+r)$ in a year. This tells us the future value of $\$1$ is $\$1(1+r)$. So let's find the present value of $\$1(1+r)$.

Sub $a=1(1+r)$ in the $PV$ formula and we get $\dfrac{1(1+r)}{(1+r)^t}$. Cancelling $1+r$, we get $\dfrac{1}{(1+r)^{t-1}}$. **Sub $t=1$ as our time period was one year.** We get $\dfrac{1}{(1+r)^0}=1$. Therefore, the present value of $\$1(1+r)$ is $\$1$.

## Perpetuity
Perpetuity is a financial instrument that **gives us the right to earn $\$x$ per year forever.** Therefore, in $t$ periods, our cash flow will be $x$ in each period. Let's try and calculate the $PV$ of a perpetuity.

The $PV$ of time period $1$ is $\dfrac{x}{1+r}$. For time period $2$, the $PV$ is $\dfrac{x}{(1+r)^{2}}$. This goes on till $\dfrac{x}{(1+r)^t}$. Since a perpetuity is infinite, it doesn't stop here and it continues forever. *This becomes a [[Academics/Mathematical methods for Economics/Limits, Continuity and Series/Series#Infinite geometric series|infinite geometric series]] with $a=\dfrac{x}{1+r}$ and the common ratio as $\dfrac{1}{1+r}$*. The sum of present values becomes $\dfrac{\dfrac{x}{1+r}}{1-\dfrac{1}{1+r}}$. This becomes $\dfrac{\dfrac{x}{1+r}}{\dfrac{r}{1+r}}$, which finally gives us the formula $$PV(Perpetuity)=\dfrac{x}{r}$$ 

## EMI
In an EMI, your cash flow will be $\$x$ for $t$ periods at $p\%$ interest, which we'll write as $r=\dfrac{p}{100}$. This makes the $PV$ for period one $\dfrac{x}{1+r}$, $PV$ for period two is $\dfrac{x}{(1+r)^{2}}$ all the way until period $t$, where the $PV$ becomes $\dfrac{x}{(1+r)^t}$.

This makes your total repayment a [[Academics/Mathematical methods for Economics/Limits, Continuity and Series/Series#Finite geometric series|finite geometric series]] with starting term $\dfrac{x}{1+r}$ and common ratio $\dfrac{1}{1+r}$. The sum of this series becomes $\dfrac{\dfrac{x}{1+r}\left[ 1-\left( \dfrac{1}{1+r} \right)^{t} \right]}{1-\dfrac{1}{1+r}}$. Take LCM in the denominator and cancel $1+r$ to get the final formula 
$$Total\:loan\:(L)= \dfrac{x}{r}\left[ 1-\left( \dfrac{1}{1+r} \right)^t \right]$$
*This means that with an EMI of $\$x$ given $r$ and $t$, we can obtain a loan of $\$L$*. Therefore an EMI loan is a function of three variables.

Let's get the converse of this and find out given the total loan, how much should my EMI be. To do this, we simply have to isolate $x$ and we have our answer. **Therefore, given a total loan, our EMI has to be** 
$$EMI\:(x)=\dfrac{rL}{1-\left( \dfrac{1}{1+r} \right)^t}$$


## Flashcards
Q1) Suppose you own an asset whose value after $t$ time is given by $V(t)=10000e^{\sqrt{ t }}$. If the interest rate is $8\%$ compounded continuously, what is the optimal time to sell the asset?
?
Ans) To solve this question, we need to understand the concept behind the question. We have two options: *we can either hold the asset and get a certain growth rate from it, or sell the asset and invest the money @ 8% continuous interest.* Logically, we will hold the asset only if we get more than an 8% return. To find out what the rate of return is, we must find the **proportionate rate of change.** This tells us how much the asset has grown wrt its original value.
.
As long as proportional growth is more than $0.08$, our asset grows at a rate faster than $0.08$ (effectively we're getting interest at a rate higher than $0.08$). **The optimal time will be when proportionate growth = rate of interest.** Before this point, growth > interest, and after this, growth < interest. Therefore, we can maximize profits by selling at growth = interest.
.
Proportionate rate of growth is $\dfrac{V'(t)}{V(t)}=\dfrac{1}{2\sqrt{ t }}=0.08$. Therefore, $\sqrt{ t }=\dfrac{1}{0.16}=\dfrac{100}{16}$. Therefore, $t=\dfrac{10000}{256}=39.06$. Therefore, the asset must be sold after $39.06$ years.