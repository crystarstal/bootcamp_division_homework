"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    num =(input())
    if  100<=int(num)<=999: 
        print(int(num[::-1]))

    return


if __name__ == '__main__':
    main()
