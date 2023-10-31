import PySimpleGUI as sg

# Criação de Layout
def criar_janela_inicial():
    sg.theme('DarkTeal9')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Todo List do Naoki', layout=layout, finalize=True)

#Janela
janela = criar_janela_inicial()

while True: 
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
            break
    elif event == 'Nova Tarefa':
         janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()