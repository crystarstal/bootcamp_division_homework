"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    year=int(input())
    month=int(input())

    if (year%4==0 and year%100 !=0) or (year%400==0):
        if month == 4 | 6 | 9 | 11:
            print('30')

        if month == 2:
            print('29')

        else:
            print('31')

    else:
        if month == 4 | 6 | 9 | 11:
            print('30')

        if month == 2:
            print('28')

        else:
            print('31')


    return


if __name__ == '__main__':
    main()
