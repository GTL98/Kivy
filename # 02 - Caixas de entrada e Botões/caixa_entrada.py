# Importar as bibliotecas
from kivy.app import App
from kivy.uix.label import Label
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


class MeuApp(App):
    def build(self):
        return MeuGridLayout()


if __name__ == '__main__':
    MeuApp().run()
