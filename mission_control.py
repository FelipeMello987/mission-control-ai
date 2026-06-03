NOME_MISSAO = "Helios Deep Survey"
NOME_EQUIPE = "Equipe Nebula"

dados_missao = [
    [22, 95, 91, 98, 93],
    [26, 83, 76, 95, 87],
    [32, 67, 60, 92, 72],
    [37, 44, 35, 85, 52],
    [41, 25, 17, 76, 30],
    [35, 58, 29, 81, 47],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]


def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura baixa demais"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(riscos):
    if riscos[-1] > riscos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos[-1] < riscos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontos_por_area):
    maior_idx = 0
    for i in range(1, len(pontos_por_area)):
        if pontos_por_area[i] > pontos_por_area[maior_idx]:
            maior_idx = i
    return areas_monitoradas[maior_idx]


def gerar_recomendacao(resultados_ciclo):
    status_temp, _, _ = resultados_ciclo[0]
    status_com, _, _ = resultados_ciclo[1]
    status_bat, _, _ = resultados_ciclo[2]
    status_oxi, _, _ = resultados_ciclo[3]
    status_est, _, _ = resultados_ciclo[4]

    criticos = []
    atencoes = []

    if status_temp == "CRÍTICO":
        criticos.append("Verificar controle térmico da missão.")
    if status_com == "CRÍTICO":
        criticos.append("Tentar restabelecer contato com a base.")
    if status_bat == "CRÍTICO":
        criticos.append("Ativar modo de economia de energia.")
    if status_oxi == "CRÍTICO":
        criticos.append("Acionar protocolo de suporte à vida.")
    if status_est == "CRÍTICO":
        criticos.append("Reduzir operações não essenciais.")

    if status_temp == "ATENÇÃO":
        atencoes.append("Monitorar temperatura.")
    if status_com == "ATENÇÃO":
        atencoes.append("Verificar sinal de comunicação.")
    if status_bat == "ATENÇÃO":
        atencoes.append("Conservar energia.")
    if status_oxi == "ATENÇÃO":
        atencoes.append("Monitorar suprimento de oxigênio.")
    if status_est == "ATENÇÃO":
        atencoes.append("Avaliar estabilidade dos sistemas.")

    if len(criticos) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
    elif criticos:
        return " ".join(criticos)
    elif atencoes:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Manter operação normal e continuar monitoramento."


def calcular_ciclo(ciclo):
    temp, com, bat, oxi, est = ciclo
    resultados = [
        analisar_temperatura(temp),
        analisar_comunicacao(com),
        analisar_bateria(bat),
        analisar_oxigenio(oxi),
        analisar_estabilidade(est),
    ]
    pontuacao = sum(r[1] for r in resultados)
    return resultados, pontuacao


def exibir_ciclo(num_ciclo, ciclo, resultados, pontuacao):
    nomes_sensores = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]
    unidades = ["°C", "%", "%", "%", "%"]
    valores = list(ciclo)

    print(f"\nCICLO {num_ciclo}")
    print("-" * 60)
    for i in range(5):
        status, _, descricao = resultados[i]
        print(f"{nomes_sensores[i]}: {valores[i]}{unidades[i]} | {status} | {descricao}")

    classificacao = classificar_ciclo(pontuacao)
    recomendacao = gerar_recomendacao(resultados)
    print(f"\nPontuação de risco do ciclo: {pontuacao}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao}")


def gerar_relatorio_final(todos_riscos, pontos_por_area):
    qtd_ciclos = len(dados_missao)
    ciclo_critico = todos_riscos.index(max(todos_riscos)) + 1
    risco_medio = sum(todos_riscos) / qtd_ciclos
    qtd_criticos = sum(1 for r in todos_riscos if r >= 6)
    tendencia = analisar_tendencia(todos_riscos)
    area_afetada = identificar_area_mais_afetada(pontos_por_area)
    class_final = classificar_ciclo(round(risco_medio))

    medias = []
    for col in range(5):
        medias.append(sum(dados_missao[l][col] for l in range(qtd_ciclos)) / qtd_ciclos)

    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"\nQuantidade de ciclos analisados: {qtd_ciclos}")
    print(f"\nMédia de temperatura: {medias[0]:.2f} °C")
    print(f"Média de comunicação: {medias[1]:.2f}%")
    print(f"Média de bateria:     {medias[2]:.2f}%")
    print(f"Média de oxigênio:    {medias[3]:.2f}%")
    print(f"Média de estabilidade:{medias[4]:.2f}%")
    print(f"\nCiclo mais crítico: Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {max(todos_riscos)}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_criticos}")
    print(f"\nTendência da missão:")
    print(f"  {tendencia}")
    print(f"\nPontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontos_por_area[i]} pontos")
    print(f"\nÁrea mais afetada:")
    print(f"  {area_afetada}")
    print(f"\nClassificação final da missão:")
    print(f"  {class_final}")
    print(f"\nConclusão:")

    if class_final == "MISSÃO CRÍTICA":
        print("  A missão atravessou períodos de risco elevado. São necessárias")
        print("  ações imediatas de recuperação antes de retomar operação plena.")
    elif class_final == "MISSÃO EM ATENÇÃO":
        print("  A missão apresentou instabilidade relevante durante a operação.")
        print("  A equipe deve manter o plano de contingência ativo e monitorar")
        print("  os sistemas críticos continuamente.")
    else:
        print("  A missão transcorreu dentro dos parâmetros normais de segurança.")
        print("  Todos os sistemas permaneceram estáveis ao longo dos ciclos.")

    print("=" * 60)


def main():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    todos_riscos = []
    pontos_por_area = [0] * 5

    for idx, ciclo in enumerate(dados_missao):
        resultados, pontuacao = calcular_ciclo(ciclo)
        exibir_ciclo(idx + 1, ciclo, resultados, pontuacao)
        todos_riscos.append(pontuacao)
        for col in range(5):
            pontos_por_area[col] += resultados[col][1]

    gerar_relatorio_final(todos_riscos, pontos_por_area)


if __name__ == "__main__":
    main()