from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from page_manager import app


# home page
class signInPage(BoxLayout):
    def __init__(self, **kwargs):
        super(signInPage, self).__init__(**kwargs)
        self.cols = 2
        buttons = [
            {
                "label":"Log in",
                "bg_normal":"assets/white.jpg",
                "bg_pressed":"assets/grey.jpg",
                "callback":self.toLogin,
            },
            {
                "label":"Register",
                "bg_normal":"assets/light_turqoise.jpg",
                "bg_pressed":"assets/dark_turqoise.jpg",
                "callback":self.toRegister,
            },
        ]
        for button in buttons:
            self.button = Button(
                text=button["label"],
                background_normal=button["bg_normal"],
                background_down=button["bg_pressed"],
                font_size=30,
                color=(0,0,0,1),
                size_hint=(1,0.15),
            )
            self.button.bind(on_press=button["callback"])
            self.add_widget(self.button)

    # sends user to the login page
    def toLogin(self, *args):
        app.page_manager.current = "loginPage"
        print("login")

    # sends user to the register page
    def toRegister(self, *args):
        app.page_manager.current = "registerPage"
        print("register")
