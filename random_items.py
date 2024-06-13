import argparse
import csv
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("capacity", type=int, help="Pojemność plecaka")
    parser.add_argument("num_items", type=int, help="Ilość przedmiotów")
    args = parser.parse_args()

    with open('database.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        items = list(reader)

    selected_items = random.sample(items, args.num_items)

    with open('random_items.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([args.capacity])
        writer.writerow([args.num_items])
        writer.writerows(selected_items)

if __name__ == "__main__":
    main()