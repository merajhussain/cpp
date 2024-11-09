

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <mutex>
#include <memory>
#include <condition_variable>
#include<queue>
#include<map>
#include<list>
#include<set>

using namespace std;

class MyGraph {

public:
    int vertices;
    vector<list<int>> adjacencyList;
    MyGraph(int v) {
        this->vertices = v;
        for (int i = 0; i < this->vertices+1; i++) {
        std:list<int> temp;
            adjacencyList.push_back(temp);
        }
       
    }

    void addConnection(int node1, int node2) {

        this->adjacencyList[node1].push_back(node2);
        this->adjacencyList[node2].push_back(node1);

    }

    void connectionsFromCurrentNode(int node, vector<bool>& visited, int& nodeInComponent)
    {

        visited[node] = true;
        nodeInComponent++;


        if (adjacencyList[node].size()>0) {

            for (auto it = adjacencyList[node].begin(); it != adjacencyList[node].end(); ++it) {

                if ( !visited[*it]) {
                    connectionsFromCurrentNode(*it, visited, nodeInComponent);
                }

            }

        }

       

       
               
    }





    vector<int> componentsInGraph() {

        set<int> componentCountList; // use vector to use all components
        vector<bool> visited;
        for (int i = 0; i <= vertices; i++) {
            visited.push_back(false);

        }

       // visited.reserve(this->vertices);

        for (int i = 1; i <= this->vertices; i++) {
            if (visited[i] == false) {
                int nodeCountInComponent = 0;
                connectionsFromCurrentNode(i, visited, nodeCountInComponent);

              //  if (nodeCountInComponent > 1) {
                    componentCountList.insert(nodeCountInComponent);
                //}
              
            }
        }



        return { componentCountList.begin(),componentCountList.end() };
    }
};

vector<int>  componentsInGraph(vector<vector<int>> gb) {

    MyGraph graph(gb.size());

    for (int i = 0; i < gb.size(); i++) {

        graph.addConnection(gb[i][0], gb[i][1]);
    }


    return graph.componentsInGraph();
}


 
int main()
{
	 
	MyGraph g(7); 
	g.addConnection(1, 5);
	g.addConnection(1, 6);
	g.addConnection(2, 4);

	cout << "Following are connected components \n";
    auto v =g.componentsInGraph();

	return 0;
}
