import random as r

def ans_num():
    ans = []
    
    while len(ans) <= 2:
        num = r.randint(1,9)
        if num not in ans:
            ans.append(num)

    return ans

def get_num():
    get = []

    num1, num2, num3 = map(int, input("숫자 3개를 입력하세요. => ").split(','))

    get.append(num1)
    get.append(num2)
    get.append(num3)

    return get

def score():
    ans = ans_num()
    get = get_num()

    ball = 0
    strike = 0
    count = 1

    while True:
        for i in range(3):

            if ans[i] == get[i]:
                strike += 1

            elif get[i] in ans and ans[i] != get[i]:
                ball += 1

        if strike != 3:
            count += 1
            print(f"{strike}S {ball}B")

            try:
                get = get_num()
            except ValueError:
                print("다시 입력하세요.\n" 
                "잘못입력 시 직전 숫자에 대한 정보가 계속 출력됩니다.")
                count -= 1

            strike = 0
            ball = 0

        elif strike == 3:
            print(f"{count}번 만에 모든 숫자를 맞히셨습니다.")
            break

        if count == 10:
            print("기회를 모두 소진했습니다."
                  f"\n 숫자는 {ans}였습니다.")
            break

    return count