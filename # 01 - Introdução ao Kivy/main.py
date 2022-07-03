# Importar as bibliotecas
from kivy.app import App
from kivy.uix.label import Label


# Criar a classe do aplicativo
class MeuApp(App):
    def build(self):
        return Label(text='Ola, Mundo!', font_size=72)


if __name__ == '__main__':
    MeuApp().run()
