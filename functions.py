from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import random
from time import sleep;

driver = webdriver.Edge()
nomes = ["Miguel", "Arthur", "Gael", "Théo", "Heitor","Ravi","Davi","Bernardo","jovercino","amanda","puta que pariu","joberson","johnny","lucas"] #Raiz IGs

def escolhe(qtd): #Função responsável por escolher um item de uma lista/ Importante quando estivermos tratando os IGs do Instagram;
    chosen = [] 
    qtd = min(qtd, len(nomes)) # "nomes" é a variável da lista;
    while len(chosen) < qtd:
        escolhido = random.choice(nomes)   
        if escolhido not in chosen:
            chosen.append(escolhido)      
    return chosen

def loop(sec,rps,nomes): #a função loop vai repetir os loops de comentários pedindo tempo entre comentários, ciclops de repetições e a qtd de nomes que vai puxar da lista usando a função escolhe;
    segundos = sec
    repslp = rps
    count = 0

    while count < repslp:
        print(count)
        sleep(segundos)
        escolhidos = escolhe(nomes)

        subitComment = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id='mount_0_0_wl']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/div[2]/div"))
        )
        subitComment.click()
        
        count = count +1
    return escolhidos

