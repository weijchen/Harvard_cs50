#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define BUFSIZE 512

int main(int argc, char* argv[])
{
	// ensure proper usage
	if (argc != 2)
	{
		fprintf(stderr, "Usage: ./recover image\n");
		return 1;
	}
	
	// open input file 
	char* infile = argv[1];
	FILE* inptr = fopen(infile, "r");
	if (inptr == NULL)
	{
		fprintf(stderr, "Could not open %s.\n", infile);
		return 2;
	}
		
	// open output file 
	char* filename = malloc(sizeof("000.jpg"));
    FILE* outptr = NULL;

	int jpgnum = 0;
  	
  	//create a buffer
  	typedef uint8_t BYTE;
    BYTE buffer[BUFSIZE];

    while(fread(&buffer, sizeof(buffer), 1, inptr) > 0) // from inptr read 512 size one time then store into buffer
    {
        // create file if new jpg found
		if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
		{
		    // close file if needed
            if (outptr != NULL)                   
            {
                fclose(outptr);
                outptr = NULL;
            }
            
			sprintf(filename, "%03d.jpg", jpgnum);
			// printf("%s",filename);
			outptr = fopen(filename, "w");

            // if file can't create
            if (outptr == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", filename);
            }
            
			fwrite(buffer, 512, 1, outptr);
			jpgnum += 1;
		}
		// in same jpg, keep write jpg's information
		else
		{
			if(outptr != NULL)
			{
				fwrite(buffer, 512, 1, outptr);
			}
		}
	}
	// close all file, release all memory
	fclose(inptr);
	fclose(outptr);
    free(filename);

	return 0;
}