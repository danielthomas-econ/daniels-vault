---
color: var(--mk-color-green)
---


## Formula
If $0< p< 1$, then the $(100p)^{th}$ percentile of the distribution of a continuous rv $X$ is denoted by $\eta(p)$ and is given by
$$p=F(\eta(p))=\int \limits_{{-\infty}}^{\eta (p)}f(y)dy$$

$p$ is the area under the curve. If $p=0.36$, it gives us the $(100p)^{th}=36^{th}$ percentile and is represented with $\eta(0.36)$. Therefore, we can say that 
$$P(X\leq \eta(p))=p$$

Example: $f(x)=\dfrac{10}{x^{2}}$, $x\geq 10$. Find the $90^{th}$ percentile.
?
Ans) From definition of percentile, $\int\limits_{-\infty}^{\eta(0.9)}f(x)dx=0.9$. Therefore, $\int\limits_{10}^{\eta(0.9)} \dfrac{10}{x^{2}} \, dx=0.9$. Integrating, $\dfrac{-10}{x}\bigg|_{10}^{\eta(0.9)}=0.9$. Therefore, $-\dfrac{10}{\eta(0.9)}+1=0.9$. Solving this, we get $\eta(0.9)=100$. Therefore, $100$ is the $90^{th}$ percentile.
<div style='border-top: 1px solid; width: 100%; margin-top:3px; margin-bottom: 0px;'></div>
