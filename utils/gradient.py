import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
import matplotlib.patches as patches

# # Read vertex coordinates from a text file
# def read_vertex_coordinates(file_path):
#     vertex_coordinates = {}
#     with open(file_path, 'r') as file:
#         for idx, line in enumerate(file):
#             x, y = map(float, line.strip().split())
#             vertex_coordinates[idx] = (x*512, y*512)
#     return vertex_coordinates

def read_vertex_coordinates(file_path, image_width, image_height):
    vertex_coordinates = {}
    with open(file_path, 'r') as file:
        for idx, line in enumerate(file):
            x, y = map(float, line.strip().split())
            # Scale the coordinates according to the image dimensions
            # scaled_x = x * image_width
            # scaled_y = y * image_height
            # vertex_coordinates[idx] = (scaled_x, scaled_y)
            vertex_coordinates[idx] = (x, y)
    return vertex_coordinates


# Read edge list from a text file
def read_edge_list(file_path):
    edge_list = []
    with open(file_path, 'r') as file:
        for line in file:
            v1, v2 = map(int, line.strip().split())
            edge_list.append((v1, v2))
    return edge_list

# # Plot skeleton graph over image
# def plot_skeleton_over_image(image_path, vertex_coordinates, edge_list):
#     # Read the image
#     img = plt.imread(image_path)

#     # Plot the image
#     plt.figure(figsize=(8, 6))
#     plt.imshow(img)

#     # Create an empty graph
#     G = nx.Graph()

#     # Add vertices with coordinates to the graph
#     for vertex, coords in vertex_coordinates.items():
#         G.add_node(vertex, pos=coords)

#     # Add edges to the graph
#     G.add_edges_from(edge_list)

#     # Get node positions
#     node_positions = nx.get_node_attributes(G, 'pos')

#     # Draw the graph over the image
#     # nx.draw_networkx_nodes(G, pos=node_positions, node_color='white', node_size=50, edgecolors='black')
#     # nx.draw_networkx_edges(G, pos=node_positions, width=2.0, alpha=0.7, edge_color='black')

#     # nx.draw_networkx_nodes(G, pos=node_positions, node_color='black', node_size=10, edgecolors='black')
#     # nx.draw_networkx_edges(G, pos=node_positions, width=2.0, alpha=0.7, edge_color='black')

#     nx.draw_networkx_nodes(G, pos=node_positions, node_color='white', node_size=60, edgecolors='black', linewidths=0.1)
#     nx.draw_networkx_edges(G, pos=node_positions, width=1.0, alpha=0.7, edge_color='black')

#     nx.draw_networkx_nodes(G, pos=node_positions, node_color='black', node_size=5, edgecolors='black')
#     nx.draw_networkx_edges(G, pos=node_positions, width=1.5, alpha=0.7, edge_color='black')
#     # Draw outer circles over vertex coordinates
#     for vertex, coords in vertex_coordinates.items():
#         x, y = coords
#         plt.gca().add_patch(patches.Circle((x, y), radius=2, edgecolor='black', facecolor='black'))


#     plt.axis('off')
#     plt.show()


# # # Main function
# # def main():
# #     image_path = "videoframe.png"  # Path to your image
# #     vertex_file_path = "video_skeleton_vertices.txt"  # Path to vertex coordinates file
# #     edge_file_path = "skeleton_edges.txt"  # Path to edge list file

# #     vertex_coordinates = read_vertex_coordinates(vertex_file_path)
# #     edge_list = read_edge_list(edge_file_path)
    
# #     plot_skeleton_over_image(image_path, vertex_coordinates, edge_list)

# # if __name__ == "__main__":
# #     main()


# def main():
#     image_path = "sketch.png"  # Path to your image
#     vertex_file_path = "sketch_skeleton_vertices.txt"  # Path to vertex coordinates file
#     edge_file_path = "skeleton_edges.txt"  # Path to edge list file

#     # Read the image dimensions
#     img = plt.imread(image_path)
#     image_height, image_width, _ = img.shape

#     vertex_coordinates = read_vertex_coordinates(vertex_file_path, image_width, image_height)
#     edge_list = read_edge_list(edge_file_path)
    
#     plot_skeleton_over_image(image_path, vertex_coordinates, edge_list)

# if __name__ == "__main__":
#     main()

# Plot skeleton graph over image
def plot_skeleton_over_image(image_path, vertex_coordinates, edge_list, alpha=1.0, foreground_alpha=1):
    # Read the image
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

    # Draw the graph over the image with adjusted alpha
    nx.draw_networkx_nodes(G, pos=node_positions, node_color='white', node_size=60, edgecolors='black', linewidths=0.1, alpha=foreground_alpha)
    nx.draw_networkx_edges(G, pos=node_positions, width=1.0, alpha=foreground_alpha*0.7, edge_color='black')

    nx.draw_networkx_nodes(G, pos=node_positions, node_color='black', node_size=5, edgecolors='black', alpha=foreground_alpha)
    nx.draw_networkx_edges(G, pos=node_positions, width=1.5, alpha=foreground_alpha*0.7, edge_color='black')

    # Draw outer circles over vertex coordinates with adjusted alpha
    for vertex, coords in vertex_coordinates.items():
        x, y = coords
        plt.gca().add_patch(patches.Circle((x, y), radius=2, edgecolor='black', facecolor='black', alpha=foreground_alpha))

    plt.axis('off')
    plt.show()


# Main function
def main():
    image_path = "sketch.png"  # Path to your image
    vertex_file_path = "frame14.txt"  # Path to vertex coordinates file
    edge_file_path = "skeleton_edges.txt"  # Path to edge list file

    # Read the image dimensions
    img = plt.imread(image_path)
    image_height, image_width, _ = img.shape

    vertex_coordinates = read_vertex_coordinates(vertex_file_path, image_width, image_height)
    edge_list = read_edge_list(edge_file_path)
    
    plot_skeleton_over_image(image_path, vertex_coordinates, edge_list, alpha=0, foreground_alpha=1)  # Set alpha value here

if __name__ == "__main__":
    main()

