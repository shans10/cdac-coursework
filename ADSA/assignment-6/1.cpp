/*
    Prim's Algorithm Implementation
*/

#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

void primMST(vector<vector<pair<int, int>>> &graph, int V)
{
    vector<int> key(V, INT_MAX);
    vector<bool> inMST(V, false);
    vector<int> parent(V, -1);

    key[0] = 0; // Start with the first vertex
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, 0}); // {weight, vertex}

    while (!pq.empty())
    {
        int u = pq.top().second;
        pq.pop();

        inMST[u] = true;

        for (auto &[v, weight] : graph[u])
        {
            if (!inMST[v] && weight < key[v])
            {
                key[v] = weight;
                parent[v] = u;
                pq.push({key[v], v});
            }
        }
    }

    cout << "Prim's MST Edges:\n";
    for (int i = 1; i < V; i++)
    {
        cout << parent[i] << " - " << i << " with weight " << key[i] << endl;
    }
}

int main()
{
    int V = 5; // Number of vertices
    vector<vector<pair<int, int>>> graph(V);

    // Add edges {u, v, weight}
    graph[0].push_back({1, 2});
    graph[0].push_back({3, 6});
    graph[1].push_back({0, 2});
    graph[1].push_back({2, 3});
    graph[1].push_back({3, 8});
    graph[2].push_back({1, 3});
    graph[2].push_back({4, 5});
    graph[3].push_back({0, 6});
    graph[3].push_back({1, 8});
    graph[4].push_back({2, 5});

    primMST(graph, V);

    return 0;
}
