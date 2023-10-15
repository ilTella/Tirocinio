import math
from .single_agent_planner import a_star

def get_euclidean_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return round((math.sqrt((x2 - x1)**2 + (y2 - y1)**2)), 2)

def get_shortest_path_length(map: list[list[bool]], start_node: tuple[int, int], goal_node: tuple[int, int], heuristics: dict) -> int:
    path = a_star(map, start_node, goal_node, heuristics, 0, [])
    return len(path) - 1