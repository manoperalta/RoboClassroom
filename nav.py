from selenium import webdriver
import time


site = input('Digite o url:')
navegador = webdriver.Chrome()
navegador.get(site)
time.sleep(3)
navegador.find_element_by_xpath().click()
