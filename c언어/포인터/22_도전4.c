// 팔린드롬은 앞으로 읽으나 뒤로 읽으나 차이가 없는 단어를 뜻한다.
// 인자로 전달되는 영단어가 회문인지 아닌지를 판단해서 그 결과를 출력하는 기능의 함수를 정의하고
// 이에 적절한 main 함수를 정의해 보고자 한다.

#include <stdio.h>
#include <string.h>

void isPalindrome(char * arr){
  int len = strlen(arr);

  for (int i = 0; i < len/2; i++){
    if(arr[i] != arr[len - i - 1]){
      printf("회문이 아닙니다.");
      return;
    }
  }
  printf("회문입니다.");
}

int main(void) {
  char arr[30];
  printf("문자열 입력: ");
  scanf("%s\n", arr);

  isPalindrome(arr);
  return 0;
}
