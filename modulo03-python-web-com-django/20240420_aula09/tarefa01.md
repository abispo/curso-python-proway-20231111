## Tarefa 1

### Criar uma página de listagem de imóveis
* Apenas imóveis que estiverem disponíveis serão listados
    * Imóvel disponível é um imóvel que:
        * Não está atualmente alugado
        * Que não está indisponível por outro motivo
* Utilize o elemento Card do bootstrap para listar os imóveis
* Quando o usuário clicar nesse card, ele vai pra página de detalhes do imóvel
    * Na página de detalhes do imóvel, ele pode visualizar o preço pelo tipo de contrato (diario e o mensal)
    * O usuário poderá clicar em um botão chamado "Alugar"
    * Ele será redirecionado para a página de aluguel do imovel
    * Nessa página, ele irá escolher o tipo de contrato (diario ou mensal), o período de tempo do aluguel (data inicio e data fim).
    * Após escolher, ele irá confirmar e os dados do contrato serão salvos
    * As informações sobre parcela, serão salvas em outra tabela, chamada tb_parcelamento. Será criada uma lista de parcelas nessa tabela associada a um contrato.
* Depois de salvo, na página principal do sistema, irá aparecer o contrato ativo do usuário
    * Quando o usuário clicar nesse contrato, irá para a página de detalhes do contrato.
    * Nessa página de detalhes, o usuário poderá visualizar:
        * Dados do contrato (data de início, data de fim, etc)
        * Dados do imóvel
        * Dados das parcelas
* Utilizar a biblioteca [jquery-mask-plugin](https://igorescobar.github.io/jQuery-Mask-Plugin/docs.html) para formatar corretamente o campo `documento` da página de perfil.