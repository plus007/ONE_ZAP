Obrigado por estar utilizando este projeto.

Se possível contribua para o nosso desenvolvimento, submeta atualizações!


Requisitos para o projeto.

Firefox Browser
https://www.mozilla.org/pt-BR/firefox/new/

Geckodriver
https://github.com/mozilla/geckodriver/releases

-

Biblioteca selenium

pip install selenium


===

exemplo de uso.

Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from one import *
>>> browser = init_browser()
Inicializando navegador
Navegador Inicializado
Redirecionando para o whatsapp
Aperte enter depois de scanear. >
QR-CODE : OK
>>> send_msg(browser, "teste")
