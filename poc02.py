import datetime, time
from xml.etree.ElementTree import parse

utc_dt = datetime.datetime.now()
s = utc_dt.strftime('%d.%m.')
atc_dt = datetime.datetime(2014, 1, 26)
e = atc_dt.strftime('%d.%m.')

doc = parse('daten.swxml')
for person in doc.findall('person'):
  bday = person.findtext('bday')
  bday = int(bday)
  bday_dt = datetime.datetime(bday)
  bday = bday_dt.strftime('%d.%m.')
  print(bday)

##if s == e:
##  print("both data sets are equal")
##else:
##  print("data set is not equal")
