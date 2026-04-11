# 1. 크기가 31인 리스트를 False로 초기화
submit = [False] * 31

# 2. 28명의 제출자를 입력받아 해당 인덱스를 True로 변경
for _ in range(28):
    submit[int(input())] = True

# 3. 1번부터 30번 중 미제출자(False)를 찾아 출력
for i in range(1, 31):
    if not submit[i]:
        print(i)




## ary=list(map(int,input().split())) => 이렇게 입력받는건 띄어쓰기로 구분된 한 줄의 입력을 받을 때 씁
# => 여러줄에 걸쳐 받을때는 반복문 돌면서 받아야함.

## temp=list   => 이렇게 초기화 하면 안되고 temp=[0]*31로 미리 초기화 해야함.
# 문법: 배열이름 = [초기화할 값] * 원하는 길이(개수)
# 2차원 배열 초기화 board = [[0] * 3 for _ in range(3)]

## for i in range(30):
##     temp[ary[i]]=1   

##for i in range(30):
##    if temp[i] != 1:
##        print(temp[i])    