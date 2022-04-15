import sys
import itertools

ret = int(sys.argv[1])

numList = [i for i in range(9, 0, -1)]

operList = [['+', '-', '*', '*(', ')*'] for i in range(0, 8)]

combList = list(itertools.product(*operList))

answers = 0
for comb in combList:
  s=""
  for i in range(0, 8):
    s += str(numList[i]) + ' ' + comb[i] + ' '

  s += str(numList[8]) 

  try:
    cal = eval(s)
  except:
    pass 
  else:
    if (cal == ret):
      if('(' in s and ')' in s):
        end = s.index(')')
        begin = s.index('(')
        if((end - begin) <= 4):
          continue 
        else:
          sub = s[s.index('(')+1 : s.index(')')]
          if(not('+' in sub or '-' in sub)):
            continue

      s += ' = ' + str(ret)
      print(s)

      answers += 1

print("\nWe have " + str(answers) + " answers!")
