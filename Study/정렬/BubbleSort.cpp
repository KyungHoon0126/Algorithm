#include <stdio.h>

// BubbleSort(버블 정렬) : 효율성이 가장 떨어지는 정렬, 옆에 있는 값과 비교해서 더 작은 값을 앞으로 반복적으로 보내는 방법.

int main(void) {

	// i, j : 반복, temp : 서로 다른 위치에 존재하는 두 개의 원소를 바꾸기 위한 용도
	
	int i, j, temp;
	int array[10] = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };

	for (i = 0; i < 10; i++) {
		for (j = 0; j < 9 - i; j++) {
			if (array[j] > array[j + 1]) {
				temp = array[j];
				array[j] = array[j + 1];
				array[j + 1] = temp;
			}
		}
	}

	for (i = 0; i < 10; i++) {
		printf("%d ", array[i]);
	}

	return 0;
}