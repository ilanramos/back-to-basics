#!/usr/bin/env python3
"""Prefix Calculator

User will send via terminal the operation then the numbers

[operation] [n1] [n2]

Operations:
sum -> +
sub -> -
mul -> *
div -> /

Eg:
$ prefixcalc.py sum 5 2
7 

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py 
operation: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Ilan Ramos"

import sys

cli_arguments = sys.argv[1:]

nums = []

if len(cli_arguments) == 0:
    op = input("Operation: ")
    nums.append(input("n1: "))
    nums.append(input("n2: "))
elif len(cli_arguments) == 3:
    op = cli_arguments[0]
    nums.append(cli_arguments[1])
    nums.append(cli_arguments[2])
else:
    print("Invalid operation. Eg. `sum 2 3`")
    sys.exit(1)

validated_nums = []

for num in nums:
    if num.isdigit():
        validated_nums.append(int(num))
    elif num.replace('.', '').isdigit():
        validated_nums.append(float(num))
    else:
        print("Invalid number")
        sys.exit(1)

if op == "sum":
    result = validated_nums[0] + validated_nums[1]
elif op == "sub":
    result = validated_nums[0] - validated_nums[1]
elif op == "mul":
    result = validated_nums[0] * validated_nums[1]
elif op == "div":
    result = validated_nums[0] / validated_nums[1]
else:
    print("Invalid operation\nValid operations: sum, sub, mul, div")
    sys.exit(1)

print(result)