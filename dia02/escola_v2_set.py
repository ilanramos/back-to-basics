#!usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequenta cada uma das atividade
"""
__version__ = "0.1.1"
__author__ = "Ilan Ramos"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    (aula_ingles, "Inglês"), 
    (aula_musica, "Música"),
    (aula_danca, "Dança")]

# Listar alunos em cada atividade por sala
for atividade, nome_atividade in atividades:

    atividade_sala1 = set(atividade) & set(sala1)
    atividade_sala2 = set(atividade) & set(sala2)

    print(f"{nome_atividade} sala 1: {atividade_sala1}")
    print(f"{nome_atividade} sala 2: {atividade_sala2}")
    print("#" * 50)
