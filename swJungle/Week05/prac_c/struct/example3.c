#include <stdio.h>
#define size 3

struct student {
    int number;
    char name[20];
    double grade;
};

int main(void)
{
    struct student list[size];

    int i;
    for(i=0 ; i <size ; i++)
    {
        printf("id : ");
        scanf("%d",&list[i].number);
        
        printf("name : ");
        scanf("%s",list[i].name);
        
        printf("grade : ");
        scanf("%lf",&list[i].grade);
    }

    for(i=0;i<size;i++)
    {
        printf("학번: %d 이름: %s 학점: %.2f ",list[i].number,list[i].name,list[i].grade);
    }

    return 0;
}