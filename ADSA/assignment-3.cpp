/*
    Comparison: BST, Hash Table, and Simple Array
*/

#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

// Binary Search Tree Node
struct BSTNode
{
    int key;
    BSTNode *left;
    BSTNode *right;
    BSTNode(int val) : key(val), left(nullptr), right(nullptr) {}
};

// BST Operations
class BST
{
public:
    BSTNode *root = nullptr;

    BSTNode *insert(BSTNode *node, int key)
    {
        if (!node)
            return new BSTNode(key);
        if (key < node->key)
            node->left = insert(node->left, key);
        else if (key > node->key)
            node->right = insert(node->right, key);
        return node;
    }

    BSTNode *search(BSTNode *node, int key)
    {
        if (!node || node->key == key)
            return node;
        if (key < node->key)
            return search(node->left, key);
        return search(node->right, key);
    }

    BSTNode *findMin(BSTNode *node)
    {
        while (node && node->left)
            node = node->left;
        return node;
    }

    BSTNode *deleteNode(BSTNode *node, int key)
    {
        if (!node)
            return node;
        if (key < node->key)
            node->left = deleteNode(node->left, key);
        else if (key > node->key)
            node->right = deleteNode(node->right, key);
        else
        {
            if (!node->left)
            {
                BSTNode *temp = node->right;
                delete node;
                return temp;
            }
            else if (!node->right)
            {
                BSTNode *temp = node->left;
                delete node;
                return temp;
            }
            BSTNode *temp = findMin(node->right);
            node->key = temp->key;
            node->right = deleteNode(node->right, temp->key);
        }
        return node;
    }
};

// Hash Table Operations
class HashTable
{
    unordered_map<int, int> table;

public:
    void insert(int key)
    {
        table[key] = key;
    }

    void remove(int key)
    {
        table.erase(key);
    }

    bool search(int key)
    {
        return table.find(key) != table.end();
    }
};

// Array Operations
class ArrayOps
{
    vector<int> arr;

public:
    void insert(int key)
    {
        arr.push_back(key);
    }

    void remove(int key)
    {
        auto it = find(arr.begin(), arr.end(), key);
        if (it != arr.end())
            arr.erase(it);
    }

    bool search(int key)
    {
        return find(arr.begin(), arr.end(), key) != arr.end();
    }
};

// Main function
int main()
{
    // Compare BST, Hash Table, and Array
    BST bst;
    HashTable hashTable;
    ArrayOps arrayOps;

    // Operations: Insert, Search, Delete
    bst.root = bst.insert(bst.root, 10);
    bst.root = bst.insert(bst.root, 5);
    bst.root = bst.insert(bst.root, 15);

    hashTable.insert(10);
    hashTable.insert(5);
    hashTable.insert(15);

    arrayOps.insert(10);
    arrayOps.insert(5);
    arrayOps.insert(15);

    cout << "BST Search 10: " << (bst.search(bst.root, 10) != nullptr) << endl;
    cout << "Hash Table Search 10: " << hashTable.search(10) << endl;
    cout << "Array Search 10: " << arrayOps.search(10) << endl;

    return 0;
}
