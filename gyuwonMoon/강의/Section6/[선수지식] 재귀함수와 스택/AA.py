def DFS(x):
  if x>0:
    # print(x, end=' ') # n, n-1, ..., 1
    DFS(x-1)
    print(x, end=' ') # 1, 2, ..., n
    
if __name__=="__main__": # 프로그램의 시작점일 때만 아래 코드를 실행
  n=int(input())
  DFS(n)