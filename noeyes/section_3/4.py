import os
import sys
os.system('clear')
sys.stdin=open("noeyes/section_3/4.txt", "rt")

n = int(input())
l1 = list(map(int,input().split()))

m = int(input())
l2 = list(map(int,input().split()))
result = []


while(True):

  i = 0
  if(len(l1) <= 0):
    
    result = result + l2
    break

  elif(len(l2) <= 0):
    result = result + l1
    break 

  else:
    if(l1[i] < l2[i]):
      result.append(l1.pop(i))
      
    elif(l2[i] < l1[i]):
      result.append(l2.pop(i))
      
      
    else:
      l1.pop(i)
      result.append(l2.pop(i))
      
    

print(result)

# 각 리스트에서 뽑아낸 숫자를 카운트한 후
# 카운트 수가 리스트의 총 길이보다 길어지면 반복문 종료한다.
# 이후 list[카운트:] 추가