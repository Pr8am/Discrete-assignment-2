#include <stdio.h>

#define MAX_SIZE 100

void convolution(int input1[], int size1, int input2[], int size2, int result[])
{
    int maxSize = size1 + size2 - 1;

    for (int i = 0; i < maxSize; i++)
    {
        result[i] = 0;
        for (int j = 0; j < size1; j++)
        {
            if (i - j >= 0 && i - j < size2)
            {
                result[i] += input1[j] * input2[i - j];
            }
        }
    }
}

void unitStepResponse(int n, int unitStep[])
{
    for (int i = 0; i < n; i++)
    {
        unitStep[i] = 1; // Unit step response
    }
}

int main()
{
    // Code for y(n) calculation
    int sum_y = 0;
    FILE *file_y = fopen("simulation.dat", "w");
    if (file_y == NULL)
    {
        printf("Error opening simulation.dat file.\n");
        return 1;
    }
    for (int i = 0; i <= 9; i++)
    {
        sum_y = (i * (i + 1) * (i + 2) * (i + 3)) / 4;
        fprintf(file_y, "%d %d\n", i, sum_y);
    }
    fclose(file_y);

    // Code for convolution and writing to analysis.dat
    int sequence[10];
    for (int i = 0; i < 10; i++)
    {
        sequence[i] = i * i * i + 3 * i * i + 2 * i;
    }
    int size = sizeof(sequence) / sizeof(sequence[0]);

    int n = size; // Number of terms to sum

    int unitStep[MAX_SIZE];
    unitStepResponse(n, unitStep);

    int result[MAX_SIZE];

    // Convolution of sequence with unit step response
    convolution(sequence, size, unitStep, n, result);

    // Write the results to analysis.dat
    FILE *file = fopen("analysis.dat", "w");
    if (file == NULL)
    {
        printf("Error opening analysis.dat file!\n");
        return 1;
    }

    // Write the results to the file
    for (int i = 0; i < size; i++)
    {
        fprintf(file, "%d %d\n", i + 1, result[i]);
    }

    fclose(file);

    printf("Data written to analysis.dat\n");

    return 0;
}

