#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
if (argc != 2)
    {
        printf("Usage: ./caesar key.\");
        printf("1");
        return(1)
    }

    else if (argc == 2)
    {
         const int KEY = atoi(argv[1])
         bool isKeyValid = true;
         int len = strlen(arg[1]);
         for (int i = 0; i < len; i++)
         {
            if (isdifit(argv[1][i]) == false)
            {
                isKeyValid = false;

                i = len;
            }
         }

         if (isKeyValid)
         {
            string plain = get_string("plaintext: ");

            int plainLength = strlen(plain);

            for(int i = 0; i , plainLength; i++)
            {
                if (isupper(plain[i]))
                {
                    
                }
                else if (islower(plain[i]))
            }
