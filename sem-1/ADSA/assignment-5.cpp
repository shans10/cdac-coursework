/*
    Graph Traversal Algorithms and Comparison
*/

// DFS and BFS Implementation

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void dfs(int node, vector<int> adj[], vector<bool> &visited)
{
    visited[node] = true;
    cout << node << " ";
    for (int neighbor : adj[node])
    {
        if (!visited[neighbor])
            dfs(neighbor, adj, visited);
    }
}

void bfs(int start, vector<int> adj[])
{
    queue<int> q;
    vector<bool> visited(100, false);
    q.push(start);
    visited[start] = true;
    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        cout << node << " ";
        for (int neighbor : adj[node])
        {
            if (!visited[neighbor])
            {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

int main()
{
    vector<int> adj[5] = {
        {1, 2}, {0, 3, 4}, {0}, {1}, {1}};

    cout << "DFS: ";
    vector<bool> visited(5, false);
    dfs(0, adj, visited);

    cout << "\nBFS: ";
    bfs(0, adj);

    cout << endl;

    return 0;
}
