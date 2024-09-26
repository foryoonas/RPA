def sumfunc(n):
    return sum(range(1, n + 1))

def main():
    num = input("1 이상의 정수를 입력하세요: ") 

    if num.isdigit():  
        num = int(num)  
        if num < 1:
            print("잘못 입력하셨습니다.") 
        else:
            result = sumfunc(num)
            print(f"1부터 {num}까지의 합은 {result}입니다.")
    else:
        print("잘못 입력하셨습니다.")  

if __name__ == "__main__":
    main()