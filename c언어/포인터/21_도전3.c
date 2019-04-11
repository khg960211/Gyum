// 길이가 10인 배열을 선언하고 총 10개의 정수를 입력 받는다.
// 단, 입력 받은 숫자가 홀수이면 배열의 앞에서부터 채워나가고, 짝수이면 뒤에서부터 채워나가는 형식을 취하기로 하자.
// 따라서 사용자가 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]을 입력했다면
// 배열에는 [1, 3, 5, 7, 9, 10, 8, 6, 4, 2]의 순으로 저장 되어야 한다.

#include <stdio.h>

int main(void) {
  int arr[10];
  int * ptr1 = arr;
  int * ptr2 = &arr[9];
  int len = sizeof(arr) / sizeof(int);

  for(int i = 0; i < len; i++){
    int num = 0;
    printf("입력: ");
    scanf("%d \n", &num);

    if (num % 2 != 0){
      *(ptr1++) = num;
    }
    else{
      *(ptr2--) = num;
    }

    for(int i = 0; i < len; i++)
      printf("%d ", arr[i]);
  }

  return 0;
}

// 해답
// int main(void)
// {
// 	int arr[10];
// 	int front=0, back=9;
// 	int num, i;
//
// 	printf("총 10개의 숫자 입력 \n");
// 	for(i=0; i<10; i++)
// 	{
// 		printf("입력: ");
// 		scanf("%d", &num);
// 		if(num%2==1)
// 			arr[front++]=num;
// 		else
// 			arr[back--]=num;
// 	}
//
// 	printf("배열 요소의 출력 : ");
// 	for(i=0; i<10; i++)
// 		printf("%d ", arr[i]);
//
// 	return 0;
// }
