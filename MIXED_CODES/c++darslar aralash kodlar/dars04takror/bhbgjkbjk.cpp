#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

const int INF = numeric_limits<int>::max();

class Graph {
private:
    int vertices;
    vector<vector<pair<int, int>>> adjacencyList;

public:
    Graph(int v) : vertices(v), adjacencyList(v) {}

    void addEdge(int from, int to, int weight) {
        adjacencyList[from].emplace_back(to, weight);
    }

    vector<int> dijkstra(int startVertex) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> distance(vertices, INF);

        pq.push({0, startVertex});
        distance[startVertex] = 0;

        while (!pq.empty()) {
            int currentVertex = pq.top().second;
            int currentDistance = pq.top().first;
            pq.pop();

            if (currentDistance > distance[currentVertex]) {
                continue;
            }

            for (const auto& neighbor : adjacencyList[currentVertex]) {
                int neighborVertex = neighbor.first;
                int weight = neighbor.second;

                int newDistance = currentDistance + weight;

                if (newDistance < distance[neighborVertex]) {
                    distance[neighborVertex] = newDistance;
                    pq.push({newDistance, neighborVertex});
                }
            }
        }

        return distance;
    }
};

int main() {
    Graph graph(6);

    // Grafni yaratish
    graph.addEdge(0, 1, 2);
    graph.addEdge(0, 2, 4);
    graph.addEdge(1, 2, 1);
    graph.addEdge(1, 3, 7);
    graph.addEdge(2, 4, 3);
    graph.addEdge(3, 4, 1);
    graph.addEdge(3, 5, 5);
    graph.addEdge(4, 5, 2);

    // Dijkstra algoritmi orqali eng qisqa yo'l aniqlash
    vector<int> shortestPaths = graph.dijkstra(0);

    // Natijalarni chiqarish
    cout << "Eng qisqa yo'l uzunliklari: ";
    for (int distance : shortestPaths) {
        cout << distance << " ";
    }
    cout << endl;

    return 0;
}
