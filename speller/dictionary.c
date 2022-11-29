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

int WordCount = 0;
// TODO: Choose number of buckets in hash table
const unsigned int N = 26;


// Hash table
node *table[N];
int n_size = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int key = hash(word);
    node* F = table[key];

    while(F != NULL)
    {
        if(strcasecmp(F->word, word) == 0)
        {
            return true;
        }
        F = F->next;
    }

    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int value = 0;

    for(int i = 0; word[i] !='\0'; i++)
    {
        value += tolower(word[i]);
    }
    return value % N;

}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    // TODO
    FILE* F = fopen(dictionary, "r");
    if (F == NULL)
    {
        return false;
    }
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    char tempWord[LENGTH + 1];

    while(fscanf(F, "%s\n", tempWord) != EOF)
    {
        node* tempNode = malloc(sizeof(node));

        strcpy(tempNode->word, tempWord);
        int key = hash(tempWord);

        if (table[key] == NULL)
        {
            tempNode->next = NULL;
            table[key] = tempNode;
        }
        else
        {
            tempNode->next = table[key];
            table[key] = tempNode;
        }
        WordCount++;
    }
    fclose(F);
    return true;

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return WordCount++;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
   {
            node *F = table[i];
            while (F != NULL)
            {
                
            }

            node *dlt = NULL;

            temp = table[i];


            {
                dlt = temp;
                temp = temp->next;
                free(dlt);
            }
        }
        return true;
    }
