// 길이가 5인 int형 배열 arr을 선언하고 이를 1~5로 선언한 뒤, 배열의 마지막 요소를 가리키는 포인터 변수 ptr을 선언한다.
// 그 다음 ptr에 저장된 값을 감소시키는 형태의 연산을 기반으로 모든 배열 요소에 접근하여
// 배열에 저장된 모든 정수를 더하여 그 결과를 출력하는 코드를 작성하라.

#include <stdio.h>

int main(void) {
  /* code */
  int arr[5] = {1, 2, 3, 4, 5};
  int * ptr = &arr[4];
  int sum = 0;

  for(int i = 0; i < 5; i++){
    sum = sum + *(ptr - i);
  }

  printf("%d\n", sum);
  return 0;
}
