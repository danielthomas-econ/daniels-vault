---
color: var(--mk-color-yellow)
tags:
  - sem1-flashcards/math_ge/calc/differentiation
---
Trig substitution is a good differentiation technique for when **we encounter square roots in our question.** Often, these roots can be complicated and lengthy to solve. We can simplify these roots by substituting them with trigonometric functions. The main idea here is to use trigonometric [[Important formulae#Pythagorean identities|Pythagorean identities]] to simplify the roots into easy to solve equations.

We should use trig sub for 3 cases:
- $\sqrt{a^2-x^2}$
- $\sqrt{x^2-a^2}$
- $\sqrt{x^2+a^{2}}$ 

### Case 1:
$\sqrt{a^2-x^2}$ resembles the identity $1-sin^2\:\theta=cos^2\:\theta$. Here, we use $x=a\:sin\:\theta$. Let's take $a=1$. Then, $\sqrt{1-x^2}$ can be written as $\sqrt{1-sin^2\:\theta}$. *From the Pythagorean identity, we know $1-sin^2\:\theta=cos^2\:\theta$*. Substituting that under the root, we get $\sqrt{cos^2\:\theta}=cos\:\theta$. Therefore, we have simplified $\sqrt{1-x^2}$ to $cos\:\theta$.

Therefore, $\dfrac{d}{d\theta}(cos\:\theta)=-sin\:\theta$. *But we need the derivative in terms of* $x$. For that, **we use the chain rule with $cos\:\theta$**. $\dfrac{d}{dx}(cos\:\theta)=\dfrac{d}{d\theta}(cos\:\theta)\times\dfrac{d\theta}{dx}$.We know $\dfrac{dx}{d\theta}=cos\:\theta$ ($x=sin\:\theta$). Substituting, we get $\dfrac{d}{dx}(cos\:\theta)=-sin\:\theta\times\dfrac{1}{cos\:\theta}$. We can sub back $x=sin\:\theta$ and $cos\:\theta=\sqrt{1-x^{2}}$ to get the final answer as $\dfrac{-x}{\sqrt{1-x^2}}$.

### Case 2:
$\sqrt{x^2-a^2}$ resembles the identity $sec^2\:\theta-1=tan^2\:\theta$. Therefore, we use $x=a\:sec\:\theta$. Taking $a=1$, we get $\sqrt{sec^2\:\theta-1}=\sqrt{tan^2\:\theta}=tan\:\theta$. The derivative of $tan\:\theta$ w.r.t $\theta$ is $sec^2\:\theta$. **Once again, to get the derivative w.r.t $x$**, **we use the chain rule.** $\dfrac{d}{dx}(tan\:\theta)=\dfrac{d}{d\theta}(tan\:\theta)\times\dfrac{d\theta}{dx}$. We know $\dfrac{dx}{d\theta}=sec\:\theta\:tan\:\theta$ ($x=sec\:\theta$). Therefore, $\dfrac{d}{dx}(tan\:\theta)=sec^2\:\theta\times\dfrac{1}{sec\:\theta\:tan\:\theta}=\dfrac{sec\:\theta}{tan\:\theta}$. We know $x=sec\:\theta$ and $\sqrt{x^2-1}=tan\:\theta$. Therefore, our final answer will be $\dfrac{x}{\sqrt{x^2-1}}$.

### Case 3:
$\sqrt{x^2+a^2}$ resembles the identity $tan^2\:\theta+1=sec^2\:\theta$. Therefore, we use $x=a\:tan\:\theta$. Taking $a=1$, we get $\sqrt{tan^2\:\theta+1}=\sqrt{sec^2\:\theta}=sec\:\theta$. To get $\dfrac{d}{dx}(sec\:\theta)$, we take $sec\:\theta\:tan\:\theta\times \dfrac{1}{sec^2\:\theta}=\dfrac{tan\:\theta}{sec\:\theta}$. Substituting $x=tan\:\theta$, we get $\dfrac{x}{\sqrt{x^2+1}}$. 


## Flashcards
Q1) Differentiate $\arctan\left( \dfrac{{\sqrt{ 1+x^{2} }-1}}{x} \right)$ wrt $\arcsin\left( \dfrac{2x}{1+x^{2}} \right)$.
?
Ans) When we see $\arcsin\left( \dfrac{2x}{1+x^{2}} \right)$, we must immediately think of the [[Important formulae#Double angle identities|important formula]] $\sin (2\theta)=\dfrac{{2\tan \theta}}{1+\tan ^{2}\theta}$. The term inside $\arcsin$ is of the exact same form. **Therefore, we substitute $x=\tan \theta$**. Let $u=\arctan\left( \dfrac{{\sqrt{ 1+x^{2} }-1}}{x} \right)$, $v=\arcsin\left( \dfrac{2x}{1+x^{2}} \right)$.
.
Sub $x=\tan \theta$ in $u$. $u=\arctan\left( \dfrac{{\sqrt{ 1+\tan ^{2}\theta }-1}}{\tan \theta} \right)=\arctan\left( \dfrac{{\sec \theta-1}}{\tan \theta} \right)$
$=\arctan\left( \dfrac{{\dfrac{1}{\cos \theta}-1}}{\dfrac{{\sin \theta}}{\cos \theta}} \right)=\arctan\left( \dfrac{{1-\cos \theta}}{\sin \theta} \right)$. We have to use trig sub again. We know $\cos 2\theta=1-2\sin ^{2}\theta$. Therefore, we can say $\cos \theta=1-2\sin ^{2}\left( \dfrac{\theta}{2} \right)$. Therefore, $\cos \theta=2\sin ^{2}\left( \dfrac{\theta}{2} \right)$. *Now we have to get $\sin \theta$ in terms of $\dfrac{\theta}{2}$ so that we can cancel terms.* We know $\sin 2\theta=2\sin \theta \cos \theta$. Therefore, $\sin \theta=2\sin\left( \dfrac{\theta}{2} \right)\cos\left( \dfrac{\theta}{2} \right)$. Sub both these in above.
.
We get $u=\arctan\left( \dfrac{{2\sin ^{2}\left( \dfrac{\theta}{2} \right)}}{2\sin\left( \dfrac{\theta}{2} \right)\cos\left( \dfrac{\theta}{2} \right)} \right)$. Cancel out the terms, and we get $u=\arctan\left( \dfrac{{\sin\left( \dfrac{\theta}{2} \right)}}{\cos\left( \dfrac{\theta}{2} \right)} \right)=\arctan\left( \tan\left( \dfrac{\theta}{2} \right) \right)$. Therefore, $u=\dfrac{\theta}{2}$
This means $\dfrac{du}{d\theta}=\dfrac{1}{2}$.
.
Sub $x=\tan \theta$ in $v$. We get $v=\arcsin\left( \dfrac{{2\tan \theta}}{1+\tan ^{2}\theta} \right)=\arcsin(\sin 2\theta)=2\theta$. Therefore, $\dfrac{dv}{d\theta}=2$. *Our main goal was to find $u$ wrt $v$ according to the question.* $\dfrac{du}{dv}=\dfrac{du}{d\theta}* \dfrac{d\theta}{dv}=\dfrac{1}{2}* \dfrac{1}{2}=\dfrac{1}{4}$.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
<!--SR:!2025-01-07,4,270-->
