import pygame
import math
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
    pygame.time.delay(1000)

def trace_route(graph, edges, edge_id, trace, start, goal):
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
                    trace_route(graph, edges, edge_id, trace, start, goal)
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
        for i in range(len(graph[u][1])-1,-1,-1):   #Loop down-to in the adjacent set of U, so we cant put the smallest index adj to to top of stack after loop
            v = graph[u][1][i]
            if(graph[v][3] == black):
                trace[v] = u
                s.append(v)
                if v == goal:
                    trace_route(graph, edges, edge_id, trace, start, goal)
                    return
        edges[edge_id(u,s[-1])][1] = white
        changeColor(graph, s[-1], red)
        changeColor(graph, u, blue)
    pass


def push_heap(heap, node, cost):
    x = (node, cost)
    cur = len(heap)
    heap.append(x)
    while(cur > 0):
        par = (cur - 1) // 2
        if(heap[par][1] >= x[1]):
            heap[cur] = heap[par]
        else:
            break
        cur = par
    heap[cur] = x

def pop_heap(heap):
    ans = heap[0]
    heap[0] = heap[-1]
    x = heap[0]
    heap.pop()
    cur = 0
    while(cur * 2 + 2 < len(heap)):
        flag = 0
        for child in range(cur * 2 + 1, cur * 2 + 3):
            if(heap[child][1] < x[1]):
                heap[cur] = heap[child]
                cur = child
                flag = 1
                break
        if(flag == 0):
            break
    return ans

INF = 1000000000

def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    # TODO: your code
    def cost(u,v):
        return math.sqrt((graph[u][0][0] - graph[v][0][0]) * (graph[u][0][0] - graph[v][0][0]) * (graph[u][0][1] - graph[v][0][1]) * (graph[u][0][1] - graph[v][0][1]))

    print("Implement Uniform Cost Search algorithm.")
    heap = []
    heap.append((start,0))
    trace = list(range(0,len(graph)))
    min_cost = list(range(0,len(graph)))
    while(len(heap) > 0):
        u = pop_heap(heap)
        if(u[0] == goal):
            pass
        if(min_cost[u[0]] < u[1]):
            continue
        u = u[0]
        if(u == goal):
            trace_route(graph, edges, edge_id, trace, start, goal)
            break
        changeColor(graph, u, yellow)
        for v in graph[u][1]:
            if(graph[v][3] == black or (graph[v][3] == red and min_cost[v] > min_cost[u] + cost(u,v))):
                min_cost[v] = min_cost[u] + cost(u,v)
                trace[v] = u
                push_heap(heap, v, min_cost[v])
                edges[edge_id(u,v)][1] = white
                changeColor(graph, v, red)
        changeColor(graph, u, blue)


def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code
    def cost(u,v):
        return math.sqrt((graph[u][0][0] - graph[v][0][0]) * (graph[u][0][0] - graph[v][0][0]) + (graph[u][0][1] - graph[v][0][1]) * (graph[u][0][1] - graph[v][0][1]))

    print("Implement A* algorithm.")
    trace = list(range(0,len(graph)))
    min_f = list(range(0,len(graph)))
    for i in range(0, len(graph)):
        min_f[i] = INF
    min_f[start] = cost(start, goal)
    min_cost = list(range(0,len(graph)))
    for i in range(0, len(graph)):
        min_cost[i] = INF
    min_cost[start] = 0
    heap = []
    heap.append((start, min_f[start]))
    while(len(heap) > 0):
        u = pop_heap(heap)
        if(u[0] == goal):
            pass
        if(min_f[u[0]] < u[1]):
            continue
        u = u[0]
        if(u == goal):
            trace_route(graph, edges, edge_id, trace, start, goal)
            break
        changeColor(graph, u, yellow)
        for v in graph[u][1]:
            if(min_cost[v] > min_cost[u] + cost(u,v)):
                min_cost[v] = min_cost[u] + cost(u,v)
                min_f[v] = min_cost[v] + cost(v, goal)
                trace[v] = u
                push_heap(heap, v, min_f[v])
                edges[edge_id(u,v)][1] = white
                changeColor(graph, v, red)
        changeColor(graph, u, blue)
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
