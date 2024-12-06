#include <iostream>
using namespace std;

enum Color
{
    RED,
    BLACK
};

struct Node
{
    int data;
    bool color;
    Node *left;
    Node *right;
    Node *parent;

    Node(int data) : data(data), color(RED), left(nullptr), right(nullptr), parent(nullptr) {}
};

class RedBlackTree
{
private:
    Node *root;

    void rotateLeft(Node *&root, Node *&pt)
    {
        Node *ptRight = pt->right;

        pt->right = ptRight->left;

        if (pt->right != nullptr)
            pt->right->parent = pt;

        ptRight->parent = pt->parent;

        if (pt->parent == nullptr)
            root = ptRight;
        else if (pt == pt->parent->left)
            pt->parent->left = ptRight;
        else
            pt->parent->right = ptRight;

        ptRight->left = pt;
        pt->parent = ptRight;
    }

    void rotateRight(Node *&root, Node *&pt)
    {
        Node *ptLeft = pt->left;

        pt->left = ptLeft->right;

        if (pt->left != nullptr)
            pt->left->parent = pt;

        ptLeft->parent = pt->parent;

        if (pt->parent == nullptr)
            root = ptLeft;
        else if (pt == pt->parent->left)
            pt->parent->left = ptLeft;
        else
            pt->parent->right = ptLeft;

        ptLeft->right = pt;
        pt->parent = ptLeft;
    }

    void fixViolation(Node *&root, Node *&pt)
    {
        Node *parentPt = nullptr;
        Node *grandParentPt = nullptr;

        while ((pt != root) && (pt->color != BLACK) &&
               (pt->parent->color == RED))
        {
            parentPt = pt->parent;
            grandParentPt = pt->parent->parent;

            if (parentPt == grandParentPt->left)
            {
                Node *unclePt = grandParentPt->right;

                if (unclePt != nullptr && unclePt->color == RED)
                {
                    grandParentPt->color = RED;
                    parentPt->color = BLACK;
                    unclePt->color = BLACK;
                    pt = grandParentPt;
                }
                else
                {
                    if (pt == parentPt->right)
                    {
                        rotateLeft(root, parentPt);
                        pt = parentPt;
                        parentPt = pt->parent;
                    }

                    rotateRight(root, grandParentPt);
                    swap(parentPt->color, grandParentPt->color);
                    pt = parentPt;
                }
            }
            else
            {
                Node *unclePt = grandParentPt->left;

                if ((unclePt != nullptr) && (unclePt->color == RED))
                {
                    grandParentPt->color = RED;
                    parentPt->color = BLACK;
                    unclePt->color = BLACK;
                    pt = grandParentPt;
                }
                else
                {
                    if (pt == parentPt->left)
                    {
                        rotateRight(root, parentPt);
                        pt = parentPt;
                        parentPt = pt->parent;
                    }

                    rotateLeft(root, grandParentPt);
                    swap(parentPt->color, grandParentPt->color);
                    pt = parentPt;
                }
            }
        }

        root->color = BLACK;
    }

public:
    RedBlackTree() : root(nullptr) {}

    void insert(const int &data)
    {
        Node *pt = new Node(data);
        root = BSTInsert(root, pt);
        fixViolation(root, pt);
    }

    Node *BSTInsert(Node *root, Node *pt)
    {
        if (root == nullptr)
            return pt;

        if (pt->data < root->data)
        {
            root->left = BSTInsert(root->left, pt);
            root->left->parent = root;
        }
        else if (pt->data > root->data)
        {
            root->right = BSTInsert(root->right, pt);
            root->right->parent = root;
        }

        return root;
    }

    void inorder()
    {
        inorderHelper(root);
    }

    void inorderHelper(Node *root)
    {
        if (root == nullptr)
            return;

        inorderHelper(root->left);
        cout << root->data << " ";
        inorderHelper(root->right);
    }
};

int main()
{
    RedBlackTree tree;

    tree.insert(10);
    tree.insert(20);
    tree.insert(30);
    tree.insert(40);
    tree.insert(50);

    cout << "Inorder traversal of the tree: ";
    tree.inorder();

    cout << endl;

    return 0;
}
