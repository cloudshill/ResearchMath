from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder


#Builder.load_file('./kv/buttons.kv')
from os import listdir
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

class AddButton(Button):
    pass

class SubtractButton(Button):
    pass

class Container(GridLayout):
    display = ObjectProperty()

    def add_one(self):
        value = int(self.display.text)
        self.display.text = str(value+1)
    def subtract_one(self):
        value = int(self.display.text)
        self.display.text = str(value-1)

class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        return Container()


if __name__ == '__main__':
    app = MainApp()
    app.run()
