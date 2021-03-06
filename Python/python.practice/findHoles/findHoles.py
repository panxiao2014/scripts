#this script reads a text file which contains a column of user IDs, and find what users are missing, write missing users to a file

import numpy as np
import pandas as pd


#read users.txt as csv and store in DataFrame:
dfUsers = pd.read_csv('users.txt')

npUsers = dfUsers['user']

maxId = npUsers.max()

tempList = [0 for i in range(0, maxId+1)]

#mark item in tempList as 1 if corresponding user exist:
for user in npUsers:
  tempList[user] = 1

npRecord = np.array(tempList)

#find out missing users:
npMissing = np.where(npRecord == 0)

#write missing users to file:
with open('missing.txt', 'w') as f:
  for user in npMissing[0]:
    f.write(str(user) + '\n')

f.close()

