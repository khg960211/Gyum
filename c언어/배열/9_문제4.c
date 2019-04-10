// 영단어 입력받아 char형 배열에 저장하고 저장된 영단어를 역순으로 뒤집는다. 널 문자의 위치를 변경해서는 안된다.
#include <stdio.h>

int main(void) {
  /* code */
  char word[50];
  int len = 0;
  char temp;

  printf("영단어 입력 : ");
  scanf("%s", word);

  // 단어 길이 계산
  while(word[len] != 0){
    len++;
  }
  // 역순으로 뒤집기
  for(int i=0; i < len / 2; i++){
    temp = word[i];
    word[i] = word[(len - i)-1];
    word[(len - i)-1] = temp;
  }

  printf("%s\n", word);
  return 0;
}
