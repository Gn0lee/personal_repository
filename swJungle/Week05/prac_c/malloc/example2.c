#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    int *pi , i;

    pi = (int *)malloc(5*sizeof(int));

    for(i=0 ; i<5;i++)
    {
        pi[i] = i;
    }

    for(i = 0 ; i <5 ;i++)
    {
        printf("%d\n",*(pi + i));
    }
    free(pi);
    return 0;

}