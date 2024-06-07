"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    time=int(input())

    if 0<=time<=24:
        if time<12:
            print('AM')

        else:
            print('PM')

    else:
        print('유효한 시간이 아닙니다.')

    return


if __name__ == '__main__':
    main()
