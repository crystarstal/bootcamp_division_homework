"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    
    while True:

        num = int(input())

        if num>0:

            a=0
            for i in range(num+1):
                a=a+i

            print(a)       
            break
           

        else:
            print('X')

    return

if __name__ == '__main__':
    main()
