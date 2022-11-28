mainq=int(5)
bonusq=int(4)
maint=int(input("How many main questions did you get right? "))
bonust=int(input("How many bonus questions did you get right? "))
mainto=int(mainq*maint)
bonusto=int(bonusq*bonust)
total=int(mainto+bonusto)
if maint>20 or maint<0 or bonust>5 or bonust<0:
  print("not possible")
  exit()
if total>100:
  print("Total mark:",100)
  exit()
else:
  print("Total mark:",total)
