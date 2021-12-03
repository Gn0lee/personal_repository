#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i ,y,x;
    int** pptr;

    pptr = (int**)malloc(8*sizeof(int*));

    for(i=0;i<8;i++)
    {
        *(pptr+i) = (int*)malloc(6*sizeof(int));
    }
    for(y=0;y<8;y++)
    {
        for(x=0;x<6;x++)
        {
            *(*(pptr+y)+x) = 6*y+x;
        }
    }
    for(y=0;y<8;y++)
    {
        for(x=0;x<6;x++)
        {
            printf("%3d",*(*(pptr+y)+x));
        }
        printf("\n");
    }

    for(y=0;y<8;y++)
    {
        free(*(pptr+y));
    }
    // free(pptr);

    return 0;
}