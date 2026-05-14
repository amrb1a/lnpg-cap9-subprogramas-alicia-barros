# lnpg-cap9-subprogramas-alicia-barros

# Atividade Prática — Capítulo 9: Subprogramas

**Disciplina:** Linguagens de Programação  
**Nome:** Alicia Maria Rocha de Barros

### Tarefa 1 — Modularização em Java

Nesta tarefa foi desenvolvido um sistema simples de controle acadêmico em Java. O programa lê o nome de 5 alunos, recebe 3 notas para cada aluno, calcula a média, determina a situação final e apresenta um relatório.

Foram criadas duas versões do programa: uma versão monolítica e uma versão modularizada.

Na versão monolítica, toda a lógica do programa está concentrada dentro do método `main`. Isso funciona, mas deixa o código mais longo e menos organizado, pois leitura de dados, cálculo de média, verificação da situação e impressão do relatório ficam misturados no mesmo bloco.

Na versão modularizada, o programa foi dividido em métodos menores, cada um com uma responsabilidade específica. Foram usados os métodos `lerAluno()`, `lerNotas()`, `calcularMedia()`, `determinarSituacao()` e `imprimirRelatorio()`.

Essa divisão melhora a legibilidade, pois o código fica mais fácil de entender. Também melhora a reutilização, porque os métodos podem ser chamados novamente sem repetir código. A manutenção fica mais simples, já que uma alteração no cálculo da média ou na regra de aprovação pode ser feita em apenas um método.

A modularização também deixa o fluxo principal mais claro, porque o método `main` mostra apenas a sequência geral do programa. Além disso, os métodos ficam menores e mais coesos, pois cada um executa uma tarefa bem definida.

## Tarefa 2 - Modularização em Python

Nesta tarefa foi desenvolvido um sistema simples de vendas em Python. O programa permite cadastrar produtos, informar quantidade e preço unitário, calcular o total de cada produto, aplicar desconto e imprimir um cupom final.

Foram criadas duas versões: uma versão monolítica e uma versão modularizada.Na versão monolítica, toda a lógica do programa está no fluxo principal. A leitura dos produtos, o cálculo dos totais, a aplicação dos descontos e a impressão do cupom ficam juntos no mesmo código.Na versão modularizada, o programa foi dividido em funções, como `ler_produto()`, `calcular_subtotal()`, `calcular_desconto()`, `calcular_total()` e `imprimir_cupom()`.

As partes mais repetitivas eram o cálculo do subtotal, o cálculo do desconto e a impressão das informações do cupom. Com a modularização, essas partes ficaram mais organizadas e reutilizáveis.

A modularização melhorou a legibilidade, pois cada função possui uma responsabilidade específica. Também facilitou a manutenção, porque uma mudança na regra de desconto pode ser feita apenas na função `calcular_desconto()`, sem alterar o restante do programa.

## Tarefa 3 - Passagem de Parâmetros por Valor em Java

Nesta tarefa foi criado um programa em Java para demonstrar a passagem de parâmetros por valor usando um tipo primitivo.

No programa, a variável `valor` recebe o número 10 no método `main`. Esse valor é passado para o método `alterarNumero(int x)`. Dentro do método, o parâmetro `x` recebe uma cópia do valor original e depois é alterado para 20.

Mesmo após essa alteração dentro do método, a variável `valor` no método `main` continua valendo 10. Isso acontece porque Java não passa a própria variável original para o método, mas sim uma cópia do valor armazenado nela.

Portanto, a alteração feita em `x` tem efeito apenas dentro do método `alterarNumero`. Esse exemplo mostra que tipos primitivos, como `int`, são passados por valor em Java.

## Tarefa 4 - Objetos e Referência em Java

Nesta tarefa foi criado um programa em Java para demonstrar o comportamento de objetos em chamadas de métodos.

Foi criada a classe `Produto`, com os atributos `nome` e `preco`. No método `main`, foi criado um objeto chamado `produto1`, representando um café com preço inicial de R$ 40,45. Depois, esse objeto foi passado para o método `aplicarDesconto(Produto p)`.

Dentro do método, foi calculado um desconto de 20% e o atributo `preco` do objeto foi alterado. Ao imprimir novamente o objeto no `main`, foi possível perceber que o preço continuou alterado.Isso acontece porque Java sempre usa passagem por valor. Porém, quando trabalhamos com objetos, o valor copiado é a referência para o objeto na memória. Assim, o parâmetro `p` recebe uma cópia da referência de `produto1`, mas essa cópia aponta para o mesmo objeto.

Portanto, Java não possui passagem por referência verdadeira. O que é copiado na chamada é o valor da referência. Como o parâmetro e a variável original apontam para o mesmo objeto, alterações feitas nos atributos permanecem após a chamada do método.

## Tarefa 5 - Projeto Livre com Subprogramas

Nesta tarefa foi desenvolvido um sistema simples de estoque em Python. O programa permite cadastrar produtos, listar os produtos cadastrados, buscar um produto pelo nome, atualizar a quantidade em estoque e calcular o valor total armazenado.

O programa foi dividido em vários subprogramas para deixar o código mais organizado. Foram criadas as funções `exibir_menu()`, `ler_opcao()`, `cadastrar_produto()`, `listar_produtos()`, `encontrar_produto()`, `buscar_produto()`, `atualizar_quantidade()`, `calcular_valor_total()` e `executar_sistema()`.

O projeto possui mais de 6 subprogramas e utiliza passagem de parâmetros em várias funções. Também possui funções com retorno, como `ler_opcao()`, `encontrar_produto()` e `calcular_valor_total()`.

A função `exibir_menu()` mostra as opções disponíveis. A função `ler_opcao()` lê a escolha do usuário. A função `cadastrar_produto()` adiciona novos produtos à lista. A função `listar_produtos()` exibe os produtos cadastrados. A função `encontrar_produto()` procura um produto pelo nome. A função `buscar_produto()` mostra os dados de um produto específico. A função `atualizar_quantidade()` altera a quantidade de um produto e a função `calcular_valor_total()` calcula o valor total do estoque.

### Diagrama simples das chamadas

executar_sistema()  
→ exibir_menu()  
→ ler_opcao()  
→ cadastrar_produto(produtos)  
→ listar_produtos(produtos)  
→ buscar_produto(produtos)  
   → encontrar_produto(produtos, nome_busca)  
→ atualizar_quantidade(produtos)  
   → encontrar_produto(produtos, nome_busca)  
→ calcular_valor_total(produtos)

### Justificativa da divisão dos subprogramas

A divisão em subprogramas foi feita para evitar que todo o código ficasse concentrado em uma única parte. Cada função possui uma responsabilidade específica, o que melhora a organização, a leitura e a manutenção do programa.

### Dificuldades encontradas

Uma dificuldade foi organizar os produtos dentro de uma lista usando dicionários. Também foi necessário criar uma função de busca para evitar repetir o mesmo código em partes diferentes do programa.

### Vantagens percebidas da modularização

A modularização deixou o programa mais claro e mais fácil de modificar. Por exemplo, se for necessário mudar a forma de cálculo do valor total ou a forma de busca dos produtos, basta alterar apenas a função responsável. Isso evita repetição de código e melhora a reutilização.
