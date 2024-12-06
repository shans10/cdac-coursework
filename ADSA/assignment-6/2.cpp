/*
    Kruskal's Algorithm Implementation
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge
{
    int u, v, weight;
    bool operator<(const Edge &other) const
    {
        return weight < other.weight;
    }
};

class UnionFind
{
    vector<int> parent, rank;

public:
    UnionFind(int n) : parent(n), rank(n, 0)
    {
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    int find(int x)
    {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    bool unionSets(int x, int y)
    {
        int rootX = find(x), rootY = find(y);
        if (rootX == rootY)
            return false;

        if (rank[rootX] > rank[rootY])
        {
            parent[rootY] = rootX;
        }
        else if (rank[rootX] < rank[rootY])
        {
            parent[rootX] = rootY;
        }
        else
        {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        return true;
    }
};

void kruskalMST(vector<Edge> &edges, int V)
{
    sort(edges.begin(), edges.end());
    UnionFind uf(V);

    vector<Edge> mst;
    int totalWeight = 0;

    for (auto &edge : edges)
    {
        if (uf.unionSets(edge.u, edge.v))
        {
            mst.push_back(edge);
            totalWeight += edge.weight;
        }
    }

    cout << "Kruskal's MST Edges:\n";
    for (auto &edge : mst)
    {
        cout << edge.u << " - " << edge.v << " with weight " << edge.weight << endl;
    }
    cout << "Total Weight: " << totalWeight << endl;
}

int main()
{
    int V = 5; // Number of vertices
    vector<Edge> edges = {
        {0, 1, 2}, {0, 3, 6}, {1, 2, 3}, {1, 3, 8}, {2, 4, 5}};

    kruskalMST(edges, V);

    return 0;
}
