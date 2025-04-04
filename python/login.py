from PySimpleGUI import PySimpleGUI as sg
import requests

url = 'http://localhost:3000/logar'

sg.theme('Dark Blue 3')
layout = [
    [sg.Text('Nome de Usuario: '), sg.Input(key='nome', size=(20, 1))],
    [sg.Text('Senha: '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Button('Entrar', key='logar')]
]

janela = sg.Window('Login', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break;
    
    if evento == 'logar' and len(valores['nome']) == 0 or len(valores['senha']) == 0:
        sg.popup('Preencha todos os campos', title='Aviso', text_color='white', background_color='red')
    else:
        login = {'nome': valores['nome'], 'senha': valores['senha']}
        try:
            resposta = requests.post(url, json=login)
            if resposta.json()['codigo'] == 1:
                sg.popup(resposta.json()['mensagem'], title='Aviso')
            elif resposta.json()['codigo'] == 0:
                sg.popup(resposta.json()['mensagem'], title='Aviso')
        except requests.exceptions.RequestException as e:
            print(f'Falha ao enviar os dados: {e}')