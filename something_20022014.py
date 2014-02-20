Anzahl = 0
Einzel = 30
MWST = 0.19
Gesamt = 0
t = 0

##temp2 = "%50s"
templ = "%10s %15s %8s %% %15s €"
print(templ % ("Anzahl", "Einzel Preis", "MWST", "Gesamt Preis"))
while t < 55:
  t = t + 1
  Anzahl = Anzahl+10
  Aufs = Anzahl*Einzel
  Gesamt = Aufs+Aufs*MWST
  print(templ % (Anzahl, Einzel, MWST, Gesamt))
#print(temp2 % ("Done!"))
## E-o-F
