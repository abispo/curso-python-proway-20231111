import os
from datetime import datetime

import requests

API_URL = "https://pokeapi.co/api/v2/pokemon/{}"
NOME_PASTA = "pokemons"

# os.getcwd()       ->  Retorna o caminho completo até a pasta onde o script está sendo executado
# os.path.join      -> Concatena os caminhos que informamos. Na linha abaixo, vai concatenar o valor retornado pela função getcwd() com o nome da pasta
CAMINHO_PASTA = os.path.join(os.getcwd(), NOME_PASTA)

if __name__ == "__main__":

    # Verifica se um arquivo ou pasta existe
    if not os.path.exists(CAMINHO_PASTA):
        # Caso não exista, será criada a pasta
        os.mkdir(CAMINHO_PASTA)
    
    while True:

        # O método .lower() transforma todas as letras da string em minúsculas
        entrada = input("Informe o nome do pokemon a ser consultado (sair para sair): ").lower()

        match entrada:
            case "sair":
                break

            case _:
                resposta = requests.get(API_URL.format(entrada))
                
                if resposta.status_code == 200:
                    dados_pokemon = resposta.json()

                    nome_arquivo = f"{dados_pokemon.get('name')}.txt"

                    with open(os.path.join(CAMINHO_PASTA, nome_arquivo), mode='w', encoding="utf-8") as arquivo:
                        
                        arquivo.write(f"ID: {dados_pokemon.get('id')}\n")
                        arquivo.write(f"Altura: {dados_pokemon.get('height') * 0.1}m\n")
                        arquivo.write("Habilidades:\n")
                        for habilidade in dados_pokemon.get("habilities"):
                            arquivo.write(f"{habilidade.get('ability').get('name')} ")

                        arquivo.write('**********\n')

                        arquivo.write("Tipos:\n")
                        for tipo in dados_pokemon.get("types"):
                            arquivo.write(f"{tipo.get('type').get('name')} ")