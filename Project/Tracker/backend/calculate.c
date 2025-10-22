#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp = fopen("backend/data.csv", "r");
    if (!fp) {
        printf("No data found.\n");
        return 0;
    }

    char line[100];
    float total = 0;
    while (fgets(line, sizeof(line), fp)) {
        char date[20], category[50];
        float amount;
        sscanf(line, "%[^,],%[^,],%f", date, category, &amount);
        total += amount;
    }
    fclose(fp);
    printf("Total Expenses: %.2f\n", total);
    return 0;
}
