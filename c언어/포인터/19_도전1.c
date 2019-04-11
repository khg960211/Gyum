// 길이가 10인 배열을 선언하고 총 10개의 정수를 입력받아서, 홀수와 짝수를 구분 지어 출력하는 프로그램을 작성하라.
// 일단 홀수 부터 출력하고 짝수를 출력하도록 하자.
// 단, 10개의 정수를 main 함수 내에서 입력 받도록 하고, 배열 내에 존재하는 홀수만 출력하는 함수와
// 배열 내에 존재하는 짝수만 출력하는 함수를 각각 정의해서 이 두 함수를 호출하는 방식으로 프로그램을 완성하자.

#include <stdio.h>

void OddNum(int param[], int len)
{
  printf("홀수 출력: ");
  for(int i = 0; i < len; i++){
    if(param[i] % 2 != 0)
      printf("%d, ", param[i]);
  }
  printf("\n");
}

void EvenNum(int param[], int len)
{
  printf("짝수 출력: ");
  for(int i = 0; i < len; i++){
    if(param[i] % 2 == 0)
      printf("%d, ", param[i]);
  }
  printf("\n");
}

int main(void)
{
  int arr[10];
  for (int i = 0; i < 10; i++){
    printf("입력: ");
    scanf("%d\n", &arr[i]);
  }

  OddNum(arr, sizeof(arr) / sizeof(int));
  EvenNum(arr, sizeof(arr) / sizeof(int));

  return 0;
}
