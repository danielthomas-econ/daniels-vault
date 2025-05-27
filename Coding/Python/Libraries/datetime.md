---
color: "#2d98da"
tags:
  - py-libraries
sticker: lucide//calendar-days
---
## datetime library
`datetime` allows you to do things related to time. You can also use `from datetime import datetime` instead of just importing the `datetime` library.

Quick access:
[[datetime#Set the date|Set the date]]
[[datetime#Time delta|Time delta]]
[[datetime#Set the current time|Set the current time]]
[[datetime#Format the time presentation|Format the time presentation]]

### Set the date
`datetime.date(year = , month = , day = )` - Sets a specific date. You can assign this value to a variable to use later. Eg: `myDate = datetime.date(year=2022, month=12, day= 7)`.

`datetime.date.today()` gives us **the current date** based on our computer clock.

We can also ask the user to input the `year`, `month` and `day` separately and then set `date = datetime.date(year, month, day)`.

*Dates can also be compared using math operators.* Example: The `>` operator will tell you if a given date is greater than another (i.e. in the future).

### Time delta
`datetime.timedelta(days = )` - Changes the date by the period specified. Example:
~~~python
today = datetime.date.today() # Today's date

difference = datetime.timedelta(days=14) # The difference I want

newDate = today + difference # Add today to the delta difference to see the date in 14 days time.
~~~

### Set the current time
`datetime.now().time()` - Outputs the current time. However, you need to use `from datetime import datetime` for this to work, because `now` is actually a method of the `datetime` class within the `datetime` module, not of the module itself.

### Format the time presentation
`.strftime('%H:%M:%S')` - Formats the time into `HH:MM:SS`, which *stops the value of seconds being displayed with decimals.* It is a much cleaner way to show the time. Just add it at the end of any `datetime` argument.
Example: `date = datetime.now(timezone).strftime('%H:%M:%S')`.

`strf` stands for `string format time` and will automatically convert the time into a string.