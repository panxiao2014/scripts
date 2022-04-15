#You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
#The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
#The lock initially starts at '0000', a string representing the state of the 4 wheels.
#You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
#Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

#Tip:
#We can think of this problem as a shortest path problem on a graph: there are `10000` nodes (strings `'0000'` to `'9999'`), and there is an edge between two nodes if they differ in one digit, 
#that digit differs by 1 (wrapping around, so `'0'` and `'9'` differ by 1), and if *both* nodes are not in `deadends`.

class Node:
  def __init__(self, nextN=None, prevN=None, data=None, isRoot=False):
    self.nextN=nextN
    self.prevN=prevN
    self.data=data
    self.isRoot=isRoot

  #print the steps to open the lock:
  def printRoute(self):
    routeList = []
    node = self
    while(node.isRoot == False):
      routeList.append(node)
      node = node.prevN

    routeList.append(node)
    routeList = routeList[::-1]
    routeStr = ""
    for i in routeList:
      if i.isRoot == True:
        routeStr = routeStr + i.data
      else:
        routeStr = routeStr + "-->" + i.data
    print(routeStr)


class Solution:
    def openLock(self, deadends, target):
        import queue

        #for each state of a slot, it could rotate in two direction:
        rotateDict={'0':['1', '9'], '1':['2', '0'], '2':['3', '1'], '3':['4', '2'], '4':['5', '3'],
                    '5':['6', '4'], '6':['7', '5'], '7':['8', '6'], '8':['9', '7'], '9':['0', '8']}

        #for a lock in any state, it could have 8 possible ways to rotate lock: each wheel can rotate in two directions
        #this function is add the next 8 possible state to the queue
        def addNeighbors(node, q, visited):
          lockState = node.data

          nextLockState="".join([rotateDict[lockState[0]][0], lockState[1], lockState[2], lockState[3]])
          if(nextLockState not in visited):
            newNode = Node(None, node, nextLockState, False)
            node.nextN = newNode
            q.put(newNode)
            visited.add(nextLockState)
            
          nextLockState="".join([rotateDict[lockState[0]][1], lockState[1], lockState[2], lockState[3]])
          if(nextLockState not in visited):
            newNode = Node(None, node, nextLockState, False)
            node.nextN = newNode
            q.put(newNode)
            visited.add(nextLockState)
            
          nextLockState="".join([lockState[0], rotateDict[lockState[1]][0], lockState[2], lockState[3]])
          if(nextLockState not in visited):
            newNode = Node(None, node, nextLockState, False)
            node.nextN = newNode
            q.put(newNode)
            visited.add(nextLockState)
            
          nextLockState="".join([lockState[0], rotateDict[lockState[1]][1], lockState[2], lockState[3]])
          if(nextLockState not in visited):
            newNode = Node(None, node, nextLockState, False)
            node.nextN = newNode
            q.put(newNode)
            visited.add(nextLockState)
            
          nextLockState="".join([lockState[0], lockState[1], rotateDict[lockState[2]][0], lockState[3]])
          if(nextLockState not in visited):
            newNode = Node(None, node, nextLockState, False)
            node.nextN = newNode
            q.put(newNode)
            visited.add(nextLockState)
            
          nextLockState="".join([lockState[0], lockState[1], rotateDict[lockState[2]][1], lockState[3]])
          if(nextLockState not in visited):
            newNode = Node(None, node, nextLockState, False)
            node.nextN = newNode
            q.put(newNode)            
            visited.add(nextLockState)
            
          nextLockState="".join([lockState[0], lockState[1], lockState[2], rotateDict[lockState[3]][0]])
          if(nextLockState not in visited):
            newNode = Node(None, node, nextLockState, False)
            node.nextN = newNode
            q.put(newNode)            
            visited.add(nextLockState)
            
          nextLockState="".join([lockState[0], lockState[1], lockState[2], rotateDict[lockState[3]][1]])
          if(nextLockState not in visited):
            newNode = Node(None, node, nextLockState, False)
            node.nextN = newNode
            q.put(newNode)
            visited.add(nextLockState)
  
        
        steps = 0
        initState = '0000'
        if (target == initState):
          return 0
        
        if(initState in deadends):
          return -1

        root=Node(None, None, initState, True)
        visited = set(deadends)
        q = queue.Queue()
        
        addNeighbors(root, q, visited)
        while(q.empty() == False):
          steps += 1
          for i in range(0, q.qsize()):
            node = q.get()
            lockState = node.data
            if(lockState == target):
              node.printRoute()
              return steps
            
            addNeighbors(node, q, visited)
          
        return -1

deadends=["0201","0101","0102","1212","2002"]
target='0202'

deadends2=["8888"]
target2="0009"

deadends3=["8887","8889","8878","8898","8788","8988","7888","9888"]
target3="8888"

solution = Solution()
steps=solution.openLock(deadends, target)

print("Total steps: %d" % steps)
