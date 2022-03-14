import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
n=int(input())

for i in range(n):
  str=input().upper()
  left=0
  right=len(str)-1
  
  while True:
    if right-left<=1 and str[left]==str[right]:
      print(f"#{i+1} YES")
      break
    elif str[left]==str[right]:
      left+=1
      right-=1
      continue
    else:
      print(f"#{i+1} NO")
      break
    
  
# ----------강의 풀이----------#
n=int(input())

for i in range(n):
  str=input().upper()
  # 1번
  # size=len(str)
  
  # for j in range(size//2):
  #   if str[j]!=s[-1-j]:
  #     print("#%d NO" %(i+1))
  #     break
  # else:
  #   print("#%d YES" %(i+1))
  
  # 2번
  if str==str[::-1]: #스트링과 리버스 스트링이 같은지 비교
    print("#%d YES" %(i+1))
  else:
    print("#%d NO" %(i+1))