def input_graph():
    graph = {}
    num_nodes = int(input("Enter number of nodes: "))
    print("Enter node names:")
    nodes = [input(f"Node {i + 1}: ").strip() for i in range(num_nodes)]

    print("\nEnter the edges and weights between the nodes:")
    for node in nodes:
        graph[node] = {}
        for neighbor in nodes:
            if neighbor != node:
                weight = input(f"Weight from {node} to {neighbor} (enter -1 if no edge): ")
                try:
                    weight = int(weight)
                except ValueError:
                    weight = -1
                if weight != -1:
                    graph[node][neighbor] = weight
    return graph


def shortest_path(graph, source, destination):
    visited = set()
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    predecessors = {}

    while len(visited) < len(graph):
        current_node = None
        min_distance = float('inf')
        for node in graph:
            if distances[node] < min_distance and node not in visited:
                min_distance = distances[node]
                current_node = node

        if current_node is None:
            break

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight
                predecessors[neighbor] = current_node

    path = []
    current_node = destination
    while current_node != source:
        if current_node not in predecessors:
            return None  # No path found
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    path.insert(0, source)
    return path


def discover_route(graph, route_table, source, destination):
    if source not in route_table:
        route_table[source] = {}

    if destination not in route_table[source]:
        path = shortest_path(graph, source, destination)
        if path:
            route_table[source][destination] = path
        else:
            return None

    return route_table[source][destination]


def main():
    graph = input_graph()
    route_table = {}

    while True:
        print("\n--- Menu ---")
        print("1. Find shortest path")
        print("2. Discover route using AODV")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1' or choice == '2':
            source = input("Enter source node: ").strip()
            destination = input("Enter destination node: ").strip()

            if source not in graph or destination not in graph:
                print("Invalid source or destination node.")
                continue

            if choice == '1':
                path = shortest_path(graph, source, destination)
                print(f"Shortest path from {source} to {destination}: {path if path else 'No path found'}")
            else:
                path = discover_route(graph, route_table, source, destination)
                print(f"AODV discovered route from {source} to {destination}: {path if path else 'No route found'}")

        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
