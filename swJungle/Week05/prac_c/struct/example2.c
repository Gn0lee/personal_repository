#include <stdio.h>
#include <math.h>

struct point
{
    int x;
    int y;
};


int main(void)
{
    struct point p1;
    struct point p2;

    double distance;
    int xdiff;
    int ydiff;

    printf("p1의 좌표를 입력하세요: ");
    scanf("%d %d",&p1.x,&p1.y);
    
    printf("p2의 좌표를 입력하세요: ");
    scanf("%d %d",&p2.x,&p2.y);

    xdiff = p1.x - p2.x;
    ydiff = p1.y - p2.y;

    distance = sqrt(xdiff*xdiff + ydiff*ydiff);

    printf("두 점사이의 거리는 %.2f 입니다.",distance);    
    

    
    return 0;

}