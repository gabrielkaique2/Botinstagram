#from wdpage import WDPage
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import random
from time import sleep;


class InstagramBot():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def Login(self):
        driver = self.driver

        driver.get('https://instagram.com')
        sleep(3)
        login_field = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_field.send_keys(self.username)
        sleep(3)
        password_field = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(self.password)
        sleep(3)
        password_field.send_keys(Keys.RETURN)
        sleep(3)
    
    def GoToLink(self,link):
        driver = self.driver

        driver.get(link)
        #iframe = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
        #driver.switch_to.frame(iframe)
        sleep(10)

    def Coment(self):
        driver = self.driver
            #text_field é a variavel que armazena o XPATH do campo de texto dos comentário.
        text_field = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
        sleep(1)
        text_field.click()
        sleep(1)
            #após o clique, deve redefinir a variavel text_field com o mesmo XPATH do campo! por algum motivo o webdriver perde a referência da DOM!
        text_field = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
        sleep(1)
        text_field.send_keys('Hello, World!')

    def SendComment(self):
        driver = self.driver
        
        pass

    def ToChoose(self,set):
        self.set = set
        #Vai escolher os IG's conforme a lista, de acordo com quantos IG's forem setados
        nomes = ["Miguel", "Arthur", "Gael", "Théo", "Heitor","Ravi","Davi","Bernardo","jovercino","amanda","puta que pariu","joberson","johnny","lucas"]

        chosen = [] 
        set = min(set, len(nomes)) # "nomes" é a variável da lista;
        while len(chosen) < set:
            escolhido = random.choice(nomes)   
            if escolhido not in chosen:
                chosen.append(escolhido)      
        return print(chosen)
        pass
    
bot = InstagramBot('rodriguesgabrielxx1999','040599gkar')
#bot.Login()
#bot.GoToLink('https://www.instagram.com/p/BnzzZb_B1gu/')
#bot.Coment()
bot.ToChoose(3)
sleep(20)