#!/usr/bin/env python3
"""Hello world multi-language

According to the language that is configured on the environment, the program will give the proper "Hello world" message.

Usage: 
It must have env variable accordingly configured
Eg: export LANG=pt_BR

Execution: 
- python3 hello.py
- ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Ilan Ramos"
__license__ = "Unlicense"

if __name__ == "__main__":
    print("Hello, world!") 
