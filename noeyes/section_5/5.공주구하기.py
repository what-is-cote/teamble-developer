import os , sys
from collections import deque
# sys.stdin=open("noeyes/section_5/5.공주구하기.txt", "rt")

n, k=map(int, input().split())
q=list(range(1, n+1))
dq=deque(q)
while len(dq) > 1:
    for _ in range(k-1):
        temp=dq.popleft()
        dq.append(temp)
    dq.popleft()
    
print(dq[0])

# 100점