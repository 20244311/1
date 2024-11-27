import random
a = int(input("선택하시오(1.가위, 2.바위, 3.보) : "))
b = random.randint(1,3)
print(f"컴퓨터의 선택(1.가위, 2.바위, 3.보) {b}")
if (a+1)%3 == b :
    print("사용자 패배")
elif a == b:
    print("무승부")
else :
    print("사용자 승리")
