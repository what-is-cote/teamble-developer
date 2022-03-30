from collections import deque
import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N, M = map(int, input().split())
patient = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
dq = deque(patient)
check = cnt = 0

while 1:
    tmp = dq.popleft()
    for i in range(len(dq)):
        if tmp[1] < dq[i][1]:
            check = 1
            break
    if check == 1:
        dq.append(tmp)
    else:
        cnt += 1
        if tmp[0] == M:
            print(cnt)
            break
    check = 0
        