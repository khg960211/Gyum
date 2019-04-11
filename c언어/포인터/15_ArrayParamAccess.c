#include <stdio.h>

void ShowArrayElem(int * param, int len)
{
  int i;
  for(i = 0; i< len; i++)
    printf("%d ", param[i]);
  printf("\n");
}

void AddArrayElem(int * param, int len, int add)
{
  int i;
  for(i = 0; i < len; i++)
    param[i] += add;
}

int main(void)
{
  int arr1[3] = {1, 2, 3};
  AddArrayElem(arr1, sizeof(arr1) / sizeof(int), 1);
  ShowArrayElem(arr1, sizeof(arr1) / sizeof(int));

  AddArrayElem(arr1, sizeof(arr1) / sizeof(int), 2);
  ShowArrayElem(arr1, sizeof(arr1) / sizeof(int));

  AddArrayElem(arr1, sizeof(arr1) / sizeof(int), 3);
  ShowArrayElem(arr1, sizeof(arr1) / sizeof(int));
  return 0;
}

// 참고 : void ShowArrayElem(int param[], int len) 형태로 주소 값을 넘기는 것도 가능하다. 완전히 동일한 선언이다.
// 참고2 : 함수 내에서는 인자로 전달 된 배열의 크기나 길이를 계산할 수 없기 때문에, 길이를 미리 계산하여 인자로 전달한다.
// 함수 내부에서 sizeof로 계산할 경우, 포인터 변수의 크기가 저장된다.
