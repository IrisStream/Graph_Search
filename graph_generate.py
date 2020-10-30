import random
import time
import math
par = []

def swap(u,v):
    tmp = u
    u = v
    v = tmp

def get_edge(edge_id):
    u = 0
    while(edge_id - (n - u - 1) >= 0):
        edge_id -= (n - u - 1)
        u += 1
    v = u + 1 + edge_id
    return u,v

def root(x):
    if(par[x] < 0):
        return x
    par[x] = root(par[x])
    return par[x]

def join(u, v):
    u = root(u)
    v = root(v)
    if(u != v):
        if(par[u] < par[v]):
            par[u] += par[v]
            par[v] = u
        else:
            par[v] += par[u]
            par[u] = v

n = 0
max_edge = 0

if __name__ == "__main__":
    random.seed(time.time())
    n = int(input("Nhap so dinh cua do thi: "))
    max_edge = (n * (n - 1)) // 2
    random_pool = [i for i in range(max_edge)]
    for i in range(n):
        par.append(-1)

    size = max_edge
    flag = 0
    file = open("input1.txt", "w")
    start = random.randint(0, n - 1)
    goal = random.randint(0, n - 1)
    while(goal == start):
        goal = random.randint(0, n - 1)
    file.write(str(start) + '\n' + str(goal) + '\n')
    while(size > 0 and flag != 10):
        edge_id = random.randint(0, size - 1)
        u,v = get_edge(random_pool[edge_id])
        random_pool[edge_id] = random_pool[size - 1]
        size -= 1
        file.write(str(u) + ' ' + str(v) + '\n')
        join(u,v)
        if(flag != 0 or par[root(u)] == -n):
            flag = random.randint(1, 10)
    
    file.close()