from kivy.app import App

from kivy.uix.label import Label

class SimpleKivy(App):
    # This SimpleKivy will inherit from the App
    def build(self):
        return Label(text='Hello World')

if __name__=='__main__':
    # The child of App needs to run 
    SimpleKivy().run()
