#include <cs50.h>
#include <stdio.h> //use printf function

int main(void)
{
    printf("x: ");
    int x = get_int();
    printf("y: ");
    int y = get_int();
    
    int z = x + y;
    
    printf("Sum of x and y is %d\n", x + y);
}