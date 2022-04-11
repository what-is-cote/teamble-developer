import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def DFS(L, sum):
    global res
    if res < L:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])
        
    
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)