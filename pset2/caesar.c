/* 
Author: Jimmy Chen
PN: Caesar, Created Jul. 2017
Ver: 1.0 (finished)
*/

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // If argument amount is wrong, return error code
    if (argc != 2 || atoi(argv[1]) < 0)
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }
    
    // make k equals to second argument
    int k = atoi(argv[1]);
    printf("plaintext: ");
    string s = get_string();
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // for lowercase
        if (islower(s[i]))
        {
            s[i] = (s[i] - 'a' + k) % 26 + 97;
        }
        // for uppercase
        else if(isupper(s[i]))
        {
            s[i] = (s[i] - 'A' + k) % 26 + 65;
        }
    }
    printf("ciphertext: %s\n", s);
    return 0;
}