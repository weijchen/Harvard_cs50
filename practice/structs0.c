#include <cs50.h>
#include <stdio.h>
#include <string.h>

#include "structs.h"

#define STUDENTS 3 // define a constant

int main(void)
{
	student students[STUDENTS];

	for (int i = 0; i < STUDENTS; i++)
	{
		printf("name: ");
		students[i].name = get_string();

		printf("dorm: ");
		students[i].dorm = get_string();
	}

	for (int = 0; i < STUDENTS; i++)
	{
		printf("%s is in %s.\n", students[i].name, students[i].dorm);
	}
}