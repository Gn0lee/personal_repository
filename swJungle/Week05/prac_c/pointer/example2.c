#include <stdio.h>




int main(void)
{
    int i = 10;
    int *p;
    
    p = &i;

    *p = 20;

    printf("i value : %d\n",i);

    return 0;
}