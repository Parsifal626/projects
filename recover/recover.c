#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc !=2)
    {
        printf("Usage: ./recover card.raw\n");
        return 1;
    }
    else
    {
        char *input_file_name = argv[1];
        FILE *input_file = fopen(input_file_name, "r");

        if (input_pointer == NULL)
        {
            printf("The programm cannot open %s\n", input_file_name);
            return 2;
        }
    }
    unsigned char buffer[512];
    int count = 0;
    FILE *output_file = NULL;
    char *filename = malloc(8 * sizeof(char));
    while (fread(&buffer, sizeof(char), 512, input_file))
        {
            // If start of a new JPEG (0xff 0xd8 0xff 0xe*):
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
            {
                // If not first JPEG, close previous
                if (!(count == 0))
                {
                    fclose(img_pointer);
                }
                // Initialise file
                sprintf(filename, "%03i.jpg", count);
                img_pointer = fopen(filename, "w");
                count++;
            }
            // If JPEG has been found, write to file
            if (!(count == 0))
            {
                fwrite(&buffer, 512, 1, img_pointer);
            }
        }
        fclose(img_pointer);
        fclose(img_pointer);
        return 0;
    }
