---
color: var(--mk-color-blue)
tags:
  - sem1-flashcards/stats/descriptive
---
Quick access:
[[Ways to display data#Stem and leaf display|Stem and leaf display]]
[[Ways to display data#Histogram|Histogram]]
	[[Ways to display data#Skewness|Skewness]]
[[Ways to display data#Box plot|Box plot]]
	[[Ways to display data#Graphing curves from boxplots|Graphing curves from boxplots]]
	[[Ways to display data#Outliers|Outliers]]

## Stem and leaf display
This display method allows you *to view the data distribution while also showing you each value.* The numbers are split into 2 parts: a **stem (10's place) and a lead (one's place).** For example, $63$ would be written as $6\:|\:3$, where $|$ divides the stem and leaf. The number of digits you include in the stem depends on the distribution.
![[images-1.png|center]]
This display is useful as **it sort of acts like a bar graph.** We get a rough idea of the distribution of values by taking a quick glance at this chart.

## Histogram
A histogram is essentially a bar graph for continuous data. It looks like this:
![[Histogram1-92513160f945482e95c1afc81cb5901e.png]]
When given tabular data, we add a column called *relative frequency.* This is $\dfrac{f}{\Sigma f}$, and this is the value we will plot in the graph. $\Sigma\:rf$ is always 1. There's another column we can make called *relative density,* which is $\dfrac{rel\:freq.}{class\:size}$. **If we are plotting data with unequal class sizes, we should always plot using relative density.** This is because it gives us a more accurate picture of the data when unequal class sizes are involved.

### Skewness
The shape of the histogram/curve reveals how skewed our data set is. Below are the three types of skewness. The first one is called **positively skewed because its tail goes in the positive x direction,** and same for negatively skewed.
![[1_nj-Ch3AUFmkd0JUSOW_bTQ.jpg|center]]

Mean isn't really useful in a skewed distribution as **it isn't a good representation of a typical value.** This is because a typical value should be what we normally see, and shouldn't be influenced by extreme values. *Mean however, gets dragged to the side of the extreme.* Since it is sensitive to extreme values, it isn't that useful.

On the other hand, *median is completely insensitive to skewness.* This is because median is a positional value. Therefore, if the central observations remain the same, the median stays the same. **This can be a disadvantage** since the median will not reflect $any$ change outside the center.

## Box plot
Box plots tell us the smallest, Q1, median, Q3 and largest observation in a dataset. The ends of the box show us Q1 and Q3, while the line in the box represents the median. The ends of the two whiskers show us the min and max values in the dataset. *The box gives us the middle 50 percent, while the whiskers give us the lower and upper quartiles.*
![[boxplot_13801952704243683193.jpg|center]]

### Graphing curves from boxplots
The two whiskers and the two parts of the box divides the distribution into 4 equal quartiles. **Therefore, the size of each element tells us over what area is this equal amount spread.** This means that *if one element covers a large area, that means its relative density is lower, so we draw the graph lower.* 

Looking at graph 2, we see that $a$ and $c$ are very small, while $b$ and $d$ are very long. Since all of them represent 25% of the data, $a$ and $c$ *being short means all the data is concentrated in a small peak.* $b$ and $d$ are longer, which means the same amount of data is spread over a longer distance. **Remember, we pay attention to the area under the curve.** Therefore, we give $b$ and $d$ short height but long width so that their area matches with the rest.
![[Untitled004.jpg]]

### Outliers
The main metric used to calculate outliers in box plots is called $fourth\:spread$. It is the difference between the upper fourth (Q3) and lower fourth (Q1). In simple terms, **the fourth spread is the width of the box.** We say that an observation is an outlier if it is more than $1.5fs$ away from the box. To put it in math terms, an observation is an outlier if:
$$
\begin{aligned}
x_i &< Q_1 - 1.5 \, fs \\

x_i &> Q_3 + 1.5 \, fs
\end{aligned}
$$
If any one of these hold true, the datapoint is said to be a *mild outlier.* Extreme outliers use the same formula, *but are 3 fs away from the upper/lower fourth.* We typically represent mild outliers as empty circles and extreme outliers as black circles.
