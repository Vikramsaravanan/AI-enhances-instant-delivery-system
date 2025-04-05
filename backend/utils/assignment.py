import numpy as np
from scipy.optimize import linear_sum_assignment

def assign_orders_to_agents(agents, orders):
    """
    Assigns orders to agents using the Hungarian Algorithm.
    
    Args:
        agents: List of agent coordinates [(lat1, lon1), (lat2, lon2), ...]
        orders: List of order coordinates [(lat1, lon1), (lat2, lon2), ...]
    
    Returns:
        List of tuples: [(agent_index, order_index, distance), ...]
    """
    # Calculate distance matrix (using Haversine or Euclidean for simplicity)
    distance_matrix = np.zeros((len(agents), len(orders)))
    for i, agent in enumerate(agents):
        for j, order in enumerate(orders):
            distance_matrix[i][j] = haversine_distance(agent, order)
    
    # Apply Hungarian Algorithm
    agent_indices, order_indices = linear_sum_assignment(distance_matrix)
    
    assignments = []
    for a_idx, o_idx in zip(agent_indices, order_indices):
        assignments.append({
            "agent_id": a_idx,
            "order_id": o_idx,
            "distance_km": distance_matrix[a_idx][o_idx]
        })
    
    return assignments

def haversine_distance(coord1, coord2):
    """
    Calculate Haversine distance between two (lat, lon) points in kilometers.
    """
    from math import radians, sin, cos, sqrt, atan2
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return 6371 * c  # Earth radius in km

# Example usage
if __name__ == "__main__":
    agents = [(40.7128, -74.0060), (40.7214, -73.9882)]  # Agent locations
    orders = [(40.7356, -73.9905), (40.7021, -74.0150)]   # Order locations
    
    assignments = assign_orders_to_agents(agents, orders)
    print("Optimal Assignments:", assignments)