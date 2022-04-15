import sys

num = int(sys.argv[1])
total = 0

for i in range(1, num+1):
  strI = str(i)
  strLen = len(strI)
  for j in range(0, strLen):
    if(strI[j] == '1'):
      total += 1

print("Total number of 2: %d" % (total))
