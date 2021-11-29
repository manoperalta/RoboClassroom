from selenium import webdriver
import tkinter as tk
from tkinter import ttk
import pandas as pd
import time

def site(Xurl):
    siteX = Xurl
    navegador = webdriver.Chrome()
    navegador.get(siteX)  #URL do classroom
    print('Carregando novo URL')
    time.sleep(35)
    print('Acesso concebido')
    navegador.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[4]/div[4]/div[1]/div/table/tbody/tr[3]/td[1]/div/div/div[2]').click() #selecionando
    print('Selecionando...')
    time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[4]/div[3]/div/div[1]/div[1]/div/button/span').click() #botao devolver
    print('Abrindo janela de devolutivas...')
    time.sleep(3)
    print('Devolvendo...')
    navegador.find_element_by_xpath('//*[@id="yDmH0d"]/div[10]/div/div[2]/div[3]/div[2]/span').click() #DEVOLVER da janela
    print('Fim do Processo...')
    time.sleep(3)
    print('Próximo evento')

def GUI():
    link = entry_xurl.get()
    site(link)


janela = tk.Tk() #Criar a Janela

#Criação da Janela
janela.title("APP Robo Classroom")

label_title = tk.Label(text="Insira a URL do Classroom")
label_title.grid(row=0, column=0, padx=15, pady=15, sticky='nswe', columnspan=4)

label_aviso = tk.Label(text="Ao abrir o Navegador você tera ")
label_aviso.grid(row=1, column=0, padx=15, pady=1, sticky='nswe', columnspan=4)

label_aviso2 = tk.Label(text="30s para realizar o login")
label_aviso2.grid(row=2, column=0, padx=15, pady=1, sticky='nswe', columnspan=4)

entry_xurl = tk.Entry()
entry_xurl.grid(row=3, column=0, padx=15, pady=15, sticky='nswe', columnspan=4)

botao_processar = tk.Button(text="Processar", command=GUI)
botao_processar.grid(row=4, column=0, padx=15, pady=15, sticky='nswe', columnspan=4)

label_by = tk.Label(text="By Jônathas M. Peralta")
label_by.grid(row=5, column=0, padx=15, pady=1, sticky='nswe', columnspan=4)

janela.mainloop()