from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import random
from time import sleep;

driver = webdriver.Edge()

driver.get("https://www.instagram.com/")
sleep(10)

userLogin = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
passwordLogin = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
submitLogin = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]")
elogios = ["linda, te amo ","muito bom ","excelente conteúdo ","você é demais ","o vasco é gigante ", "testando robo python "]

userLogin.send_keys("aqui vem o login da conta")
sleep(3)
passwordLogin.send_keys("aqui vem a senha da conta")
sleep(3)
submitLogin.submit()
sleep(5)
driver.get("aqui vem o post do sorteio no insta")
commentField = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"//textarea[@aria-label='Adicione um comentário...']"))
)
commentField.click()
sleep(3)
sendComment = driver.find_element(By.XPATH,"//textarea[@aria-label='Adicione um comentário...']")

contador = 0

while contador < 5:
    sendComment.send_keys(random.choice(elogios))
    contador = contador + 1
    sleep(2)

sleep(5)