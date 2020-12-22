#include <stdio.h>

// Selection Sort : 선택 정렬, 비효율적인 알고리즘

int main(void) {

	// i, j : 배열에 있는 원소 탐색, min : 최솟값, inex : 가장 작은 원소 위치, temp :  특정한 두 숫자를 바꾸기 위해 사용.

	int i, j, min, index, temp;
	int array[20] = { 1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11 };

	for (i = 0; i < 20; i++) {
		min = 9999;
		for (j = i; j < 20; j++) {
			if (min > array[j]) {
				min = array[j];
				index = j;
			}
		}
		temp = array[i];
		array[i] = array[index];
		array[index] = temp;
	}
	for (i = 0; i < 20; i++) {
		printf("%d ", array[i]);
	}
	return 0;
}

