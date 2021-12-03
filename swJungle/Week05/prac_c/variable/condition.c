#include <stdio.h>

int main(void){
    int x = -50 , y = 30;

    int absX = (x>0) ? x : -x;
    int max = (x>y) ? x : y;
    int min = (x<y) ? x : y;

    printf("x의 절대값은 %d\n",absX);
    printf("x와 y의 최대값은 %d\n",max);
    printf("x와 y의 최소값은 %d\n",min);

    return 0;
}