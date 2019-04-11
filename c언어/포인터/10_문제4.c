// 길이가 6인 int형 배열 arr을 선언하고 1~6으로 초기화 한 후, 배열에 저장된 값의 순서가
// 6, 5, 4, 3, 2, 1이 되도록 변경하는 코드를 작성하라.
// 단, 배열의 앞과 뒤를 가리키는 포인터 변수 2개를 선언해서 이를 활용하여 저장된 값의 순서를 뒤바꿔야 한다.

#include <stdio.h>

int main(void) {
  /* code */
  int arr[6] = {1, 2, 3, 4, 5, 6};
  int *ptr1 = arr;
  int *ptr2 = &arr[5];
  int temp = 0;

  for(int i = 0; i < 3; i++){
    temp = *(ptr2 - i);
    * (ptr2 - i) = * (ptr1 + i);
    *(ptr1 + i) = temp;
  }

  for(int i = 0; i < 6; i++){
    printf("%d", arr[i]);
  }
  return 0;
}
