#!usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequenta cada uma das atividade
"""
__version__ = "0.1.1"
__author__ = "Ilan Ramos"

# Dados
salas = {
    "Sala 1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "Sala 2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

aulas = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala
for aula, alunos_atividade in aulas.items():
    for sala, alunos_sala in salas.items():
        alunos = set(alunos_atividade) & set(alunos_sala)

        print(f"Alunos da {sala} para atividade de {aula}: {alunos}")
    print("#" * 50) 
