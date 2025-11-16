#include <stdio.h>
int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    if (a < b) {
        for (int i = a; i <= b; i++) {
            printf("%d %d", i, b - (i - a));
            if (i != b) {
                printf(" - ");
            }
        }
    } else {
        for (int i = a; i >= b; i--) {
            printf("%d %d", i, b + (a - i));
            if (i != b) {
                printf(" - ");
            }
        }
    }
    printf("\n");
    return 0;
}
