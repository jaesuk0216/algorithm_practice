#include<stdio.h>
#include<stdlib.h>

#pragma warning(disable:4996)

#define SWAP(x, y, t) ( (t)=(x), (x)=(y), (y)=(t) )

#define MAX_SIZE 1000000


int sorted[MAX_SIZE];
void merge(int list[], int left, int mid, int right)
{
	int i, j, k, l;
	i = left; j = mid + 1; k = left;
	// 분할 정렬된 list의 합병
	while (i <= mid && j <= right) {
		if (list[i] <= list[j]) sorted[k++] = list[i++];
		else sorted[k++] = list[j++];
	}
	if (i > mid) 	// 남아 있는 레코드의 일괄 복사
		for (l = j; l <= right; l++)
			sorted[k++] = list[l];
	else 	// 남아 있는 레코드의 일괄 복사
		for (l = i; l <= mid; l++)
			sorted[k++] = list[l];
	// 배열 sorted[]의 리스트를 배열 list[]로 복사
	for (l = left; l <= right; l++)
		list[l] = sorted[l];
}

void merge_sort(int list[], int left, int right)
{
	int mid;
	if (left < right)
	{
		mid = (left + right) / 2;              // 리스트의 균등분할
		merge_sort(list, left, mid);     // 부분리스트 정렬
		merge_sort(list, mid + 1, right);//부분리스트 정렬
		merge(list, left, mid, right);    // 합병
	}
}




int main(void)
{
	int size;
	int num;

	scanf("%d", &size);

	int* list = (int*)malloc(sizeof(int) * size);


	for (int i = 0; i < size; i++)
	{
		scanf("%d", &num);
		list[i] = num;
	}

	merge_sort(list, 0, size - 1);
	for (int i = 0; i < size; i++)
	{
		printf("%d\n", list[i]);
	}
	
}
