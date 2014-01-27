import datetime, time

utc_dt = datetime.datetime.now()
s = utc_dt.strftime('%d.%m.')
atc_dt = datetime.datetime(2014, 1, 26)
e = atc_dt.strftime('%d.%m.')

if s == e:
  print("both data sets are equal")
else:
  print("data set is not equal")
