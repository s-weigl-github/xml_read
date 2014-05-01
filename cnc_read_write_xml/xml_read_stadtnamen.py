#########################
###  read and compute datasets from a xml file
###  Sebastian Weigl
###  ver.03 - 16.02.2014
#########################
import urllib.request
from xml.etree.ElementTree import parse

wert = 100000000

doc = parse('stadtnamen.xml')
for stadt in doc.findall('stadt'):
  sn = stadt.findtext('name')
  pid = stadt.findtext('id')
  hs = stadt.findtext('hauptstadt')
  ew = stadt.findtext('einwohner')
  ew = int(ew)

  if ew < wert:
    print(sn, ew, pid, hs)
  else:
    print("fehler")

## print(sn, pid, hs, ew)

## E-o-F
