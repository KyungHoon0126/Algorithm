#include <stdio.h>

// Selection Sort : ���� ����, ��ȿ������ �˰���

int main(void) {

	// i, j : �迭�� �ִ� ���� Ž��, min : �ּڰ�, inex : ���� ���� ���� ��ġ, temp :  Ư���� �� ���ڸ� �ٲٱ� ���� ���.

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

