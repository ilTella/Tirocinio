from enum import Enum

class GoalsChoice(Enum):
    GREEDY_MINIMIZE_DISTANCE = 1            # incomplete, suboptimal

class GoalsAssignment(Enum):
    ARBITRARY = 1                           # suboptimal
    RANDOM = 2                              # suboptimal
    GREEDY = 3                              # suboptimal
    EXHAUSTIVE_SEARCH_ASTAR = 4             # suboptimal (does not consider collisions), impractical for medium-large instances
    MINIMIZE_DISTANCE_ASTAR = 5             # suboptimal (does not consider collisions)
    MINIMIZE_DISTANCE_CBS = 6               # optimal

class ConnectionCriterion(Enum):
    NONE = 1
    DISTANCE = 2
    PATH_LENGTH = 3