import os

def clear_execution():
    sistema_operativo = os.name
    if sistema_operativo == "nt":
        os.system("cls")
    else:
        os.system("clear")