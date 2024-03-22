/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() {
   int n, i = 0, sum=0, fac=1;
	scanf("%d", &n);

	for (i=n;i>=0;i--)
	{
		sum = sum + i;
	}
	printf("%d: 1부터 %d까지의 합\n", sum, n);

	for (i = n ; i >= 1; i--)
	{
		fac = fac * i;
	}
	printf("%d: %d!\n", fac, n);
	printf("%d \n%d", sum, fac);

    return 0;
}