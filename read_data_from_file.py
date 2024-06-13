import csv

def read_data_from_file(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        data = list(reader)

        if not data:
            print("Plik jest pusty.")
            return None

        try:
            CapacityOfTheBackpack = int(data[0][0])
            n = int(data[1][0])
        except ValueError:
            print("Niewłaściwe dane dla pojemności lub ilości przedmiotów.")
            return None

        names = []
        weightsArr = []
        valuesArr = []

        for row in data[2:]:
            try:
                name, weight, value = row
                names.append(name)
                weightsArr.append(int(weight))
                valuesArr.append(int(value))
            except ValueError:
                print(f"Niewłaściwe dane w rzędzie: {row}.")
                return None

        return CapacityOfTheBackpack, weightsArr, valuesArr, names, n