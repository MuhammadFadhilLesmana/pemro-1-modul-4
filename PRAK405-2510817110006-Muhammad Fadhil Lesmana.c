#include <stdio.h>

int main() {
    int n, kelipatan;
    scanf("%d %d", &n, &kelipatan);
    int total = 0;
    for (int i = 1; i <= n; i++) {
        int jumlah = 0;
        for (int j = i; j >= 1; j--) {
            int hasil = j * kelipatan;
            jumlah += hasil;
            printf("(%d * %d)", j, kelipatan);
            if (j > 1) {
                printf(" + ");
            }
        }
        printf(" = %d\n", jumlah);
        total += jumlah;
    }
    printf("%d\n", total);
    return 0;
}
