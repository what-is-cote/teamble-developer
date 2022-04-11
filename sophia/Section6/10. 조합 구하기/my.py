import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def DFS(L, s):
    global cnt
    if L == M:
        for i in range(M):
            print(res[i], end = ' ')
        cnt += 1
        print()
    else:
        for i in range(s, N+1):
            res[L] = i
            s = i + 1
            DFS(L+1, i+1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    num = list(range(1, N))
    res = [0] * M
    cnt = 0
    DFS(0, 1)
    print(cnt)
