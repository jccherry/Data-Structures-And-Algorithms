#code used to analyse answer to R-3.25 that example3 is O(n^2)
#example3 function modified from book and everything else is original
def example3(S):
  n = len(S)
  #print("n = " + str(n))
  totalNumOperations = 0
  for j in range(n):
      for k in range(1+j):
          totalNumOperations+=1

  #print("numOperations = " + str(totalNumOperations))
  #returns a tuple so it can be used as an ordered pair
  return (n,totalNumOperations)

#create a list of n items with all 1s
def nItemList(n):
    aList = []
    for i in range(n):
        aList.append(1)
    return aList

points = []

#prints out a series of ordered pairs
for i in range(1,1000):
    #points.append(example3(nItemList(i)))
    print(str(example3(nItemList(i))))
