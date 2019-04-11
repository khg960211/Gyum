// 변수 num에 저장된 값의 제곱을 계산하는 함수를 정의하고, 이를 호출하는 main 함수를 작성해보자.
// 단, 여기서는 Call-By-Value 기반의 SquareByValue 함수와 Call-By-Reference 기반의 SquareByReference 함수 2가지를 정의한다.
// SquareByValue 함수는 인자로 전달된 값의 제곱을 반환해야 하며
// SquareByReference 함수는 정수가 저장되어 있는 변수의 주소 값을 인자로 받아서 해당 변수에 저장된 값의 제곱을 그 변수에 다시 저장해야 한다.

#include <stdio.h>

int SquareByValue(int n)
{
  return n * n;
}

void SquareByReference(int * ptr)
{
  int n = *ptr;
  *ptr = n * n;
}

int main(void) {
  int num = 10;
  printf("%d \n", SquareByValue(num));
  SquareByReference(&num);
  printf("%d \n", num);
  return 0;
}
