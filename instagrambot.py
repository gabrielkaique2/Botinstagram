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

    #antigo nome Coment() -> novo nome getField()
    def getField(self,text):
        driver = self.driver
        self.text = text

        #text_field é a variavel que armazena o XPATH do campo de texto dos comentário.
        text_field = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
        sleep(1)
        text_field.click()
        sleep(1)
        #após o clique, deve redefinir a variavel text_field com o mesmo XPATH do campo! por algum motivo o webdriver perde a referência da DOM!
        text_field = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')
        #sleep(1)
        text_field.send_keys()
        #text_field.send_keys(Keys.RETURN)

    def SendComment(self):
        driver = self.driver
        
        #função que encontra o botão de enviar comentário e clica nele para enviar! é necessário separar ele da função getField para não haver problemas de continuidade!

        subitComment = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mount_0_0_wl']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/div[2]/div")))
        subitComment.click()

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
    
        return chosen_string
    
    def loop(self,sec,rps): 
        driver = self.driver
        self.sec = sec
        self.rps = rps
        count = 0

        while count < rps:
            print(count)
            sleep(sec)
            escolhidos = self.ToChoose("""self.nomes""")
        """
            subitComment = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//*[@id='mount_0_0_wl']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/div[2]/div"))
            )
            subitComment.click()
            count = count +1
        return escolhidos
        """

    def writer(self,word):
        driver = self.driver
        self.word = word

        for char in word:
            sleep(random.uniform(0.1,1.2))
            #self.text_field.send_keys(char)
            #print(char)

    def comentar(self,n):
        driver = self.driver
        self.n = n

        while True:
            self.Coment(self.ToChoose(n))
        pass

bot =  InstagramBot('11','dsad')
bot.writer(bot.ToChoose(3))
