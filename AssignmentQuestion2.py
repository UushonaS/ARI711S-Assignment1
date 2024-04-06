import random

distance_matrix = [
    [0, 7, 20, 15, 12],
    [10, 0, 6, 14, 18],
    [20, 6, 0, 15, 30],
    [15, 14, 25, 0, 2],
    [12, 18, 30, 2, 0]
]
def total_distance(path):
    
    total = 0
    for i in range(len(path) - 1):
        total += distance_matrix[path[i]][path[i+1]]
    total += distance_matrix[path[-1]][path[0]]  
    return total

def hill_climbing_tsp(num_places, max_iterations=10000):
    current_path = list(range(num_places))  
    current_distance = total_distance(current_path) 
    for _ in range(max_iterations):
        
        neighbor_path = current_path.copy()
        i, j = random.sample(range(num_places), 2)
        neighbor_path[i], neighbor_path[j] = neighbor_path[j], neighbor_path[i]
        neighbor_distance = total_distance(neighbor_path)
        
        
        if neighbor_distance < current_distance:
            current_path = neighbor_path
            current_distance = neighbor_distance
    return current_path


def main():
    num_places = 5  
    solution = hill_climbing_tsp(num_places)
    print("Optimal path:", solution)
    print("Total distance:", total_distance(solution), "kilometers")
if __name__ == "__main__":
    main()