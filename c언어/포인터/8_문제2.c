// 문제1에서는 ptr에 저장된 값을 변경시켜가면서 배열 요소에 접근하라고 했다.
// 이번에는 ptr에 저장된 값을 변경시키지 않고, ptr을 대상으로 덧셈연산을 하여
// 그 결과로 반환되는 주소 값을 통해서 모든 배열요소에 접근하여 값을 2씩 증가시키는 코드를 작성하라.

#include <stdio.h>

int main(void){
  int arr[5] = {1, 2, 3, 4, 5};
  int * ptr = arr;

  for(int i = 0; i < 5; i++){
    arr[i] = *(ptr + i) + 2;

  }

  for (int i = 0; i < 5; i++){
    printf("%d ", arr[i]);
  }

  return 0;
}
