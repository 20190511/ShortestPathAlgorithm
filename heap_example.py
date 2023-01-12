import heapq

def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h,value) #새리스트에, value값을 heap형태로 삽입.
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result


#최대힙
def maxHeapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h,-value)
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
result2 = maxHeapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
print(result2)
