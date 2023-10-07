#include <stdio.h>
#include <stdlib.h>
#define SIZE 100000

typedef struct Tree
{
	int data;
	struct Tree* left;
	struct Tree* right;
}Tree;

Tree* alloc_new_node(int data)
{
	Tree* tree = (Tree*)malloc(sizeof(tree));
	tree->data = data;
	tree->right = NULL;
	tree->left = NULL;

	return tree;

}

void insert_tree(Tree* root, int data)
{

	if (root->data > data)
	{
		if (root->left == NULL)
		{
			root->left = alloc_new_node(data);
		}
		else
		{
			insert_tree(root->left, data);
		}

	}
	else if (root->data < data)
	{
		if (root->right == NULL)
		{
			root->right = alloc_new_node(data);
		}
		else
		{
			insert_tree(root->right, data);
		}

	}
}


void print_tree(Tree* tree)
{
	if (tree == NULL)
	{
		return;
	}
	print_tree(tree->left);
	print_tree(tree->right);
	printf("%d\n", tree->data);
}


int main()
{
	int data;
	scanf("%d", &data);
	Tree* tree = alloc_new_node(data);
	while (scanf("%d", &data) != EOF)
	{
		insert_tree(tree, data);
	}
	print_tree(tree);
	return 0;
}