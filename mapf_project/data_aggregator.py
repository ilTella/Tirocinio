import os
import sys
import matplotlib.pyplot as plt
import numpy as np

def aggregate_data() -> None:
    number_of_cliques = []

    uninformed_optimality_values = []
    uninformed_times = []
    informed_optimality_values = []
    informed_times = []

    hungarian_heuristic_values = []
    hungarian_cbs_values = []
    hungarian_times = []
    random_heuristic_values = []
    random_cbs_values = []

    informed_times_non_verbose = []

    for filename in os.listdir("./outputs/"):
        path = "./outputs/" + filename
        specs = filename.split("_test_")[0]
        with open(path, 'r') as f:
            while True:
                line = f.readline()
                if line == "":
                    break
                if "Cliques found" in line:
                    elements = line.split(": ")
                    number_of_cliques.append(specs + ":" + elements[1].strip())
                if "Uninformed clique generation optimality" in line:
                    elements = line.split(": ")
                    uninformed_optimality_values.append(specs + ":" + elements[1].strip())
                if "Informed clique generation optimality" in line:
                    elements = line.split(": ")
                    informed_optimality_values.append(specs + ":" + elements[1].strip())
                if "Goals positions (uninformed clique generation) search time" in line:
                    elements = line.split(": ")
                    uninformed_times.append(specs + ":" + elements[1].strip())
                if "Goals positions (informed clique generation) search time" in line:
                    elements = line.split(": ")
                    informed_times.append(specs + ":" + elements[1].strip())
                if "Goals generation time" in line:
                    elements = line.split(": ")
                    informed_times_non_verbose.append(specs + ":" + elements[1].strip())
                if "Hungarian algorithm heuristic cost" in line:
                    elements = line.split(": ")
                    hungarian_heuristic_values.append(specs + ":" + elements[1].strip())
                if "Hungarian algorithm time" in line:
                    elements = line.split(": ")
                    hungarian_times.append(specs + ":" + elements[1].strip())
                if "Hungarian algorithm CBS cost" in line:
                    elements = line.split(": ")
                    if elements[1].strip() == "not found":
                        hungarian_cbs_values.append(specs + ":" + str(-1))
                    else:
                        hungarian_cbs_values.append(specs + ":" + elements[1].strip())
                if "Random assignment heuristic cost" in line:
                    elements = line.split(": ")
                    random_heuristic_values.append(specs + ":" + elements[1].strip())
                if "Random assignment CBS cost" in line:
                    elements = line.split(": ")
                    if elements[1].strip() == "not found":
                        random_cbs_values.append(specs + ":" + str(-1))
                    else:
                        random_cbs_values.append(specs + ":" + elements[1].strip())

    f = open("./data/number_of_cliques.txt", "w")      
    sys.stdout = f
    for value in number_of_cliques:
        print(value)

    f = open("./data/uninformed_optimality_values.txt", "w")      
    sys.stdout = f
    for value in uninformed_optimality_values:
        print(value)

    f = open("./data/informed_optimality_values.txt", "w")      
    sys.stdout = f
    for value in informed_optimality_values:
        print(value)

    f = open("./data/uninformed_times.txt", "w")      
    sys.stdout = f
    for value in uninformed_times:
        print(value)

    f = open("./data/informed_times.txt", "w")      
    sys.stdout = f
    for value in informed_times:
        print(value)

    f = open("./data/informed_times_non_verbose.txt", "w")      
    sys.stdout = f
    for value in informed_times_non_verbose:
        print(value)
    
    f = open("./data/hungarian_heuristic_values.txt", "w")      
    sys.stdout = f
    for value in hungarian_heuristic_values:
        print(value)
    
    f = open("./data/hungarian_cbs_values.txt", "w")      
    sys.stdout = f
    for value in hungarian_cbs_values:
        print(value)
    
    f = open("./data/hungarian_times.txt", "w")      
    sys.stdout = f
    for value in hungarian_times:
        print(value)
    
    f = open("./data/random_heuristic_values.txt", "w")      
    sys.stdout = f
    for value in random_heuristic_values:
        print(value)
    
    f = open("./data/random_cbs_values.txt", "w")      
    sys.stdout = f
    for value in random_cbs_values:
        print(value)

    sys.stdout = sys.__stdout__

