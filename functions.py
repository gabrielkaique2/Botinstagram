from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import random
from time import sleep;

nomes = ["Miguel", "Arthur", "Gael", "Théo", "Heitor","Ravi","Davi","Bernardo","jovercino","amanda","puta que pariu","joberson","johnny","lucas"]

def escolhe(qtd): #Função responsável por escolher um item de uma lista/ Importante quando estivermos tratando os IGs do Instagram;
    chosen = [] 
    qtd = min(qtd, len(nomes)) # "nomes" é a variável da lista;
    while len(chosen) < qtd:
        escolhido = random.choice(nomes)   
        if escolhido not in chosen:
            chosen.append(escolhido)      
    return chosen

