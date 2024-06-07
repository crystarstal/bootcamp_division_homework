"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    n = int(input())

    a=0
    b=1

    if 0<n<=12:

        for i in range(n+1):
            a+=i

        for i in range(1,n+1):
            b*=i

        print('{}: 1부터 {}까지의 합'.format(a,n))
        print('{}: {}! ({})'.format(b,n,(" * ".join(str(i) for i in range(n+1)))))
        print(a)
        print(b)

    if n==0:
        for i in range(n+1):
            a+=i

        for i in range(1,n+1):
            b*=i

        print('{}: 1부터 {}까지의 합'.format(a,n))
        print('{}: {}! ({})'.format(b,n,'1'))
        print(a)
        print(b)
    

    return

if __name__ == '__main__':
    main()
