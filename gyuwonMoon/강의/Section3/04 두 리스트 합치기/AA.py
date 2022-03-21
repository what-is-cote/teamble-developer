import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# 시간복잡도 logN
n1=int(input())
list1=list(map(int, input().split()))
n2=int(input())
list2=list(map(int, input().split()))

res=list1+list2
res.sort()

for r in res:
  print(r, end=" ")

# ----------강의 풀이----------#
# 시간복잡도 N
# n=int(input())
# a=list(map(int, input().split()))
# m=int(input())
# b=list(map(int, input().split()))
# p1=p2=0
# c=[]

# while p1<n and p2<m:
#   if a[p1] <= b[p2]:
#     c.append(a[p1])
#     p1+=1
#   else:
#     c.append(b[p2])
#     p2+=1

# if p1<n:
#   c+=a[p1:]
# if p2<m:
#   c+=b[p2:]
 
# for x in c:
#   print(x, end=" ")