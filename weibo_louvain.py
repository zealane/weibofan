import networkx as nx
import csv

import matplotlib.pyplot as plt
import matplotlib.cm as cm
#from networkx.algorithms import community #
import itertools
import community as community_louvain
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

  # print(G.number_of_nodes())
  # for n in G.nodes():
  #     print("degree",G.degree(n))
  #     if G.degree(n)==1:
  #          print("del")
  #          G.remove_node(n)

    #获取平均度
d = dict(G.degree)
# print(d)
print("平均度：",sum(d.values())/len(G.nodes))

print(sorted(d, key=lambda x:x[1], reverse=True))

#获取度分布
# nx_h=nx.degree_histogram(G)
#
# #度分布直方图
# x= list(range(max(d.values())+1))
# y= [i/sum(nx.degree_histogram(G)) for i in nx_h]
#
# plt.bar(x,y,width=0.5,color="blue")
# plt.xlabel("$k$")
# plt.ylabel("$p_k$")
# plt.xlim([0,100])

#first compute the best partition
partition = community_louvain.best_partition(G)

# compute the best partition
#partition = community_louvain.best_partition(G)

# draw the graph
pos = nx.spring_layout(G)
NodeId = list(G.nodes())
print("NodeID:%s"%NodeId)
node_size = [G.degree(i)**1.2*90 for i in NodeId] # 节点大小
nx.draw(G,pos, with_labels=True, node_size =node_size, node_color='w', node_shape = '.')

# color the nodes according to their partition
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
# nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
#                        cmap=cmap, node_color=list(partition.values()),with_labels=True)
nx.draw_networkx_nodes(G, pos, partition.keys(),node_color=list(partition.values()),with_labels=True)
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()