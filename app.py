import pyautogui
import pandas as pd
import time

#passos para abri navegador
#apertar tecla windo

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

pyautogui.write("https://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")
time.sleep(1)

pyautogui.click(x=524, y=418)
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("SimplificaPython")
time.sleep(1)

pyautogui.press("tab")
pyautogui.press("enter")

tabela = pd.read_csv("alunos.csv")
time.sleep(3)

for linha in tabela.index:
    pyautogui.click(x=478, y=349)

    nome = tabela.loc[linha, "Nome"]
    pyautogui.write(nome)
    pyautogui.press("tab")

    email = tabela.loc[linha, "Email"]
    pyautogui.write(email)
    pyautogui.press("tab")

    endereco = tabela.loc[linha, "Endereco"]
    pyautogui.write(email)
    pyautogui.press("tab")

    telefone = tabela.loc[linha, "Telefone"]
    pyautogui.write(telefone)
    pyautogui.press("tab")

    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.scroll(5000)

