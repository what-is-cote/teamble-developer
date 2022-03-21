import os , sys

sys.stdin=open("noeyes/section_4/6.씨름선수.txt", "rt")

n = int(input())
members = []

for i in range(n):
  h , w = map(int,input().split())
  members.append([h,w])
  
members.sort(reverse=True)

count = 0
largest= 0

for i in range(n):
  
  if members[i][1] > largest:
    largest = members[i][1]
    count+=1
    
print(count)
