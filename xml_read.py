#########################
###  read and compute datasets from a xml file
###  Sebastian Weigl
###  ver.02 - 27.01.2014
#########################
import urllib.request
from xml.etree.ElementTree import parse
import time, datetime
import webbrowser

dt = datetime.datetime.now()
s = dt.strftime("%d.%m.")

ag = int(25)

doc = parse('daten.swxml')
for person in doc.findall('person'):
  bday = person.findtext('bday')
  pid = person.findtext('id')
  name = person.findtext('name')
  surname = person.findtext('surname')
  gender = person.findtext('gender')
  if gender.startswith('f'):
    print(name, surname, pid,'\n', bday, gender)
