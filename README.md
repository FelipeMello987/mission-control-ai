# Mission Control AI

Sistema em Python que simula o monitoramento de uma missão espacial por meio de ciclos de análise.

## Como funciona

O programa armazena os dados da missão em uma matriz chamada `dados_missao`, onde cada linha representa um ciclo e cada coluna representa um sensor: temperatura, comunicação, bateria, oxigênio e estabilidade.

A cada ciclo, o sistema classifica cada sensor como **NORMAL**, **ATENÇÃO** ou **CRÍTICO**, calcula uma pontuação de risco e classifica o ciclo como **MISSÃO ESTÁVEL**, **MISSÃO EM ATENÇÃO** ou **MISSÃO CRÍTICA**.

Ao final, é gerado um relatório com médias, ciclo mais crítico, tendência da missão, área mais afetada e conclusão geral.

## Estrutura do código

- Funções individuais para analisar cada sensor
- Função para classificar o ciclo com base na pontuação
- Função para identificar tendência e área mais afetada
- Função para gerar recomendações automáticas
- Função principal que percorre os ciclos e exibe o relatório final
