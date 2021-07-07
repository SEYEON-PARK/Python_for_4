list1 = []
N = int(input('입력받을 정수의 개수를 입력하시오 : '))
if N >1:
    for x in range(N):
        a = int(input("정수를 입력하시오 : "))
        list1.append(a)

    M = int(input("정수 M을 입력하시오 : "))

    for x in range(N):
        if list1[x] < M:
            print(list1[x], end=" ")
