#include <iostream>

using namespace std;

void selectionSort(int arr[], int size)
{
	for (int j = 0; j < size - 1; j++)
	{
		// 배열순회하면서, 가장 작은 숫자 찾기
		// 찾은 숫자를 제일 앞쪽 인덱스와 교환
		// 최솟값의 위치, 최소값을 저장할 변수 필요

		int minV; // 최소값을 저장할 변수
		int minP; // 최소값의 위치를 저장할 변수

		// ★ 변수초기화 할때 값은, 항상 이유가 있어야한다. ★
		// 임의의 값을 초기화하면 문제가 생길 수도 있다.
		minV = arr[j]; // 값
		minP = j; // 위치  


		for (int i = j + 1; i < size; i++)
		{
			// 최솟값 찾기
			// 최솟값과 배열의 값 요소 비교
			if (minV > arr[i])
			{
				minV = arr[i]; // 최소값 교체
				minP = i; // 최소값 위치 교체
			}
		}

		// 최소값 위치 찾았으니, 제일 앞자리와 자리 교환
		int temp = arr[j]; // arr[0] 에서 한자리씩 완성되면 arr[1]이 확정되어야 하므로 j를 넣어준다.
		arr[j] = minV;
		arr[minP] = temp;
	}

	for (int i = 0; i < size; i++)
	{
		cout << arr[i] << " ";
	}

	cout << endl;
}

#if false
int main()
{
	int arr[10] = { 10,1,4,5,3,7,2,6,8,9 };
	int size = 10;
	selectionSort(arr, size);
}
#endif
