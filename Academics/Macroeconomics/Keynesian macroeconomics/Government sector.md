---
color: var(--mk-color-yellow)
tags:
  - sem2-flashcards/macro/keynesian_macro
---
Quick access:
- [[#Impact of government on AD|Impact of government on AD]]
	- [[#Impact of government on AD#New equilibrium condition|New equilibrium condition]]
- [[#Automatic stabilizers|Automatic stabilizers]]
- [[#Impacts of fiscal policy on output|Impacts of fiscal policy on output]]
	- [[#Impacts of fiscal policy on output#Change in government spending|Change in government spending]]
	- [[#Impacts of fiscal policy on output#Change in transfers|Change in transfers]]
	- [[#Impacts of fiscal policy on output#Change in tax rate|Change in tax rate]]
- [[#Impacts of fiscal policy on the budget|Impacts of fiscal policy on the budget]]
	- [[#Impacts of fiscal policy on the budget#Change in government spending|Change in government spending]]
	- [[#Impacts of fiscal policy on the budget#Change in tax rate|Change in tax rate]]
	- [[#Impacts of fiscal policy on the budget#Balanced budget multiplier|Balanced budget multiplier]]
- [[#Full employment budget surplus|Full employment budget surplus]]


## Impact of government on AD
We know $AD=\bar{C}+cY+\bar{I}+\bar{G}$ in an economy with the government sector. *The government can impact AD in two ways here:*
i) It can change government spending ($\bar{G}$)
ii) It can change the tax rate $t$, which changes income $(Y)$

Due to taxes, households will now base their consumption on disposable income, which is post-tax income. Therefore, now we say that **disposable income determines AD, not just income.** We say disposable income $YD=Y+\bar{TR}-tY$, where $tY$ represents income tax revenue. Subbing $YD$ in place of $Y$ in the $AD$ equation gives us $$\begin{align}
AD&=\bar{C}+c(Y+\bar{TR}-tY)+\bar{I}+\bar{G} \\
&=(\bar{C}+c\bar{TR}+\bar{I}+\bar{G}) + cY-ctY \\
&=\bar{A}+c(1-t)Y \\
\end{align}$$
This changes our MPC to $c(1-t)$. Therefore, the *MPC is now affected by the tax rate.* However, we can also write this as $\bar{A}+cY^{d}$, so the MPC out of disposable income remains $c$. However, the MPC out of total income $c(1-t)$ is always less than $c$ (old MPC out of total income) because $0<t<1$. Therefore, *the slope of the AD curve with government is always flatter than the AD curve of a two sector economy.* 

### New equilibrium condition
Now that we have a new equation for AD with government sector, we get a new equilibrium by equating it with $Y$. We get $Y=\bar{A}+c(1-t)Y\implies Y[1-c(1-t)]=\bar{A}$. Therefore,
$$Y_{0}=\left[ \dfrac{1}{1-c(1-t)} \right]\bar{A}$$
Our new equilibrium condition is very similar to the old one. The only change is that now we have our new MPC affected by tax.

## Automatic stabilizers
These are tools that automatically reduce the change in output due to a change in autonomous spending (without government intervention). In other words, *automatic stabilizers are things that reduce the multiplier.* We know with tax, the multiplier is $\dfrac{1}{1-c(1-t)}$. Therefore, **a rise in income tax rate reduces the multiplier and hence is an automatic stabilizer.** Intuitively, increased income tax means there is a smaller change in income. Therefore, income increases less during booms and falls less during recessions, which is the goal of a stabilizer.

Unemployment benefits are another example of automatic stabilizers. With these benefits, $TR$ rises even when $Y$ falls due to the loss of a job. Therefore, the total change in AD shrinks, which is what a stabilizer does.

## Impacts of fiscal policy on output
### Change in government spending
Suppose government spending increases. This increases $\bar{A}$, so the $AD$ curve shifts upwards by $\Delta G$. Clearly, this also increases output by $\Delta Y$. Our question however, is *how much has $Y$ increased due to an increase in $G$*?
![[WhatsApp Image 2025-04-27 at 15.23.49_a65aa816.jpg|center|400]]
To answer our question, we start by differentiating both sides of the $Y=AD$ equilibrium condition. **Differentiating both sides is the standard procedure to derive a multiplier.** This gives us $\Delta Y=\Delta G+c(1-t)\Delta Y$. Note that $\bar{A}$ becomes $\Delta G$, not $\Delta A$. This is because *we are differentiating wrt G and the other terms in A are not dependent on G, so they simply become zero.* Isolating $\Delta Y$ gives us:
$$\Delta Y=\left[ \dfrac{1}{1-c(1-t)} \right]\Delta G$$
Therefore, our multiplier, denoted by $\alpha_{G}$ is $\dfrac{1}{1-c(1-t)}$, the same government multiplier as before but now it is impacted by taxes.

### Change in transfers
Suppose transfers increase. Once again, we'll differentiate $Y=AD$ to get $\alpha_{TR}$, the transfers multiplier.

We start out with $Y=\bar{C}+\bar{I}+\bar{G}+c \bar{TR}+c(1-t)Y$. Differentiating with respect to $TR$ yields $\Delta Y=c\Delta TR+c(1-t)\Delta Y$. Isolating $\Delta Y$, we get $$\Delta Y=\left[ \dfrac{c}{1-c(1-t)} \right]\Delta \bar{TR}$$
Since $c<1$, $\alpha_{TR}<\alpha_{G}$. *The multiplier for transfers is smaller than that of government by a factor of $c$*, *because only $c$ of $TR$ is spent and $1-c$ is saved.* The part that is saved does not have an impact on output, so only $c$ of $TR$ actually impacts $Y$. Unlike transfers, all of government spending directly impacts output and there is nothing saved, so $\alpha_{G}>\alpha_{TR}$. **This tells us that an increase in government spending is more effective at increasing output than an increase in transfers,** which can have useful policy implications.

### Change in tax rate
Let the tax rate fall from $t\to t'$. The slope of the new $AD$ curve rises since $c(1-t')<c(1-t)$. An increased slope means output also increases from $Y_{0}\to Y_{1}$. *Unfortunately, we cannot differentiate both sides to find the change in Y. We must subtract $Y_{1}-Y_{0}$ to get the multiplier for tax rate.*

At equilibrium, $Y_{0}=\dfrac{\bar{A}}{1-c(1-t)}$, $Y_{1}=\dfrac{\bar{A}}{1-c(1-t')}$. Subtracting gives
$$\begin{align}
Y_{1}-Y_{0}&=\dfrac{\bar{A}}{1-c(1-t')}-\dfrac{\bar{A}}{1-c(1-t)} \\
&=\dfrac{{\bar{A}[1-c(1-t)]-\bar{A}[1-c(1-t')]}}{[1-c(1-t')][1-c(1-t)]} \\
&=\dfrac{{c\bar{A}(t-t')}}{[1-c(1-t')][1-c(1-t)]} \\
&=\dfrac{{c\cancel{\bar{A}}(t-t')Y_{0}}}{[1-c(1-t')]\cancel{\bar{A}}} \\
&=\dfrac{{cY_{0}(t-t')}}{1-c(1-t')} \\
&=\left[ \dfrac{{cY_{0}}}{1-c(1-t')} \right]\Delta t \\
\end{align}$$
**The key in this derivation is to substitute $\dfrac{Y_{0}}{\bar{A}}=\dfrac{1}{1-c(1-t)}$** (follows from $\alpha_{G}$) to simplify the denominator and cancel $\bar{A}$. We consider the old output level and old tax rate so that the $t'$ term isn't cancelled out. The multiplier $\alpha_{t}$ is like $\alpha_{G}$ but uses the new tax rate and also multiplies $\alpha_{G}$ with a fraction of the initial output.

## Impacts of fiscal policy on the budget
The government's budget surplus is denoted by $BS=TA-\bar{G}-\bar{TR}$ or $BS = tY-\bar{G}-\bar{TR}$ in case of proportional income tax. It is a positively sloped linear function, and it tells us that *at low levels of income, we have a negative budget surplus (deficit), and at high levels of income we have a budget surplus.* If $tY>{{\bar{G}+\bar{TR}}}$, we have a surplus as tax revenues are greater than government expenditure.
![[WhatsApp Image 2025-04-27 at 16.52.54_8e658935.jpg]]

### Change in government spending
Let's see how much an increase in government spending changes budget. At first, it might seem trivial. From the $BS$ equation, you'd expect $BS$ and $G$ to have a 1:1 negative relationship. *However, an increase in G also increases Y due to the multiplier, which increases tax revenues. Therefore, a rise in G will both decrease and increase the budget surplus.* We'll express this mathematically to see which effect is greater.

Deriving the budget surplus multiplier due to a change in government spending gives us
$$\begin{align}
BS&=tY-\bar{G}-\bar{TR} \\
\Delta BS&=t\Delta Y-\Delta \bar{G} \\
&=t\alpha_{G}\Delta \bar{G}-\Delta \bar{G} \\
&=\left[ \dfrac{t}{1-c(1-t)}-1 \right]\Delta \bar{G} \\
&=-\left[ \dfrac{{(1-c)(1-t)}}{1-c(1-t)} \right]\Delta \bar{G}  \\
&<0
\end{align}$$
**Clearly, the budget surplus multiplier is negative. Therefore, increasing government spending does in fact reduce the budget surplus.** When deriving this, keep in mind that we are considering a change in $G$. The change in $Y$ then becomes [[Government sector#Change in government spending|the multiplier]] times the change in $G$. Then we take $\Delta \bar{G}$ common and simplify.

### Change in tax rate
Just like government spending, changing the tax rate has two effects on the budget. *Since we increase the tax rate, we get increased tax revenue. However, raises the tax rate also decreases income, meaning we get reduced tax revenue.* Once again, we'll mathematically deduce which effect is stronger.

We will calculate the change in budget surplus wrt a change in tax, making both $t$ and $Y$ functions (as $Y$ is a function of $t$). **Therefore, we must use the product rule when differentiating.** Previously, since $t$ was just a scalar, we could take it out and write it as $t\Delta Y$. We can no longer do that in this case.
$$\begin{align}
BS&=tY-\bar{G}-\bar{TR} \\
\Delta BS&=\Delta (tY) \\
&=Y_{0}\Delta t+t\Delta Y_{0} \\
&=Y_{0}\Delta t+t\left[ \dfrac{cY_{0}}{1-c(1-t')} \right]\Delta t \\
&=Y_{0}\Delta t\left[ 1+\dfrac{ct}{1-c(1-t')} \right] \\
&>0
\end{align}$$
Here, we know what $\Delta t$ is, but we don't know what $\Delta Y_{0}$ is. Therefore, we express $\Delta Y$ in terms of $\Delta t$. **Since $\Delta t$ is known, we don't have to substitute anything for it.** All the elements of this multiplier are positive, therefore the multiplier is positive. This tells us that *increasing tax rate does increase the budget surplus.*

### Balanced budget multiplier
In this case, our increase in $G$ is equally offset by an increase in $tY$ so that the budget always stays in balance. **In a balanced budget, $\alpha_{G}=1$ always.** Therefore, $\Delta Y=\Delta G$.

## Full employment budget surplus
We have seen that increased government spending increases income but leads to budget deficits, while increased taxation decreases income but leads to budget surpluses. Therefore, *a budget surplus can serve as a tool to see the direction of the overall fiscal policy.* Eg: deficit $\implies$ expansionary fiscal policy $\implies$ increased output and employment.

However, it comes with one big issue: **the budget surplus can change due to changes in autonomous private spending.** If $\bar{A}$ changes, then $Y$ changes, which changes tax revenue ($tY$). This change in budget surplus due to autonomous private spending is bad news for a tool meant to examine the direction of fiscal policy because it means our budget deficit can increase without a change in fiscal policy. **This makes budget surplus an unreliable tool** to look at the direction of fiscal policy.

To fix this, we need some tool that is independent of the business cycle, so that it is not affected by private spending and shows only the effects of fiscal policy. *This is achieved by the full employment budget surplus.* The full employment budget surplus is determined by full employment GDP, which is a **benchmark level of GDP, and is not impacted by current changes in private investment since its a theoretical level.** Therefore, it eliminates the noise of private spending and focuses only on fiscal policy.

The full employment budget surplus represents the budget surplus at the full employment level of income or at potential output. Subtracting our actual budget surplus from the full employment level of budget surplus, we get
$$BS^{*}-BS =t(Y^{*}- Y)$$

**The only difference between the two is the level of income tax collected.** If output $Y$ is less than full employment output $Y^*$, we see that the full employment budget surplus is positive and vice versa. The difference between $BS^*$ and $BS$ is called *the cyclical component of the budget.*

**In a recession, we have a deficit because $Y<Y^*\implies BS<BS^*$**. Conversely, in a boom, we have a surplus since our output exceeds the benchmark level of output.

Even this measure isn't perfect. Firstly, *we don't know the true level of full employment output.* It is simply an estimate of output at a high level of employment. Even if we consider it just as a high employment level of budget surplus, *it isn't a perfect measure of the thrust of fiscal policy since a change in spending perfectly offset by change in tax doesn't affect the deficit.* There are so many variables in fiscal policy like tax rate, transfers and government purchases that it is difficult to describe fiscal policy in a single number.