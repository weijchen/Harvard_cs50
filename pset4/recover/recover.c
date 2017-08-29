#include <stdio.h>
#include <stdlib.h>
#define BUFSIZE 512

int main(int argc, char *argv[])
{
	// ensure proper usage
	if (argc != 2)
	{
		fprintf(stderr, "Usage: ./recover image\n");
		return 1;
	}

	// remember filenames
	char *infile = argv[1];
	typedef uint8_t  BYTE;
    BYTE buffer[BUFSIZE];

	// open input file 
	FILE *inptr = fopen(infile, "r");
	if (inptr == NULL)
	{
		fprintf(stderr, "Could not open %s.\n", infile);
		return 2;
	}
	// open output file 
    char *outptr = NULL;

	int jpgnum = 0;
	char filename[8];

	while(fread(&buffer, sizeof(buffer), 1, inptr) > 0) // from inptr read 512 size one time then store into buffer
	{
		if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
		{
			sprintf(filename, "%03i.jpg", jpgnum);
			outptr = fopen(filename, 'w');
			// fwrite(&buffer, sizeof(buffer), 1, outptr);
		}
	}
}