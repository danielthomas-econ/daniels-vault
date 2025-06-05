---
color: var(--mk-color-yellow)
tags:
  - "#sem2-flashcards/stats/hypothesis_testing"
---
Quick access:
- [[#Statistical hypothesis|Statistical hypothesis]]
- [[#Procedure for hypothesis testing|Procedure for hypothesis testing]]

## Statistical hypothesis
A statistical hypothesis is a claim or an assertion about a certain statistical value, like the value of a parameter, shape of a distribution etc. When we conduct hypothesis testing, *we have two contradictory hypotheses under consideration.* Our goal is to use our sample data to decide which of the two are correct.

Just like how the judicial system follows 'innocent until proven guilty', **we will start by initially assuming a certain hypothesis** and only reject this if our sample data provides very strong evidence for the other hypothesis. The **null hypothesis** ($H_{0}$) is the claim we assume to be initially true while the **alternative hypothesis** ($H_{a}$) is the hypothesis that contradicts $H_{0}$. $H_{a}$ is often called the *'researcher's hypothesis'* since its the claim the researcher would like to validate. The null hypothesis is named that because null means no value or effect, so this hypothesis represents the hypothesis of no change (the status quo is true).

*Since we have two hypothesis, our outcomes are either reject $H_{0}$ or fail to reject $H_{0}$*. Note that **we never say accept $H_{0}$** as the outcome "fail to reject $H_{0}$" simply means our current sample does not have enough evidence to reject the null. Had we taken another sample, we may have rejected the null. Therefore, we don't accept null as true, we simply say we cannot reject it.

## Procedure for hypothesis testing
To conduct a hypothesis test, we must follow these steps:
1) Obtain a sample
2) Select a **test statistic**
3) Create a **decision rule** to reject $H_{0}$ (ex: reject $H_{0}$ if $\bar{X} >5$)
4) Compute the value of the test statistic using our sample
5) Use the decision rule and test statistic value to decide which hypothesis to accept

This procedure has two main components:
1) A test statistic which is a function of the sample data. The decision rule will be based on this test statistic.
2) A *rejection region* which is defined by the decision rule. If our decision rule was reject $H_{0}$ if $\bar{X}>5$, then all values of $\mu$ greater than $5$ becomes our rejection region. The null hypothesis is rejected iff the computed value of the test statistic falls in the rejection region.

This basic approach works well, but it has one major issue: *our decision rule and rejection region are arbitrarily decided.* Later on, we'll look at how to define these two more rigorously.

Based on what kind of decision rule we use, we have three kinds of tests:
1) If $H_{a}$ is $\mu > x$, this is a **right tailed test.**
2) If $H_{a}$ is $\mu < x$, this is a **left tailed test.**
3) If $H_{a}$ is $\mu \ne x$, this is a **two tailed test.**
The reasoning behind the names is due to the location of the rejection region in each of these cases.
![[WhatsApp Image 2025-05-26 at 14.46.06_03203336.jpg]]
