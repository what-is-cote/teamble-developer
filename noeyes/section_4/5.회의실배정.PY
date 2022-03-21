import os , sys

# sys.stdin=open("noeyes/section_4/5.회의실배정.txt", "rt")

n = int(input())
meeting = []

for i in range(n):
  s , e = map(int,input().split())
  meeting.append((s,e))
  
meeting.sort(key = lambda x: (x[1],x[0]))

count = 0
end = 0
for s , e in meeting:
  if(s >= end):
    count += 1
    end = e
    
print(count)
  
