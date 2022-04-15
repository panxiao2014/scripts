import sys

capital = int(sys.argv[1])            #money invest in each year
interest = int(sys.argv[2]) / 100
year = int(sys.argv[3])


totalReturn = 0

for i in range(year, 0, -1):
  retMoney = capital * ((1+interest) ** i)
  print("year " + str(i)  + ": " + str(retMoney))

  totalReturn += retMoney

print("Total return is: " + str(totalReturn))

