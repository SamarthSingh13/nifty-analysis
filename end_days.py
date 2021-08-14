from datetime import date, timedelta
from pandas import *

data = read_csv('3131.csv')
csv_dates = data['datetime'].tolist()

d = date(2006,1,2)
d += timedelta(days = 3)
while d.year < 2020:
	if str(d) in csv_dates:
		print(d)
	elif str(d-timedelta(days=1)) in csv_dates:
		print(d)
	else:
		print(d)
	d += timedelta(days = 7)



