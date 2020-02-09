import kivy
from kivy.app import App
import os

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class signInPage(BoxLayout):
    def __init__(self, **kwargs):
        super(signInPage,self).__init__(**kwargs)
        self.cols = 2
        button_labels = [
           ("Log in", (1,1,1,1), self.btn1),
           ("Register",(0.25,0.65,0.84,1), self.btn2),
        ]
        for label in button_labels:
            self.button = Button(
                text=label[0],
                background_color=label[1],
                font_size=30,
                color=(1,0,0,1),
                size_hint=(1,0.15),
                padding=(10,10),
            )
            self.button.bind(on_press=label[2])
            self.add_widget(self.button)

    def btn1(self, *args):
        app.page_manager.current = "loginPage"

    def btn2(self, *args):
        app.page_manager.current = "registerPage"

class loginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.col = 1

class registerPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.col = 1

class Manager(App):
    def build(self):
        self.page_manager = ScreenManager()

        self.first_page = signInPage()
        screen = Screen(name="signInPage")
        screen.add_widget(self.first_page)
        self.page_manager.add_widget(screen)

        self.second_page = loginPage()
        screen = Screen(name="loginPage")
        screen.add_widget(self.second_page)
        self.page_manager.add_widget(screen)

        self.second_page = registerPage()
        screen = Screen(name="registerPage")
        screen.add_widget(self.second_page)
        self.page_manager.add_widget(screen)

        app.page_manager.current = "signInPage"

        return self.page_manager

if __name__=="__main__":
    app = Manager()
    app.run()
