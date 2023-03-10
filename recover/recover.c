#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
bool is_start_new_jpeg(BYTE buffer[]);
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
        printf("The programm cannot open\n");
        return 1;
    }

    BYTE buffer[512];
    int file_index = 0;
    bool have_found_first_jpg = false;
    FILE* output_file;
    while (fread(buffer, 512, 1, input_file))
    {
        if(is_start_new_jpeg(buffer))
        {
        if(!have_found_first_jpg)
            have_found_first_jpg = true;
             else
             {
                fclose(output_file);
             }
                char filename[8];
                sprintf(filename, "%03i.jpg", file_index++);
                output_file = fopen(filename, "w");
                if (output_file == NULL)
                    return 1;
                fwrite(buffer, 512, 1, output_file);
        }

        else if (have_found_first_jpg)
        {
        fwrite(buffer, 512, 1, output_file);
        }
    }


        fclose(input_file);
        fclose(output_file);

}
bool is_start_new_jpeg(BYTE buffer[])
{
    return buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0;
}

