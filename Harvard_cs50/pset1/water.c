/* 
Author: Jimmy Chen
PN: Water, Created Jul. 2017
Ver: 1.0 (finished)
*/

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("Minutes: ");
    // Key in minute variable
    int minute = get_int();
    if(minute > 0)
    {
        printf("Bottles: %d\n", minute * 12);
    }
    else
    {
        printf("error\n");
    }
}