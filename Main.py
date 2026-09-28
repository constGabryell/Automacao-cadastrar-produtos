import pyautogui
import pandas

#pyautogui.click -> clica com mouse
#pyautogui.write -> escreve com teclado
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta uma combinação de teclas(atalho)

#pyautogui.PAUSE -> pausa entre cada Ação do pyautogui

pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #Link do site que será feito o cadastro dos produtos
tabela = pandas.read_csv("produtos.csv") #Tabela com os produtos que serão cadastrados no site

print(tabela)

#algoritmo para executar todo o processo de login no site
pyautogui.sleep(3)  
pyautogui.press("win")#abre aba windows
pyautogui.write("brave")#abre o navegador
pyautogui.press("enter")

pyautogui.write(link)#link do site 
pyautogui.press("enter")    
pyautogui.sleep(3)  

#Login do site
pyautogui.click(x= 713, y=375)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")    

pyautogui.sleep(3)

#formulario de cadastro de produtos
for linha in tabela.index:


    #Código do produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x= 672, y=254)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #Marca do produto
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #Tipo do Produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #Categoria do Produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #Preço unitario do Produto
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    #Preco de custo do Produto
    preco_custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(preco_custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":

      pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")




