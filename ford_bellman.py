#include <iostream>
#include <vector>
#include <limits>
#include <sstream>
#include <iterator>

using namespace std;

class Graph {
public:
    int V;
    vector<vector<int>> graph;

    void init(int numberOfVertices) {
        V = numberOfVertices;
        graph.clear();
    }

    void add_edge(int u, int v, int w) {
        graph.push_back({u - 1, v - 1, w});
    }

    void bellman_ford(int src) {
        vector<int> dist(V, numeric_limits<int>::max());
        dist[src] = 0;

        for (int i = 0; i < V - 1; ++i) {
            for (const auto& edge : graph) {
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];

                if (dist[u] != numeric_limits<int>::max() && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
            }
        }

        for (int i = 0; i < V; ++i) {
            if (dist[i] == numeric_limits<int>::max()) {
                dist[i] = 30000;
            }
        }

        ostringstream oss;
        copy(dist.begin(), dist.end(), ostream_iterator<int>(oss, " "));
        string result = oss.str();
        result.pop_back();  // Remove trailing space
        cout << result << endl;
    }
};

int main() {
    int n, m;
    cin >> n >> m;

    Graph g;
    g.init(n);

    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        g.add_edge(u, v, w);
    }

    g.bellman_ford(0);

    return 0;
}
