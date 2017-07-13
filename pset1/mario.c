/* 
Author: Jimmy Chen
PN: Mario, Created Jul. 2017
Ver: 1.0 (finished)
*/

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Declare and intialize variables
	int height = 0;
	
	// do ... while ... loop condition
	do
    {
		printf("Height:");
		height = get_int();
        if (height == 0)
        {
            return 0;
        } 
    }while (height < 1 || height > 23);

    // if FALSE to condition, do this
    for (int i = 1; i <= height; i++)
    {
        for(int j = height - i; j > 0; j--)
        {
            printf(" ");
        }
        for(int k = 1; k <= i+1; k++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}