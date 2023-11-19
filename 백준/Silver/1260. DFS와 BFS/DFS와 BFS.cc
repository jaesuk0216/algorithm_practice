#include<stdio.h>
#include<stdlib.h>
#include <queue>
#include<limits.h>
using namespace std;
#define MAX_VERTICES 1001
#define TRUE 1
#define FALSE 0


typedef struct GraphType
{
	int n;
	int adj_mat[MAX_VERTICES][MAX_VERTICES];
}GraphType;

int bvisited[MAX_VERTICES];
int dvisited[MAX_VERTICES];



void init(GraphType* g)
{
	int r, c;
	g->n = 0;
	for (r = 0; r < MAX_VERTICES; r++)
		for (c = 0; c < MAX_VERTICES; c++)
		{
			g->adj_mat[r][c] = 0;
		}
}

void insert_vertex(GraphType* g, int v)
{
	if (((g->n) + 1) > MAX_VERTICES)
	{
		return;
	}
	g->n++;
}

void insert_edge(GraphType* g, int start, int end)
{
	if (start > g->n || end > g->n)
	{
		return;
	}
	g->adj_mat[start][end] = 1;
	g->adj_mat[end][start] = 1;
}

void dfs_mat(GraphType* g, int v)
{
	int w;
	dvisited[v] = TRUE;
	printf("%d ", v);
	for (w = 0; w <= g->n; w++)
		if (g->adj_mat[v][w] && !dvisited[w])
			dfs_mat(g, w);
}

void bfs_mat(GraphType* g, int v)
{
	queue<int> q;
	q.push(v);
	int w;
	bvisited[v] = TRUE;
	printf("%d ", v);
	while (!q.empty())
	{
		v = q.front();
		q.pop();
		for (w = 0; w <= g->n; w++)
			if (g->adj_mat[v][w] && !bvisited[w])
			{
				bvisited[w] = TRUE;
				printf("%d ", w);
				q.push(w);
			}
	}
}

int main()
{
	int vertex, edge, start;
	int n1, n2;
	GraphType* g;
	g = (GraphType*)malloc(sizeof(GraphType));
	init(g);
	scanf("%d %d %d", &vertex, &edge, &start);
	for (int i = 0; i < vertex; i++)
	{
		insert_vertex(g, vertex);
	}
	for (int i = 0; i < edge; i++)
	{
		scanf("%d %d", &n1, &n2);
		insert_edge(g, n1, n2);
	}

	dfs_mat(g, start);
	printf("\n");
	bfs_mat(g, start);
	return 0;

}
