Requalificação Profissional – Análise e Recomendação em Python

Este projeto foi desenvolvido como parte da atividade da Global Solution, com foco em criar uma solução simples em Python capaz de analisar profissões em risco de automação e sugerir caminhos de requalificação.
A ideia é usar estruturas básicas da linguagem para coletar dados, processar a base de conhecimento e apresentar orientações de forma organizada.

## Objetivo do Sistema
O programa permite:

Consultar profissões com maior risco de automação
Identificar uma trilha de requalificação recomendada
Ver a base utilizada em formato de DataFrame
Rodar uma simulação completa verificando riscos e áreas futuras sugeridas
Tudo isso via menu no terminal, com interação direta com o usuário.
Tecnologias Utilizadas
Python 3
Pandas (para estruturar a base de dados)

# Para rodar o programa:
pip install pandas
python atividade.py
Estruturas Utilizadas no Código
A atividade exige alguns tipos de estruturas específicas. Abaixo explico como cada uma foi aplicada no programa.

# 1. Estrutura de Entrada

A coleta de dados é feita por input(), onde o usuário digita:
opção do menu
profissão atual
status de inclusão

# 2. Estrutura de Saída

Os resultados são exibidos diretamente no console:
Profissão analisada
Área de foco futuro
Habilidades necessárias
DataFrame com a base completa
Relatório final da simulação

# 3. Estrutura de Repetição

O menu roda dentro de um while True, permitindo que o usuário execute várias consultas sem reiniciar o programa.
Laços for percorrem a base para análise e simulação.

# 4. Estruturas Condicionais

if/elif/else tomam decisões com base na lógica do sistema, por exemplo:
quando a profissão é localizada
quando apenas o status de inclusão coincide
quando nenhum dado combina

# 5. Funções

O código é dividido em funções independentes:

buscar_trilha()

simular_base()

iniciar_sistema()

Essa separação mantém o código organizado e facilita a leitura.

6. Função Dentro de Função

Dentro de buscar_trilha() existe uma função interna chamada normalizar(), usada para padronizar os textos antes da comparação.
Ela só existe dentro daquela função, cumprindo o requisito de encapsulamento solicitado.

7. DataFrame

A base de profissões foi estruturada com o pandas.DataFrame, permitindo visualizar e manipular os dados de forma mais organizada.

Como Funciona o Sistema

O usuário acessa o menu inicial.

Escolhe entre buscar uma profissão, ver a base, rodar simulação ou sair.

O programa processa a escolha e apresenta o resultado.

O menu continua até que a opção de sair seja escolhida.
