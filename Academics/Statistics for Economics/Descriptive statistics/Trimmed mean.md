---
color: var(--mk-color-blue)
tags:
  - sem1-flashcards/stats/descriptive
---
Quick access:
[[Trimmed mean#What is trimmed mean|What is trimmed mean]]
[[Trimmed mean#Calculating trimmed mean|Calculating trimmed mean]]
[[Trimmed mean#When the percentage isn't an integer|When the percentage isn't an integer]]

## What is trimmed mean
The biggest problem with mean and median is that they are very sensitive or completely insensitive to the skewness of a distribution. This is a problem since neither are perfectly suited for use in a skewed distribution.

Trimmed mean seeks to *fix the inadequacies of mean and median by eliminating the extreme values.* It is represented by $\bar{x}_{(10\%\:tm)}$ or $10\%\:tm$. To get a $\alpha \%$ trimmed mean, we remove $\alpha\%$ of the total observations from both sides. So if we have a dataset of $100$ observations, taking $10\%$ trimmed mean means *we remove 10 observations from both sides.* In a way, median is a $50\%$ trimmed mean.

The goal of trimming the distribution is to **eliminate extreme values from messing with our dataset.** Since we trim the edges, we remove the extremes and this makes our dataset a lot more symmetrical.

## Calculating trimmed mean
Finding $10\%$ and $20\%$ trimmed mean is very easy. Simply remove the extreme observations and you'll get it. To get $15\%$ trimmed mean, we can take the average of $10\%$ and $20\%$ trimmed mean.

Finding $18\%$ or other awkward values is a little harder. In this case, we have to *use values we know to interpolate the value of the trimmed mean.* To simplify this, we can use a diagrammatic representation. We know $18\%$ splits $10\%$ and $20\%\:tm$ in the ratio $8:2=4:1$. Therefore, our goal is to *get the length of this line and divide it in the ratio.*

To find the length, we subtract the values of the extremes. Here, it is $15.833-15.625=0.208$. Multiplying that by $\frac{4}{5}$ gives us the length of the first part, which is $0.1664$. Since we know $10\%\:tm$ is $15.625$ and that $18\%\:tm$ is $0.1664$ units away, **we add the distance to get the value of** $18\%\:tm$.
![[Untitledfeafeuioe.jpg]]

### When the percentage isn't an integer
In certain cases, the number of observations we drop may not be an integer. For example, if $n=11$ and we're asked to find $10\%\:tm$, then we have to drop $1.1$ observations. Obviously, this is not possible.

To solve this problem, *we drop 1 observation and find the trimmed mean, then drop 2 observations and find the trimmed mean.* Once again, we can draw a line and $1.1$ observations splits this line in the ratio of $1:9$. If 1 observation trimmed mean is $14.1$ and 2 observations trimmed mean is $14.4$, then the distance of the line is $0.3$. This means the first distance is $0.3\times\frac{1}{10}=0.03$. Therefore, $10\%\:tm$ here would be $14.1+0.03=14.13$.