from collections import deque
import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N, K  = map(int, input().split())
dq = list(range(1, N+1))
dq = deque(dq)
    
while dq:
    for _ in range(K-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
