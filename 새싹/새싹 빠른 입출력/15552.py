import sys
input=sys.stdin.readline #이렇게 하면 추후에 사용하는 input을 sys.stdin으로 사용 가능.

a=int(input().rstrip())

for _ in range(1,a+1):
    b,c=map(int,(input().split()))
    print(b+c)

# range(1,b) 는 1부터 b-1까지 반복이라서 b+1을 해줘야지 b만큼 반복한다.
# input은 호출될 때마다 안내 메세지 출력하고 입력 대기 + 개행 문자 제거하는 등 로직 수행
# sys.stdin.readline은 훨씬 큰 단위의 버퍼를 사용하여 데이터를 한꺼번에 읽어옴.
# => i/o에 접근하는 시스템 콜 횟수를 줄이는 것이 성능 향상의 핵심.
#.rstrip() 을 사용하게 되면 문자 끝에있는 공백이나 개행문자를 제거해줌.