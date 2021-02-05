from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def init_browser():
    print("Inicializando navegador")
    browser = webdriver.Firefox()
    browser.maximize_window()
    print("Navegador Inicializado")
    print("Redirecionando para o Whatsapp")
    browser.get("https://web.whatsapp.com/")
    if input("Aperte enter depois de scanear. >") != None:
        print("QR-CODE : OK")
        return(browser)

def abrir_conversa(numero, browser):
    sleep_point(browser)
    link_cnvs = ("https://api.whatsapp.com/send?phone=55%s"%(numero)) # Considere mudar o 55 para o codigo do seu pais, não se esqueça de incluir o DDD do número, 51 9999999
    send_msg(browser, link_cnvs)
    def get_msg(browser): # retorna mensagens da conversa
        try:
            time.sleep(0.3)
            msgs = browser.find_elements_by_class_name("copyable-text")
            return(msgs)
        except:
            pass

    def click_link(browser):
        msgs = get_msg(browser)
        if msgs != None:
            texto = msgs[len(msgs)-2].click()
    click_link(browser)

def send_msg(browser,msg): # Envia uma mensagem no chat aberto
    time.sleep(0.2)
    input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    time.sleep(0.1)
    for i in msg.split("\n"):
        input_box.send_keys(Keys.SHIFT+Keys.ENTER)
        input_box.send_keys(i)

    time.sleep(0.1)
    input_box.send_keys(Keys.ENTER)

def sleep_point(browser): # Vai a um chat chamado nomeado Sleep para armazenar links e informações, o grupo precisa estar fixado.
    name = "Sleep"
    contatos = browser.find_elements_by_class_name("_1C6Zl")
    for contato in contatos:
        if name in contato.text :
            contato.click()
            break
