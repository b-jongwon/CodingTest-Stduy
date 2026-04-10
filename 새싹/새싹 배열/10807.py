a = int(input()) 

b= list(map(int,input().split()))

target= int(input())

count =0

for i in range(a):
    if b[i] == target:
        count+=1
        
print(count)        

# list(map(int,input().split())) 이런 형태를 사용하면 배열을 한꺼번에 받을 수 있다.
# count=0 이렇게 초기화를 해주어야지 나중에 연산에서 사용 가능하다.