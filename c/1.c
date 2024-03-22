/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() {
    int num, num1, num2, num3;
	int i, j, k;
	scanf("%d", &num);

	for (i=-1; num > 0; i++)
	{
		num = num - 100;
	}
	num1 = num + 100;

	for (j = -1; num1 > 0; j++)
	{
		num1 = num1 - 10;
	}
	num2 = num1 + 10;
	num3 = 100 * num2 + 10* j + i;
	printf("%d\n", num3);
	
	return 0;
}