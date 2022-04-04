# ----------내 풀이----------#
# #1 전위 순회
# def DFS(x):
#   if x>7:
#     return
#   else:
#     print(x, end=' ')
#     DFS(x*2)
#     DFS(x*2+1)

# #2 중위 순회
# def DFS(x):
#   if x>7:
#     return
#   else:
#     DFS(x*2)
#     print(x, end=' ')
#     DFS(x*2+1)
    
# #3 후위 순회
# def DFS(x):
#   if x>7:
#     return
#   else:
#     DFS(x*2)
#     DFS(x*2+1)
#     print(x, end=' ')
  
    
# if __name__=="__main__":
#   DFS(1)


# ----------강의 풀이----------#
# DFS-재귀 / BFS-queue
# 전위 순회: 부, 왼, 오
# 중위 순회: 왼, 부, 오
# 후위 순회: 왼, 오, 부

def DFS(v):
  if v>7:
    return
  else:
    print(v, end=' ') # 본연의 작업을 다음 호출 전에 함! => 전위 순회
    DFS(v*2)
    # print(v, end=' ') # 중위 순회
    DFS(v*2+1)
    # print(v, end=' ') # 후위 순회
  
    
if __name__=="__main__":
  DFS(1)