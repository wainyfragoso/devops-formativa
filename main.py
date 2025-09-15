from utils import boas_vindas
import sys

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(boas_vindas(nome))
    print("Programa encerrado. Até logo! 👋")
    sys.exit(0)  # encerra a execução do programa