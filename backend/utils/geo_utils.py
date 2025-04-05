import osmnx as ox
import networkx as nx
from typing import Tuple, List

def get_road_network(city: str) -> nx.Graph:
    """
    Fetch real-world road network data using OSMnx.
    
    Args:
        city: String like "Manhattan, New York"
    
    Returns:
        NetworkX graph representing the road network.
    """
    return ox.graph_from_place(city, network_type="drive")

def shortest_path(coords: Tuple[float, float], 
                 destination: Tuple[float, float],
                 city: str = "Manhattan, New York") -> List[Tuple[float, float]]:
    """
    Calculate shortest path between two points using real roads.
    
    Args:
        coords: (lat, lon) of start point
        destination: (lat, lon) of end point
        city: City name for road network context
    
    Returns:
        List of (lat, lon) points along the route
    """
    G = get_road_network(city)
    orig_node = ox.distance.nearest_nodes(G, coords[1], coords[0])
    dest_node = ox.distance.nearest_nodes(G, destination[1], destination[0])
    
    route = nx.shortest_path(G, orig_node, dest_node, weight="length")
    return [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in route]

def travel_time(coords: Tuple[float, float], 
               destination: Tuple[float, float],
               avg_speed_kmh: float = 30) -> float:
    """
    Estimate travel time between two points (simplified).
    """
    distance_km = haversine_distance(coords, destination)
    return (distance_km / avg_speed_kmh) * 60  # Minutes

# Example usage
if __name__ == "__main__":
    start = (40.7128, -74.0060)  # NYC coordinates
    end = (40.7214, -73.9882)
    
    route = shortest_path(start, end)
    print(f"Route with {len(route)} waypoints:", route[:3], "...")
    
    time = travel_time(start, end)
    print(f"Estimated travel time: {time:.1f} minutes")