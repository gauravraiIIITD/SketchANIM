import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as patches
# Read vertex coordinates from a text file
def read_vertex_coordinates(file_path):
    vertex_coordinates = {}
    with open(file_path, 'r') as file:
        for idx, line in enumerate(file):
            x, y = map(float, line.strip().split())
            vertex_coordinates[idx] = (x*2048, y*2048)
    return vertex_coordinates

# Read edge list from a text file
def read_edge_list(file_path):
    edge_list = []
    with open(file_path, 'r') as file:
        for line in file:
            v1, v2 = map(int, line.strip().split())
            edge_list.append((v1, v2))
    return edge_list

def plot_skeleton_graph(vertex_coordinates, edge_list, joint_colors, joint_to_vertex):
    G = nx.Graph()

    # Add vertices with coordinates to the graph
    for vertex, coords in vertex_coordinates.items():
        G.add_node(vertex, pos=coords)

    # Add edges to the graph
    G.add_edges_from(edge_list)

    # Get node positions
    node_positions = nx.get_node_attributes(G, 'pos')

    # Draw the graph with different colors for each joint number
    plt.figure(figsize=(8, 6))
    plt.xlim(2048, -2048)
    plt.ylim(2048, -2048)
    for joint_number, color in joint_colors.items():
        vertices = joint_to_vertex.get(joint_number, [])  # Get vertices corresponding to the joint
        nodes = [node for node in G.nodes() if node in vertices]  # Filter nodes by vertices
        edges = [edge for edge in G.edges() if edge[0] in nodes and edge[1] in nodes]
        nx.draw_networkx_nodes(G, pos=node_positions, nodelist=nodes, node_color=color, node_size=60, edgecolors='black', linewidths=0.1)
        nx.draw_networkx_edges(G, pos=node_positions, edgelist=edges, width=1.0, alpha=0.7, edge_color='black')

        # Annotate nodes with joint numbers
        for node in nodes:
            x, y = node_positions[node]
            # Offset the annotation from the joint position
            dx = 0.07 * (max(vertex_coordinates.values(), key=lambda item: item[0])[0] - min(vertex_coordinates.values(), key=lambda item: item[0])[0])
            dy = 0.05 * (max(vertex_coordinates.values(), key=lambda item: item[1])[1] - min(vertex_coordinates.values(), key=lambda item: item[1])[1])
            # plt.text(x + dx, y + dy, str(joint_number), fontsize=8, ha='center', va='center')

    # Draw small black nodes on top
    nx.draw_networkx_nodes(G, pos=node_positions, nodelist=G.nodes(), node_color='black', node_size=5, edgecolors='black')
    nx.draw_networkx_edges(G, pos=node_positions, edgelist=G.edges(), width=1.5, alpha=0.7, edge_color='black')
    # plt.gca().invert_yaxis()
    plt.gca().invert_xaxis()
    # Show the plot
    plt.axis('off')
    plt.show()

# Main function
def main():
    vertex_file_path = "sketch_skeleton_vertices.txt"  # Path to vertex coordinates file
    edge_file_path = "skeleton_edges.txt"  # Path to edge list file

    # # Define joint colors
    # joint_colors = {
    #     0: 'cyan',
    #     1: 'red',
    #     2: 'cyan',
    #     3: 'lightgreen',
    #     4: 'pink',
    #     5: 'violet',
    #     6: 'lightgreen',
    #     7: 'pink',
    #     8: 'violet',
    #     9: 'cyan',
    #     10: 'lightgreen',
    #     11: 'pink',
    #     12: 'cyan',
    #     13: 'lightgreen',
    #     14: 'pink'
    #     # Add more colors for other joint numbers as needed
    # }

    joint_colors = {
        0: 'white',
        1: 'white',
        2: 'white',
        3: 'white',
        4: 'white',
        5: 'white',
        6: 'white',
        7: 'white',
        8: 'white',
        9: 'white',
        10: 'white',
        11: 'white',
        12: 'white',
        13: 'white',
        14: 'white'
        # Add more colors for other joint numbers as needed
    }


    # joint_colors = {
    #     0: 'grey',
    #     1: 'grey',
    #     2: 'grey',
    #     3: 'grey',
    #     4: 'grey',
    #     5: 'grey',
    #     6: 'grey',
    #     7: 'grey',
    #     8: 'grey',
    #     9: 'grey',
    #     10: 'grey',
    #     11: 'grey',
    #     12: 'grey',
    #     13: 'grey',
    #     14: 'grey'
    #     # Add more colors for other joint numbers as needed
    # }

    # Define joint to vertex mapping
    joint_to_vertex = {
        0: [0],  
        1: [1],  
        2: [2],  
        3: [3],  
        4: [4],  
        5: [5], 
        6: [6], 
        7: [7],  
        8: [8], 
        9: [9], 
        10: [10],  
        11: [11],
        12: [12],
        13: [13],
        14: [14]
        
    }

    # # Define joint to vertex mapping
    # joint_to_vertex = {
    #     0: [1],  
    #     1: [0],  
    #     2: [1],  
    #     3: [2],  
    #     4: [3],  
    #     5: [4], 
    #     6: [2], 
    #     7: [3],  
    #     8: [4], 
    #     9: [1], 
    #     10: [2],  
    #     11: [3],
    #     12: [1],
    #     13: [2],
    #     14: [3]
        
    # }

    #     # Define joint to vertex mapping
    # joint_to_vertex = {
    #     1: [0],  
    #     0: [1],  
    #     1: [2],  
    #     2: [3],  
    #     3: [4],  
    #     5: [5], 
    #     2: [6], 
    #     3: [7],  
    #     4: [8], 
    #     1: [9], 
    #     2: [10],  
    #     3: [11],
    #     1: [12],
    #     2: [13],
    #     3: [14]
        
    # }

    vertex_coordinates = read_vertex_coordinates(vertex_file_path)
    edge_list = read_edge_list(edge_file_path)
    
    plot_skeleton_graph(vertex_coordinates, edge_list, joint_colors, joint_to_vertex)

if __name__ == "__main__":
    main()

