#include <stdio.h>

int main() {
    int n = 9; // Maximum value of n
    int sum = 0;
    int i, j, term;

    // Open the file for writing
    FILE *file = fopen("simulation.dat", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Write data to the file
    for (i = 0; i <= n; i++) {
        term = 1;
        for (j = i; j <= i + 2; j++) {
            term *= j;
        }
        sum += term;
        fprintf(file, "%d %d\n", i + 1, sum);
    }

    // Close the file
    fclose(file);

    return 0;
}

