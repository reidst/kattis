// kattis-accepted
#include <stdio.h>

int factorial(int n) {
	int i = 1;
	for (; n > 0; n--)
		i *= n;
	return i;
}

int main(int argc, char const *argv[])
{
	int rows, row;
	scanf("%d", &rows);
	for (; rows > 0; rows--) {
		scanf("%d", &row);
		printf("%d\n", factorial(row) % 10);
	}
	return 0;
}
