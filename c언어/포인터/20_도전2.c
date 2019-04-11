// 프로그램 사용자로부터 10진수 형태로 정수를 하나 입력받은 다음, 이를 2진수로 변환해서 출력하는 프로그램을 작성하라.
#include <Stdio.h>

int main(void) {
  int num = 0;
  int idx = 0;
  char arr[30];
  printf("10진수 정수 입력: ");
  scanf("%d\n", &num);

  while(num > 0){
    arr[idx++] = num % 2;
    num = num / 2;
  }
  while(idx > 0){
    printf("%d", arr[--idx]);
  }
  return 0;
}
