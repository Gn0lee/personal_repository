#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct book
{
    char name[50];
    int number;
};

void showbook(struct book *p,int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        printf("번호 %d 의 책이름은 %s입니다.\n",(p+i)->number,(p+i)->name);
    }
}

int main(void)
{
    struct book *p;

    p = (struct book*)malloc(2*sizeof(struct book));

    p->number = 1;
    strcpy(p->name,"orange");
    (p+1) -> number = 2;
    strcpy((p+1)->name,"namoo");

    showbook(p,2);
    free(p);
    return 0;
}