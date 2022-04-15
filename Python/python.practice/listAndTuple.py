#demonstrate tuple cost less time than list to create, since python use cache to store tuple, the memory won't be garbege collected when a tuple is deleted

import datetime


repeat = 100000

begin = datetime.datetime.now()

for i in range(0, repeat):
  li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

end = datetime.datetime.now()

listTime = end - begin

begin = datetime.datetime.now()

for i in range(0, repeat):
  li = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

end = datetime.datetime.now()

tupleTime = end - begin

print('List time:')
print(listTime)

print('Tuple time:')
print(tupleTime)
