#include <stdlib.h>
#include <stdio.h>
typedef char data;

typedef struct _Node
{
    int key;
    struct _Node *left;
    struct _Node *right;   

} Node;

Node *searchNode(Node *root,int x)
{
    Node *p = root;
    
    while(p != NULL)
    {
        if(p->key == x)
            return p;
        else if(p->key < x)
            p = p->right;
        else
            p = p ->left;
    }
    return NULL;

}


Node *addNode(Node *root,int x)
{
    Node *p = root;
    Node *parent = NULL;

    while(p != NULL)
    {
        parent = p;
        if(p->key == x)
        {    
            printf("일치하는 노드가 있습니다.\n");
            return p;
        }
        else if(p->key < x)
            p = p->right;
        else
            p = p ->left;
    }
    
    Node *addnode = (Node *)malloc(sizeof(Node));
    addnode ->left = NULL;
    addnode ->right = NULL;
    addnode ->key = x;
    
    if(parent != NULL)
    {
        if(parent->key > addnode->key)
            parent -> left = addnode;
        
        else
            parent->right = addnode;
    }

    return addnode;

}

Node* deleteNode(Node *root,int x)
{
    Node *p = root;
    Node *parent = NULL;
    
    while((p != NULL) && (p->key != x))
    {
        parent = p;
        
        if(p->key < x)
            p = p->right;
        else
            p = p ->left;
    }

    if(p==NULL){
        printf("찾는 노드가 없습니다.\n");
        return root;
    }

    if(p->left == NULL && p->right == NULL)
    {
        if(parent == NULL){
            root = NULL;
        }
        else{
            if(parent->left == p)
                parent->left = NULL;
            else
                parent->right = NULL;
        }
    }
    else if(p->right == NULL || p->left == NULL){
        Node* child = (p->right != NULL) ? p->right : p->left;
        
        if(parent == NULL){
            root = child;
        }
        else{
            if(parent->left == p)
                parent->left = child;
            else
                parent->right = child;
        }

    }
    else{
        Node* succ_parent = p;
        Node* succ = p ->right;

        while(succ->left != NULL){
            succ_parent = succ;
            succ = succ->left;
        }
        p->key = succ->key;
        if(succ_parent->left == succ){
            succ_parent -> left = succ->right;
        }
        else{
            succ_parent-> right = succ->right;
        }
        p = succ;

    }

    free(p);
    return root;

}
void inorder(Node* root)
{
    if(root == NULL)
        return;

    inorder(root->left);
    printf("%d",root->key);
    inorder(root->right);
}
void postorder(Node* root)
{
    if(root==NULL)
        return;

    postorder(root->left);
    postorder(root->right);
    printf("%d",root->key);
}
void preorder(Node* root)
{
    if(root==NULL)
        return;

    printf("%d",root->key);
    preorder(root->left);
    preorder(root->right);
}


int main(void)
{
    Node* root = addNode(NULL,5);
    addNode(root,2);
    addNode(root,4);
    addNode(root,6);
    addNode(root,1);
    addNode(root,9);
    addNode(root,8);
    addNode(root,3);
    addNode(root,7);

    root = deleteNode(root,2);
    inorder(root);
    // printf("\n");
    // postorder(root);
    // printf("\n");
    
    return 0;
}