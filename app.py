'''
from wdpage import WDPage
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import random
from time import sleep;
from functions import loop;

bot = webdriver.Firefox()
bot.get('https://www.instagram.com/')
sleep(5)
login_field = bot.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
password_field = bot.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
submit = bot.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
login_field.send_keys('rodriguesgabrielxx1999') #Here comes the IG from instagram
password_field.send_keys('040599gkar') #Here comes the password from the IG above
submit.submit()
sleep(5)
bot.get('https://www.instagram.com/p/BnzzZb_B1gu/')
sleep(5)
iframe = WebDriverWait(bot, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
bot.switch_to.frame(iframe)
sleep(5)'''
#botao = WebDriverWait(bot, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, '_aamx')))
txt_area = bot.find_element(By.XPATH, '//div[@id="mount_0_0_bp"]//section/main//div[@class="x1i10hfl"]//div[@class="x6s0dn4 x78zum5 xdt5ytf xl56j7k"]/svg')
sleep(3)
txt_area.click()
#print(txt_area)

