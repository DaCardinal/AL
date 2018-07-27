import networkx as nx
import matplotlib.pyplot as plt


def find_root(G, child):
    parent = list(G.predecessors(child))
    if len(parent) == 0:
        # print("found root: {}".format(child))
        return child
    else:
        # print(parent)
        return find_root(G, parent[0])


def find_ancestors(G, child, ancestors):
    parent = list(G.predecessors(child))

    if len(parent) == 0:
        # print("found root: {}".format(child))
        return child, ancestors
    else:
        ancestors.append(parent[0])
        print(parent)
        return find_ancestors(G, parent[0], ancestors)


A = nx.DiGraph(data=[('glu', 'skin'), ('glu', 'bmi'), ('glu', 'bp'), ('glu', 'age'), ('npreg', 'glu')])
# print(A.edges)
# test = find_root(G, "age")

D = nx.DiGraph()
# D.add_edge('skin', 'glu')
# D.add_edge('glu', 'skin')
# D.add_edge('npreg', 'skin')
# D.add_edge('glu', 'bmi')
# D.add_edge('glu', 'bp')
# D.add_edge('glu', 'age')
# D.add_edge('npreg', 'glu')
# D.add_edge('car', 'dog')
D.add_edge(0,1)
D.add_edge(1,0)
D.add_edge(0,2)
D.add_edge(2,0)
D.add_edge(1,2)
D.add_edge(2,1)
print(D.adj)
# print(list(D.predecessors("glu")))
print("ancestors {}".format(nx.ancestors(D, 0)))
for v in D.nodes():
    D.node[v]['state']= v
# test = find_root(D, "age")
# print("root {}".format(test))

# anc = find_ancestors(D, "age", list())
# print("ancestors: {}".format(anc))

# G = nx.complete_graph(5)
# print(G.nodes)
#
# G = nx.cubical_graph()
# plt.subplot(121)
#
# # <matplotlib.axes._subplots.AxesSubplot object at ...>
# nx.draw(G)  # default spring_layout
#
# plt.subplot(122)
# <matplotlib.axes._subplots.AxesSubplot object at ...>
# nx.draw(D, pos=nx.circular_layout(D), nodecolor='r', edge_color='b')
node_labels = nx.get_node_attributes(D,'state')
pos = nx.spring_layout(D)
nx.draw(D, pos, nodecolor='r', edge_color='b')
nx.draw_networkx_labels(D, pos, labels = node_labels)
plt.show()

G = nx.Graph()
G.add_edge(1,2)
G.add_edge(2,3)
for v in G.nodes():
    G.node[v]['state']='X'
G.node[1]['state']='Y'
G.node[2]['state']='Z'

for n in G.edges():
    G.add_edge(n[0], n[1], state='X')
    # G.edges[n[0]][n[1]]['state']='X'
# G.edges[2][3]['state']='Y'
G[1][2].update({'state': 'Y'})
# G.add_edge(2, 3, state='X')

pos = nx.spring_layout(G)

nx.draw(G, pos)
node_labels = nx.get_node_attributes(G,'state')
nx.draw_networkx_labels(G, pos, labels = node_labels)
edge_labels = nx.get_edge_attributes(G,'state')
nx.draw_networkx_edge_labels(G, pos, labels = edge_labels)
# plt.savefig('this.png')
plt.show()

# graph = { "a" : ["c"],
#       "b" : ["c", "e"],
#       "c" : ["a", "b", "d", "e"],
#       "d" : ["c"],
#       "e" : ["c", "b"],
#       "f" : []
#     }
#
# E = nx.Graph()
#
# for k,v in graph.items():
#     for vv in v:
#         E.add_edge(k,vv)
# nx.draw(E)
# plt.show()
