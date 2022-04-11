import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def DFS(L):
    global cnt
    if L == M:
        for i in range(M):
            print(res[i], end = ' ')
        cnt += 1
        print()
    else:
        for i in range(1, N+1):
            if check[i] == 0:
                res[L] = i
                check[i] = 1
                DFS(L+1) 
                check[i] = 0

if __name__ == "__main__":
    N, M = map(int, input().split())
    num = list(range(1, N))
    res = [0] * M
    check = [0] * (N+1)
    cnt = 0
    DFS(0)
    print(cnt)
