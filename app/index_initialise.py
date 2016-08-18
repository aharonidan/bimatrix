import json
from numpy import zeros
# import numpy

def parse_lrsnash_input():
    with open('lrsnash_input') as f:
        lines = [line.split() for line in f.readlines()]

    m,n = (int(lines[0][0]),int(lines[0][1]))

    A, i = zeros((m,n)), 2
    for j in range(m):
        A[j] = lines[i]
        i+= 1
    i+=1

    B = zeros((m,n))
    for j in range(m):
        B[j] = lines[i]
        i+= 1

    return m,n,A,B

def create_matrix(player):
        if player == 1:
            payoff_matrix = B.transpose()
            rows = n+1
        else:
            payoff_matrix = A
            rows = m+1

        columns = m+n+1

        result = zeros((rows,columns))
        # first row in the form of 0 1 1 ... 1 0 0 ... 0
        result[0,:] = [0] + [1 for i in range(columns - rows)] + [0 for i in range(rows-1)]

        for i in range(1,rows):
            zero_row = zeros(rows-1)
            zero_row[i-1] = 1
            result[i,:] = [-1] + payoff_matrix[i-1].tolist() + zero_row.tolist()

        return  result

def create_components_hash(raw_clique_output):
    raw_clique_output = [item.split() for item in raw_clique_output if item != '\n']
    counter = 0
    result = {}
    for j in range (len(raw_clique_output)):
        if raw_clique_output[j][0] == "Connected":
            result[counter] = []
            j += 1
            while(j < len(raw_clique_output) and raw_clique_output[j][0] != "Connected"):
                if raw_clique_output[j]:
                    result[counter].append(raw_clique_output[j])
                j += 1
            result[counter] = parse_component(result[counter])
            counter += 1
    return result

def parse_component(rows):
    result = []
    for row in rows:
        row = (" ".join(row)).split('x')
        if len(row) > 2: print "ERROR!! unexpected format"
        player1_strategies = row[0].replace('{','').replace('}','').split(',')
        player2_strategies = row[1].replace('{','').replace('}','').split(',')
        for strg_player1 in player1_strategies:
            for strg_player2 in player2_strategies:
                pair = [int(strg_player1),int(strg_player2)]
                if pair not in result:
                    result.append(pair)
    return result

def find_eq_by_numbers(number1, number2, all_equilibria):
    result = None
    for i in range(len(all_equilibria)):
        current_eq = all_equilibria[i]
        if current_eq.x.number == number1 and current_eq.y.number == number2:
            result = current_eq
    return result

m, n, A, B  = parse_lrsnash_input()
matrix_1 = create_matrix(1)
matrix_2 = create_matrix(2)
strategy_hash_player_1 = {}
strategy_hash_player_2 = {}


with open('index_input', 'r') as file:
    equilibria_hash = {}
    if file.read(): equilibria_hash = json.loads(file.read())

with open('clique_output', 'r') as file:
    components_hash = create_components_hash(file.readlines())




