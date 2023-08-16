#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10

Tabuada do 1
1
2
3
...
--------------------
Tabuada do 2
2
4
6
...
--------------------
"""
__version__ = "0.1.0"
__author__ = "Ilan Ramos"

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))

# Iterables (objetos percorríveis)
for number in numbers:
    print("Tabuada do", number)
    for other_number in numbers:
        print(number, "x", other_number, "=", number * other_number)
    print("-----------------")