import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

N = int(input())
l1 = list(map(int, input().split()))

M = int(input())
l2 = list(map(int, input().split()))

#------방법 1, 시간 복잡도: NlogN------
# l1 += l2
# l1.sort()

# for i in l1:
#     print(i, end = ' ')


#------방법 2, 시간 복잡도: N------
l = []
p1 = 0
p2 = 0

while p1 < N and p2 < M:
    if l1[p1] <= l2[p2]:
        l.append(l1[p1])
        p1 += 1
    else:
        l.append(l2[p2])
        p2 += 1

if p1 == N:
    for i in range(p2, M):
        l.append(l2[i])
else:
    for i in range(p1, N):
        l.append(l1[i])

for i in l:
    print(i, end = ' ')