#include <stdio.h>
#include <stdlib.h>

typedef char data;

typedef struct _Node
{
    int key;
    struct _Node *left;
    struct _Node *right;

}Node;

Node* searchNode(Node* root, char x)
{
    Node* p = root;

    while(p != NULL)
    {
        if(p->key == x)
            return p;
        else if (p->key > x)
            p = p->left;
        else
            p = p->right;

    }
    return NULL;
}

Node* addNode(Node* root, char x)
{
    Node* p = root;
    Node* parent = NULL;
    
    while(p != NULL)
    {
        parent = p;
        if(p->key == x){
            printf("이미 존재하는 노드입니다.\n");
            return p;
        }
        else if (p->key > x)
            p = p->left;
        else
            p = p->right;

    }
    
    Node* addnode = (Node*)malloc(sizeof(Node));
    addnode -> key = x;
    addnode -> left = NULL;
    addnode -> right = NULL;
    
    if(parent != NULL)
    {
        if(parent->key > x)
            parent->left = addnode;
        else
            parent->right = addnode;
    }
    
    return addnode;
}

Node* deleteNode(Node* root, int x)
{
    Node* p = root;
    Node* parent = NULL;
    while((p!=NULL)&&(p->key != x))
    {
        parent = p;
        if(p->key > x)
            p = p->left;
        else
            p = p->right;
    }
    
    if(p==NULL){
        printf("삭제하려는 노드는 존재하지 않습니다.");
        return root; //메인에서 루트를 갱신하므로 루트를 반환해 주어야 한다
    }

    if((p->left == NULL)&&(p->right == NULL)){
        if(parent->right == p)
            parent->right = NULL;
        else
            parent->left = NULL;
    }
    else if ((p->left == NULL)||(p->right == NULL)){
        Node* child = (p->right == NULL) ? p->left : p->right;
        if(parent==NULL)
            root = child;
        else{
            if(parent->right == p)
                parent->right = child;
            else
                parent->left = child;
        }
        
        
    }
    else{
        Node* succ = p->left;
        Node* succ_parent = p;

        while(succ->right != NULL){
            succ_parent = succ;
            succ = succ ->right;
        }
        p->key = succ->key;

        if(succ_parent->right == succ)
            succ_parent->right = succ->left;
        else
            succ_parent->left = succ->left;
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
    printf("%d ",root->key);
    inorder(root->right);
}

int main(void)
{
    Node* root = addNode(NULL,8);
    addNode(root,2);
    addNode(root,5);
    addNode(root,9);
    addNode(root,10);
    addNode(root,7);
    addNode(root,4);
    addNode(root,12);
    addNode(root,3);
    addNode(root,6);
    addNode(root,11);
    addNode(root,13);
    root = deleteNode(root,8);
    inorder(root);

    return 0;
}