# Importar as bibliotecas
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class MeuGridLayout(GridLayout):
    # Iniciar a classe
    def __init__(self, **kwargs):
        # Chamar o construtor do layout de grade
        super(MeuGridLayout, self).__init__(**kwargs)

        # Configurar as colunas
        self.cols = 2

        # Adicionar o widget para a Label "Nome:"
        self.add_widget(Label(text='Nome:'))
        # Adicionar a caixa de entrada para o campo "Nome"
        self.nome = TextInput(multiline=False)
        self.add_widget(self.nome)

        # Adicionar o widget para a Label "Pizza:"
        self.add_widget(Label(text='Pizza:'))
        # Adicionar a caixa de entrada para o campo "Pizza"
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        # Adicionar o widget para a Label "Cor:"
        self.add_widget(Label(text='Cor:'))
        # Adicionar a caixa de entrada para o campo "Cor"
        self.cor = TextInput(multiline=False)
        self.add_widget(self.cor)

        # Criar o botão "Enviar"
        self.enviar = Button(text='Enviar', font_size=32)
        # Passar uma função ao botão
        self.enviar.bind(on_press=self.funcao_botao)
        # Colocar o botão na tela
        self.add_widget(self.enviar)

    def funcao_botao(self, instancia):
        # Mostrar o texto de cada entrada do aplicativo
        cor = self.cor.text
        nome = self.nome.text
        pizza = self.pizza.text

        # Mostrar no aplicativo
        self.add_widget(Label(text=f'Olá {nome}! Você gosta da pizza de {pizza} e a sua cor favorita é {cor}!'))

        # Limpar a caixa de entrada
        self.cor.text = ''
        self.nome.text = ''
        self.pizza.text = ''
        

class MeuApp(App):
    def build(self):
        return MeuGridLayout()


if __name__ == '__main__':
    MeuApp().run()
