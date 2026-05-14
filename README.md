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

Nesta tarefa foi desenvolvido um sistema simples de vendas em Python. O programa lê o nome dos produtos, a quantidade e o preço unitário. Depois calcula o subtotal, aplica desconto quando necessário, calcula o total final e imprime um cupom formatado.

Foram criadas duas versões: uma versão monolítica e uma versão modularizada.Na versão monolítica, toda a lógica está escrita diretamente no fluxo principal do programa. A leitura dos dados, o cálculo do subtotal, o cálculo do desconto, o cálculo do total e a impressão do cupom ficam juntos no mesmo bloco de código.Na versão modularizada, o programa foi dividido em funções. Foram usadas as funções `ler_produto()`, `calcular_subtotal()`, `calcular_desconto()`, `calcular_total()` e `imprimir_cupom()`.

As partes mais repetitivas estavam relacionadas à leitura dos dados dos produtos e ao cálculo dos valores. Com as funções, essas partes ficaram mais organizadas e mais fáceis de reutilizar.

A modularização melhorou a legibilidade porque cada função possui uma responsabilidade específica. Também facilitou a manutenção, pois uma alteração na regra de desconto, por exemplo, pode ser feita apenas na função `calcular_desconto()`, sem precisar modificar o programa inteiro.
