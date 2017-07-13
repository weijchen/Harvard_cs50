/* 
Author: Jimmy Chen
PN: Initials, Created Jul. 2017
Ver: 1.0 (finished)
*/

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string();

    // Deal ewith first letter
    printf("%c", toupper(s[0]));

    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // Deal with remaining letters (First check alphabatic)
        if (s[i] != '\0' && s[i] == ' ')
        {
            printf("%c", toupper(s[i+1]));
        }
    }
    printf("\n");
}