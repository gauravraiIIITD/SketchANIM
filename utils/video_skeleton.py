import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import os
import imageio

# # Read vertex coordinates from a text file
# def read_vertex_coordinates(file_path):
#     frames = []
#     with open(file_path, 'r') as file:
#         frame = {}
#         for idx, line in enumerate(file):
#             if line.strip() == "":
#                 frames.append(frame)
#                 frame = {}
#             else:
#                 x, y = map(float, line.strip().split())
#                 frame[idx] = (x, y)
#     return frames

# Read vertex coordinates from a text file
def read_vertex_coordinates(file_path):
    frames = []
    with open(file_path, 'r') as file:
        frame = {}
        frame_index = 0
        for line in file:
            if line.strip() == "":
                frames.append(frame)
                frame_index += 1
                frame = {}
            else:
                coordinates = line.strip().split()
                x, y = map(float, coordinates[:2])  # Consider only the first two values
                frame[frame_index] = frame.get(frame_index, []) + [(x, y)]
    return frames


# Read edge list from a text file
def read_edge_list(file_path):
    edge_list = []
    with open(file_path, 'r') as file:
        for line in file:
            v1, v2 = map(int, line.strip().split())
            edge_list.append((v1, v2))
    return edge_list

# Plot skeleton graph for a single frame
def plot_skeleton_graph(vertex_coordinates, edge_list, frame_index, output_folder):
    # Create an empty graph
    G = nx.Graph()

    # Add vertices with coordinates to the graph
    for vertex, coords in vertex_coordinates[frame_index].items():
        G.add_node(vertex, pos=coords)

    # Add edges to the graph
    G.add_edges_from(edge_list)

    # Get node positions
    node_positions = nx.get_node_attributes(G, 'pos')

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos=node_positions, node_color='blue', node_size=50, edgecolors='black')
    nx.draw_networkx_edges(G, pos=node_positions, width=2.0, alpha=0.7, edge_color='gray')
    plt.axis('off')

    # Save the plot as an image
    output_file = os.path.join(output_folder, f"frame_{frame_index}.png")
    plt.savefig(output_file)
    plt.close()

# Create GIF from frames
def create_gif(frames_folder, output_gif):
    images = []
    for filename in sorted(os.listdir(frames_folder)):
        if filename.endswith('.png'):
            file_path = os.path.join(frames_folder, filename)
            images.append(imageio.imread(file_path))
    imageio.mimsave(output_gif, images, duration=0.5)

# Main function
def main():
    vertex_file_path = "skeleton_vertices_across_frames.txt"  # Path to vertex coordinates file
    edge_file_path = "skeleton_edges.txt"  # Path to edge list file
    output_folder = "frames"  # Folder to save individual frames
    output_gif = "skeleton_animation.gif"  # Output GIF file path

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    vertex_frames = read_vertex_coordinates(vertex_file_path)
    edge_list = read_edge_list(edge_file_path)
    
    # Plot and save each frame
    for frame_index in range(len(vertex_frames)):
        plot_skeleton_graph(vertex_frames, edge_list, frame_index, output_folder)

    # Create GIF from frames
    create_gif(output_folder, output_gif)

    # Remove individual frames
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        os.remove(file_path)
    os.rmdir(output_folder)

if __name__ == "__main__":
    main()
