#####################################
###  compute and write to file
###  Sebastian Weigl
###  ver. 1.2 - 22.02.2014
###  ver. 1.3 - 09.07.2016 little corrections, found computation error
#####################################
import os
import math

Anzahl = 1      # how many boxes 
Einheiten = 6   # pieces in 1 box
Einzel = 5.70   # price per piece
MWST = 0.19     # VAT 19% in Germany
Gesamt = 0      # all together
t = 0           # counter for the loop
numb = 25       # numb def how often the loop will be execute

# open a file and close it right a way and leave it empty
open('berechnung.txt','w').close()

def ptf():
  text = open('berechnung.txt','a')
  text.write(ausgabe)
  text.close()
def pfl():
  text = open('berechnung.txt','a')
  text.write(firstline)
  text.close()

temp2 = "%5s"
templ = "%10s %10s stk %15s € %8s %% %15s €"

print(templ % ("Anzahl", "Einheiten", "Einzel Preis", "MWST", "Gesamt Preis"))
firstline = str(templ % ("Anzahl", "Einheiten", "Einzel Preis", "MWST", "Gesamt Preis")+'\n'+'\n')
pfl()

while t < numb:
  t = t + 1
  Anzahl = Anzahl+Einheiten
  Aufs = Anzahl*Einzel
  Gesamt = Aufs+Aufs*MWST
  Gesamt = round(Gesamt, 2)
  Gesamt = '{:,}'.format(Gesamt)
  print(templ % (Anzahl, Einheiten, Einzel, MWST, Gesamt))
  ausgabe = str(templ % (Anzahl, Einheiten, Einzel, MWST, Gesamt)+'\n')
  ptf()

print("-------------------", temp2 % ("Done!"), "-------------------")

## E-o-F
