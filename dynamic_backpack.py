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