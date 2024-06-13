#   Obsługa: w celu pozyskania przedmiotów dostępnych do wczytywania przez plik można wykonać program 
#   random_items.py z argumentami (random_items.py pojemność ilość_przedmiotów), który do pliku
#   random_items.csv wypisze w pierwszym i drugim wierszu argumenty, a w kolejnych liczbę 
#   wylosowanych przedmiotów podanych jako drugi argument
#   funkcję main wywołuje się poprzez: 
#   python3 main.py (--file nazwa_pliku)/--console --type dynamic/brute_force

import argparse, sys
from read_data_from_file import read_data_from_file
from read_data_from_console import read_data_from_console
from dynamic_backpack import plecak_dynamiczny
from brute_force_backpack import plecak_silowy

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=str, help="Path to the input file")
    group.add_argument("--console", action='store_true', help="Input data from console")
    parser.add_argument("--type", type=str, choices=["dynamic", "brute_force"], required=True, help="Type of solution to use")
    args = parser.parse_args()

    if args.file:
        result = read_data_from_file(args.file)
        if result is None:
            sys.exit("Program zakończony z powodu niepoprawnych danych wejściowych lub pustego pliku.")
        CapacityOfTheBackpack, weight, valuesArr, names, n = result
    elif args.console:
        CapacityOfTheBackpack, weight, valuesArr, names, n = read_data_from_console()

    if args.type == "dynamic":
        maxValue, ItemsInBackpack = plecak_dynamiczny(CapacityOfTheBackpack, weight, valuesArr, names, n)
    elif args.type == "brute_force":
        maxValue, ItemsInBackpack = plecak_silowy(CapacityOfTheBackpack, weight, valuesArr, names, n)

    print(f"Maksymalna wartość, którą można umieścić w plecaku to: {maxValue}\n")
    print("Przedmioty, które znajdą się w plecaku to:", ItemsInBackpack)

if __name__ == "__main__":
    main()