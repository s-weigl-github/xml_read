####################
###  lottozahlen generator
###  S.Weigl - 08.06.2014
###  ver. 01 - beta
####################

from xml.etree.ElementTree import parse
import random

rerun = 0

def lotto():
  wert = 0
  count = 6
  while wert < count:
    wert = wert + 1
##    print(" ", random.choice([6,11,22,26,31,32,33,38,43,49]))
    print(" ", random.choice([3,6,9,11,17,22,25,26,27,31,32,33,36,38,42,43,49]))
  print("\n-------------------\n")
  print("Done!")

doc = parse('lottozahlen.xml')
for zahlen in doc.findall('zahlen'):
  kugelwert = zahlen.findtext('numb')
  kugelwert = int(kugelwert)
  gezogen = zahlen.findtext('picked')
  gezogen = int(gezogen)

  while rerun != 1:
    rerun = rerun + 1
    print("-------------------\n")
    lotto()

## E-o-F    
##
##  if gezogen > 471:
##    print(gezogen, kugelwert)
##    print("die am meist gezogenen lottozahlen")
