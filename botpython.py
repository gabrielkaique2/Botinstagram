from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import random
from time import sleep;
from functions import loop;

driver = webdriver.Edge()

driver.get("https://www.instagram.com/")
sleep(10)

userLogin = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
passwordLogin = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
submitLogin = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]")

userLogin.send_keys("rodriguesgabrielxx1999") #Aqui vai o login do user
sleep(3)
passwordLogin.send_keys("040599gkar") #Aqui vai a senha
sleep(3)
submitLogin.submit()
sleep(5)

driver.get("https://www.instagram.com/p/Bonut3iBVoq/") #Aqui vai o post do sorteio
commentField = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"//textarea[@aria-label='Adicione um comentário...']"))
)

commentField.click()
sleep(3)
sendComment = driver.find_element(By.XPATH,"//textarea[@aria-label='Adicione um comentário...']")

sendComment.send_keys(loop(5,1,3))
sleep(10)

