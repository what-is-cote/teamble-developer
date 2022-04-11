import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def DFS(L, total):
    global minimum
    if L > minimum:
        return
    if total > M:
        return
    elif total == M:
        if minimum > L:
            minimum = L
    else:
        for i in range(N):
            DFS(L+1, total + money[i])

        
    
if __name__ == "__main__":
    N = int(input())
    money = list(map(int, input().split()))
    money.sort(reverse=True)
    M = int(input())
    total = 0
    minimum = 2147000000
    DFS(0, 0)
    print(minimum)