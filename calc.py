# get two integer parameters
# return sum
def plus(x, y):
    return x+y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus")
        check = int(input())
        if check == 1:
            while True :
                try:
                    print("First Number")
                    x = int(input())
                    break #숫자 입력시 빠져나옴
                except ValueError: #글자를 넣는 다면 강제종료x 안내문 출력
                    print("숫자를 입력하시오!!")
                    continue #다시 처음부터 반복문 시작
            while True:    
                try:
                    print("Second Number")
                    y = int(input())
                    break
                except ValueError:
                    print("숫자를 입력하시오!!")
                    continue
            print("answer : ", plus(x,y))
        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
