import networkx as nx
import csv

import matplotlib.pyplot as plt
from networkx.algorithms import community #
import itertools
import matplotlib.pyplot as plt

#G = nx.karate_club_graph() # 空手道俱乐部



filePath="fans.csv"
G = nx.Graph()
with open(filePath,'r') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    # print(row[0])
    #
    # print(row[1])
    G.add_edge(row[0],row[1])

#print (G.degree)
degrees = G.nodes()
print(sorted(degrees, key=lambda x:x[1], reverse=True))

comp = community.girvan_newman(G) # GN算法

k = 6 # 想要4个社区
limited = itertools.takewhile(lambda c: len(c) <= k, comp) # 层次感迭代器
for communities in limited:
    b = list(sorted(c) for c in communities)




pos = nx.spring_layout(G) # 节点的布局为spring型

NodeId = list(G.nodes())
#print("NodeID:%s"%NodeId)
node_size = [G.degree(i)**1.2*90 for i in NodeId] # 节点大小





plt.figure(figsize = (8,6)) # 图片大小
nx.draw(G,pos, with_labels=True, node_size =node_size, node_color='w', node_shape = '.')
'''
node_size表示节点大小
node_color表示节点颜色
node_shape表示节点形状
with_labels=True表示节点是否带标签
'''
color_list = ['brown','orange','r','g','b','y','m','gray','black','c','pink']
# node_shape = ['s','o','H','D']

print(len(b))
for i in range(len(b)):
    # nx.draw_networkx_nodes(G, pos, nodelist=b[i], node_color=color_list[i], node_shape=node_shape[i], with_labels=True)
    #print (b[i])
    nx.draw_networkx_nodes(G, pos, nodelist=b[i], node_color=color_list[i],  with_labels=True)

plt.show()
