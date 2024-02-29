#include <stdio.h>

// Function to calculate the sum of the series
int sumOfSeries(int n) {
    int sum = 0;
    int i, j, term;

    for (i = 1; i <= n; i++) {
        term = 1;
        for (j = i; j <= i + 2; j++) {
            term *= j;
        }
        sum += term;
    }

    return sum;
}

int main() {
    int n;
    for (n = 1; n <= 10; n++) {
        int result = sumOfSeries(n);
        printf("%d\n", result);
    }
    return 0;
}

