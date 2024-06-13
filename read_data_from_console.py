import sys

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