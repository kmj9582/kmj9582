def dan(number):
    print(number,"단 출력합니다.")
    for i in range(1, 10):
        print(number,"x",i,"=",number*i)

number = int(input("몇 단을 입력할까요? "))
dan(number)