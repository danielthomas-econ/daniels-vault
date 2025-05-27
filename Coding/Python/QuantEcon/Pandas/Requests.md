---
color: var(--mk-color-yellow)
---


We will be using the [[Coding/Python/QuantEcon/Pandas/Requests|requests]] library to get our datasets.

## Basic request
~~~python
r = requests.get('url_to_the_dataset_')
~~~
We can improve this by creating a variable called `url` for the link to the dataset. Then, we can run the following code:
~~~python
source = requests.get(url).content.decode().split("\n")
~~~
`.content.decode()` retrieves the raw content (in bytes) from `requests.get(url)` and then decodes it into raw strings so that we can use it. `.split("\n")` splits up the big string into smaller parts using a new line.

We can also make this into a dataframe using
~~~python
data = pd.read_csv(url,index_col=0, parse_dates = True)
~~~
