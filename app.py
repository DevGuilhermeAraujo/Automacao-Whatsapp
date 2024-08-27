"""
PRECISO AUTOMATIZAR MINHAS MENSAGENS P/ MEUS CLIENTES GOSTARIA DE SABER VALORES, E GOSTARIA QUE ENTRASSEM 
EM CONTATO COMIGO P/ EXPLICAR MELHOR, QUERO PODER MANDAR MENSAGENS DE COBRANÇA EM DETERMINADO DIA COM 
CLIENTES COM VENCIMENTO DIFERENTE
"""
# Descrever os passos manuais e depois transformar isso em código
import openpyxl as oxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui


webbrowser.open('https://web.whatsapp.com/')
sleep(30)

# Ler planilha e guardar informações sobre nome, telefone e data de vencimento
workbook = oxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Plan1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    
    mensagem = f'Ola {nome} seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Favor pagar no link https://www.link_do_pagamento.com'
    
    # Criar links personalizados do whatsapp e enviar mensagens para cada cliente
    # Com base nos dados da planilha
    
    try:
        link_mensagem_whatsapp= f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
        seta = pyautogui.locateCenterOnScreen('send.png')
        sleep(2)
        pyautogui.click(seta[0],seta[1])
        sleep(2)
        pyautogui.hotkey('ctrl'+'w')
        sleep(2)
    except:
        print(f'Não foi possível enviar mensagem')
        with open('erros.csv', 'a', newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}')