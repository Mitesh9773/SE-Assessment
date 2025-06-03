#include <stdio.h>

void showmenu();
float add(float a, float b);
float sub(float a, float b);
float mul(float a, float b);
float div(float a, float b);

void main()
{
    int choice;
    float num1, num2, result;

    while (1)
    {
        showmenu();

        // Ask for user choice
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);

        // Exit condition
        if (choice == 5)
        {
            printf("Thank you for using calculator.\n");
            break;
        }

        // Invalid choice check
        if (choice < 1 || choice > 5)
        {
            printf("Invalid choice. Please choose a valid option.\n\n");
            continue;
        }

        // Take input
        printf("Enter first Number: ");
        scanf("%f", &num1);

        printf("Enter second Number: ");
        scanf("%f", &num2);

        // Perform operation
        switch (choice)
        {
        case 1:
            result = add(num1, num2);
            printf("Addition = %.2f\n\n", result);
            break;
        case 2:
            result = sub(num1, num2);
            printf("Subtraction = %.2f\n\n", result);
            break;
        case 3:
            result = mul(num1, num2);
            printf("Multiplication = %.2f\n\n", result);
            break;
        case 4:
            if (num2 == 0)
            {
                printf("Division by zero is not allowed.\n\n");
            }
            else
            {
                result = div(num1, num2);
                printf("Division = %.2f\n\n", result);
            }
            break;
        }
    }
}

// Show menu
void showmenu()
{
    printf("-----------MENU-------------\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("5. Exit\n");
    printf("----------------------------\n");
}

// Business logic functions
float add(float a, float b)
{
    return a + b;
}
float sub(float a, float b)
{
    return a - b;
}
float mul(float a, float b)
{
    return a * b;
}
float div(float a, float b)
{
    return a / b;
}
