import sys

maxCount = int(sys.argv[1])

count = 0

currentNum = 1

while (count < maxCount):
  strNum = str(currentNum)
  strLen = len(strNum)
  for j in range(0, strLen):
    if(strNum[j] == '8'):
      count += 1

  currentNum += 1


print("page number is %d" % (currentNum-1))
