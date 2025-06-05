---
color: var(--mk-color-purple)
tags:
  - "#sem2-flashcards/mme/vectors_and_matrices"
---
Quick access:
- [[#Context|Context]]
- [[#The model|The model]]
	- [[#The model#Demand for a good|Demand for a good]]

## Context
This model was used in the Soviet Union, a command economy. Since the resources are owned by the state, they can decide exactly how much to use and where to use it. **The resources in this model are interdependent.**

## The model
The coefficient $a_{ij}$ represents the output that the $i^{th}$ industry needs to produce so we can produce one unit of the $j^{th}$ good. If $a_{IS}=0.6$, that means we need $0.6$ units of industrial output ($I$) to produce $1$ unit of service output ($S$). This is how the model shows the interdependence of resources.

It follows that *if we want to produce $x_{j}$ units of the $j^{th}$ good, we'll need $a_{ij}x_{j}$ units of the $i^{th}$ good.* Logically, $a_{ii}$ must be less than 1. We must use less than $1$ unit of the $i^{th}$ good to produce more of the $i^{th}$ good, otherwise we'd just lose output when producing the $i^{th}$ good.

### Demand for a good
The demand for the $i^{th}$ good is **its total input demand from all industries and demand from consumers.** We know demand from the $j^{th}$ industry for $x_{j}$ units of output is $a_{ij}x_{j}$. Let final demand from consumers be denoted by $b_{i}$. Then, the total demand for the $i^{th}$ good is $x_{i}=a_{i_{1}}x_{1}+a_{i_{2}}x_{2}+\dots+a_{in}x_{n}+b_{i}$. This goes for all $i=1,2,\dots,n$, which gives us a system of equations.
![[WhatsApp Image 2025-05-28 at 12.15.36_a926593e.jpg]]

We can move all the $x$ terms to one side and isolate the constant $b_{i}$. Doing that gives us the system:
![[WhatsApp Image 2025-05-28 at 12.20.03_31083ea6.jpg]]
This is the **final Leontief system.** We can represent this as $(I-A)X=B$. The $a$ terms are called input (or technical) coefficients. Solving this system for $x_{i}$ will give outputs of each industry such that the combined demand of industry and final consumption can be exactly met.