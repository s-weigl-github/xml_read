####################
###  lottozahlen generator
###  S.Weigl - 10.05.2014
###  ver. 02 - beta
####################

import random

rerun = 0

def lotto():
  wert = 0
  count = 6
  while wert < count:
    wert = wert + 1
    print("  ",random.choice([3,6,9,11,17,22,25,26,31,32,33,36,38,43,49]))
  print("-------------------")
  print("Done!")

while rerun != 5:
  rerun = rerun + 1
  lotto()

## E-o-F