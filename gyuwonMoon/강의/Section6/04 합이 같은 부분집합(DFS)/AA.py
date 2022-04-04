import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# def DFS(i):
#   if i==len(num): # 마지막 노드까지 오면
#     tmp=[] # 포함 상태인 숫자를 요소로 가지는 리스트
#     for i in range(len(ch)):
#       if ch[i]==1:
#         tmp.append(i)
#     res.append(tmp)

#   else:
#     ch[num[i]]=1 # 해당 요소를 포함
#     DFS(i+1)
#     ch[num[i]]=0 # 해당 요소 포함X
#     DFS(i+1)


# if __name__=="__main__":
#   n=int(input())
#   num=list(map(int, input().split()))
  
#   ch=[0]*(max(num)+1)
#   res=[] # 모든 부분집합 저장
#   DFS(0)
  
#   for i in range(len(res)//2+1): # res는 무조건 짝수 길이임(2**n)
#     if sum(res[i])==sum(res[-1-i]): # 서로소 집합의 합이 같으면
#       print("YES")
#       break
#   else:
#     print("NO")


# ----------강의 풀이----------#
def DFS(L, sum):
  if sum>total//2: # 이미 절반보다 커진 경우 다음 합 구할 필요X
    return
  if L==n:
    if sum==(total-sum): # 하나의 부분집합의 합을 구하면, 자연스럽게 나머지 부분집합의 합도 알수있음
      print("YES")
      sys.exit(0) # 프로그램 자체를 종료
  else:
    DFS(L+1, sum+a[L]) # L번째 요소를 포함하는 경우
    DFS(L+1, sum) # 포함하지 않는 경우


if __name__=="__main__":
  n=int(input())
  a=list(map(int, input().split()))
  total=sum(a)
  DFS(0, 0)
  print("NO") # 프로그램이 정상적으로 종료된 경우