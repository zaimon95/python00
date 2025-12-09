def ft_count_harvest_iterative():
    harvest = int(input("Days until harvest: "))
    for i in range(1, int(harvest) + 1):
        print("Day", i)
    print("Harvest time!")
