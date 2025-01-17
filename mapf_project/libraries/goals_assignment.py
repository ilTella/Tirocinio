from .single_agent_planner import compute_heuristics
from .utils import get_shortest_path_length
from random import shuffle, seed
import munkres

LOCAL_SEARCH_TRAJECTORIES = 5

def search_goals_assignment_hungarian(map: list[list[bool]], starts: list[tuple[int, int]], goal_positions: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # the Hungarian algorithm is used to return an optimal agent-goal assignment
    # cost for each couple (agent start, goal) is calculated with A*
    new_goals = []
    cost = 0

    path_length_matrix = get_path_length_matrix(map, starts, goal_positions)

    m = munkres.Munkres()
    indexes = m.compute(path_length_matrix)
    for row, col in indexes:
        cost += path_length_matrix[row][col]
        new_goals.append(goal_positions[col])

    return new_goals, cost

def search_goals_assignment_local_search(map: list[list[bool]], starts: list[tuple[int, int]], goal_positions: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # returns an assignment found with a local search, not garanteed to be optimal
    seed()
    new_goals = []

    path_length_matrix = get_path_length_matrix(map, starts, goal_positions)
    
    # local search begins from a random assignments, then works to improve it
    initial_assignments_container = []
    for _ in range(LOCAL_SEARCH_TRAJECTORIES):
        initial_assignment = []
        for i in range(len(goal_positions)):
            initial_assignment.append(i)
        shuffle(initial_assignment)
        initial_assignments_container.append(initial_assignment)

    costs = []
    explored_assignments_container = []
    for i in range(LOCAL_SEARCH_TRAJECTORIES):
        costs.append(get_assignment_cost_astar(path_length_matrix, initial_assignments_container[i])) 
        explored_assignments_container.append({})
        explored_assignments_container[i][tuple(initial_assignments_container[i])] = costs[i]

    chosen_assignments = []
    for i in range(LOCAL_SEARCH_TRAJECTORIES):
        chosen_assignments.append(initial_assignments_container[i])

    candidate_assignments_container = []
    for i in range(LOCAL_SEARCH_TRAJECTORIES):
        candidate_assignments_container.append([initial_assignments_container[0]])

    # multiple "trajectories" are considered:
    # the local search starts from different random assignments, then the best outcome is chosen
    for traj in range(LOCAL_SEARCH_TRAJECTORIES):

        while (len(candidate_assignments_container[traj]) >= 1):
            assignment = candidate_assignments_container[traj].pop()

            go_on = True
            while(go_on):
                go_on = False
                # the algorithm improves the assignment by switching indexes and checking if the cost has been reduced
                for i in range(len(assignment)):
                    for j in range(i + 1, len(assignment)):
                        new_assignment = swap_assigment_indexes(assignment.copy(), i, j)
                        if tuple(new_assignment) in explored_assignments_container[traj]:
                            continue
                        new_cost = get_assignment_cost_astar(path_length_matrix, new_assignment)
                        explored_assignments_container[traj][tuple(new_assignment)] = new_cost
                        if new_cost == costs[traj]:
                            candidate_assignments_container[traj].append(new_assignment)
                        elif new_cost < costs[traj]:
                            candidate_assignments_container[traj] = [new_assignment]
                            chosen_assignments[traj] = new_assignment
                            costs[traj] = new_cost
                            go_on = True
                            break
                    else:
                        continue
                    break 

    final_assignment = chosen_assignments[0]
    final_cost = costs[0]

    for i in range(LOCAL_SEARCH_TRAJECTORIES):
        if costs[i] < final_cost:
            final_cost = costs[i]
            final_assignment = chosen_assignments[i]

    for i in final_assignment:
        new_goals.append(goal_positions[i])

    return new_goals, final_cost

def get_random_goal_assignment(map: list[list[bool]], starts: list[tuple[int, int]], goal_positions: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # returns a randomly generated agent-goal assignment
    seed()
    new_goals = []
    
    assignment = []
    for i in range(len(goal_positions)):
        assignment.append(i)
    shuffle(assignment)
    for i in assignment:
        new_goals.append(goal_positions[i])

    matrix = get_path_length_matrix(map, starts, goal_positions)
    cost = get_assignment_cost_astar(matrix, assignment)

    return new_goals, cost

def get_path_length_matrix(map: list[list[bool]], starts: list[tuple[int, int]], goal_positions: list[tuple[int, int]]) -> list[list[int]]:
    path_length_matrix = []
    for _ in range(len(starts)):
        path_length_matrix.append([])
    
    for g in range(len(goal_positions)):
        heuristics = compute_heuristics(map, goal_positions[g])
        for s in range(len(starts)):
            path_length_matrix[s].append(get_shortest_path_length(map, starts[s], goal_positions[g], heuristics))
 
    return path_length_matrix

def get_assignment_cost_astar(path_length_matrix: list[list[int]], assignment: list[int]) -> int:
    total = 0

    i = 0
    for j in range(len(assignment)):
        total += path_length_matrix[i][assignment[j]]
        i += 1

    return total

def swap_assigment_indexes(assignment: list[int], index1: int, index2: int) -> None:
    temp = assignment[index1]
    assignment[index1] = assignment[index2]
    assignment[index2] = temp
    return assignment

def print_goals_assignment(goals: list[tuple[int, int]]) -> None:
    for i in range(len(goals)):
        print("agent " + str(i) + " goes to: " + str(goals[i][1]) + ", " + str(goals[i][0]))