import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label


class pyTFHCEApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    pyTFHCEApp().run()
