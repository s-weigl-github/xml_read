import os

Anzahl = 0
Einzel = 30
MWST = 0.19
Gesamt = 0
t = 0

temp2 = "%5s"
templ = "%10s %15s %8s %% %15s €"
print(templ % ("Anzahl", "Einzel Preis", "MWST", "Gesamt Preis"))
while t < 56:
  t = t + 1
  Anzahl = Anzahl+10
  Aufs = Anzahl*Einzel
  Gesamt = Aufs+Aufs*MWST
  print(templ % (Anzahl, Einzel, MWST, Gesamt))
  ausgabe = (templ % (Anzahl, Einzel, MWST, Gesamt))

  text = open('berechnung.txt', 'w')
  text.write(ausgabe)
  text.close()
  
print("-------------------", temp2 % ("Done!"), "-------------------")

## E-o-F
