import calendar
from datetime import datetime

import bot_functions

current_date = datetime.now()

total_days = 365
if calendar.isleap(current_date.year):
    total_days = 366

text = f'Happy day {current_date.timetuple().tm_yday} of {total_days}!'

bot_functions.make_tweet(text)