def generate_charts() -> None:
    # uninformed/informed goals generation times
    D = [[],[]]
    f = open("./data/uninformed_times.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            D[0].append(float(value))
    f = open("./data/informed_times.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            D[1].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["Uninformed", "Informed"], showfliers=False)
    ax.set_title("Goals generation execution time")
    ax.set_ylabel("seconds")
    plt.show()

    # uninformed/informed optimality
    D = [[],[]]
    f = open("./data/uninformed_optimality_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            D[0].append(float(value))
    f = open("./data/informed_optimality_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            D[1].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["Uninformed", "Informed"], showmeans=True)
    ax.set_title("Optimality")
    plt.show()

    # uninformed/informed optimality related to number of cliques
    x = []
    y = []
    f = open("./data/uninformed_optimality_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            x.append(float(value))
    f = open("./data/number_of_cliques.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            y.append(int(value))

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("Optimality related to number of cliques")
    ax.set_xlabel("Uninformed generation goals optimality")
    ax.set_ylabel("Number of cliques")
    plt.show()

    x = []
    f = open("./data/informed_optimality_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            x.append(float(value))

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("Optimality related to number of cliques")
    ax.set_xlabel("Informed generation goals optimality")
    ax.set_ylabel("Number of cliques")
    plt.show()

    # Hungarian algorithm execution times
    x = []
    f = open("./data/hungarian_times.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            x.append(float(value))
    fig, ax = plt.subplots()
    ax.hist(x, bins=6)
    ax.set_title("Hungarian algorithm execution time")
    ax.set_xlabel("seconds")
    plt.show()

    # Hungarian/random goals assignment heuristic (A*) costs
    hungarian_heuristic_costs = []
    random_heuristic_costs = []
    f = open("./data/hungarian_heuristic_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            hungarian_heuristic_costs.append(int(value))
    f = open("./data/random_heuristic_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            random_heuristic_costs.append(int(value))
    percentages = []
    for i in range(len(hungarian_heuristic_costs)):
        diff = ((random_heuristic_costs[i] - hungarian_heuristic_costs[i]) / random_heuristic_costs[i]) * 100
        percentages.append(diff)

    fig, ax = plt.subplots()
    ax.boxplot(percentages, labels=[""])
    ax.set_title("Difference in heuristic cost (A*)\nusing Hungarian algorithm vs. random assignment")
    ax.set_ylabel("%")
    plt.show()

    # Hungarian/random goals assignment real (CBS) costs

    hungarian_cbs_costs = []
    random_cbs_costs = []
    f = open("./data/hungarian_cbs_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            hungarian_cbs_costs.append(int(value))
    f = open("./data/random_cbs_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            random_cbs_costs.append(int(value))
    percentages = []
    for i in range(len(hungarian_cbs_costs)):
        if random_cbs_costs[i] == -1 or hungarian_cbs_costs[i] == -1:
            continue
        diff = ((random_cbs_costs[i] - hungarian_cbs_costs[i]) / random_cbs_costs[i]) * 100
        percentages.append(diff)

    fig, ax = plt.subplots()
    ax.boxplot(percentages, labels=[""])
    ax.set_title("Difference in cost (CBS)\nusing Hungarian algorithm vs. random assignment")
    ax.set_ylabel("%")
    plt.show()

    # optimality related to different sizes

    D = [[],[],[],[]]
    f = open("./data/uninformed_optimality_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            if "s8" in specs:
                D[0].append(float(value))
            if "s10" in specs:
                D[1].append(float(value))
            if "s12" in specs:
                D[2].append(float(value))
            if "s15" in specs:
                D[3].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["8x8", "10x10", "12x12", "15x15"], showmeans=True)
    ax.set_title("Optimality related to map size\n(uninformed generation)")
    ax.set_xlabel("Map size")
    plt.show()

    D = [[],[],[],[]]
    f = open("./data/informed_optimality_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            if "s8" in specs:
                D[0].append(float(value))
            if "s10" in specs:
                D[1].append(float(value))
            if "s12" in specs:
                D[2].append(float(value))
            if "s15" in specs:
                D[3].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["8x8", "10x10", "12x12", "15x15"], showmeans=True)
    ax.set_title("Optimality related to map size\n(informed generation)")
    ax.set_xlabel("Map size")
    plt.show()
    
    # execution time related to different sizes

    D = [[],[],[],[]]
    f = open("./data/uninformed_times.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            if "s8" in specs:
                D[0].append(float(value))
            if "s10" in specs:
                D[1].append(float(value))
            if "s12" in specs:
                D[2].append(float(value))
            if "s15" in specs:
                D[3].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["8x8", "10x10", "12x12", "15x15"], showfliers=False)
    ax.set_title("Execution time related to map size\n(uninformed generation)")
    ax.set_ylabel("seconds")
    ax.set_xlabel("Map size")
    plt.show()

    D = [[],[],[],[]]
    f = open("./data/informed_times.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            if "s8" in specs:
                D[0].append(float(value))
            if "s10" in specs:
                D[1].append(float(value))
            if "s12" in specs:
                D[2].append(float(value))
            if "s15" in specs:
                D[3].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["8x8", "10x10", "12x12", "15x15"], showfliers=False)
    ax.set_title("Execution time related to map size\n(informed generation)")
    ax.set_ylabel("seconds")
    ax.set_xlabel("Map size")
    plt.show()

    # optimality related to different densities

    D = [[],[],[]]
    f = open("./data/uninformed_optimality_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            if "d10" in specs:
                D[0].append(float(value))
            if "d20" in specs:
                D[1].append(float(value))
            if "d30" in specs:
                D[2].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["10%", "20%", "30%"], showmeans=True)
    ax.set_title("Optimality related to obstacles density\n(uninformed generation)")
    ax.set_xlabel("Obstacles density")
    plt.show()

    D = [[],[],[]]
    f = open("./data/informed_optimality_values.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            if "d10" in specs:
                D[0].append(float(value))
            if "d20" in specs:
                D[1].append(float(value))
            if "d30" in specs:
                D[2].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["10%", "20%", "30%"], showmeans=True)
    ax.set_title("Optimality related to obstacles density\n(informed generation)")
    ax.set_xlabel("Obstacles density")
    plt.show()

    # execution time related to different densities

    D = [[],[],[]]
    f = open("./data/uninformed_times.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            if "d10" in specs:
                D[0].append(float(value))
            if "d20" in specs:
                D[1].append(float(value))
            if "d30" in specs:
                D[2].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["10%", "20%", "30%"], showfliers=False)
    ax.set_title("Execution time related to obstacles density\n(uninformed generation)")
    ax.set_ylabel("seconds")
    ax.set_xlabel("Obstacles density")
    plt.show()

    D = [[],[],[]]
    f = open("./data/informed_times.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "a8" in specs:
            if "d10" in specs:
                D[0].append(float(value))
            if "d20" in specs:
                D[1].append(float(value))
            if "d30" in specs:
                D[2].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["10%", "20%", "30%"], showfliers=False)
    ax.set_title("Execution time related to obstacles density\n(informed generation)")
    ax.set_ylabel("seconds")
    ax.set_xlabel("Obstacles density")
    plt.show()

    # informed goals generation times for medium/large instances

    D = [[],[],[]]
    f = open("./data/informed_times_non_verbose.txt", "r")      
    while True:
        line = f.readline()
        if line == "": break
        splitted = line.split(":")
        specs = splitted[0]
        value = splitted[1]
        if "s15" in specs:
            D[0].append(float(value))
        if "s30" in specs:
            D[1].append(float(value))
        if "s50" in specs:
            D[2].append(float(value))
    fig, ax = plt.subplots()
    ax.boxplot(D, labels=["15x15\n12 agents", "30x30\n15 agents", "50x50\n20 agents"], showfliers=False)
    ax.set_title("Goals generation (informed) execution time\nfor medium-large instances")
    ax.set_ylabel("seconds")
    plt.show()

aggregate_data()
generate_charts()