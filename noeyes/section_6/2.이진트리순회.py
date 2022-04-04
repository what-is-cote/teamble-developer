import os , sys

# sys.stdin=open("noeyes/section_6/2.이진트리순회.txt", "rt")

def DFS(n):
  if n > 7:
    return;
  else:
    # 해당 작업의 위치에 따라 전위, 중위, 후위
    print(n, end= " ")
    DFS(n * 2)
    DFS(n * 2 + 1)

if __name__ == "__main__":
  DFS(1)

