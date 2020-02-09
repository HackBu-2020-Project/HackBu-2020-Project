import kivy
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class SignInPage(BoxLayout):
    def __init__(self, **kwargs):
        super(SignInPage,self).__init__(**kwargs)
        # main_layout = BoxLayout(orientation="vertical", padding=10)
        self.cols = 2
        # subLayout = BoxLayout(orientation="horizontal")
        button_labels = [
           ("Log in", (1,1,1,1)),
           ("Register",(0.25,0.65,0.84,1)),
        ]
        for label in button_labels:
            self.button = Button(
                text=label[0],
                text_size=30,
                color=(1,0,0,1),
                size_hint=(1,0.2),
                background_color=label[1],
                padding=(10,10),
            )
            # self.register = Button(text="Register")
            self.add_widget(self.button)
            # main_layout.add_widget(button)
            # # subLayout.add_widget(button)

class App1(App):
    def build(self):
        return SignInPage()

if __name__=="__main__":
    App1().run()
