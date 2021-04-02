#include <iostream>

using namespace std;

// 순열

#if false
int main() 
{
	// 배열 {1, 2, 3}의 순열 만들기
	// 각 순번에 숫자들이 겹치지 않게 선택하기
	// 각 순번마다 들어갈 수 있는 수 (1-3)

	int arr[3] = { 1, 2, 3 };
	int N = 3;
	// 첫번째 숫자 고르기
	for (int i = 0; i < N; i++) // i = 0 - 2
	{
		// 첫번째 숫자 하나 고른상태
		// 두번째 숫자 고르기
		for (int j = 0; j < N; j++)
		{
			// 두번째 숫자까지 고른상태
			// 첫번째 숫자와 두번째 숫자가 같으면, 작업 X
			if (i == j)
			{
				continue;
			}
			// 세번째 숫자 고르기
			for (int k = 0; k < N; k++)
			{
				// 세번째 숫자까지 고른상태
				// 세번째 숫자가 첫번째 숫자와 두번째 숫자 모두 같지 않으경우 선택완료
				if (k == i || k == j)
				{
					continue;
				}

				cout << arr[i] << arr[j] << arr[k] << endl;
			}
		}
	}
}
#endif