## Tarefa 1

Implementar o cadastro do usuário. Para salvar o usuário na tabela de usuários (`auth_user`), precisamos fazer algumas validações, que serão as seguintes:

* Verificar se todos os dados do formulário de cadastro foram preenchidos.
    * Precisamos validar se as informações de cadastro (`nome`, `sobrenome`, `nome_de_usuario`, `senha` e `confirmacao_senha` foram preenchidos). Você pode validar campo a campo ou utilizar a função `built-in` do python `all`.
    * Precisamos validar também se o `nome_de_usuario` já não existe na tabela `auth_user`.
    * Por fim, precisamos validar se o valor de `senha` é igual ao valor de `confirmacao_senha`.

Se quiser, você pode criar um módulo apenas para essas funções de validação.

Caso alguma validação falhe, deve ser exibida no formulário.

Se os dados forem validados, será necessário criar um usuário com os dados informados. Utilize o método `User.objects.create_user` para criar um usuário na tabela `auth_user`. Você vai precisar passar os valores recebidos para os parâmetros `first_name`, `last_name`, `username`, `email`, `password`.

Após criar o usuário, você deverá invalidar o pre-registro (coluna `valido` igual a `False`)

Por fim, o usuário será redirecionado para a url `confirmacao-cadastro`, que irá renderizar o template `registro/confirmacao_cadastro.html`. O conteúdo do template será um texto de informação para o usuário, e um link para a página de login.