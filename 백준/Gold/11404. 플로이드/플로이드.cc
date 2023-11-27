#include<stdio.h>
#include<stdlib.h>
#pragma warning(disable:4996)
#define MAX 101
#define INF 10000000

typedef struct Graph
{
	int n;
	int weight[MAX][MAX];
}Graph;

int A[MAX][MAX];

void print_graph(Graph* g)
{
	for (int i = 1; i <= g->n; i++)
	{
		for (int j = 1; j <= g->n; j++)
		{
			if (g->weight[i][j] == INF)
				printf("0 ");
			else
				printf("%d ", g->weight[i][j]);
		}
		printf("\n");
	}
}

void Floyd(Graph* g)
{
	for (int w = 1; w <= g->n; w++)
	{
		for (int i = 1; i <= g->n; i++)
		{
			for (int j = 1; j <= g->n; j++)
			{
				if (i != j && g->weight[i][w] + g->weight[w][j] < g->weight[i][j])
					g->weight[i][j] = g->weight[i][w] + g->weight[w][j];
			}
		}
	}
	print_graph(g);
}

int main()
{
	int city;
	int bus;
	scanf("%d", &city);
	scanf("%d", &bus);
	Graph* g = (Graph*)malloc(sizeof(Graph));
	g->n = city;

	for (int i = 1; i <= g->n; i++)
	{
		for (int j = 1; j <= g->n; j++)
		{
			g->weight[i][j] = INF;
		}
	}
	int start, end, expense;
	for (int i = 1; i <= bus; i++)
	{
		scanf("%d %d %d", &start, &end, &expense);
		if (g->weight[start][end] > expense)
			g->weight[start][end] = expense;
	}
	Floyd(g);
}