"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():

    score=int(input())

    if 90<=score<=100:
        grade='A'

    if score<90 and score>=80:
        grade='B'

    if score<80 and score>=70:
        grade='C'

    if score<70 and score>=60:
        grade='D'

    if score<60:
        grade='F'

    print(grade)

    return


if __name__ == '__main__':
    main()
