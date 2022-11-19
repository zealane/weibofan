import csv
import networkx as nx
import matplotlib.pyplot as plt

filePath="fan.csv"
G = nx.Graph()
with open(filePath,'r') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    print(row[0])
    print(row[1])
    G.add_edge(row[0],row[1])


# wnode = [[1,2],[3,4],['B','C']]
# G.add_nodes_from(wnode[0])
# G.add_nodes_from(wnode[1])
# G.add_nodes_from(wnode[2])
# G.add_edge(wnode[0][0],wnode[1][0],weight = 4)
# G.add_edge(wnode[0][0],wnode[2][0],weight = 2)
# G.add_edge(wnode[0][0],wnode[0][1],weight = 2)




nx.draw(G)
plt.show()