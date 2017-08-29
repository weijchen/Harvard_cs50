#include <cs50.h>
#include <stdio.h>

bool valid_triangle(int a, int b, int c);

int main(void)
{
	printf("%s\n", "First side's length: ");
	int a = get_int();
	
	printf("%s\n", "Second side's length: ");
	int b = get_int();
	
	printf("%s\n", "Third side's length: ");
	int c = get_int();

	valid_triangle(a, b, c);
 }

bool valid_triangle(int a, int b, int c)
{
	if ((a <= 0) || (b <= 0) || (c <= 0))
	{
		return false;
	}

	if ((a + b >= c) && (a + c >= b) && (b + c >= a))
	{
		return true;
	}
	else
	{
		return false;
	}
}