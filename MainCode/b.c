#include <stdio.h>

int main() {
    int n = 9; // Maximum value of n
    int sum = 0;
    int i, j, term;

    for (i = 0; i <= n; i++) {
        term = 1;
        for (j = i; j <= i + 2; j++) {
            term *= j;
        }
        sum += term;
        printf("%d %d", i+1,sum);
        printf("\n");
    }

    return 0;
}

