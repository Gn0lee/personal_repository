#include <stdio.h>

int hour;
int minute;
int minuteAdd;

void counter(){

    minute += minuteAdd;
    hour += minute / 60;
    minute %= 60;
    hour %= 24;

}




int main(void){

    printf("type hour: ");
    scanf("%d",&hour);
    printf("type minute: ");
    scanf("%d",&minute);
    printf("type minuteAdd: ");
    scanf("%d",&minuteAdd);

    counter();

    printf("now is %d:%d",hour,minute);
    

    return 0;
}