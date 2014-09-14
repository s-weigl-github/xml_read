####################
###  lottozahlen generator
###  S.Weigl - 31.08.2014
###  ver. 01
####################

from xml.etree.ElementTree import parse
import random
import sys

rerun = 0

def lotto():
  wert = 0
  count = 6
  while wert < count:
    wert = wert + 1
    wahl = random.randint(1,49)
    print(" ", wahl)
  print("\n-------------------\n")
  print("Done!\n")

while rerun != 1:
  rerun = rerun + 1
  print("-------------------\n")
  lotto()

## E-o-F
