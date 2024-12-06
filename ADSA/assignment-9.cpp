#include <iostream>
#include <vector>
#include <climits>
using namespace std;

// Function to find the MST for a single cycle graph
int findMSTForCycle(const vector<pair<int, int>> &edges, const vector<int> &weights)
{
    int maxWeight = INT_MIN, maxEdgeIndex = -1;

    // Find the edge with the maximum weight
    for (int i = 0; i < edges.size(); i++)
    {
        if (weights[i] > maxWeight)
        {
            maxWeight = weights[i];
            maxEdgeIndex = i;
        }
    }

    // MST weight is the total weight of all edges minus the maximum weight edge
    int totalWeight = 0;
    for (int w : weights)
        totalWeight += w;
    return totalWeight - maxWeight;
}

int main()
{
    // Example graph: A cycle with 4 vertices
    // Edges: (0-1, 1-2, 2-3, 3-0)
    vector<pair<int, int>> edges = {{0, 1}, {1, 2}, {2, 3}, {3, 0}};
    vector<int> weights = {4, 1, 2, 3};

    int mstWeight = findMSTForCycle(edges, weights);

    cout << "Weight of the MST: " << mstWeight << endl;
    return 0;
}
