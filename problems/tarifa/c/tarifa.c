#include <stdio.h>

int main() {

	int x, n, p, sum;
	scanf("%d", &x);
	scanf("%d", &n);

	sum = x;

	for(; n > 0; n--) {
		scanf("%d", &p);
		sum += x - p;
	}

	printf("%d\n", sum);

	return 0;
}