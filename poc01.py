import datetime, time

aday = time.strftime('%d.%m.%Y')
bday = datetime.date.today()
cday = time.strftime('%H:%M:%S')
dday = time.time()
eday = datetime.datetime.today()
fday = datetime.datetime(2013, 9, 22) > datetime.datetime(2012, 9, 22)
gday = datetime.datetime(2013, 9, 22) - datetime.datetime(2012, 9, 22)
hday = datetime.datetime(2013, 9, 22) - datetime.timedelta(10)

print(aday, ";-; heute euro stil")
print(bday, ";-; heute us stil")
print(cday, ";-; uhrzeit aktuell")
print(dday, ";-; internetzeit")
print(eday, ";-; komplet format")
print(fday, ";-; datum vergleich True & False als ausgabe")
print(gday, ";-; difference zweier daten")
print(hday, ";-; datum rechnen mit festwert")
#wert = 27.09.1959
#aday = float(aday)
hneu = datetime.datetime(1959, 9, 27)
neu = eday - hneu
neu1 = neu / 365
print(neu, neu1)
