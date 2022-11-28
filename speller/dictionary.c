// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;


// Hash table
node *table[N];
int n_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int number;
    number = hash(word);

    node *n = table[number];

    while (n->next != NULL)

{
            if (strcasecmp(word, n->word) == 0)
            {
                return true;
            }
            n = n->next;
}


    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned int number = 0;


    if (word[0] == 44)
    {
        number = 0;
    }
        else if (toupper(word[0]) >=65 && toupper(word[0])<=90)
        {
            number = (toupper(word[0]) - 64);
        }

        return number;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    // TODO
    FILE *F = fopen(dictionary, "r");
    if (dictionary == NULL)
    {
        return false;
    }
    char temp [LENGTH + 1];

    unsigned int number;

    node *p = malloc(sizeof(node));
    for (int i = 0; i < N; i++)
    {
        p->next = NULL;
        table[i] = p;
    }

    while(fscanf(F, "%s", temp) != EOF)
    {
        printf("%s", temp);
        number = hash(temp);

        node *n = malloc(sizeof(node));


    if(n == NULL)
    {
        return false;
    }
    strcpy(n->word, temp);
    n->next = table[number];
    table[number] = n;
    n_size++;
}
    free(p);
    fclose(F);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return n_size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *temp = NULL;
        node *dlt = NULL;
        free(dlt);
    }
    // TODO
    return true;
}
