#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10

---Tabuada do 1---
    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
...
###################
---Tabuada do 2---
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
...
###################
"""
__version__ = "0.1.1"
__author__ = "Ilan Ramos"

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))

# Iterables (objetos percorríveis)
for number1 in numbers:
    print("{:-^18}".format(f"Tabuada do {number1}"))
    for number2 in numbers: 
        result = number1 * number2
        print("{:^18}".format(f"{number1} x {number2} = {result}"))
        
    print("#" * 18)