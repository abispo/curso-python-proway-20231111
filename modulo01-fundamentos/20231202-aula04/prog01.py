"""
Entrada e Saída de arquivos em Python (File I/O)

Leitura de arquivos .txt em Python
"""

if __name__ == "__main__":
    
    """
    Utilizamos a função built-in open() para abrir um arquivo. Esse arquivo pode ser de qualquer tipo, mas por padrão, o python considera que está sendo aberto um arquivo de texto plano. Além desse tipo de arquivo, também podemos abrir arquivos binários dentro do Python (executável, imagem, arquivo de som, etc.)

    O único argumento obrigatório dessa função, é o nome do arquivo, que passamos abaixo como "linguagens.txt". A funçao open vai procurar esse arquivo na mesma pasta onde o script está sendo executado.

    Geralmente, passamos 2 ou 3 parâmetros para a função open, que são os seguinte:

    1) O nome do arquivo. Esse valor é obrigatório
    2) O modo de abertura de abertura do arquivo. Caso não passemos esse valor, o Python considera que o arquivo está sendo aberto no modo somente-leitura e que ele é um arquivo texto-plano. Abaixo estão alguns modos de abertura de arquivos:

        r -> Modo somente leitura. Nesse modo não é possível alterar o conteúdo do arquivo, apenas lê-lo.
        w -> Modo somente escrita. Nesse modo não é possível ler o conteúdo do arquivo, apenas alterá-lo. Detalhe: Caso o arquivo não exista, ele será criado. Caso exista, o seu conteúdo será substituído.
        a -> Modo somente escrita (append). Assim como o modo w, não permita a leitura do arquivo. O que o diferencia do modo w, é que se o arquivo já existir, o seu conteúdo não é apagado, e sim o novo conteúdo é adicionado ao final do arquivo.

        Opcionalmente, podemos indicar o tipo de arquivo que está aberto, passando o valor após o modo de abertura. Os possíveis valores são 't' e 'b'. Por exemplo: Para abrir um arquivo binário em modo somente-leitura, temos que indicar o modo de abertura como 'rb'.

        Também é possível "misturar" os modos de abertura, por exemplo: r+ permite abrir o arquivo como leitura e escrita, ou seja, podemos ler e modificar o conteúdo ao mesmo tempo.

    3) O "encoding"s (codificação de caracteres) do arquivo. É importante definir nos casos onde podemos ter a manipulação desse arquivo em sistema diferentes. Por exemplo, salvamos o arquivo com a codificação padrão do windows (cp1252) e tentarmos abrir em um editor que trabalha com a codificação utf-8.
    """

    # Abrimos o arquivo, passando o único parâmetro obrigatório
    arquivo = open("linguagens.txt")

    # A função open() vai retornar um objeto que representa o arquivo que abrimos. Esse objeto possui alguns métodos para leitura do conteúdo do arquivo. Um deles é o read(), que retorna o conteúdo desse arquivo como uma string
    conteudo = arquivo.read()

    # Aqui imprimimos o conteúdo no terminal. É importante frisar que todos os caracteres são lidos, inclusive os caracteres especiais, como \n (quebra de linha), \t (tabulação), etc.
    print(conteudo)

    # Como boa prática, é muito importante sempre fecharmos o arquivo (método close()) depois que terminamos de usá-lo. Não fechar um arquivo depois que o abrimos, pode levar a comportamentos inesperados no sistema operacional.
    arquivo.close()

    # Existe uma maneira de abrir qualquer arquivo sem nos preocuparmos com chamar explicitamente o método close(), que é usando a palavra reservada with. with cria um contexto de execução no código, onde no momento em que saímos desse contexto de execução, o arquivo é fechado automaticamente

    with open(file="linguagens.txt", mode="r", encoding="utf-8") as arquivo:
        
        # No método read, podemos indicar quantos bytes(caracteres) queremos ler por vez.
        print(arquivo.read(5))

        # Existem outros métodos para leitura do conteúdo de um arquivo. São eles:

        # readline(bytes): Lê o conteúdo do arquivo na linha atual onde está o cursor. Podemos indicar também a quantidade de caracteres que queremos ler
        print(arquivo.readline())
        print(arquivo.readline(5))


        # readlines(bytes) Lê o conteúdo do arquivo e gera uma lista de strings, com cada string representando uma linha. bytes é a quantidade de caracteres que queremos ler. Caso o valor "passe" para a próxima linha, a próxima linha inteira será retornada.
        print(arquivo.readlines(12))

        print(arquivo.readlines())

        # Como o cursor do arquivo chegou no final, a linha abaixo retornará uma string vazia, pois não há mais nada a ser lido. Caso queiramos "rebobinar" o cursor, precisamos chamar o método seek, passando a posição 0 (início do arquivo)
        print(arquivo.read())

        # "Rebobinamos o cursor, jogando ele para o início do arquivo"
        arquivo.seek(0)

        print(arquivo.readlines())