import time
import concurrent.futures

def gcd(pair):
  a, b = pair
  low = min(a, b)
  for i in range(low, 0, -1):
    if(a%i == 0 and b%i == 0):
      return i

numbers = [(19633094, 22659732), (20306779, 38141733), (3535354, 453545353), (398375342, 349530498)]

def low_performance():
  start = time.time()
  result = list(map(gcd, numbers))
  end = time.time()
  print('[%s]' % ',' . join(map(str, result)))
  print('low performance Took %.3f seconds' % (end - start))

def high_performance():
  start = time.time()
  pool = concurrent.futures.ProcessPoolExecutor(max_workers = 4)
  result = list(pool.map(gcd, numbers))
  end = time.time()
  print('[%s]' % ',' . join(map(str, result)))
  print('high performanceTook %.3f seconds' % (end - start))
 
low_performance()
high_performance()
