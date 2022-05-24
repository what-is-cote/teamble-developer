import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

str=input().upper()
d=dict()
    
# s라는 key가 존재하면 s에 +1
# 아니면 반환된 0에 +1 및 key 생성
for s in str:
  d[s]=d.get(s, 0) + 1

max=-2147000000

for k, v in d.items(): # dictionary의 key, value로 순회
  if v>max:
    max=v
    max_key=k
  elif v==max:
    max_key='?'

print(max_key)
