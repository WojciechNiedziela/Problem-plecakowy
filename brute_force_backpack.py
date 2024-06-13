def plecak_silowy(CapacityOfTheBackpack, weightsArr, valuesArr, namesArr, n):
    items = list(zip(weightsArr, valuesArr, namesArr))
    max_value = 0
    best_subset = []

    for i in range(2**n):
        subset = []
        total_weight = 0
        total_value = 0

        for j in range(n):
            if (i >> j) & 1:
                subset.append(items[j][2])
                total_weight += items[j][0]
                total_value += items[j][1] 

        if total_weight <= CapacityOfTheBackpack and total_value > max_value:
            max_value = total_value
            best_subset = subset

    return max_value, best_subset