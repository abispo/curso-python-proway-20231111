from config import sessao

from models import Dica

from mensagens import menu_dicas

def criar_dica(texto):
    
    dica = Dica(texto=texto)
    sessao.add(dica)
    sessao.commit()


def listar_dicas():
    return sessao.query(Dica).all()

def atualizar_dica(id_dica, texto):
    linhas_alteradas = sessao.query(Dica).filter_by(id=id_dica).update(
        {"texto": texto}
    )
    sessao.commit()

    # dica = sessao.query(Dica).get(id_dica)
    # dica.texto = texto
    # sessao.add(dica)
    # sessao.commit()

    return linhas_alteradas

def apagar_dica(id_dica):
    linhas_alteradas = sessao.query(Dica).filter_by(id=id_dica).delete()
    sessao.commit()

    return linhas_alteradas

if __name__ == "__main__":
    
    while True:
        print(menu_dicas)
        opcao = int(input("Informe a opção desejada: "))

        match opcao:
            case 0:
                print("Saindo...")
                break

            case 1:
                print("***** LISTA DE DICAS *****")

                for dica in listar_dicas():
                    print(dica)

                print("**************************")

            case 2:
                texto = input("Informe o texto da nova dica: ")
                criar_dica(texto)
                print("Dica inserida com sucesso.")

            case 3:
                id_dica = int(input("Informe o id da dica: "))
                texto = input("Informe o novo texto da dica: ")

                atualizado = bool(atualizar_dica(id_dica=id_dica, texto=texto))

                if atualizado:
                    print("O registro foi atualizado com sucesso!")
                else:
                    print(f"Não foi possível encontrar a dica com o id {id_dica}.")
            
            case 4:
                id_dica = int(input("Informe o id da dica a ser apagada: "))

                apagado = bool(apagar_dica(id_dica=id_dica))

                if apagado:
                    print("O registro foi apagado com sucesso!")
                else:
                    print(f"Não foi possível encontrar a dica com o id {id_dica}.")
