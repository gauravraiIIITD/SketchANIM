import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as patches
# Read vertex coordinates from a text file
# def read_vertex_coordinates(file_path):
#     vertex_coordinates = {}
#     with open(file_path, 'r') as file:
#         for idx, line in enumerate(file):
#             x, y = map(float, line.strip().split())
#             vertex_coordinates[idx] = (x*2048, y*2048)
#     return vertex_coordinates

def read_vertex_coordinates(file_path, image_width, image_height):
    vertex_coordinates = {}
    with open(file_path, 'r') as file:
        for idx, line in enumerate(file):
            x, y = map(float, line.strip().split())
            # Scale the coordinates according to the image dimensions
            scaled_x = x * image_width
            scaled_y = y * image_height
            vertex_coordinates[idx] = (scaled_x, scaled_y)
            # vertex_coordinates[idx] = (x*512, y*512)
    return vertex_coordinates

# Read edge list from a text file
def read_edge_list(file_path):
    edge_list = []
    with open(file_path, 'r') as file:
        for line in file:
            v1, v2 = map(int, line.strip().split())
            edge_list.append((v1, v2))
    return edge_list

def plot_skeleton_graph(image_path, vertex_coordinates, edge_list, joint_colors, joint_to_vertex, alpha=1.0, foreground_alpha=1):
    img = plt.imread(image_path)

    # Plot the image
    plt.figure(figsize=(8, 6))
    plt.imshow(img, alpha=alpha)  # Set alpha for the background image

    # Create an empty graph
    G = nx.Graph()

    # Add vertices with coordinates to the graph
    for vertex, coords in vertex_coordinates.items():
        G.add_node(vertex, pos=coords)

    # Add edges to the graph
    G.add_edges_from(edge_list)

    # Get node positions
    node_positions = nx.get_node_attributes(G, 'pos')

    # Draw the graph with different colors for each joint number
    for joint_number, color in joint_colors.items():
        vertices = joint_to_vertex.get(joint_number, [])  # Get vertices corresponding to the joint
        nodes = [node for node in G.nodes() if node in vertices]  # Filter nodes by vertices
        nx.draw_networkx_nodes(G, pos=node_positions, nodelist=nodes, node_color=color, node_size=60, edgecolors='black', linewidths=0.1, alpha=foreground_alpha)

    # Draw remaining nodes and edges
    nx.draw_networkx_nodes(G, pos=node_positions, node_color='black', node_size=5, edgecolors='black', alpha=foreground_alpha)
    nx.draw_networkx_edges(G, pos=node_positions, width=1.5, alpha=foreground_alpha*0.7, edge_color='black')

    # Adjust axes and display
    plt.axis('off')
    plt.show()


# Main function
def main():
    image_path = "videoframe.png"
    vertex_file_path = "video_skeleton_vertices.txt"  # Path to vertex coordinates file
    edge_file_path = "skeleton_edges.txt"  # Path to edge list file

    # Define joint colors
    joint_colors = {
        0: 'cyan',
        1: 'red',
        2: 'cyan',
        3: 'lightgreen',
        4: 'pink',
        5: 'violet',
        6: 'lightgreen',
        7: 'pink',
        8: 'violet',
        9: 'cyan',
        10: 'lightgreen',
        11: 'pink',
        12: 'cyan',
        13: 'lightgreen',
        14: 'pink'
        # Add more colors for other joint numbers as needed
    }

    # joint_colors = {
    #     0: 'white',
    #     1: 'white',
    #     2: 'white',
    #     3: 'white',
    #     4: 'white',
    #     5: 'white',
    #     6: 'white',
    #     7: 'white',
    #     8: 'white',
    #     9: 'white',
    #     10: 'white',
    #     11: 'white',
    #     12: 'white',
    #     13: 'white',
    #     14: 'white'
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
    # Read the image dimensions
    img = plt.imread(image_path)
    image_height, image_width, _ = img.shape

    vertex_coordinates = read_vertex_coordinates(vertex_file_path, image_width, image_height)
    edge_list = read_edge_list(edge_file_path)
    
    plot_skeleton_graph(image_path, vertex_coordinates, edge_list, joint_colors, joint_to_vertex, alpha=0, foreground_alpha=1)

if __name__ == "__main__":
    main()

