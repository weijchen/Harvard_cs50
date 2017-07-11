/* 
Author: Jimmy Chen
PN: helpers, Created Jul. 2017
Ver: 1.0 (finished)
*/
 
#include <cs50.h>
#include <stdio.h>
#include "helpers.h"

/**
 * Search algorithm
 */

bool linear_search(int value, int values[], int n)
{
    int boolnum = 0;
    // break while n is negative
    if (n < 1)
    {
        return false;
    }
    else
    {
       for (int i = 0; i < n; i++)
       {
           if (values[i] == value)
           {
               boolnum = 1;
               break;
           }
       }
       if (boolnum == 1)
       {
           return true;
       }
       else
       {
           return false;
       }
    }
}

/**
 * Sort algorithm.
 */
void bubble_sort(int values[], int n)
{
    for(int i3 = 0; i3 < n - 1; i3++)
    {
        printf("%i\n", values[i3]);  
    }
    for (int j = 0; j <= n - 1; j++)
    {
        for (int i = 0; i < n - 1; i++)
        {
            if (values[i] > values[i + 1])
            {
                int temp = values[i];
                values[i] = values[i + 1];
                values[i + 1] = temp;
            }
        }
    }
    return;
}

// Call search, sort function
bool search(int value, int values[], int n)
{
    return linear_search(value, values, n);
}

void sort(int values[], int n)
{
    return bubble_sort(values, n);
}