import random

def ToChoose(self,set):
    #driver = self.driver
    set = set
    #Vai escolher os IG's conforme a lista, de acordo com quantos IG's forem setados

    nomes = ["Miguel", "Arthur", "Gael", "Théo", "Heitor","Ravi","Davi","Bernardo","jovercino","amanda","puta que pariu","joberson","johnny","lucas"]

    chosen = [] 
    set = min(set, len(nomes)) # "nomes" é a variável da lista;
    while len(chosen) < set:
        escolhido = random.choice(nomes)   
        if escolhido not in chosen:
            chosen.append(escolhido)      
    return print(chosen)

ToChoose(1,5)