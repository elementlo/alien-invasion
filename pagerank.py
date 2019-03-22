import os
import networkx as nx
import matplotlib.pyplot as plt

filename = 'facebook_combined.txt'
G=nx.DiGraph()
with open(filename) as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head,tail)

pr=nx.pagerank(G,alpha=0.85)

x = 0;
for node, value in pr.items():
    print(value)   
    x = x + value

########画图
# layout = nx.spring_layout(G)
# plt.figure(1)
# nx.draw(G, pos=layout, node_color='y')

# pr=nx.pagerank(G,alpha=0.85)
# print(pr)
# for node, pageRankValue in pr.items():
#     print("%d,%.4f" %(node,pageRankValue))

# plt.figure(2)
# nx.draw(G, pos=layout, node_size=[x * 6000 for x in pr.values()],node_color='m',with_labels=True)
# plt.show()