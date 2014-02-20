Device = 20
Total = 30
Used = 40
Free = 50
Use = 60
Type = 70
Mount = 80
t = 0

temp2 = "%10s"
templ = "%10s %8s %8s %8s %5s %% %9s €  %5s"
print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type", "Mount"))
while t < 30:
  print(templ % (Device, Total, Used, Free, Use, Type, Mount))
  t = t + 1
  Device = Device+10
  Total = Total+10
  Used = Used+10
  Free = Free+10
  Use = Use+10
  Type = Type+10
  Mount = Mount+10
print(temp2 % ("Done!"))
## E-o-F
