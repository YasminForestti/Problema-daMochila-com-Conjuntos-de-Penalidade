import numpy as np
from utils.knapsack import Knapsack
class Construcao: 
    """"
    Classe que monta a lista de candidatos
    """
    def __init__(self,alpha):
        self.alpha = alpha 

    def LCR(self, mochila:Knapsack, verbose = False):
        """
        Método que monta a lista de candidatos restritas
        """
        while mochila.is_valid():
            current_items = mochila.get_items()
            ratios = mochila.get_cost_benefit_ratio()

            min_value = min(ratios)
            max_value = max(ratios)
            min_threshold = max_value - self.alpha*(max_value-min_value)

            lcr = [i for i in range(len(ratios)) if ratios[i] >= min_threshold]
            random_index = np.random.choice(lcr)

            new_items = current_items.copy()
            new_items[random_index] = 1
            mochila.replace_items(new_items)
        return current_items

    def perturbação(self,  mochila:Knapsack):
        swap = 0

        while mochila.is_valid():
            itens = mochila.get_items()

            dentro = np.where(itens == 1)[0]
            fora = np.where(itens == 0)[0]
            if swap < (len(dentro) * 0.1):

                item_descartado = np.random.choice(dentro)
                itens[item_descartado] = 0
                mochila.replace_items(itens)

                item_add = np.random.choice(fora)
                new_items = itens.copy()
                new_items[item_add] = 1
                mochila.replace_items(new_items)

                swap += 1
            else: 
                break
        
        return itens        



class BuscaLocal:
       
    def melhor_aprimorante(self, mochila):
        """
        Método que encontra o melhor aprimorante para a mochila percorrendo
        toda vizinhança da mochila. A vizinhança é explorada pelo método SWAP.

        Retorna: nova mochila com melhor solução encontrada ou a própria mochila se não houver melhoria.
        """
        melhor_mochila_itens = mochila.get_items().copy()
        melhor_valor = mochila.get_profit()
        # print(f"Profit inicial : {melhor_valor}")
        itens = mochila.get_items()

        dentro = np.where(itens == 1)[0]
        fora = np.where(itens == 0)[0]

        for i in dentro:
            vizinho_itens = itens.copy()
            vizinho_itens[i] = 0
            mochila.replace_items(vizinho_itens) 

            potencial_profit = mochila.get_potential_profits()
            profit = mochila.get_profit() 
            for j in fora:
                if potencial_profit[j] + profit > melhor_valor:
                    vizinho_itens[j] = 1
                    mochila.replace_items(vizinho_itens)
                    if mochila.is_valid():
                        melhor_mochila_itens = vizinho_itens.copy()
                        melhor_valor = mochila.get_profit()
                    vizinho_itens[j] = 0
                    mochila.replace_items(vizinho_itens)                     
       
        return melhor_mochila_itens
    
    def primeiro_aprimorante(self, mochila):
        """
        Método que encontra o melhor aprimorante para a mochila percorrendo
        toda vizinhança da mochila. A vizinhança é explorada pelo método SWAP.

        Retorna: nova mochila com melhor solução encontrada ou a própria mochila se não houver melhoria.
        """
        melhor_valor = mochila.get_profit()
        itens = mochila.get_items()

        dentro = np.where(itens == 1)[0]
        fora = np.where(itens == 0)[0]

        for i in dentro:
            vizinho_itens = itens.copy()
            vizinho_itens[i] = 0
            mochila.replace_items(vizinho_itens) 

            potencial_profit = mochila.get_potential_profits()  
            profit = mochila.get_profit() 
            for j in fora:          
                if potencial_profit[j] + profit > melhor_valor:
                    vizinho_itens[j] = 1
                    mochila.replace_items(vizinho_itens)
                    if mochila.is_valid():
                        return vizinho_itens
                    vizinho_itens[j] = 0
                    mochila.replace_items(vizinho_itens)  