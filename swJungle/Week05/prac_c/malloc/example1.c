#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i;
    char *pc;
    
    pc = (char *)malloc(100*sizeof(char));

    for(i=0;i<26;i++)
        *(pc + i) = i + 'a';

    *(pc+i) = 0;

    printf("%s",pc);

    free(pc);
    return 0;
}