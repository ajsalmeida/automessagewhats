# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import random
from selenium import webdriver
import time


def retrieve_quote(): #essa função recupera uma frase aleatoria desse site
    url_base = 'https://www.frasesdobem.com.br/frases-inspiradoras'
    url_consulta = url_base+'/'+str(random.randint(1,11))
    #print("Pagina sorteada: "+url_consulta)

    url = requests.get(url_consulta)
    html = url.text

    fraseN = (random.randint(1,15))
    frase = ('frase'+str(fraseN))
    #print("Frase sorteada: "+frase)

    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)
    
    frases = soup.find('p', id=frase).text
    print("Frase escolhida: => "+frases)
    return frases

class WhatsappBot:
        def __init__(self):
            self.contatos = ['Eu Tim']
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        def EnviarMensagens(self):
            #<span dir="auto" title="Eu Tim" class="_35k-1 _1adfa _3-8er">Eu Tim</span>
            #<div tabindex="-1" class="_2A8P4">
            #<span data-testid="send" data-icon="send" class="">
            self.driver.get("https://web.whatsapp.com")
            time.sleep(30)
            for contato in self.contatos:
                contato = self.driver.find_element_by_xpath("//span[@title='Eu Tim']")
                time.sleep(3)
                contato.click()
                while True:
                    chat_box = self.driver.find_element_by_class_name('_2A8P4')
                    time.sleep(3)
                    chat_box.click()
                    self.mensagem = retrieve_quote()
                    chat_box.send_keys(self.mensagem)
                    botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                    time.sleep(3)
                    botao_enviar.click()
                    time.sleep(5) #periodo de envio de mensagem
            
bot = WhatsappBot()
bot.EnviarMensagens()