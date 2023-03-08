from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):

        visited[v] = True

        temp.append(v)

        for i in self.adj[v]:
            if visited[i] == False:

                temp = self.DFSUtil(temp, i, visited)
        return temp

    def addEdge(self, v, w):
        self.adj[v].append(w)
        # self.adj[w].append(v)

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

    def countDegree1(self, cc):
        d1 = defaultdict(list)
        for v in cc:
            if len(self.adj[v]) == 1:
                d1[self.adj[v][0]].append(v)
        return d1


def find_good_pairs(banana_list):
    idx_good_pairs = defaultdict(list)
    for i in range(len(banana_list) - 1):
        for j in range(i + 1, len(banana_list)):
            if is_good(banana_list[i], banana_list[j]):
                idx_good_pairs[i].append(j)
                idx_good_pairs[j].append(i)
    return idx_good_pairs


def is_good(a1, a2):
    a1, a2 = min(a1, a2), max(a1, a2)
    while a1 % 2 == a2 % 2 and a1 != a2:
        a1, a2 = min(a1 + a1, a2 - a1) // 2, max(a1 + a1, a2 - a1) // 2
    if a1 == a2:
        return False
    else:
        return True


def create_graph(banana_list):
    idx = find_good_pairs(sorted(banana_list))
    g = Graph(len(banana_list))
    for v1 in idx:
        for v2 in idx[v1]:
            g.addEdge(v1, v2)
    return g


def count_others(gr, used_trainers, g):
    for v1 in gr:
        if not used_trainers[v1]:
            for v2 in g.adj[v1]:
                if not used_trainers[v2] and v2 in g.adj[v1]:
                    used_trainers[v1], used_trainers[v2] = 1, 1
                    break
    return used_trainers.count(0)


def find_bored_trainers(g, cc):
    bored_trainers = 0
    used_trainers = [0] * g.V
    for gr in cc:
        v_degree1 = g.countDegree1(gr)
        for v in v_degree1:
            for v1 in v_degree1[v][1:]:
                used_trainers[v1] = 1
                gr.pop(gr.index(v1))
                bored_trainers += 1
            gr.pop(gr.index(v))
            used_trainers[v] = 1
            gr.pop(gr.index(v_degree1[v][0]))
            used_trainers[v][0] = 1
        if len(gr) == 1:
            used_trainers[gr[0]] = 1
            bored_trainers += 1
        else:
            bored_trainers += count_others(gr, used_trainers, g)
    return bored_trainers


def solution(banana_list):
    g = create_graph(banana_list)
    bored_trainers = find_bored_trainers(g, g.connectedComponents())

    return bored_trainers


print(solution([1, 1]))
