## Tarefa 1

Validar o pré-registro quando o usuário acessa a rota de confirmação de pré-registro

* Verificar se o pre registro ainda é válido
    * Consideramos um pré-registro válido se o id existe a a coluna `valido` é `True`

* Verificar se o pre registro não está expirado
    * O usuário deve confirmar o seu pré-registro em no máximo 24h. Quando o usuário acessar essa rota, será feito um cálculo de quanto tempo se passou. Se esse tempo for igual ou maior a 24h, o pré-registro é inválido. Dica: Compare a quantidade de segundos que se passaram do momento atual até a data do pré-registro (utilize o módulo `timezone.now()` de `django.utils`)