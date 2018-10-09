from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('Stuff.kv')

class Widgets(Widget):
    pass

class SimpleKivy3(App):
    def build(self):
        return Widgets()

if __name__ == '__main__':
    SimpleKivy3().run()
