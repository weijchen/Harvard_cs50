#include <stdio.h>
// include package for get_string()
#include <cs50.h>

int main(void){
    
    string s = get_string();
    print("hello, %s\n", s)
}