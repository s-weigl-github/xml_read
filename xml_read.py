#########################
###  read and compute datasets from a xml file
###  Sebastian Weigl
###  ver.06 beta - 31.01.2014
#########################
import urllib.request
from xml.etree.ElementTree import parse
import time, datetime
import webbrowser

dt = datetime.datetime.now()
s = dt.strftime("%d")
t = dt.strftime("%m")
u = dt.strftime("%Y")
u = int(u)

wert = 0
age = None
ye_ar = None

doc = parse('daten.swxml')
for person in doc.findall('person'):
  da_y = person.findtext('da_y')
  da_y = int(da_y)
  mon_th = person.findtext('mon_th')
  mon_th = int(mon_th)
  ye_ar = person.findtext('ye_ar')
  ye_ar = int(ye_ar)
  pid = person.findtext('id')
  name = person.findtext('name')
  surname = person.findtext('surname')
  gender = person.findtext('gender')
##  if gender.startswith('f') or gender.startswith('m'):
##    print(surname+', '+name,'| ID', pid,'\n', da_y+'.'+mon_th+'.'+ye_ar+' - '+gender)
  if da_y == s and mon_th == t:
    age = u - ye_ar
    if u - ye_ar == age:
      age = str(age)
      print("Geburtstag - ist Heute "+age+" geworden ", da_y+'.'+mon_th+'. -', name)
  elif da_y+1 == s and mon_th == t:
    age = u - ye_ar
    if u - ye_ar == age:
      age = str(age)
      print("Geburtstag verpasst")
  elif da_y-1 == s and mon_th == t:
    age = u - ye_ar
    if u - ye_ar == age:
      age = str(age)
      print(name+" hat morgen Geburtstag und wird"+age)
  else:
    wert = wert + 1
    print(wert, "dauert noch")
