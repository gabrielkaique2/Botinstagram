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
        driver.set_window_size(1980,1080)

        driver.get('https://instagram.com')
        sleep(3)
        login_field = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_field.send_keys(self.username)
        sleep(3)
        password_field = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(self.password)
        sleep(3)
        password_field.send_keys(Keys.RETURN)
        sleep(10)
        print(f'{self}: Login bem sucedido')

    def GoToLink(self,link):
        driver = self.driver
        driver.get(link)
        sleep(5)
        print(f'{self}: Link acessado')

    def getField(self):
        driver = self.driver
        #text_field é a variavel que armazena o XPATH do campo de texto dos comentário.
        text_field = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
        sleep(1)
        text_field.click()
        sleep(1)
        #após o clique, deve redefinir a variavel text_field com o mesmo XPATH do campo! por algum motivo o webdriver perde a referência da DOM!
        text_field = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
        #sleep(1)
        print(f'{self}: Campo encontrado')
        return text_field

    def SendComment(self):
        driver = self.driver
        
        #função que encontra o botão de enviar comentário e clica nele para enviar! é necessário separar ele da função getField para não haver problemas de continuidade!

        submitComment = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
        submitComment.send_keys(Keys.RETURN)
        print(f"{self}: comentário enviado com sucesso")
        #submitComment.clear()

    def ToChoose(self, num_to_choose):
        #em nomes será adicionado os IG's
        nomes = ["Miguel", "Arthur", "Gael", "Théo", "Heitor","Ravi","Davi","Bernardo","jovercino","amanda","puta que pariu","joberson","johnny","lucas"]
        
        #verifica se o valor num_to_choose é menor que o comprimento da lista nomes
        num_to_choose = min(num_to_choose, len(nomes))

        chosen = []

        #escolhe os nomes não adicionados na lista chosen
        while len(chosen) < num_to_choose:
            escolhido = random.choice(nomes)   
            if escolhido not in chosen:
                chosen.append(escolhido)
        # Concatena os elementos da lista chosen em uma única string separada por espaços
        chosen_string = ' '.join(chosen)
        print(f'{self}: IGs: {chosen_string}')
        return chosen_string
    
    def writer(self,word):
        #quando for chamar a função writer, colocar como parâmetro 'word' a função ToChoose(n) para escrever a partir dos IGs

        driver = self.driver
        self.word = word

        text_field = self.getField()

        for char in word:
            sleep(random.uniform(0.1,0.9))
            text_field.send_keys(char)
            #print(char)

    def main(self,n,time,link):
        #Função principal onde se encontra o comando que realmente faz o código funcionar!
        #'n' é a qtd de @s
        #'time' é o intervalo entre envios
        #'link' é o link do sorteio
        driver = self.driver
        self.Login()
        self.GoToLink(link)
        counter = 0
        while counter < n:
            self.getField()
            self.writer(self.ToChoose(3))
            self.SendComment()
            sleep(time)
            counter += 1
        print(f'{self}: Fim de ciclo')

bot =  InstagramBot()
bot.main()