#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Depth-First Search (DFS)
void dfs(int node, vector<int> adj[], vector<bool> &visited)
{
    visited[node] = true;
    cout << node << " ";

    for (int neighbor : adj[node])
    {
        if (!visited[neighbor])
        {
            dfs(neighbor, adj, visited);
        }
    }
}

// Breadth-First Search (BFS)
void bfs(int start, vector<int> adj[], int V)
{
    vector<bool> visited(V, false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

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
    int V = 5;
    vector<int> adj[5] = {
        {1, 2}, {0, 3, 4}, {0}, {1}, {1}};

    cout << "DFS Traversal: ";
    vector<bool> visited(V, false);
    dfs(0, adj, visited);

    cout << "\nBFS Traversal: ";
    bfs(0, adj, V);

    cout << endl;

    return 0;
}
