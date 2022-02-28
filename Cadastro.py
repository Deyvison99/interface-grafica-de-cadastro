from PySimpleGUI import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.theme('DarkRed1')

        # Criando Layout
        layout = [
            [sg.Text('CADASTRO')],
            [sg.Text('Nome:'), sg.Input(size=(20, 1), key='nome')],
            [sg.Text('Idade:'), sg.Input(size=(5, 0), key='idade')],
            [sg.Text('Altura:')],
            [sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(15, 20), key='sliderAltura')],
            [sg.Text('Peso:'), sg.Input(size=(5, 0), key='peso')],
            [sg.Text('Sexo:')],
            [sg.Checkbox('Masculino', key='masculino'), sg.Checkbox('Feminino', key='feminino')],
            [sg.Button('ENTER')],
            [sg.Output(size=(30, 20))]

        ]

        # Criando a Janela
        self.janela = sg.Window('Tela de cadastro').layout(layout)

        self.button, self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            altura = self.values['sliderAltura']
            peso = self.values['peso']
            aceit_masculino = self.values['masculino']
            aceit_feminino = self.values['feminino']

            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'altura: {altura}')
            print(f'peso: {peso}')
            print(f'sexo masculino: {aceit_masculino}')
            print(f'sexo feminino: {aceit_feminino}')


tela = TelaPython()
tela.Iniciar()