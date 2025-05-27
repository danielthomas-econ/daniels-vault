---
color: var(--mk-color-turquoise)
tags:
  - sem2-flashcards/macro/financial_markets
---
Quick access:
- [[#Assumptions|Assumptions]]
- [[#The determinants of money demand|The determinants of money demand]]
- [[#The equation for money demand|The equation for money demand]]
- [[#Money demand with checkable deposits|Money demand with checkable deposits]]
- [[#Demand for central bank money|Demand for central bank money]]


## Assumptions
Suppose you start out with a certain level of wealth and *you only have the choice between two assets: money or bonds.* Money can be used for transactions and is more convenient, but it does not pay interest. On the other hand, bonds pay a positive rate of interest, but they cannot be used for transactions. Also note that **bonds come with a transaction cost** (like calling up your broker every time you want to make a transaction).

## The determinants of money demand
Based on the scenario given above, most people would want to hold both money and bonds. The proportion is decided by:

i) **Level of transactions:** You will want to hold enough money to cover your short term transactions. This way you can avoid the cost of having to convert your bonds to cash. Therefore, someone with a higher level of transactions will *demand more money.*
ii) **Interest rate:** The only reason you would want bonds is for their interest rate. The higher the interest rate on bonds, the higher the demand for bonds, which subsequently leads to *lower demand for money.*

## The equation for money demand
We know an individual's demand for money depends on their level of transactions and the interest rate. Similarly, the market's demand for money is determined by the total level of transactions and the interest rate. *It can be hard to measure total level of transactions in the economy. However, it is roughly proportional to nominal income.* Therefore, we use nominal income in the equation. The relation between demand for money, nominal income and the interest rate is given by:
$$\begin{align}
M^{d}=\$Y L(i) \\
(-)
\end{align}$$
This tells us that **money demand has a 1:1 positive relation with income, and a negative relation with interest based on the function L.** 
![[WhatsApp Image 2025-03-24 at 21.26.08_05196a90.jpg]]

## Money demand with checkable deposits
There are two types of money: *currency (supplied by central banks) and checkable deposits (supplied by commercial banks).* Till now, we've assumed only currency exists. Let's make this more realistic by introducing checkable deposits.

Now due to the existence of checkable deposits, **banks must keep reserves.** For a commercial bank, their assets are these reserves and bonds, while their liabilities are the deposits. For a central bank, their assets are bonds and their liability is central bank money.

The introduction of reserves into our model gives us the main difference: **not all central bank money is held as currency by the public as some of it is kept as reserves by banks.** The interest rate in this economy is determined by the *supply and demand for central bank money.*

## Demand for central bank money
We know that once a person decides how much money they'll hold, they must also decide *what proportion will be held as currency and checkable deposits.* Note that they only have two options. Therefore, their money is either in currency or checkable deposit form.

Let's say they hold a fixed proportion of their money $c$ as currency, and consequently they hold a fixed proportion $(1-c)$ as checkable deposits. Then, we have currency demand $CU^d$ and deposit demand $D^d$ as:
$$\begin{align}
CU^d&=cM^d \\
D^d&=(1-c)M^d
\end{align}$$

We know that **the larger the amount of checkable deposits, the larger the amount of bank reserves.** Let the bank's reserve ratio (amount of reserves per checkable deposit) be $\theta$. By definition, $R=\theta D$. Therefore, we can simply sub in $D^d$ to get the demand for reserves $R^d$. So we have:
$$R^{d}=\theta(1-c)M^d$$

We know *the demand for central bank money is the demand for currency and the demand for reserves* (as reserves are commercial bank money held with the central bank, so commercial banks demand reserves from the central bank). Let $H^d$ represent the demand for central bank money. It is also called *high powered money or monetary base.* We get $$\begin{align}
H^d&=CU^{d}+R^d \\
H^d&=cM^{d}+\theta(1-c)M^d \\
H^d&=[c+\theta(1-c)]M^d
\end{align}$$
We already know that $M^d=\$YL(i)$. Replacing that in the above equation gives us the final money demand equation.
$$H^d=[c+\theta(1-c)]\$YL(i)$$
where,
$c$ is the proportion of money held in currency
$\theta$ is the reserve ratio

**Let us interpret this with an example:** Suppose $c=0, \theta=0.1$. In this extreme case, people only hold checkable deposits and the reserve ratio is $0.1$. Substituting this in the equation gives us $H^d=0.1\$YL(i)$. *This is interpreted as the demand for central bank money makes up 1/10 of the total demand for money.* This makes perfect sense. Since the public deposits all their money, they do not demand any central bank money (no currency demand). Banks however, will demand 10% of the deposits as reserves, which is central bank money. So the demand for central bank money is entirely driven by the demand for reserves, which is 1/10th the demand for money. 

*Note that the demand for central bank money is always less than the overall demand for money.* This is because the demand for reserves is only a fraction of the demand for checkable deposits. Mathematically, $[c+\theta(1-c)]$ is never greater than $1$ for $c, \theta\in(0,1)$.

![[WhatsApp Image 2025-03-24 at 23.58.21_4186ad0f.jpg]]