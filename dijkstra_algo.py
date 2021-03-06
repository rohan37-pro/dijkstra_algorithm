import networkx as nx
from matplotlib import pyplot as plt


demo_net = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]]



def add_node(net_array,g):
    node = 0
    total_path = 0
    for i in net_array:
        node_neighbor=0
        for j in i:
            if j!=0:
                g.add_edge(node,node_neighbor, length=j)
                total_path +=1
            node_neighbor+=1
        node+=1

def extract_graph_from_file(file):
    with open(file,"r") as f:
        graph = f.read()
        graph = graph.replace('\n',' ')
        graph = graph.strip()
        graph = eval(graph)
        return graph

def savefile(graph,file_name):
    g = nx.Graph()
    add_node(graph,g)
    nx.draw(g,with_labels=True)
    plt.savefig(file_name)
    plt.clf()


def zero_array(nodes):
    array = []
    for i in range(nodes):
        array.append([])
        for j in range(nodes):
            array[i].append(0)
    return array



def min_length(dics):
    length = 9*10**999
    for i in dics:
        element = dics[i][0]
        if element<length:
            length = element
            key = i
    try:
        return key
    except:
        return None



def neighbor_nodes(lis):
    neighbor = []
    for i in lis:
        if i!=0:
            neighbor.append(lis.index(i))
    return neighbor



def dijkstra_algo(graph,source):
    tentative = {}
    permanent = {source:[0,source]}
    permanent_graph = zero_array(len(graph))
    node_visited = []
    

    node = source
    distance_form_source = 0
    not_shorted = True

    while len(node_visited)<=len(graph):
        node_visited.append(node)
        all_neighbors = neighbor_nodes(graph[node])
        print(f"\nneighbor of node {node} are {all_neighbors}")
        for neighbor in all_neighbors:
    
            if neighbor in tentative and neighbor not in permanent:
                if graph[node][neighbor]+distance_form_source < tentative[neighbor][0]:
                    tentative[neighbor][0] = graph[node][neighbor]+distance_form_source
                    tentative[neighbor][1] = node


            if neighbor not in tentative and neighbor not in permanent:
                tentative[neighbor] = [0,0]
                tentative[neighbor][0] = graph[node][neighbor]+distance_form_source
                tentative[neighbor][1] = node

        print(f"tentative is {tentative}")        


        key = min_length(tentative)
        if key == None:
            break
        permanent[key] = tentative[key]
        print(f"permanent is {permanent}")
        distance = tentative[key][0]
        print(f"node {node} distance = {distance} key = {key}\n")
        permanent_graph[tentative[key][1]][key] = distance
        distance_form_source = tentative[key][0]
        tentative.pop(key)
        node = key

        if len(node_visited) == len(graph):
            break

    return permanent_graph



if __name__ == "__main__":
    inp = input("input from file or manual(f/m) : ")
    if inp == "m":
        graph = eval(input("enter the array of the graph : "))
    if inp == "f":
        file = input("enter name of you text file : ")
        graph = extract_graph_from_file(file)
    source = int(input("enter the source node : "))
    shorted_graph = dijkstra_algo(graph,source)
    
    print(f"graph of shortest path : \n{shorted_graph}")

    savefile(graph,"graph of network.png")
    savefile(shorted_graph,"graph of shortest path.png")
 
