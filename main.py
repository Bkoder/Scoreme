def longest_path(graph: list) -> int:
    n = len(graph)

    # Step 1: Perform Topological Sorting
    def topological_sort(graph):
        indegree = [0] * n
        for u in range(n):
            for v, _ in graph[u]:
                indegree[v] += 1

        zero_indegree_queue = [u for u in range(n) if indegree[u] == 0]
        topo_order = []

        while zero_indegree_queue:
            u = zero_indegree_queue.pop(0)
            topo_order.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    zero_indegree_queue.append(v)

        return topo_order

    # Step 2: Calculate Longest Path using Topological Sort
    def calculate_longest_path(graph, topo_order):
        dist = [-float('inf')] * n
        for node in topo_order:
            if dist[node] == -float('inf'):
                dist[node] = 0
            for neighbor, weight in graph[node]:
                if dist[node] + weight > dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
        return max(dist)

    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)


# Example Usage
if __name__ == "__main__":
    graph1 = [
        [(1, 1), (2, 1)],
        [(3, 1)],
        [(3, 1)],
        []
    ]
    print(longest_path(graph1))  # Output should be 3
