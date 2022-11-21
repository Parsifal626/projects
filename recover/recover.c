#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc !=2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    else
    {
        char *input_file_name = argv[1];
        FILE *input_pointer = fopen(input_file_name, "r");

        if (input_pointer == NULL)
        {
            printf("Error: cannot open %s\n", input_file_name);
            return 2;
        }
    }

}