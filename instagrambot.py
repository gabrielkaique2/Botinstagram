from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
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
        sleep(20)
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
        sleep(1)
        submitComment.send_keys(Keys.RETURN)
        print(f"{self}: comentário enviado com sucesso")
        sleep(3)
        #submitComment.clear()

    def ToChoose(self,num_to_choose):
        # Lista de nomes de usuários do Instagram
        nomes = ["crisiane_melissas", "eu_fafa_", "naaty._ap", "lai.ribeiroo", "eu_pedagogazi", "danioliveiras22", "admilton.gr", "fatinhaaparecida_", "sanndymarinho", "eusoumah_delgado35", "_ange26", "edutoledo299","lipe_odz", "crispv2021","patricialopes5451","sandradossantos7635","manuella_nawane_1308","lais_051993","olindinamarlene1955_ms"]

        chosen = []
        if num_to_choose <= 1:
            escolhido = random.choice(nomes)
            escolhido_com_arroba = "@" + escolhido
            chosen.append(escolhido_com_arroba)
            chosen_string = ''.join(chosen)
            print(f"{self}: {chosen_string}")
            return chosen_string
        else:
            num_to_choose = min(num_to_choose, len(nomes))# Escolhe os nomes não adicionados na lista chosen
            while len(chosen) < num_to_choose:
                escolhido = random.choice(nomes)
                # Adiciona "@" ao início do nome escolhido
                escolhido_com_arroba = "@" + escolhido
                if escolhido_com_arroba not in chosen:
                    chosen.append(escolhido_com_arroba)
            
            # Concatena os elementos da lista chosen em uma única string separada por espaços
            chosen_string = ' '.join(chosen)
            print(f"{self}: {chosen_string}")
            return chosen_string

    def writer(self,word):
        #quando for chamar a função writer, colocar como parâmetro 'word' a função ToChoose(n) para escrever a partir dos IGs
        driver = self.driver
        self.word = word
        text_field = self.getField()
        for char in word:
            text_field.clear()
            sleep(random.uniform(0.1,0.5))
            text_field.send_keys(char)

    def main(self,cicle,restTime,igs,link):
        #Função principal onde se encontra o comando que realmente faz o código funcionar!
        #'cicle' é a quantidade de ciclos
        #'restTime' é o intervalo entre envio
        #'igs' é a quantidade de pessoas que vc quer mencionar por comentário
        #'link' é o link do sorteio
        driver = self.driver
        self.Login()
        self.GoToLink(link)
        counter = 0
        while counter < cicle:
            self.getField()
            self.writer(self.ToChoose(igs))
            sleep(2)
            self.SendComment()
            sleep(restTime)
            counter += 1
        print(f'{self}: Fim de ciclo')

bot =  InstagramBot('username','password')
bot.main('cicles','rest time','@s','link do sorteio')