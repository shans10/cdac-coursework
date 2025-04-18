class AONode:
    def __init__(self, name, heuristic_cost):
        self.name = name
        self.heuristic_cost = heuristic_cost  # Heuristic cost of the node
        self.successors = []  # List of AND/OR successor groups
        self.solved = False  # Whether the node is solved
        self.best_successor = None  # Best successor group (optimal path)

    def add_successors(self, successors):
        """
        Add a successor group to the node.
        Each successor group is a list of nodes (AND branch).
        """
        for group in successors:
            if not all(isinstance(child, AONode) for child in group):
                raise ValueError("All children in successors must be instances of AONode.")
        self.successors.extend(successors)

def ao_star(node, trace_path=[]):
    """
    The AO* algorithm to find the optimal solution path.
    """
    if node.solved:
        return node.solved

    print(f"Visiting Node: {node.name}")
    trace_path.append(node.name)

    # If it's a leaf node, mark it as solved
    if not node.successors:
        node.solved = True
        trace_path.pop()
        return True

    # Evaluate all successor groups to find the best one
    min_cost = float('inf')
    best_successor = None

    for successors in node.successors:
        # Compute the total cost for this group
        total_cost = sum(child.heuristic_cost for child in successors)
        if total_cost < min_cost:
            min_cost = total_cost
            best_successor = successors

    # Set the best successor group
    node.best_successor = best_successor

    # Recursively solve the best successor group
    all_solved = True
    for child in best_successor:
        if not ao_star(child, trace_path):
            all_solved = False

    # If all successors in the best group are solved, mark the node as solved
    node.solved = all_solved
    if all_solved:
        node.heuristic_cost = min_cost

    trace_path.pop()
    return node.solved

def print_solution(node):
    """
    Print the solution path found by the AO* algorithm.
    """
    if not node or not node.best_successor:
        return
    print(f"Node {node.name} -> ", [child.name for child in node.best_successor])
    for child in node.best_successor:
        print_solution(child)

# Example usage
if __name__ == "__main__":
    # Creating an example And-Or graph
    A = AONode("A", 10)
    B = AONode("B", 8)
    C = AONode("C", 7)
    D = AONode("D", 6)
    E = AONode("E", 5)

    # Define successors (AND/OR groups)
    A.add_successors([[B, C]])  # AND group: A -> {B AND C}
    A.add_successors([[D]])    # OR group: A -> D
    B.add_successors([[E]])    # OR group: B -> E

    # Run AO* algorithm
    trace_path = []
    ao_star(A, trace_path)

    print("\nSolution Path:")
    print_solution(A)
