#include <stdio.h>
#include <stdlib.h>

struct Node
{
    struct Node *next;
    int data;
};


int main(void)
{
    struct Node *head = malloc(sizeof(struct Node));

    struct Node *node1 = malloc(sizeof(struct Node));
    head ->next = node1;
    node1 ->data = 10;

    struct Node *node2 = malloc(sizeof(struct Node));
    node1->next = node2;
    node2 ->data = 20;
    node2->next = NULL;

    struct Node *curr = malloc(sizeof(struct Node));
    curr = node1;
    // curr->data = node1->data;

    while (curr != NULL)
    {
        printf("%d\n",curr->data);
        curr = curr ->next;
    }
    
    free(head);
    free(node1);
    free(node2);

    return 0;
}