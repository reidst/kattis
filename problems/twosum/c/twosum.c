#include <stdio.h>

main() {
    int a = 0, b = 0;
    char c, last;
    
    while ((c = getchar()) >= '0' && c <= '9') {
        a = a * 10 + (c - '0');
    }
    while ((c = getchar()) < '0' || c > '9')
        ;
    b = c - '0';
    while ((c = getchar()) >= '0' && c <= '9') {
        b = b * 10 + (c - '0');
    }
    
    printf("%d\n", a + b);
}