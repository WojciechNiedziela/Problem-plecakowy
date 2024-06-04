import argparse, sys

def plecak_dynamiczny(CapacityOfTheBackpack, weightsArr, valuesArr, namesArr, n): 
    MaxValue = [[0 for weight in range(CapacityOfTheBackpack + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for weight in range(CapacityOfTheBackpack + 1): 
            if i == 0 or weight == 0:
                MaxValue[i][weight] = 0
            elif weightsArr[i - 1] <= weight:
                MaxValue[i][weight] = max(valuesArr[i - 1] + MaxValue[i - 1][weight - weightsArr[i - 1]], MaxValue[i - 1][weight])
            else:
                MaxValue[i][weight] = MaxValue[i - 1][weight]
    
    result = MaxValue[n][CapacityOfTheBackpack]
    weight = CapacityOfTheBackpack
    ItemsInBackpack = []
    
    for i in range(n, 0, -1):
        if result <= 0:
            break
        if result == MaxValue[i - 1][weight]:
            continue
        else:
            ItemsInBackpack.append(namesArr[i - 1])
            result = result - valuesArr[i - 1]
            weight = weight - weightsArr[i - 1]
    
    return MaxValue[n][CapacityOfTheBackpack], ItemsInBackpack

def read_data_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        if not lines:
            print("Plik jest pusty.")
            return None

        CapacityOfTheBackpack = int(lines[0])
        n = int(lines[1])
        if len(lines) < 2 * n + 2:
            print("Plik nie zawiera wystarczającej liczby danych dla podanej ilości przedmiotów.")
            return None

        valuesArr = []
        weightsArr = []
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
                value, weight = map(int, item_data)
            except ValueError:
                print(f"Nie można przekonwertować danych przedmiotu '{name}' na liczby całkowite.")
                return None

            valuesArr.append(value)
            weightsArr.append(weight)
            line_index += 1

    return CapacityOfTheBackpack, weightsArr, valuesArr, names, n

def read_data_from_console():
    try:
        CapacityOfTheBackpack = int(input("Podaj pojemność plecaka: "))
        n = int(input("Podaj liczbę przedmiotów: "))
    except ValueError:
        print("Podano nieprawidłową wartość. Program zostanie zakończony.")
        sys.exit(1)

    valuesArr = []
    weightsArr = []
    names = []
    for i in range(n):
        name = input(f"Podaj nazwę przedmiotu {i+1}: ").strip()
        if not name:
            print(f"Nie podano nazwy dla przedmiotu {i+1}. Program zostanie zakończony.")
            sys.exit(1)
        names.append(name)

        try:
            value, weight = map(int, input(f"Podaj wartość i wagę przedmiotu '{name}' (p w): ").split())
        except ValueError:
            print(f"Nieprawidłowe dane dla przedmiotu '{name}'. Program zostanie zakończony.")
            sys.exit(1)

        valuesArr.append(value)
        weightsArr.append(weight)
    return CapacityOfTheBackpack, weightsArr, valuesArr, names, n


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
        CapacityOfTheBackpack, weight, valuesArr, names, n = result
    elif args.console:
        CapacityOfTheBackpack, weight, valuesArr, names, n = read_data_from_console()
    
    maxValue, ItemsInBackpack = plecak_dynamiczny(CapacityOfTheBackpack, weight, valuesArr, names, n)
    print(f"Maksymalna wartość, którą można umieścić w plecaku to: {maxValue}")
    print("Przedmioty, które znajdą się w plecaku to:", ItemsInBackpack)

if __name__ == "__main__":
    main()
