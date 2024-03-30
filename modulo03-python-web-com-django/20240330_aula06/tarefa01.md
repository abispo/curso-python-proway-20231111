## Tarefa 1

Construir o formulário de cadastro. Esse formulário deve ter os seguintes campos:

* Nome  (type=text, name=nome)
* Sobrenome (type=text, name=sobrenome)
* Nome de usuário (type=text, name=nome_de_usuario)
* Senha (type=password, name=senha)
* Confirmação de senha (type=password, name=confirmacao_senha)
* botão de envio (button type=submit)

Além disso, você vai precisar criar 2 elementos do tipo input type=hidden:
* ID pre registro
    (type="hidden", name="id_pre_registro", value=<`valor_vindo_da_url`>)
* email
    (type="hidden", name="email", value=<`email_do_pre_registro`>)

Dica: Todas as informações de requisição, estão no parâmetro `request`, tanto `GET` quanto `POST`