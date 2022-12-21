# MEDIÇÕES DO SLA
## Menu/Cardápio
Tipo de operação: leitura

Arquivos envolvidos (lista de arquivos envolvidos na implementação do Menu/Cardápio):
- menu.page.php (app\controllers\menu.page.php)
- menu.tpl.html (app\templates\menu.tpl.html)
- Product.class.php (app\classes\Product.class.php)
- products.page.php (app\controllers\$restful\products.page.php)
- ProductStatus.class.php (app\classes\ProductStatus.class.php)

Data da medição: 21/12/2022

Descrição das configurações -> Quantidade de docker's: 1

Testes de carga (SLA):
- latência: 5,88 ms
- vazão: 2543,09 requisições/s -- 152.590 requisições/min
- concorrência (limite de requisições simultâneas): 2544 requisições
    
Potenciais gargalos do sistema:
- Pela necessidade de recuperar os produtos guardados na base de dados, a comunicação com o DB MySQL acaba por gerar um pouco de gargalo nesse serviço pela necessidade da execução de um SELECT internamente para ser retornado do back-end ao front-end e, assim, o cliente poder ter acesso aos lanches da Quero Burguer.

## Atualizar Cadastro
Tipo de operação: atualização

Arquivos envolvidos (lista de arquivos envolvidos na implementação do Atualizar Cadastro):
- users.page.php (app\controllers\$restful\users.page.php)

Data da medição: 21/12/2022

Descrição das configurações -> Quantidade de docker's: 1

Testes de carga (SLA):
- latência: 856,45 ms
- vazão: 17,81 requisições/s -- 1,069 requisições/min
- concorrência (limite de requisições simultâneas): 18 requisições

Potenciais gargalos do sistema:
- Como é um serviço que realiza UPDATE na base de dados relacional e a conexão com o banco de dados MySQL é fundamental para o funcionamento correto do serviço, o gargalo do sistema se deve à comunicação com a nossa base de dados.