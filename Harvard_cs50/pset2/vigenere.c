/* 
Author: Jimmy Chen
PN: Vigenere, Created Jul. 2017
Ver: 1.0 (finished)
*/

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./vigenere k\n");
        return 1;
    }
    
    // 1. Key in keyword
    string keyword = argv[1];
    int m = strlen(keyword);
    
    // 2. check keyword's validity
    for (int i = 0; i < m; i++)
    {
        if(!isalpha(keyword[i]))
            {
                printf("Need a valid key \n");
                return 1;
            }
    }

    // 3. transfer keyword to all lowercase
    for (int k = 0, l = strlen(keyword); k < l; k++)
    {
        if (islower(keyword[k]))
        {
            keyword[k] = keyword[k];
        }
        else if (isupper(keyword[k]))
        {
            keyword[k] = keyword[k] + 32;
        }
    }
    
    // initialize iterator
    int i = 0;
    printf("plaintext: ");
    string plaintext = get_string();
    
    for (int j = 0, n = strlen(plaintext); j < n; j++)
    {
        if (isalpha(plaintext[j]))
        {
            // for lowercase
            if (islower(plaintext[j]))
            {
                plaintext[j] = (plaintext[j] - 'a' + (keyword[i] - 97)) % 26 + 97;
            }
            // for uppercase
            else if(isupper(plaintext[j]))
            {
                plaintext[j] = (plaintext[j] - 'A' + (keyword[i] - 97)) % 26 + 65;
            }

            // test whether keyword iterator over length
            if (i == (m - 1)) // if over length, set i as 0 to rerun keyword
            {
                i = 0;
            }
            else
            {
                i++;
            }
        }
    }
    printf("ciphertext: %s\n", plaintext);
    return 0;
}