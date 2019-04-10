#include <stdio.h>

int main(void){
  int num1 = 10;
  int num2 = 20;
  int * ptr1 = &num1;
  int * ptr2 = &num2;
  int * temp;

  (*ptr1)+=10;
  (*ptr2)-=10;

  temp = ptr1;
  ptr1 = ptr2;
  ptr2 = temp;

  printf("ptr1 : %d ", *ptr1);
  printf("ptr2 : %d\n", *ptr2);

  return 0;
}
