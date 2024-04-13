from django.contrib.auth.models import User

def todos_dados_preenchidos(*args) -> bool:
    return all(args)


def username_nao_existe(username: str) -> bool:
    return not User.objects.filter(username=username).exists()


def senhas_sao_iguais(senha: str, confirmacao_senha: str) -> bool:
    return senha.strip() == confirmacao_senha.strip()
