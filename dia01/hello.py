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
__version__ = "0.1.2"
__author__ = "Ilan Ramos"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "pt_BR.UTF-8")[:5] # snake case

msg = {
    "en_US": "Hello, world!",
    "pt_BR": "Olá, mundo!",
    "it_IT": "Ciao, mondo!",
    "sp_SP": "Hola, mundo!",
    "fr_FR": "Bonjour, monde!",
}

print(msg.get(current_language, "Hello, world!"))
