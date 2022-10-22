#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    int spaces;
    int hashes;

    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int i = 1; i < height; i++)
{
    for (spaces = (height - i); spaces > 0; spaces --)
    {
        printf(" ");
    }
    for (hashes = 1; hashes <= (i); hashes++)
    {
        printf("#");
    }
    printf("\n");
}
return 0;
}