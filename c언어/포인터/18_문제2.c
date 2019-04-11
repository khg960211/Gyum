// 세 변수에 저장된 값을 서로 뒤바꾸는 함수를 정의하라.

#include <stdio.h>
void Swap(int *ptr1, int *ptr2, int *ptr3)
{
  int temp;
  temp = *ptr1;
  *ptr1 = *ptr2;
  *ptr2 = *ptr3;
  *ptr3 = temp;
}

int main(void)
{
  int num1 = 1, num2 = 2, num3 = 3;
  Swap(&num1, &num2, &num3);
  printf("num1: %d, num2: %d, num3: %d \n", num1, num2, num3);
  return 0;
}
