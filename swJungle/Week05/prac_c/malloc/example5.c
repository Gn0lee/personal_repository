#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    int i,y,x,n,m;
    printf("input row: ");
    scanf("%d",&n);
    printf("input col: ");
    scanf("%d",&m);

    int** pptr = (int**)malloc(n*sizeof(int*));

    for(i=0;i<n;i++)
    {
        *(pptr+i) = (int *)malloc(m*sizeof(int));
    }

    for(y=0;y<n;y++)
    {
        for(x=0;x<m;x++)
        {
            *(*(pptr + y) + x) = m * y + 1 + x;
        }
    }
    for(y=0;y<n;y++)
    {
        for(x=0;x<m;x++)
        {
            printf("%4d",*(*(pptr+y)+x));
        }
        printf("\n");
    }
    
    for(y=0;y<n;y++)
    {
        free(*(pptr+y));
    }

    return 0;
}