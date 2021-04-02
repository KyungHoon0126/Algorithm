#include <iostream>

using namespace std;

void selectionSort(int arr[], int size)
{
	for (int j = 0; j < size - 1; j++)
	{
		// �迭��ȸ�ϸ鼭, ���� ���� ���� ã��
		// ã�� ���ڸ� ���� ���� �ε����� ��ȯ
		// �ּڰ��� ��ġ, �ּҰ��� ������ ���� �ʿ�

		int minV; // �ּҰ��� ������ ����
		int minP; // �ּҰ��� ��ġ�� ������ ����

		// �� �����ʱ�ȭ �Ҷ� ����, �׻� ������ �־���Ѵ�. ��
		// ������ ���� �ʱ�ȭ�ϸ� ������ ���� ���� �ִ�.
		minV = arr[j]; // ��
		minP = j; // ��ġ  


		for (int i = j + 1; i < size; i++)
		{
			// �ּڰ� ã��
			// �ּڰ��� �迭�� �� ��� ��
			if (minV > arr[i])
			{
				minV = arr[i]; // �ּҰ� ��ü
				minP = i; // �ּҰ� ��ġ ��ü
			}
		}

		// �ּҰ� ��ġ ã������, ���� ���ڸ��� �ڸ� ��ȯ
		int temp = arr[j]; // arr[0] ���� ���ڸ��� �ϼ��Ǹ� arr[1]�� Ȯ���Ǿ�� �ϹǷ� j�� �־��ش�.
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
