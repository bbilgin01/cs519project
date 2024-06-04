import random
import sys

import matplotlib.pyplot as plt
import networkx as nx

def generate_graph(nodes, edges):
    # Generate random edges while avoiding duplicates and self-loops
    graph = set()
    while len(graph) < edges:
        source = random.randint(1, nodes)
        target = random.randint(1, nodes)
        weight = int(100 * random.random())
        if source != target and (source, target) not in graph:
            graph.add((source, target, weight))
    return list(graph)

nodes = int(sys.argv[1])
edges = int(sys.argv[2])
try:
    generate_maxtrix = bool(sys.argv[3])
except:
    generate_maxtrix = False
    
with open('inputMatrix', 'w') as f:
    f.write(str(nodes) + '\n')
    f.write(str(edges) + '\n')

    G = nx.DiGraph()  # Use a directed graph
    graph = generate_graph(nodes, edges)

    # Print the graph in the desired format
    for source, target, weight in graph:
        f.write(f"{source} {target} {weight}\n")
    if(generate_maxtrix):
        # Add edges with weights to the graph
        for source, target, weight in graph:
            G.add_edge(source, target, weight=weight)

# Basic layout (you can explore different layouts provided by networkx)
if(generate_maxtrix):
    pos = nx.spring_layout(G)
if(generate_maxtrix):
    # Plot the nodes and edges with weights
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=100, edge_color='gray', arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Save the plot to a file
    plt.savefig('graph.png')
    plt.close()
