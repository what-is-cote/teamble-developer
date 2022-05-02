import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum + a[i])
             

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    sum = 0
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
