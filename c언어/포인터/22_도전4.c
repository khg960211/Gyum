// �ȸ������ ������ ������ �ڷ� ������ ���̰� ���� �ܾ ���Ѵ�.
// ���ڷ� ���޵Ǵ� ���ܾ ȸ������ �ƴ����� �Ǵ��ؼ� �� ����� ����ϴ� ����� �Լ��� �����ϰ�
// �̿� ������ main �Լ��� ������ ������ �Ѵ�.

#include <stdio.h>
#include <string.h>

void isPalindrome(char * arr){
  int len = strlen(arr);

  for (int i = 0; i < len/2; i++){
    if(arr[i] != arr[len - i - 1]){
      printf("ȸ���� �ƴմϴ�.");
      return;
    }
  }
  printf("ȸ���Դϴ�.");
}

int main(void) {
  char arr[30];
  printf("���ڿ� �Է�: ");
  scanf("%s\n", arr);

  isPalindrome(arr);
  return 0;
}
