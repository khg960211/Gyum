// 이중 포인터 변수의 활용
// maxPtr에는 가장 큰 값이 저장된 배열 요소의 주소 값이, minPtr에는 가장 작은 값이 저장된 배열 요소의 주소 값이 저장
#include <stdio.h>

void MaxAndMin(int ** mxPtr, int ** mnPtr, int * arr, int size)
{
  int *max, *min;

  max = min = &arr[0];
  for(int i = 0; i < size; i++)
  {
    if(*max < arr[i])
      max = &arr[i];
    if(*min > arr[i])
      min = &arr[i];
  }

  *mxPtr = max;
  *mnPtr = min;
}

int main(void) {
  int * maxPtr;
  int * minPtr;
  int arr[5];

  for (int i = 0; i < 5; i++)
  {
    printf("number%d : ", i + 1);
    scanf("%d", &arr[i]);
  }

  MaxAndMin(&maxPtr, &minPtr, arr, sizeof(arr)/sizeof(int));
  printf("Max: %d, Min: %d\n", *maxPtr, *minPtr);
  return 0;
}
