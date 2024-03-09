# Enquetes

## Desafio

### Na página de resultados, criar uma estrutura de feedback de perguntas

Quando o usuário vota, ele é redirecionado para a página de resultados. Nessa página é exibida uma lista com as opções da pergunta, e quantos votos cada uma obteve. Após essa listagem, deverá ser criado um formulário que irá receber as seguintes informações:
* Nota de 1 a 5 (padrão 3), que o usuário irá atribuir à enquete.
* Um comentário opcional que ele poderá fazer.

O usuário irá enviar esses dados após clicar em um botão "Enviar". Essa informação ficará salva no banco de dados. Após clicar em enviar, o usuário volta para a página principal de enquetes

[Diferencial] O usuário não poderá dar mais de 1 nota para a mesma pergunta. Para ter esse controle, você pode criar os usuário no painel administrativo do Django.