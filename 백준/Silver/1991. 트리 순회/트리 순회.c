#include <stdio.h>
#include <stdlib.h>


typedef struct TreeNode {
    char data;
    struct TreeNode* left, * right;
}TreeNode;



TreeNode* allocNewNode(char data)
{
    TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
    node->data = data;
    node->left = NULL;
    node->right = NULL;

    return node;
}

void insertNode(TreeNode* root, char data, char left, char right)
{
    if (root == NULL)
    {
        return;
    }
    if (root->data == data)
    {
        if (left != '.')
        {
            root->left = allocNewNode(left);
        }
        if (right != '.')
        {
            root->right = allocNewNode(right);
        }
    }
    else
    {
        insertNode(root->left, data, left, right);
        insertNode(root->right, data, left, right);
    }

}

void pre_order_recursive(TreeNode* root)
{
    if (root == NULL)
    {
        return;
    }
    printf("%c", root->data);
    pre_order_recursive(root->left);
    pre_order_recursive(root->right);
}

void in_order_recursive(TreeNode* root)
{
    if (root == NULL)
    {
        return;
    }
    in_order_recursive(root->left);
    printf("%c", root->data);
    in_order_recursive(root->right);
}

void post_order_recursive(TreeNode* root)
{
    if (root == NULL)
    {
        return;
    }
    post_order_recursive(root->left);
    post_order_recursive(root->right);
    printf("%c", root->data);
}


int main()
{
    int cnt;
    char data;
    char left;
    char right;
    TreeNode* root = allocNewNode('A');
    scanf("%d", &cnt);



    for (int i = 0; i < cnt; i++)
    {
        scanf(" %c %c %c", &data, &left, &right);
        insertNode(root, data, left, right);
    }
    pre_order_recursive(root);
    printf("\n");
    in_order_recursive(root);
    printf("\n");
    post_order_recursive(root);


}