## Tarefa 1

### Criar uma página de perfil do usuário.

O usuário irá entrar na página de perfil, pode poderá visualizar e editar o seu perfil.

Os dados de perfil que serão editáveis serão os seguintes: Nome, Sobrenome, E-mail, Documento, Gênero e Data de Nascimento. (Vamos criar uma model `Perfil` (tb_perfis) que terá as informações de Documento, gênero e Data de Nascimento).

Você pode querer utilizar o elemento [input type="date"](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date) para informar a data de nascimento do usuário.

A rota para a página de perfil do usuário será `/gestao/inquilinos/<id_do_usuario>/perfil`.
A model `Perfil` [terá um relacionamento 1:1 com a model `User` do pacote `django.contrib.auth.models`](https://docs.djangoproject.com/en/5.0/topics/db/examples/one_to_one/).

Quando um novo usuário for criado, um registro na `tb_perfis` também deve ser criado. Você pode querer utilizar os [Sinais do Django](https://docs.djangoproject.com/en/5.0/ref/signals/).