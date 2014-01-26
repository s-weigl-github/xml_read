import urllib.request
from xml.etree.ElementTree import parse
import time, datetime
import webbrowser

utc_datetime = datetime.datetime.now()
s = utc_datetime.strftime("%d%m%Y")

ag = int(40)

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
        print(bday, gender, age, name, surname, pid)
