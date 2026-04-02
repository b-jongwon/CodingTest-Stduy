a=int(input())

for i in range(1, a+1):
    for j in range(i):
        print('*', end='')
    print('')

# 파이썬에서 range 활용을 i 를 이용할려 하지말고 바로 range로 범위 구하는게 더 나음
# print는 기본적으로 개행문자가 들어가기 때문에 \n를 위해서 문자로 출력 할 필요 없다.
# print(문자,end='') 꼴을 하면 줄바꿈을 방지 가능하다.        