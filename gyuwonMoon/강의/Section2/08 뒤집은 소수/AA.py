import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# def reverse(x):
#   x=str(x)
#   # reversed_x=int(''.join(reversed(x)))
#   reversed_x=int(x[::-1])

#   return reversed_x

# def isPrime(x):
#   if x==1:
#     return False
#   # elif x==2:  # 필요X
#   #   return True
#   else:
#     cnt=0
#     for i in range(2, x+1):
#       if x%i==0:
#         cnt+=1
#       if cnt>1:
#         return False
#     else:
#       return True
  
# N=int(input())
# nums=list(map(int, input().split()))

# for num in nums:
#   num=reverse(num)
  
#   if isPrime(num):
#     print(num, end=" ")


# ----------강의 풀이----------#
def reverse(x):
  res=0
  while x>0:
    t=x%10
    res=res*10+t
    x=x//10
  return res

def isPrime(x):
  if x==1:
    return False

  # 자기자신을 제외한 약수는 절반(x//2) 이내에만 존재함
  # ex) 16의 약수: 1,2,4,8 (16 = 1*16 = 2*8 = 4*4)
  for i in range(2, x//2+1):
    if x%i==0:
      return False
  else: # x가 2인 경우 for문 동작X (성공O) -> 바로 else문으로 감
    return True
  
N=int(input())
nums=list(map(int, input().split()))

for num in nums:
  tmp=reverse(num)
  
  if isPrime(tmp):
    print(tmp, end=' ')