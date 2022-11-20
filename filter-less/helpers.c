#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (float i = 0; i < height; i++)
    {
        for (float j = 0; j < width; j++)
        {
            float red = image[i][j].rgbtRed;
            float blue = image[i][j].rgbtBlue;
            float green = image[i][j].rgbtGreen;

            int average = round((Red + Green + Blue) / 3);
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j]rgbtBlue = average;

        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
