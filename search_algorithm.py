import pygame
import graphUI
import queue
from node_color import white, yellow, black, red, blue, purple, orange, green

"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""

def changeColor(graph, node, color):
    graph[node][3] = color
    graph[node][2] = white
    graphUI.updateUI()
    pygame.time.delay(500)

def traceroute(graph, edges, edge_id, trace, start, goal):
    cur = goal
    graph[start][3] = orange
    graph[goal][3] = purple
    while(cur != start):
        edges[edge_id(cur, trace[cur])][1] = green
        cur = trace[cur]
    graphUI.updateUI()

def BFS(graph, edges, edge_id, start, goal):
    """
    BFS search
    """
    # TODO: your code
    print("Implement BFS algorithm.")

    trace = list(range(0,len(graph)))
    q = queue.Queue()
    q.put(start)
    while(q.empty() == False):
        u = q.get()
        changeColor(graph, u, yellow)
        for v in graph[u][1]:
            if(graph[v][3] == black):
                trace[v] = u
                q.put(v)
                edges[edge_id(u,v)][1] = white
                changeColor(graph, v, red)
                if v == goal:
                    traceroute(graph, edges, edge_id, trace, start, goal)
                    return
        changeColor(graph, u, blue)
    pass


def DFS(graph, edges, edge_id, start, goal):
    """
    DFS search
    """
    # TODO: your code
    print("Implement DFS algorithm.")
    trace = list(range(0,len(graph)))
    s = []
    s.append(start)
    while(len(s) != 0):
        u = s.pop()
        changeColor(graph, u, yellow)
        for v in graph[u][1]:
            if(graph[v][3] == black):
                trace[v] = u
                s.append(v)
                edges[edge_id(u,v)][1] = white
                changeColor(graph, v, red)
                if v == goal:
                    traceroute(graph, edges, edge_id, trace, start, goal)
                    return
        changeColor(graph, u, blue)
    pass


def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    # TODO: your code
    print("Implement Uniform Cost Search algorithm.")
    pass


def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code
    print("Implement A* algorithm.")
    pass


def example_func(graph, edges, edge_id, start, goal):
    """
    This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                     [0] : (x,y) coordinate in UI
                     [1] : adjacent node indexes
                     [2] : node edge color
                     [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """

    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()

    # Ex2: Set color of Node 2 is Red
    graph[2][3] = red
    graphUI.updateUI()

    # Ex3: Set all edge between node in a array.
    path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = blue
    graphUI.updateUI()
