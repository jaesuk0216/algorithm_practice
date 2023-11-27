//#include<stdio.h>
//#include<stdlib.h>
//
//
//
//#define INF 1000000
//
//#pragma warning(disable:4996)
//
//typedef struct GraphType
//{
//	int n;
//	int weight[102][102];
//}GraphType;
//
//
//int A[102][102];
//void init(GraphType* g, int n)
//{
//
//	g->n = n;
//	for (int i = 1; i <= g->n; i++)
//		for (int j = 1; j <= g->n; j++)
//			g->weight[i][j] = INF;
//
//	for (int i = 1; i <= g->n; i++)
//		g->weight[i][i] = 0;
//}
//
//void floyd(GraphType* g)
//{
//	int i, j, k;
//	for (i = 1; i <= g->n; i++)
//		for (j = 1; j <= g->n; j++)
//			A[i][j] = g->weight[i][j];
//
//	for (k = 1; k <= g->n; k++)
//		for (i = 1; i <= g->n; i++)
//			for (j = 1; j <= g->n; j++)
//				if (A[i][j] > A[i][k] + A[k][j])
//					A[i][j] = A[i][k] + A[k][j];
//
//	for (int i = 1; i <= g->n; i++) {
//		for (int j = 1; j <= g->n; j++)
//			if (A[i][j] == INF) printf("0 ");
//			else printf("%d ", A[i][j]);
//		printf("\n");
//	}
//
//
//
//}
//
//int main()
//{
//	int n, m;
//	int a, b, c;
//	GraphType* g = (GraphType*)malloc(sizeof(GraphType));
//
//	scanf("%d", &n);
//	scanf("%d", &m);
//
//	init(g, n);
//	for (int i = 0; i < m; i++)
//	{
//		scanf("%d %d %d", &a, &b, &c);
//
//		if (g->weight[a][b] > c)
//			g->weight[a][b] = c;
//	}
//	floyd(g);
//
//	return 0;
//}

#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

#define INF 1000000000;
#define MAX 1002

typedef struct Graph
{
	int n;
	int weight[MAX][MAX];
}Graph;

int distance[MAX];
int visited[MAX];

void Dijkstra(Graph* g, int first)
{
	distance[first] = 0;
	int s;
	int min;
	for (int i = 1; i <= g->n; i++)
	{
		min = INF;
		for (int i = 1; i <= g->n; i++)
		{
			if (distance[i] < min && visited[i] == 0)
			{
				min = distance[i];
				s = i;
			}
		}
		visited[s] = 1;
		for (int w = 1; w <= g->n; w++)
		{
			if (g->weight[w][s] != min && distance[w] > distance[s] + g->weight[s][w])
				distance[w] = distance[s] + g->weight[s][w];
		}
	}
}

int main()
{
	int city, bus;
	scanf("%d", &city);
	scanf("%d", &bus);
	Graph* g = (Graph*)malloc(sizeof(Graph));
	g->n = city;
	for (int i = 1; i <= city; i++)
	{
		for (int j = 1; j <= city; j++)
		{
			g->weight[i][j] = INF;
		}
		distance[i] = INF;
		visited[i] = 0;
	}
	int start, end, expense;
	for (int i = 1; i <= bus; i++)
	{
		scanf("%d %d %d", &start, &end, &expense);
		if (g->weight[start][end] > expense)
			g->weight[start][end] = expense;
	}

	int first, last;
	scanf("%d", &first);
	scanf("%d", &last);
	Dijkstra(g, first);
	printf("%d\n", distance[last]);
}
