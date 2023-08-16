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

import os

current_language = os.getenv("LANG", "pt_BR.UTF-8")[:5] # snake case

msg = "Hello, world!"

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, mondo!"
elif current_language == "sp_SP":
    msg = "Hola, mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, monde!"

print(msg) 
