#include <stdio.h>
#include <stdlib.h>
#define MAX_ELEMENT 100001

typedef struct
{
	int heap[MAX_ELEMENT];
	int heap_size;
}HeapType;

HeapType* create()
{
	return (HeapType*)malloc(sizeof(HeapType));
}

void init(HeapType* h)
{
	h->heap_size = 0;
}

void insert_heap(HeapType*h, int item)
{
	int i;
	i = ++(h->heap_size);
	while (i != 1 && item > h->heap[i / 2])
	{
		h->heap[i] = h->heap[i / 2];
		i /= 2;
	}
	h->heap[i] = item;
}



int delete_heap(HeapType* h)
{
	int parent, child;
	int item,temp;

	item = h->heap[1];
	temp = h->heap[(h->heap_size)--];
	parent = 1;
	child = 2;
	while (child <= h->heap_size)
	{
		if (child < h->heap_size && h->heap[child] < h->heap[child + 1])
			child++;
		if (temp >= h->heap[child]) break;
		
		h->heap[parent] = h->heap[child];
		parent = child;
		child *= 2;
	}
	h->heap[parent] = temp;
	return item;
}


int main(void)
{
	HeapType* heap;
	heap = create();
	init(heap);

	int cnt;
	int num;
	scanf("%d", &cnt);
	for (int i = 0; i < cnt; i++)
	{
		scanf("%d", &num);
		if (num == 0)
		{
			if (heap->heap_size == 0)
				printf("0\n");
			else
				printf("%d\n", delete_heap(heap));
		}
		else
		{
			insert_heap(heap, num);
		}
	}
	return 0;
}