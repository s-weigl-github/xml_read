import os

Anzahl = 0
Einzel = 30
MWST = 0.19
Gesamt = 0
t = 0

def ptf():
  text = open('berechnung.txt', 'a')
  text.write(ausgabe)
  text.close()
def pfl():
  text = open('berechnung.txt', 'a')
  text.write(firstline)
  text.close()

temp2 = "%5s"
templ = "%10s %15s %8s %% %15s €"

print(templ % ("Anzahl", "Einzel Preis", "MWST", "Gesamt Preis"))
firstline = str(templ % ("Anzahl", "Einzel Preis", "MWST", "Gesamt Preis")+'\n'+'\n')
pfl()

while t < 56:
  t = t + 1
  Anzahl = Anzahl+10
  Aufs = Anzahl*Einzel
  Gesamt = Aufs+Aufs*MWST
  print(templ % (Anzahl, Einzel, MWST, Gesamt))
  ausgabe = str(templ % (Anzahl, Einzel, MWST, Gesamt)+'\n')
  ptf()

print("-------------------", temp2 % ("Done!"), "-------------------")

## E-o-F
