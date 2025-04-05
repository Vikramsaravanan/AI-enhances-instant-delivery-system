import networkx as nx
import osmnx as ox

def get_shortest_path(start_coords, end_coords):
    G = ox.graph_from_place("Manhattan, New York", network_type="drive")
    start_node = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0])
    end_node = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0])
    route = nx.shortest_path(G, start_node, end_node, weight="length")
    return route