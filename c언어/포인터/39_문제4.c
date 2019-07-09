// 다음 예제의 출력결과는 무엇인가? 예제를 실행하지 않고 답을 해야 한다.
int main(void) {
  int arr[3][2]={{1, 2}, {3, 4}, {5, 6}};
  printf("%d %d \n", arr[1][0], arr[0][1]);
  printf("%d %d \n", *(arr[2]+1), *(arr[1]+1));
  printf("%d %d \n", (*(arr+2))[0], (*(arr+0))[1]);
  printf("%d %d \n", **arr, *(*(arr+0)+0));
  return 0;
}
