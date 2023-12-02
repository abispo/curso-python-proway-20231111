"""
Trabalhando com arquivos csv (Comma Separated Values - Valores Separados por Vírgula)

Lendo um arquivo csv com a função reader e a classe DictReader
"""
import csv
import os

def exibir_valores(nome, idade, valor):
    return f"{nome}, {idade} anos possui o valor {valor}."

if __name__ == "__main__":
    
    # Abrindo o arquivo
    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "clientes.csv")
    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:

        # Após abrir o arquivo, precisamos criar o objeto que representa o arquivo csv em si
        # Por padrão, o método reader considera que a vírgula é o separador. Caso o arquivo tenha um separador diferente, podemos indicar pelo parâmetro delimiter
        arquivo_csv = csv.reader(arquivo, delimiter=';')

        # O objeto que representa o arquivo csv, não possui métodos como read() ou readlines() para receber o conteúdo do arquivo. Nesse caso, precisamos iterar sobre o objeto csv para conseguir ler o conteúdo do arquivo.
        for linha in arquivo_csv:

            # A linha vai ser retornada como uma lista de valores. Cada valor dessa lista, é o item do arquivo separado pelo delimitador
            print(exibir_valores(*linha))

    
    # Também podemos alterar o retorno dos dados do arquivo, para o formato de dicionários.
    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:

        # Vamos utilizar a classe DictReader
        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            # A linha será um dicionário, que terá como chaves nome, idade e valor, que são os valores da primeira linha do arquivo csv. Os valores do dicionário serão as demais linhas
            print(exibir_valores(**linha))