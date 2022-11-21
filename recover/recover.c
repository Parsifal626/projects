#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define BLOCK_NAME_SIZE 512
#define FILE_NAME_SIZE 8
bool is_start_new_jpeg(BYTE);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMG\n");
        return 1;
    }
    FILE* input_file = fopen(argv[1], "r");
    if (input_file == NULL)
    {
        printf("The programm cannot open");
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];

    bool have_found_first_jpg = false;
    FILE* outfile;
    while (fread(buffer, BLOCK_SIZE, 1, infile))
    {
        if(is_start_new_jpeg(buffer))
        {
            if(!have_found_first_jpg)
            have_found_first_jpg = true;
            else
                fclose(outfile);
                char filename[FILE_NAME_SIZE];
                sprint(filename, "%03i.jpg", file_index++);
                outfile = fopen(filename, "w");
                if (outfile == NULL)
                return 1;
                fwrite(buffer, BLOCK_SIZE, 1, outfile);


        }
        else if (have_found_first_jpg)
        fwrite(buffer, BLOCK_SIZE, 1, outfile);
    }
}

        fclose(input_file);
        fclose(output_file);



}
bool is_start_new_jpeg(BYTE buffer[])
{
    return (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
}

