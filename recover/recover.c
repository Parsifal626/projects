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
        printf("Error: cannot open %s\n", input_file_name);
        return 2;
    }

}