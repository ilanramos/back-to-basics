#!/usr/bin/env python3
"""Hello world multi-language

According to the language that is configured on the environment, the program will give the proper "Hello world" message.

Usage: 
It must have env variable accordingly configured
Eg: export LANG=pt_BR
Or inform through CLI argument `--lang`

Execution: 
- python3 hello.py
- ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Ilan Ramos"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": os.getenv("LANG", "pt_BR.UTF-8")[:5],
    "count": 1,
}

for index, arg in enumerate(sys.argv[1:]):
    # TODO: Tratar ValueError
    arg = arg.lstrip('-')
    if index % 2 == 0 and arg not in arguments.keys():
        print(f"Comando `{arg}` não reconhecido")
        sys.exit()

    if arg in arguments.keys():
        arguments[arg] = sys.argv[index + 2]

current_language =  arguments['lang'] # snake case

msg = {
    "en_US": "Hello, world!",
    "pt_BR": "Olá, mundo!",
    "it_IT": "Ciao, mondo!",
    "sp_SP": "Hola, mundo!",
    "fr_FR": "Bonjour, monde!",
}

print(
    msg.get(current_language, "Hello, world!") * int(arguments['count']))
