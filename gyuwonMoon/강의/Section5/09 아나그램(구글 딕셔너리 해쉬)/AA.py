import sys, os
sys.stdin=open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

# ----------내 풀이----------#
# #1 딕셔너리 해쉬
# s1=input()
# s2=input()

# sp1=dict()
# sp2=dict()

# for s in s1:
#   if bool(sp1.get(s)):
#     sp1[s]+=1
#   else:
#     sp1[s]=1

# for s in s2:
#   if bool(sp2.get(s)):
#     sp2[s]+=1
#   else:
#     sp2[s]=1
    
# if sp1==sp2:
#   print('YES')
# else:
#   print('NO')


# ----------강의 풀이----------#
# #1 딕셔너리 해쉬
# a=input()
# b=input()
# str1=dict()
# str2=dict()

# for x in a:
#   str1[x]=str1.get(x, 0)+1 # x가 있으면 x의 value를, 없으면 0을 반환
# for x in b:
#   str2[x]=str2.get(x, 0)+1

# for i in str1.keys():
#   if i in str2.keys():
#     if str1[i]!=str2[i]:
#       print('NO')
#       break
#   else:
#     print('NO')
#     break
# else:
#   print('YES')

# #2 딕셔너리 해쉬 개선 ver
a=input()
b=input()
sH=dict()

for x in a:
  sH[x]=sH.get(x, 0)+1
for x in b:
  sH[x]=sH.get(x, 0)-1 # 원상복귀!

for x in a:
  if sH.get(x)>0:
    print('NO')
    break
else:
  print('YES')

# #3 리스트 해쉬
# a=input()
# b=input()
# str1=[0]*52 # 알파벳 대소문자 개수
# str2=[0]*52

# for x in a:
#   if x.isupper():
#     str1[ord(x)-65]+=1 # 아스키코드 대문자: 65~90
#   else:
#     str1[ord(x)-71]+=1 # 아스키코드 소문자: 97~122

# for x in b:
#   if x.isupper():
#     str2[ord(x)-65]+=1 # 아스키코드 대문자: 65~90
#   else:
#     str2[ord(x)-71]+=1 # 아스키코드 소문자: 97~122
    
# for i in range(52):
#   if str1[i]!=str2[i]:
#     print('NO')
#     break
# else:
#   print('YES')