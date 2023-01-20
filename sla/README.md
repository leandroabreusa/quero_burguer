# MEDIÇÕES DO SLA

OBS: Ambos os serviços testados no primeiro teste possuem uma página HTML com o seu nome gerado por meio do K6 Reporter v2.3.0 - Ben Coleman 2021. Basta abrir a 
pasta "primeiro-teste" e executar esse html no seu navegador.

## Menu/Cardápio
Tipo de operação: leitura

Arquivos envolvidos (lista de arquivos envolvidos na implementação do Menu/Cardápio):
- menu.page.php (app\controllers\menu.page.php)
- menu.tpl.html (app\templates\menu.tpl.html)
- Product.class.php (app\classes\Product.class.php)
- products.page.php (app\controllers\$restful\products.page.php)
- ProductStatus.class.php (app\classes\ProductStatus.class.php)

### MEDIÇÃO 1

Data da medição: 21/12/2022

Descrição das configurações -> Quantidade de docker's: 1

Testes de carga (SLA):
- latência: 95º percentil - 13,97 ms
- vazão: 2543,09 requisições/s -- 152.590 requisições ao longo do teste
- concorrência (limite de requisições simultâneas): 2543 requisições
    
Potenciais gargalos do sistema:
- Pela necessidade de recuperar os produtos guardados na base de dados, a comunicação com o DB MySQL acaba por gerar um pouco de gargalo nesse serviço pela necessidade da execução de um SELECT internamente para ser retornado do back-end ao front-end e, assim, o cliente poder ter acesso aos lanches da Quero Burguer.

### MEDIÇÃO 2

Data da medição: 19/01/2023

Descrição das configurações -> Quantidade de docker's: 1

Testes de carga (SLA):
- latência: 95º percentil - 11 ms
- vazão: 2.041 requisições/s -- 124.528 requisições ao longo do teste
- concorrência (limite de requisições simultâneas): 2.690 requisições

GRÁFICOS comparativos das medições feitas:
- Os gráficos estão na pasta "segundo-teste", que possui os arquivos PDF com as métricas e os gráficos para cada um dos serviços que os testes foram executados.

Melhorias/otimizações:
- Como esse serviço já foi aprimorado durante a realização de PCS no período passado, acabou que não teve nada para ser alterado,
tendo em vista que utilizamos o Framework Springy para o back-end PHP e o Framework Flask para o back-end em Python. Com isso, todas as otimizações
que utilizamos em nossas empresas foram replicadas para esse projeto, de modo que é o mesmo desempenho se colocado em máquinas virtuais semelhantes
ao que nossas empresas utilizam. Como não temos nenhum host de qualidade e temos que usar nosso próprio computador tanto para rodar os testes quanto
para rodar o docker responsável pelo sistema utilizado por esses testes, acabou que aconteceram variações por agora utilizarmos o k6 cloud para ser 
possível a criação de gráficos sobre a progressão dos testes, e, por isso, existiram algumas diferenças do primeiro
para o segundo teste, as vezes negativa e as vezes positiva.

## Atualizar Cadastro
Tipo de operação: atualização

Arquivos envolvidos (lista de arquivos envolvidos na implementação do Atualizar Cadastro):
- users.page.php (app\controllers\$restful\users.page.php)

### MEDIÇÃO 1

Data da medição: 21/12/2022

Descrição das configurações -> Quantidade de docker's: 1

Testes de carga (SLA):
- latência: 95º percentil - 1.287,63 ms
- vazão: 17,81 requisições/s -- 1,069 requisições ao longo do teste
- concorrência (limite de requisições simultâneas): 18 requisições

Potenciais gargalos do sistema:
- Como é um serviço que realiza UPDATE na base de dados relacional e a conexão com o banco de dados MySQL é fundamental para o funcionamento correto do serviço, o gargalo do sistema se deve à comunicação com a nossa base de dados.

### MEDIÇÃO 2

Data da medição: 19/01/2023

Descrição das configurações -> Quantidade de docker's: 1

Testes de carga (SLA):
- latência: 95º percentil - 1.079 ms
- vazão: 19 requisições/s -- 1.118 requisições ao longo do teste
- concorrência (limite de requisições simultâneas): 19 requisições

GRÁFICOS comparativos das medições feitas:
- Os gráficos estão na pasta "segundo-teste", que possui os arquivos PDF com as métricas e os gráficos para cada um dos serviços que os testes foram executados.

Melhorias/otimizações:
- Como esse serviço já foi aprimorado durante a realização de PCS no período passado, acabou que não teve nada para ser alterado,
tendo em vista que utilizamos o Framework Springy para o back-end PHP e o Framework Flask para o back-end em Python. Com isso, todas as otimizações
que utilizamos em nossas empresas foram replicadas para esse projeto, de modo que é o mesmo desempenho se colocado em máquinas virtuais semelhantes
ao que nossas empresas utilizam. Como não temos nenhum host de qualidade e temos que usar nosso próprio computador tanto para rodar os testes quanto
para rodar o docker responsável pelo sistema utilizado por esses testes, acabou que aconteceram variações por agora utilizarmos o k6 cloud para ser 
possível a criação de gráficos sobre a progressão dos testes, e, por isso, existiram algumas diferenças do primeiro
para o segundo teste, as vezes negativa e as vezes positiva.
