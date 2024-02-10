from datetime import datetime

from config import sessao

from models import Usuario, Perfil

from mensagens import menu_usuarios, info_usuario

def criar_usuario(email, senha, nome, data_nascimento):
    
    usuario = Usuario(
        email=email, senha=senha
    )

    sessao.add(usuario)
    sessao.commit()

    criar_perfil_usuario(usuario.id, nome, data_nascimento)


def criar_perfil_usuario(id_usuario, nome, data_nascimento):
    
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    except:
        perfil = Perfil(id=id_usuario, nome=nome)

    else:
        perfil = Perfil(
            id=id_usuario,
            nome=nome,
            data_nascimento=data_nascimento
        )

    finally:
        sessao.add(perfil)
        sessao.commit()


def listar_usuarios():
    return sessao.query(Usuario).all()

if __name__ == "__main__":
    
    while True:

        print(menu_usuarios)

        opcao = int(input("Escolha a opção: "))

        match opcao:
            case 0:
                print("Saindo...")
                break

            case 1:
                for usuario in listar_usuarios():

                    data_nascimento = usuario.perfil.data_nascimento

                    mensagem = info_usuario.format(
                        email=usuario.email,
                        nome=usuario.perfil.nome,
                        data_nascimento="Não informado" if not data_nascimento else datetime.strftime(data_nascimento, "%d/%m/%Y")
                    )

                    print(mensagem)

            case 2:
                email = input("Informe o email do usuário: ")
                senha = input("Informe a senha do usuário: ")
                nome = input("Informe o nome do usuário: ")
                data_nascimento = input("Informe a data de nascimento do usuário (dd/mm/yyyy): ")

                criar_usuario(
                    email=email,
                    senha=senha,
                    nome=nome,
                    data_nascimento=data_nascimento
                )

            case 3 | 4:
                pass