# 리스트

def DFS():
  # global a
  # a=a+[4]
  a[0]=7 # 이러한 경우 새로운 리스트 생성하는 것 아님, 원래 있는 a리스트의 요소를 바꾸는 것 -> 자동으로 전역변수로 인식 
  # a=[7, 8] # 로컬 변수 a 새로 선언, 윗줄이 남아있는 경우 에러 발생
  print(a)

if __name__=="__main__":
  a=[1, 2, 3]
  DFS()
  print(a)