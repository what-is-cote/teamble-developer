import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
s=input()
num=""

for c in s:
  if ord('0')<=ord(c)<=ord('9'):
    num+=c

num=int(num)

cnt=1
for i in range(1, num//2+1):
  if num%i==0:
    cnt+=1

print(num)
print(cnt)
    
  
# ----------강의 풀이----------#
s=input()

res=0
for c in s:
  if c.isdecimal(): # 0~9까지의 숫자인지 판단 cf) isdigit(): 숫자인지 판단
    res=res*10+int(c)
print(res)

cnt=0
for i in range(1, res+1):
  if res%i==0:
    cnt+=1
print(cnt)