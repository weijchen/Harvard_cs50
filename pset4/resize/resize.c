/**
 * Copies a BMP piece by piece, just because.
 */
       
#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize n infile outfile\n");
        return 1;
    }

    // remember filenames
    // char *n = argv[1];
    int n = atoi(argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file 
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }
    
    // determine padding for scanlines
    int old_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    
    // resize biHeight and biWidth
    int old_Height = bi.biHeight;
    bi.biHeight = old_Height * n;
    int old_Width = bi.biWidth;
    bi.biWidth = old_Width * n;
    // after changing biWidth, find new padding
    int new_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + new_padding) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);
    
    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);
    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(old_Height); i < biHeight; i++)
    {
        // vertical resize
        for (int vertical_resize = 0; vertical_resize < n; vertical_resize++)
        {
            // iterate over pixels in scanline
            for (int j = 0; j < old_Width; j++)
            {
                // horizontal resize
                for (int horizontal_resize = 0; horizontal_resize < n; horizontal_resize++)
                {
                    // temporary storage
                    RGBTRIPLE triple;
                    // read RGB triple from infile
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr); 
                    
                    // move file pointer back one pixel if not at last pixel
                    if (horizontal_resize != (n-1))
                        fseek(inptr, -(long int)sizeof(RGBTRIPLE), SEEK_CUR);
                }
            }
            // skip over padding, if any
            fseek(inptr, old_padding, SEEK_CUR);
            // then add new padding back (to demonstrate how)
            for (int k = 0; k < new_padding; k++)
            {
                fputc(0x00, outptr);
            }
            
            // move file pointer back to the beginning of the row if not at last row
            if (vertical_resize != (n-1))
                fseek(inptr, (-(long int)sizeof(RGBTRIPLE) * old_Width) - old_padding , SEEK_CUR);
        }
    }
    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
