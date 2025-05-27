---
color: "#2d98da"
tags:
  - py-libraries
sticker: lucide//globe-2
---
## pytz library
`pytz` - Allows you to set timezones in Python. The problem with the [[datetime]] library is that *if you run `datetime` on a remote server, it takes the time of wherever the server is hosted.* 

The library might not come installed by default. In that case, run `pip install pytz` and install the library.

Quick access:
[[pytz#View all timezones|View all timezones]]
[[pytz#Set a timezone|Set a timezone]]
[[pytz#Get the current time in the selected timezone|Get the current time in the selected timezone]]

### View all timezones
`print(pytz.all_timezones)` - Lists all the timezone codes. The code for Dubai is `Asia/Dubai`.

### Set a timezone
`timezone = pytz.timezone('Asia/Dubai')` - Sets the timezone to be Dubai's time.

### Get the current time in the selected timezone
`current_time = datetime.now(timezone).time()` - Gives us the current time at a certain timezone by passing the `timezone` variable set above as an argument in `now()`.