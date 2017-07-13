/* 
Author: Jimmy Chen
PN: Greedy, Created Jul. 2017
Ver: 1.0 (finished)
*/

#include <cs50.h>
#include <stdio.h>
#include <math.h>

// Define initial values
#define QUARTER 25;
#define DIME 10;
#define NICKEL 5;

int main(void) 
{
    // Declare variables
    float given_amount = 0;
    int cent_amount = 0;
    int quarter_count = 0;
    int dime_count = 0;
    int nickel_count = 0;
    int left = 0;
    int coin_count = 0;
    
    //Input handling
    do 
    {
        printf("O hai! How much change is owed?\n");
        given_amount = GetFloat();

        //Check for whether given amount is zero or less than zero
        if (given_amount <= 0)
        {
            printf("Number Should be greater then Zero\n");
        }
    }while(given_amount <= 0);

    cent_amount = (int)round(given_amount*100);

    quarter_count = cent_amount / QUARTER;
    left = cent_amount % QUARTER;
    
    dime_count = left / DIME;
    left = left % DIME;
    
    nickel_count = left / NICKEL;
    left = left % NICKEL;
    
    // Add residual amounts of each steps
    coin_count = quarter_count + dime_count + nickel_count + left;
    
    printf("%d\n", coin_count);
    
    return 0;
}