#!/usr/bin/env python3


def ft_count_harvest_iterative() -> None:
    harvest = int(input("Days until harvest: "))
    for i in range(1, int(harvest) + 1):
        print("Day", i)
    print("Harvest time!")
