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

doc = parse('daten.swxml')
for person in doc.findall('person'):
  bday = person.findtext('bday')
  pid = person.findtext('id')
  name = person.findtext('name')
  surname = person.findtext('surname')
  gender = person.findtext('gender')
  if gender.startswith('f') or gender.startswith('m'):
    print(surname+', '+name,'| ID', pid,'\n', bday+' - '+gender)
