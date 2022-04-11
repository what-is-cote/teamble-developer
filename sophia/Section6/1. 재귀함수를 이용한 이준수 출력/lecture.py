import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end = '')

if __name__ == "__main__":
    n = int(input())
    DFS(n)