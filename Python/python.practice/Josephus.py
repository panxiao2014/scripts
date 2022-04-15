"""Soldiers are standing in a circle waiting to be executed. Counting begins at a specified point in the circle and proceeds around the circle in a specified direction. After a specified number of people are skipped, the next person is executed. The procedure is repeated with the remaining people, starting with the next person, going in the same direction and skipping the same number of people, until only one person remains, and is freed."""

import datetime

numSoldier = int(input("Total number of soldier: "))
beginPos = int(input("Which soldier begin to count:"))
countNumber = int(input("Counting number:"))

beginTime = datetime.datetime.now()

class Soldier:
  count = 0

  def __init__(self, index):
    self.index = index
    Soldier.count +=1
    self.next = None

  def setNext(self, soldier):
    self.next = soldier

#initialize the circle of soldiers:
firstSoldier = Soldier(1)

index = 1
currentSoldier = firstSoldier
while (index < numSoldier):
  index += 1
  nextSoldier = Soldier(index)

  currentSoldier.setNext(nextSoldier)
  currentSoldier = nextSoldier

#make it a circle:
currentSoldier.setNext(firstSoldier)

#now move to the begin soldier:
beginSoldier = firstSoldier
step = 1
while (step < beginPos):
  beginSoldier = beginSoldier.next
  step += 1

currentSoldier = beginSoldier

#time to kill:
count = 1
while (Soldier.count != 1):
  if ((count + 1) == countNumber):
    #next soldier is the one to be killed:
    killSoldier = currentSoldier.next
    currentSoldier.setNext(killSoldier.next)
    
    del killSoldier
    Soldier.count -= 1
    count =1

  else:
    count +=1

  currentSoldier = currentSoldier.next

print ("Survivor is %d \n" % currentSoldier.index)

endTime = datetime.datetime.now()
diff = endTime - beginTime
print ("Time cost: ")
print (diff)

