---
color: var(--mk-color-pink)
tags:
  - sem1-flashcards/math_ge/calc/polar
---
The polar coordinate system is an alternative to the normal cartesian plane we use (x,y coordinates). In the polar plane, there is only one axis, called the **polar axis.** The origin is replaced by a dot called the **pole.**

To specify a point on the polar plane, *we specify a line $r$ and the angle $\theta$ by which we should rotate this line.* This line of length $r$ is called the **terminal line.** If we extend it in the opposite direction by the same distance, it is called **extended terminal.** By convention, a positive value of $\theta$ moves in the anti-clockwise direction and vice versa. Having the values of $r$ and $\theta$ will give us the polar coordinate $P(r,\theta)$.
![[Point_in_Polar_coordinates.png|center]]

### Extended terminal
To plot values of $-r$, we plot it like how we normally would with $r$. Once we plot it, just **flip it $\pi$ or 180 degrees.** Just like how flipping $x$ 180 degrees gives $-x$ in the cartesian system, we get $-r$ here.
![[Pasted image 20240914151123.png|center]]

### Pole
The pole serves as the polar system's *equivalent to the origin* in the cartesian system. The pole serves as the vertex from which we measure $\theta$. *At the pole, $\theta$ is not defined* since the pole is a point. Therefore, we denote pole by $r=0$ (without mentioning a value of $\theta$).
![[f-d_cf134b8f0657654119196b4e998a32cd6cd860174b2f6468de3f6270+IMAGE_TINY+IMAGE_TINY.jpg|center|350]]


## Polar coordinates aren't unique
While a certain $P(r,\theta)$ will always give one unique point, there are many ways to express a certain value in the polar plane. First of all, **we know that $2\pi$ is one full rotation of a circle.** Since polar coordinates rely on angles, adding $2\pi$ to $\theta$ will end up resulting in the same angle. Therefore, $P(r,\theta)=P(r,\theta\pm2n\pi)$.

Another way to represent a coordinate is to *change the sign of $r$ and add $\pi$ to the angle.* This works because changing the sign itself flips it $\pi$ degrees, so adding $\pi$ back reverses that change. Therefore, $P(r,\theta)=P(-r,\theta\pm\pi)$.
![[Pasted image 20240914152441.png|center]]