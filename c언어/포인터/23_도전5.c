// 배열에 저장되어 있는 요소들을 내림차순으로 정렬하는 함수를 정의하자.
// 그리고 이 함수를 호출하는 예제를 작성해보자.
// 길이가 7인 int형 배열을 선언해서 7개의 정수를 입력받고 내림차순으로 정렬하고 출력하라.

#include <stdio.h>

void DesSort(int arr[], int len) {
  int temp;

  for(int i = 0; i < len - 1; i++)
  {
    for(int j = 0; j < (len - i) - 1; j++)
    {
      if(arr[j] < arr[j+1])
      {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

int main(void) {
  int arr[7];
  for (int i = 0; i < 7; i++){
    printf("입력 : ");
    scanf("%d\n", &arr[i]);
  }

  DesSort(arr, sizeof(arr) / sizeof(int));

  for (int i = 0; i < 7; i++)
    printf("%d ", arr[i]);

  return 0;
}
