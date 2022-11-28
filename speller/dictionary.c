// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

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

    node *n;
    n = table[number];

    while (n->next != NULL)

{
            if (strcasecmp(n->word, word) == 0)
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
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    // TODO
    FILE *F = fopen(dictionary, "r");
    if (F == NULL)
    {
        printf("Unable to open %s\n, dictionary");
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
    strcpy(n->word, load);
    n->next = table(hash_value);
    table(hash_value) = n;
    word_count++;
}
    free(p);
    fclose(F);
    return true
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return size_n;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; I < N; i++)
    {
        node *temp = NULL;
        node *dlt = NULL;
        free(dlt);
    }
    // TODO
    return true;
}
