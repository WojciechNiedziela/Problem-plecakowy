# TODO
# 
# - clean code
# 

import argparse
import sys

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
        lines = f.readlines()
        if not lines:
            print("Plik jest pusty.")
            return None

        C = int(lines[0])
        n = int(lines[1])
        if len(lines) < 2 * n + 2:
            print("Plik nie zawiera wystarczającej liczby danych dla podanej ilości przedmiotów.")
            return None

        val = []
        wt = []
        names = []
        line_index = 2
        for i in range(n):
            name = lines[line_index].strip()
            if not name:
                print(f"Brak nazwy dla przedmiotu {i+1}.")
                return None
            names.append(name) #TODO - JANEK - NAZWA PRZEDMIOTU MUSI ZNAJDOWAC SIE NA LISCIE PRZEDMIOTOW
            line_index += 1

            item_data = lines[line_index].split()
            if len(item_data) != 2:
                print(f"Niepoprawne dane dla przedmiotu '{name}'. Oczekiwano wartości i wagi.")
                return None

            try:
                v, w = map(int, item_data)
            except ValueError:
                print(f"Nie można przekonwertować danych przedmiotu '{name}' na liczby całkowite.")
                return None

            val.append(v)
            wt.append(w)
            line_index += 1

    return C, wt, val, names, n

def read_data_from_console():
    try:
        C = int(input("Podaj pojemność plecaka: "))
        n = int(input("Podaj liczbę przedmiotów: "))
    except ValueError:
        print("Podano nieprawidłową wartość. Program zostanie zakończony.")
        sys.exit(1)

    val = []
    wt = []
    names = []
    for i in range(n):
        name = input(f"Podaj nazwę przedmiotu {i+1}: ").strip()
        if not name:
            print(f"Nie podano nazwy dla przedmiotu {i+1}. Program zostanie zakończony.")
            sys.exit(1)
        names.append(name)

        try:
            v, w = map(int, input(f"Podaj wartość i wagę przedmiotu '{name}' (p w): ").split())
        except ValueError:
            print(f"Nieprawidłowe dane dla przedmiotu '{name}'. Program zostanie zakończony.")
            sys.exit(1)

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
        result = read_data_from_file(args.file)
        if result is None:
            sys.exit("Program zakończony z powodu niepoprawnych danych wejściowych lub pustego pliku.")
        C, wt, val, names, n = result
    elif args.console:
        C, wt, val, names, n = read_data_from_console()
    
    max_value, items_in_knapsack = plecak_dynamiczny(C, wt, val, names, n)
    print(f"Maksymalna wartość, którą można umieścić w plecaku to: {max_value}")
    print("Przedmioty, które znajdą się w plecaku to:", items_in_knapsack)

if __name__ == "__main__":
    main()
