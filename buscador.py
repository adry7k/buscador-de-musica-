import pyautogui
import time
def buscador():          
    print("Qual musica você está procurando?")
    nome_da_banda_ou_musico = input("Informe o nome da banda/cantor(a):")
    nome_da_musica = input("Informe o nome da musica:")
    return nome_da_banda_ou_musico, nome_da_musica
nome_da_banda_ou_musico, nome_da_musica = buscador()
busca = f"{nome_da_banda_ou_musico} - {nome_da_musica}"
print(busca)
time.sleep(2)
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=425, y=904)
time.sleep(1)
pyautogui.click(x=402, y=87,clicks=2)
pyautogui.write(busca)
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.click(x=918, y=565)