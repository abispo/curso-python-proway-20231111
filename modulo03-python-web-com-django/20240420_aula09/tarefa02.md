## Tarefa 2

### Começar a definir a estrutura das tabelas.

Vamos considerar a tabela `tb_perfis` como a tabela de locatários (tb_locatarios).

1. Criar um comando para carregar os [dados de usuários](https://raw.githubusercontent.com/abispo/shared-files/main/usernames_django.csv) e salvar na tabela `auth_user`.
2. Criar um comando para carregar os [dados de kitnets](https://raw.githubusercontent.com/abispo/shared-files/main/gerenciamento_kitnets/imoveis.csv) e salvar na tabela `tb_imoveis`.
3. Criar um comando para carregar os [dados de tipo de contrato](https://raw.githubusercontent.com/abispo/shared-files/main/gerenciamento_kitnets/tipos_contratos.csv) e salvar na tabela `tipos_contrato`.

Lembrete: Você deve criar a model `Imovel` para a tabela `tb_imoveis` e uma model `TipoContrato` para a tabela `tipos_contrato`. A chave primária da tabela `tb_imoveis` deve ser do tipo `uuid` (Classe `models.UUIDField` do pacote `django.db.models`).