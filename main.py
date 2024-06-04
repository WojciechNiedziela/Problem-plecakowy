# TODO
# 
# - podzielic sie zadaniami
# - sprawdzic czy wczytywanie z pliku dziala
# - sprawdzic czy wczytywanie z konsoli dziala
# - sprawdzic czy algorytm dziala (plecak_dynamiczny)
# - dodac komentarze tlumaczace co robi kod
# - clean code
# 
# 

import argparse

def plecak_dynamiczny(C, wt, val, n):
    K = [[0 for w in range(C + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(C + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][C]

def read_data_from_file(filename):
    with open(filename, 'r') as f:
        C = int(f.readline())
        n = int(f.readline())
        items = [list(map(int, line.split())) for line in f]
        val = [item[0] for item in items]
        wt = [item[1] for item in items]
    return C, wt, val, n

def read_data_from_console():
    C = int(input("Podaj pojemność plecaka: "))
    n = int(input("Podaj liczbę przedmiotów: "))
    print("Podaj wartość i wagę każdego przedmiotu (p w):")
    items = [list(map(int, input().split())) for _ in range(n)]
    val = [item[0] for item in items]
    wt = [item[1] for item in items]
    return C, wt, val, n

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=str, help="Path to the input file")
    group.add_argument("--console", action='store_true', help="Input data from console")
    args = parser.parse_args()

    if args.file:
        C, wt, val, n = read_data_from_file(args.file)
    elif args.console:
        C, wt, val, n = read_data_from_console()
    print(plecak_dynamiczny(C, wt, val, n))

if __name__ == "__main__":
    main()
