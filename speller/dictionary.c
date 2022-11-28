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

    int n = strlen(word);
    char copy[n + 1];
    // TODO
    for(int i = 0; i < n; i++)
    {
        lword[i] = tolower(word[i]);
    }
    lword[n] = '\0';
    int hash_code = hash(lword);

    node *head = table[copy_index];
    node *cursor = head;
    if (head != NULL)
    {
        while (cursor != NULL)
        {
            if (strcasecmp(copy.cursor -> word) == 0)
            {
                return true;
            }
            else
            {
                cursor = cursor -> next;
            }
        }
    }

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
    char word [LENGTH+1];
    while (fscanf(file, "%s\n", word) != EOF)

    node *n = malloc(sizeof(node));

    if(n == NULL)
    {
        return false;
    }
    strcpy(n->word, word);
    hash_value = hash(word);
    n->next = table(hash_value);
    table(hash_value) = n;
    word_count++;
}
    fclose(file);
    return true
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
