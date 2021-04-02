#include <iostream>
#include <vector>
#include <time.h>

// 주어진 배열 A에서 가장 많이 등장하는 숫자를 반환한다.
// 만약 두 가지 이상 있을 경우 아무것이나 반환한다.

int majority1(const std::vector<int>& A)
{
	/*
		수행 시간 측정 시작
	*/
	/*time_t start, end;
	double result;
	start = + time(NULL);*/


	int N = A.size(); // 배열 길이
	int majority = -1, majorityCount = 0;
	for (size_t i = 0; i < N; i++)
	{
		int V = A[i], count = 0;
		for (size_t j = 0; j < N; ++j)
		{
			if (A[j] == V)
			{
				++count;
			}
		}

		if (count > majorityCount)
		{
			majorityCount = count; // 배열의 값을 돌면서 그 수가 다른 숫자보다 많아지면 바꾼다.
			majority = V; // 그리고 수가 가장 많기 때문에 이수에 더해준다.
		}
	}

	/*
		시간 측정 끝
	*/
	/*end = time(NULL);
	result = (double)(end - start);
	printf("수행시간 : %f", result);*/

	return majority;
}

// A의 각 원소가 0부터 100 사이의 값일 경우 가장 많이 등장하는 숫자를 반환한다.
#if false
int majority2(const std::vector<int>& A)
{
	int N = A.size();
	std::vector<int> count(101, 0);

	for (size_t i = 0; i <= 100; ++i)
	{
		count[A[i]]++;
	}

	int majority = 0;

	for (size_t i = 0; i <= 100; ++i)
	{
		if (count[i] > count[majority])
		{
			majority = i;
		}
	}

	return majority;
}
#endif // false

int main()
{
	// vector : 배열
	std::vector<int> array = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
							  2, 6, 7, 8, 5, 6, 2, 6, 7, 4,
							  5, 7, 8, 5, 3, 5, 4, 6, 4, 6,
							  2, 1, 34, 5, 6, 5, 2, 4 , 6 };

	std::cout << majority1(array) << std::endl;
} 