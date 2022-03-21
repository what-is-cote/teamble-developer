import os , sys

os.system('clear')
sys.stdin=open("noeyes/section_4/1.이분검색.txt", "rt")

n , m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

lt = 0
rt = n-1

while lt <= rt:

  midIdx = (lt + rt) //2

  if(arr[midIdx] == m):
    print(arr[midIdx])
    break
    
  elif(m< arr[midIdx] ):
    rt = midIdx -1
  else: 
    lt = midIdx + 1



