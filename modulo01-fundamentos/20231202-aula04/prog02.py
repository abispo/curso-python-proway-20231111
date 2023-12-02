"""
Entrada e Saída de arquivos em Python (File I/O)

Escrita de arquivos .txt em Python
"""

if __name__ == "__main__":

    lista_compras = ["Arroz", "Feijão", "Alface", "Tomate", "Cebolinha", "Frango"]

    # Como dito anteriormente, caso o arquivo não exista, ele será criado. E caso exista, o seu conteúdo será apagado e substituído pelo novo
    with open(file="lista_de_compras.txt", mode="w", encoding="utf-8") as arquivo:
        
        for item in lista_compras:
            # O método write() escreve o conteúdo no arquivo. Na linha abaixo também estamos passando o caractere especial \n (nova linha), pois se não fizermos isso, o texto será impresso "colado"
            arquivo.write(f"{item}\n")

        
        # writelines: Recebe uma lista de itens, que serão escritos no arquivo
        itens_adicionais = ["Vinho do Porto\n", "Rapadura\n"]
        arquivo.writelines(itens_adicionais)
