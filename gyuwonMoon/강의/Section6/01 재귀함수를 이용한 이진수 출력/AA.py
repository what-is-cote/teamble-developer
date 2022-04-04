import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------# 
def DFS(x):
  q=x//2 # 몫
  r=x%2 # 나머지
  if q>0:
    DFS(q)
  print(r, end='')
  
if __name__=="__main__":
  n=int(input())
  DFS(n)


# ----------강의 풀이----------#
def DFS(x):
  if x==0:
    return # 함수 종료
  else:
    DFS(x//2)
    print(x%2, end='')

if __name__=="__main__":
  n=int(input())
  DFS(n)