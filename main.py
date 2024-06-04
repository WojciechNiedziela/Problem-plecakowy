# TODO
# 
# - sprawdzic czy wczytywanie z pliku dziala
# - clean code
# 

import argparse

def plecak_dynamiczny(C, wt, val, names, n):
    K = [[0 for w in range(C + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(C + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    
    # Dodanie funkcji do wyświetlania przedmiotów, które znajdą się w plecaku
    res = K[n][C]
    w = C
    items_in_knapsack = []
    
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            items_in_knapsack.append(names[i - 1])
            res = res - val[i - 1]
            w = w - wt[i - 1]
    
    return K[n][C], items_in_knapsack

def read_data_from_file(filename):
    with open(filename, 'r') as f:
        C = int(f.readline())
        n = int(f.readline())
        names = [f.readline().strip() for _ in range(n)]  # Wczytywanie nazw przedmiotów
        items = [list(map(int, f.readline().split())) for _ in range(n)]
        val = [item[0] for item in items]
        wt = [item[1] for item in items]
    return C, wt, val, names, n

def read_data_from_console():
    C = int(input("Podaj pojemność plecaka: "))
    n = int(input("Podaj liczbę przedmiotów: "))
    val = []
    wt = []
    names = []
    for i in range(n):
        name = input(f"Podaj nazwę przedmiotu {i+1}: ")
        names.append(name) #TODO - JANEK - NAZWA PRZEDMIOTU MUSI ZNAJDOWAC SIE NA LISCIE PRZEDMIOTOW
        v, w = map(int, input(f"Podaj wartość i wagę przedmiotu '{name}' (p w): ").split())
        val.append(v)
        wt.append(w)
    return C, wt, val, names, n

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=str, help="Path to the input file")
    group.add_argument("--console", action='store_true', help="Input data from console")
    args = parser.parse_args()

    if args.file:
        C, wt, val, names, n = read_data_from_file(args.file)
    elif args.console:
        C, wt, val, names, n = read_data_from_console()
    
    max_value, items_in_knapsack = plecak_dynamiczny(C, wt, val, names, n)
    print(f"Maksymalna wartość, którą można umieścić w plecaku to: {max_value}")
    print("Przedmioty, które znajdą się w plecaku to:", items_in_knapsack)

if __name__ == "__main__":
    main()
