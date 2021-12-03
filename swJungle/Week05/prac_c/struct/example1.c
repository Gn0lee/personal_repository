#include <stdio.h>

struct student
{
    int number;
    char name[10];
    double grade;
};


int main(void)
{
    struct student s ;
    printf("id number : ");
    scanf("%d",&s.number);
    
    printf("name : ");
    scanf("%s",s.name);
    
    printf("grade : ");
    scanf("%lf",&s.grade);

    printf("학번 : %d\n",s.number);
    printf("이름 : %s\n",s.name);
    printf("학점 : %.1f\n",s.grade);

    return 0;
}