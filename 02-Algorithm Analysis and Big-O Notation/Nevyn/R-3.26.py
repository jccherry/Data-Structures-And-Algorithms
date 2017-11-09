#answer for exercise R-3.26

def example4(S):
  n = len(S)
  prefix = 0
  totalOps = 0
  for j in range(n):
      prefix += 1
      totalOps += prefix
  return str(n) + " ---> " + str(totalOps)

def listItems(n):
    someList = []
    for i in range(n):
        someList.append(1)
    return someList

points = []

for i in range(1,500):
    print(str(example4(listItems(i))))
