import pandas as pd
import random
import matplotlib.pyplot as plt

class Participante:
    def __init__(self, nome, capital_inicial):
        self.nome = nome
        self.capital = capital_inicial
        self.posicao = 0
        self.capitais_historico = []
        self.posicoes_historico = []
        self.algoritmo_probabilistico = self.gerar_algoritmo()

    def gerar_algoritmo(self):
        return lambda x: random.uniform(0, 1) > 0.5

    def tomar_decisao(self, cotacao):
        if self.algoritmo_probabilistico(cotacao):
            quantidade_compra = random.randint(1, 10)
            custo = quantidade_compra * cotacao
            if custo <= self.capital:
                self.posicao += quantidade_compra
                self.capital -= custo
        else:
            if self.posicao > 0:
                quantidade_venda = random.randint(1, self.posicao)
                self.posicao -= quantidade_venda
                self.capital += quantidade_venda * cotacao

        self.capitais_historico.append(self.capital)
        self.posicoes_historico.append(self.posicao)

def simular_cenario_com_dados(dataset_path, num_participantes, num_intervalos):
    try:
        df = pd.read_csv(dataset_path)
        cotacoes = df['cotação'].tolist()

        participantes = [Participante(f"Participante {i}", capital_inicial=10000) for i in range(num_participantes)]

        for intervalo in range(num_intervalos):
            cotacao_atual = cotacoes[intervalo]
            print(f"\nIntervalo {intervalo + 1} - Cotação Atual: {cotacao_atual}")

            for participante in participantes:
                participante.tomar_decisao(cotacao_atual)
                print(f"{participante.nome}: Posição = {participante.posicao}, Capital = {participante.capital}")

        for participante in participantes:
            plt.plot(participante.capitais_historico, label=f"{participante.nome} - Capital")
            plt.plot(participante.posicoes_historico, label=f"{participante.nome} - Posição")

        plt.xlabel('Intervalo')
        plt.ylabel('Valor')
        plt.legend()
        plt.show()

        for participante in participantes:
            print(f"\nEstatísticas para {participante.nome}:")
            print(f"Capital Final: {participante.capital}")
            print(f"Posição Final: {participante.posicao}")

    except Exception as e:
        print(f"Erro ao processar os dados: {e}")

simular_cenario_com_dados('dados_banco_central.csv', num_participantes=5, num_intervalos=5)

