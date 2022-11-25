// Implements a dictionary's functionality
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"
#define HASHTABLE_SIZE 1985

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
node *hashtable[HASHTABLE_SIZE];

// Hash table
int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int n = strlen(word);
    char copy[n + 1];
    // TODO
    copy [n] = '\0';
    for(int i = 0; i < n; i++)
    
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict_pointer = fopen(dictionary, "r");
    if (dictionary == NULL)
    {
        printf("Unable to open %s\n, dictionary");
        return false;
    }
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
