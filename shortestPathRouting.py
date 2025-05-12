import heapq

# Function to get the graph from user
def get_network_graph():
    nodes = int(input("Enter number of routers/nodes: "))
    graph = {i: {} for i in range(nodes)}

    print("\nEnter the adjacency matrix (enter 0 for no direct connection):")
    for i in range(nodes):
        for j in range(nodes):
            cost = int(input(f"Cost from node {i} to node {j}: "))
            if cost != 0:
                graph[i][j] = cost
    return graph, nodes

# Function to display routing table
def display_routing_table(distances, source):
    print(f"\nRouting Table for Router {source}:")
    print("Destination\tCost")
    for dest in sorted(distances.keys()):
        print(f"{dest}\t\t{distances[dest]}")

# Function to perform Dijkstra’s Algorithm
def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    priority_queue = [(0, source)]
    while priority_queue:
        curr_dist, curr_node = heapq.heappop(priority_queue)

        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Main function to simulate routing
def main():
    graph, total_nodes = get_network_graph()
    
    for source in range(total_nodes):
        distances = dijkstra(graph, source)
        display_routing_table(distances, source)

if __name__ == "__main__":
    main()
