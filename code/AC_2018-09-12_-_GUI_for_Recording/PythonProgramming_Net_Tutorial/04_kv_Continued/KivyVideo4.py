from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.widget import Widget

################################################################################
# IMPORT kv FILES
################################################################################
from kivy.lang import Builder
from os import listdir
kv_path = './'
for kv in listdir(kv_path):
    print(kv_path+kv)
    Builder.load_file(kv_path+kv)

class Widgets(Widget):
    pass


class SimpleKivy2(App):
    def build(self):
        return Widgets()


if __name__ == "__main__":
    SimpleKivy2().run()
