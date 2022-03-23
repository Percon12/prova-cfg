"""
A gramática abaixo no formato EBNF possui um conjunto infinito de exemplos.

start    : fizz

fizz     : "fizz"
         | "fizz(" fizz [ SEP buzz ] ")" 

buzz     : "buzz"
         | "buzz(" (NUMBER SEP)+ buzz ")"

SEP      : ", "
NUMBER   : 1 - 100 

Crie um programa que gere strings aleatórias desta linguagem. O programa deve ser capaz
de gerar **TODAS** strings possíveis e **SOMENTE STRINGS VÁLIDAS**, mesmo que a 
probabilidade de gerar um exemplo específico seja muito baixa. 

DICA: podemos criar um gerador para uma CFG criando uma função geradora para cada símbolo
(terminal e não-terminal) da gramática. Estas funções podem então se chamar de forma
recursiva espelhando as regras da gramática.

Abaixo seguem alguns exemplos de strings aleatórias válidas geradas por esta gramática:

    fizz
    fizz(fizz)
    fizz(fizz, buzz)
    fizz(fizz(fizz, buzz(10, 42, 1, 100, buzz(1, buzz))))
"""
import random


def random_example() -> str:
    return "..."


def fizzbuzz():
    return "..."


def fizz():
    return "..."


def buzz():
    return "..."


def NUMBER():
    return str(random.randint(1, 100))


if __name__ == "__main__":
    for i in range(1, 11):
        print(f"{i}) {random_example()}")
