import six
import sys
import mlrose_hiive as mlrose

def imprimir_solucao(solucao):
    custo_total = 0
    for i in range(len(solucao)):
        if solucao[i] == 1:
            print(f'{produtos[i][0]} - {produtos[i][2]}')
            custo_total += produtos[i][2]
    print(f'Custo total: {custo_total:.2f}')  # Exibe o custo total formatado

def fitness_function(solucao):
    custo = 0
    soma_espaco = 0
    for i in range(len(solucao)):
        if solucao[i] == 1:
            custo += produtos[i][2]
            soma_espaco += produtos[i][1]
    return custo if soma_espaco <= espaco_disponivel else 1  # Retorna custo ou penalidade

# Definição dos produtos (nome, espaço, custo)
produtos = [
    ('Refrigerador A', 0.751, 999.90),
    ('Celular', 0.0000899, 2911.12),
    ('TV 55', 0.400, 4346.99),
    ('TV 50', 0.290, 3999.90),
    ('TV 42', 0.200, 2999.00),
    ('Notebook A', 0.00350, 2499.90),
    ('Ventilador', 0.496, 199.90),
    ('Microondas A', 0.0424, 308.66),
    ('Microondas B', 0.0544, 429.90),
    ('Microondas C', 0.0319, 299.29),
    ('Refrigerador B', 0.635, 849.00),
    ('Refrigerador C', 0.870, 1199.89),
    ('Notebook B', 0.498, 1999.90),
    ('Notebook C', 0.527, 3999.00)
]
espaco_disponivel = 3

# Criação do problema de otimização
fitness = mlrose.CustomFitness(fitness_function)
problema = mlrose.DiscreteOpt(length=len(produtos), fitness_fn=fitness, maximize=True, max_val=2)

# Aplicação do algoritmo Hill Climbing
melhor_solucao_hc, melhor_custo_hc = mlrose.hill_climb(problema)
print('\nMétodo: Hill Climbing')
imprimir_solucao(melhor_solucao_hc)

# Aplicação do algoritmo Simulated Annealing
melhor_solucao_sa, melhor_custo_sa = mlrose.simulated_annealing(problema)
print('\nMétodo: Simulated Annealing')
imprimir_solucao(melhor_solucao_sa)

# Aplicação do algoritmo Genetic Algorithm
melhor_solucao_ga, melhor_custo_ga = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2)
print('\nMétodo: Genetic Algorithm')
imprimir_solucao(melhor_solucao_ga)
