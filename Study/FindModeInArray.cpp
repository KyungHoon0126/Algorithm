#include <iostream>
#include <vector>
#include <time.h>

// �־��� �迭 A���� ���� ���� �����ϴ� ���ڸ� ��ȯ�Ѵ�.
// ���� �� ���� �̻� ���� ��� �ƹ����̳� ��ȯ�Ѵ�.

int majority1(const std::vector<int>& A)
{
	/*
		���� �ð� ���� ����
	*/
	/*time_t start, end;
	double result;
	start = + time(NULL);*/


	int N = A.size(); // �迭 ����
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
			majorityCount = count; // �迭�� ���� ���鼭 �� ���� �ٸ� ���ں��� �������� �ٲ۴�.
			majority = V; // �׸��� ���� ���� ���� ������ �̼��� �����ش�.
		}
	}

	/*
		�ð� ���� ��
	*/
	/*end = time(NULL);
	result = (double)(end - start);
	printf("����ð� : %f", result);*/

	return majority;
}

// A�� �� ���Ұ� 0���� 100 ������ ���� ��� ���� ���� �����ϴ� ���ڸ� ��ȯ�Ѵ�.
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
	// vector : �迭
	std::vector<int> array = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
							  2, 6, 7, 8, 5, 6, 2, 6, 7, 4,
							  5, 7, 8, 5, 3, 5, 4, 6, 4, 6,
							  2, 1, 34, 5, 6, 5, 2, 4 , 6 };

	std::cout << majority1(array) << std::endl;
} 