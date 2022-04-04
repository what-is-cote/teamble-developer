import os , sys

sys.stdin=open("noeyes/section_6/1.이진수출력.txt", "rt")

n = int(input())

def DFS(n):
  if n > 0:
    DFS(n // 2)
    print(n % 2,end='')

if __name__ == "__main__":
  DFS(n)
