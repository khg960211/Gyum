#include <stdio.h>
// char�� 1���� �迭�� ����� ���ÿ� Good time���� �ʱ�ȭ �ϰ� �ʱ�ȭ ���Ŀ��� ����� ������ ����ϴ� ����

int main(void) {
  char arr[] = "Good time";
  int length = sizeof(arr) / sizeof(char);
  int i;

  for(i=0; i<length; i++){
    printf("%c", arr[i]);
  }
  printf("\n");

  return 0;
}
