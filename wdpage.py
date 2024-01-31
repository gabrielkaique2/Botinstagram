from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
import random
from time import sleep;

class WDPage:
    def __init__(self,link):
        self._link = link
        webdriver = webdriver.Chrome()

        webdriver(link)
        sleep(10)