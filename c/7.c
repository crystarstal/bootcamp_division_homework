/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() {
    int year, month;
	printf("입력 (연도, 월 순서대로 입력)");
	scanf("\n%d\n%d", &year, &month);

	if (year%4==0&&year%100!=0)
	{
		if (month ==2 )
			printf("29");
		if (month == 4 || month == 6 || month == 9 || month == 11)
			printf("30");
		if(month!=2 && month && 4 && month && 6 && month != 9&& month && 11)
		{
			printf("31");
		}
	}
	if (year % 400 == 0)
	{
		if (month == 2)
			printf("29");
		if (month == 4 || month == 6 || month == 9 || month == 11)
			printf("30");
		if (month != 2 && month && 4 && month && 6 && month != 9 && month && 11)
		{
			printf("31");
		}
		
	}
	if (year % 4 != 0 && year % 100 == 0 || year % 400 != 0)
	{
		if (month == 2)
			printf("28");
		if (month == 4 || month == 6 || month == 9 || month == 11)
			printf("30");
		if (month != 2 && month && 4 && month && 6 && month != 9 && month && 11)
		{
			printf("31");
		}
	}

    return 0;
}