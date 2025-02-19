# README

## Cálculo da Tensão de Desequilíbrio do Neutro

Este repositório contém um programa que calcula a **tensão de desequilíbrio do neutro** em um sistema elétrico com **estrela isolada**, considerando o caso em que uma das fases fique completamente aberta devido à queima de um fusível.

### Objetivo
O objetivo principal deste programa é demonstrar que, em tais condições de desequilíbrio, pode-se utilizar um **TC de neutro** posicionado entre as estrelas isoladas com uma tensão significativamente menor que a **tensão de linha do sistema**. Esse resultado pode viabilizar economicamente o uso de TCs de neutro de menor especificação, reduzindo custos sem comprometer a precisão da medição.

### Funcionamento
O código simula a situação em que uma das fases do sistema trifásico deixa de conduzir corrente, calculando:
- A nova posição do neutro flutuante;
- A tensão resultante do neutro em relação à terra;
- A diferença de tensão entre os neutros das duas estrelas isoladas;
- A viabilidade de medição da tensão de neutro com um TC de menor especificação.

### Estrutura do Código
O programa é estruturado para:
1. Definir os parâmetros elétricos do sistema;
2. Simular o desequilíbrio causado pela fase aberta;
3. Calcular as novas tensões de neutro;
4. Apresentar os resultados para análise da viabilidade do TC de neutro.

### Como Usar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Execute o código conforme as instruções no arquivo principal.
3. Analise os resultados e compare com os critérios de escolha do TC de neutro.

### Contribuição
Caso queira contribuir com melhorias ou novos casos de estudo, sinta-se à vontade para abrir um pull request ou entrar em contato.

### Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

