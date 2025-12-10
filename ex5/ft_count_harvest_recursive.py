#!/usr/bin/env python3


def ft_count_harvest_recursive(day: int = -1) -> None:
    if day == -1:
        ft_count_harvest_recursive(int(input("Days until harvest: ")))
        print("Harvest time!")
        return
    if day > 1:
        ft_count_harvest_recursive(day - 1)
    print("Day", day)
