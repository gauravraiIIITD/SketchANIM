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
            vertex_coordinates[idx] = (x*512, y*512)
    return vertex_coordinates

# Read edge list from a text file
def read_edge_list(file_path):
    edge_list = []
    with open(file_path, 'r') as file:
        for line in file:
            v1, v2 = map(int, line.strip().split())
            edge_list.append((v1, v2))
    return edge_list

def plot_skeleton_graph(vertex_coordinates, edge_list, joint_colors):
    # Flip y-coordinates vertically
    for vertex, coords in vertex_coordinates.items():
        x, y = coords
        vertex_coordinates[vertex] = (x, -y)

    # Create an empty graph
    G = nx.Graph()

    # Add vertices with coordinates to the graph
    for vertex, coords in vertex_coordinates.items():
        G.add_node(vertex, pos=coords)

    # Add edges to the graph
    G.add_edges_from(edge_list)

    # Get node positions
    node_positions = nx.get_node_attributes(G, 'pos')

    # Create separate lists for nodes and edges for each joint number
    node_lists = {}
    edge_lists = {}

    for joint_number, color in joint_colors.items():
        node_lists[joint_number] = []
        edge_lists[joint_number] = []

    for edge in G.edges():
        v1, v2 = edge
        if v1 in joint_colors:
            node_lists[v1].append(v1)
        if v2 in joint_colors:  # Check if v2 is in joint_colors
            node_lists[v2].append(v2)
        if v1 in joint_colors and v2 in joint_colors:  # Only append edge if both vertices have colors
            edge_lists[v1].append(edge)

    # Draw the graph with different colors for each joint number
    plt.figure(figsize=(8, 6))
    plt.xlim(-512, 512)
    plt.ylim(-512, 512)
    for joint_number, nodes in node_lists.items():
        if nodes:
            nx.draw_networkx_nodes(G, pos=node_positions, nodelist=nodes, node_color=joint_colors[joint_number], node_size=100, edgecolors='black')
            nx.draw_networkx_edges(G, pos=node_positions, edgelist=edge_lists[joint_number], width=2.0, alpha=0.7, edge_color='black')

    # Draw small black nodes on top
    nx.draw_networkx_nodes(G, pos=node_positions, nodelist=G.nodes(), node_color='white', node_size=10, edgecolors='white')
    nx.draw_networkx_edges(G, pos=node_positions, edgelist=G.edges(), width=2.0, alpha=0.7, edge_color='black')
    
    # Show the plot
    plt.axis('off')
    plt.show()


# Main function
def main():
    vertex_file_path = "video_skeleton_vertices.txt"  # Path to vertex coordinates file
    edge_file_path = "skeleton_edges.txt"  # Path to edge list file

    # Define joint colors
    joint_colors = {
        0: 'red',
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'pink',
        6: 'grey',
        7: 'skyblue',
        8: 'brown',
        9: 'green',
        10: 'cyan',
        11: 'orange',
        12: 'orange',
        13: 'green',
        14: 'pink'
        # Add more colors for other joint numbers as needed
    }

    vertex_coordinates = read_vertex_coordinates(vertex_file_path)
    edge_list = read_edge_list(edge_file_path)
    
    plot_skeleton_graph(vertex_coordinates, edge_list, joint_colors)

if __name__ == "__main__":
    main()