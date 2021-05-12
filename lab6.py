import random

import numpy as np


def generate_matrix_stohastic():
    matrix = np.zeros(shape=(10, 10))
    for i in range(len(matrix)):
        matrix[i] = np.random.dirichlet(np.ones(10), size=1)
    # print(np.round(matrix, 3))
    return matrix


# # вектор начальных мнений агентов (без влияния)
def generate_start_vector():
    start_vector_opinions_of_agents = np.zeros(shape=(10, 1))
    for i in range(len(start_vector_opinions_of_agents)):
        start_vector_opinions_of_agents[i] = np.random.randint(1, 20 + 1)
    return start_vector_opinions_of_agents


def generate_vector_without_influence(matrix, start_vector_of_opinions):
    prev_vector_opinions = matrix.dot(start_vector_of_opinions)
    eps = 10 ** (-6)
    count = 0
    while True:
        flag = 1
        count += 1
        cur_vector_opinions = matrix.dot(prev_vector_opinions)
        for i in range(len(cur_vector_opinions)):
            if prev_vector_opinions[i] - cur_vector_opinions[i] >= eps:
                prev_vector_opinions = cur_vector_opinions
                flag = 0
                break
        if flag == 1:
            cur_vector_opinions = cur_vector_opinions.reshape(1, 10)
            print("x(", count, ")=", np.round(cur_vector_opinions, 3))
            break


matrix = generate_matrix_stohastic()
print("Матрица А:")
print(np.round(matrix, 3))
print("Результирующие мнения агентов (без влияния):")
start_vector_of_opinions = generate_start_vector()
generate_vector_without_influence(matrix, start_vector_of_opinions)


def generate_vector_influnce_of_agents(N):
    number_agents = [0] * N
    for i in range(len(number_agents)):
        number_agents[i] = i
    # print(number_agents)
    random_agents_first_player = random.randint(1, len(number_agents) - 4)
    agents_of_first_player = random.sample(number_agents, random_agents_first_player)
    number_agents = list(set(number_agents) ^ set(agents_of_first_player))
    # print(number_agents)
    random_agents_second_player = random.randint(1, len(number_agents))
    agents_of_second_player = random.sample(number_agents, random_agents_second_player)
    agents_of_first_player.sort()
    agents_of_second_player.sort()
    #print(agents_of_first_player)
    print("Агенты первого игрока-", [x+1 for x in agents_of_first_player])
    print("Агенты второго игрока-", [x+1 for x in agents_of_second_player])
    start_opinion_agents_first_player = random.randint(0, 100)
    start_opinion_agents_second_player = random.randint(-100, 0)
    print("Начальное мнение агентов первого игрока:", start_opinion_agents_first_player)
    print("Начальное мнение агентов второго игрока:", start_opinion_agents_second_player)
    #print(agents_of_first_player)
    start_vector_opinions_of_agents_with_influence = np.zeros(shape=(10, 1))
    # for i in range(len(start_vector_opinions_of_agents_with_influence)):
    for opinion_first_player in range(len(agents_of_first_player)):
        start_vector_opinions_of_agents_with_influence[
            agents_of_first_player[opinion_first_player]] = start_opinion_agents_first_player
    for opinion_second_player in range(len(agents_of_second_player)):
        # print(opinion_second_player)
        start_vector_opinions_of_agents_with_influence[
            agents_of_second_player[opinion_second_player]] = start_opinion_agents_second_player

    for i in range(len(start_vector_opinions_of_agents_with_influence)):
        if start_vector_opinions_of_agents_with_influence[i] == 0:
            start_vector_opinions_of_agents_with_influence[i] = np.random.randint(1, 20 + 1)

    return start_vector_opinions_of_agents_with_influence

    # print(agents_of_first_player)
    # print(agents_of_second_player)


start_vector_opinions_of_agents_with_influence = generate_vector_influnce_of_agents(10)
print(start_vector_opinions_of_agents_with_influence.reshape(1, 10))
print("Результирующие мнения агентов")
generate_vector_without_influence(matrix, start_vector_opinions_of_agents_with_influence)
