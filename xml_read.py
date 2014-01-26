#########################
###  read and compute datasets from a xml file
###  Sebastian Weigl
###  ver.01 - 26.01.2014
#########################
import urllib.request
from xml.etree.ElementTree import parse
import time, datetime
import webbrowser

utc_datetime = datetime.datetime.now()
s = utc_datetime.strftime("%d%m%Y")

ag = int(25)

#bday =

doc = parse('data.xml')
for person in doc.findall('person'):
    age = int(person.findtext('age'))
    if age >= ag:
      bday = person.findtext('bday')
      name = person.findtext('name')
      surname = person.findtext('surname')
      pid = person.findtext('id')
      gender = person.findtext('gender')
      if gender.startswith('male'):
        print(name, surname, pid,'\n', bday, age, gender)
