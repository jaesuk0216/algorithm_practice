#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>

#define MAX 100001

int parent[MAX];

typedef struct Edge
{
	int start;
	int end;
	int weight;
}Edge;

typedef struct Graph
{
	int vertex;
	int edge;
	Edge* edges;
}Graph;

int compare(const void* a, const void* b)
{
	Edge A = *(Edge*)a;
	Edge B = *(Edge*)b;

	if (A.weight > B.weight)
		return 1;
	else if (A.weight < B.weight)
		return -1;
	return 0;

}

int set_find(int curr)
{
	if (parent[curr] == -1)
		return curr;
	return set_find(parent[curr]);
}

void set_union(int start, int end)
{
	int root1 = set_find(start);
	int root2 = set_find(end);

	if (root1 < root2)
		parent[root2] = root1;
	else
		parent[root1] = root2;
}

int kruskal(Graph g)
{
	int sum = 0;
	qsort(g.edges, g.edge, sizeof(Edge), compare);
	
	for (int i = 1; i <= g.vertex; i++)
		parent[i] = -1;

	for (int i = 0; i < g.edge; i++)
	{
		Edge e = g.edges[i];
		int uset = set_find(e.start);
		int vset = set_find(e.end);
		if (uset != vset)
		{
			sum += e.weight;
			set_union(uset, vset);
		}
	}
	return sum;
}

int main(void)
{
	int V, E, A, B, C;
	Graph g;

	scanf("%d %d", &V, &E);
	g.vertex = V;
	g.edge = E;
	g.edges = (Edge*)malloc(sizeof(Edge) * E);

	for (int i = 0; i < E; i++)
	{
		scanf("%d %d %d", &A, &B, &C);
		g.edges[i].start = A;
		g.edges[i].end = B;
		g.edges[i].weight = C;
	}
	int sum = kruskal(g);
	printf("%d\n", sum);
	return 0;
}