// kattis-accepted
#include <stdio.h>

int main(int argc, char const *argv[])
{
	int jon, doc;
	char c;

	for (jon = 0; (c = getchar()) == 'a'; jon++)
		;
	while ((c = getchar()) != 'a' && c != 'h')
		;
	if (c == 'a')
		doc = 1;
	else
		doc = 0;
	for (; (c = getchar()) == 'a'; doc++)
		;

	if (doc > jon)
		printf("no\n");
	else
		printf("go\n");

	return 0;
}
