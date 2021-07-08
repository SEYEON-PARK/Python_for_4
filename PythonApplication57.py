list1 = [] # 리스트 list1 생성
N = int(input('입력받을 정수의 개수를 입력하시오 : ')) # 사용자로부터 정수 입력받기
if N >1: # 만약 N이 1보다 크다면
    for x in range(N): # x에 0부터 N-1까지 대입하며 반복
        a = int(input("정수를 입력하시오 : ")) # 사용자로부터 정수 입력받기
        list1.append(a) # 입력받은 정수를 리스트 list1에 추가하기

    M = int(input("정수 M을 입력하시오 : ")) # 사용자로부터 정수 입력받기

    for x in range(N):
        if list1[x] < M: # 만약, list1[x]가 M보다 작다면
            print(list1[x], end=" ") # list1[x] 출력하기
