import kivy
from kivy.app import App
import os

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

# home
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

# login page
class loginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.col = 1

class registerPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        buttons = [
            {
                "label":"Organization",
                "bg_normal":"assets/orange.jpg",
                "bg_pressed":"assets/dark_orange.jpg",
                "callback":self.toOrgRegistration,
            },
            {
                "label":"Donor",
                "bg_normal":"assets/light_turqoise.jpg",
                "bg_pressed":"assets/dark_turqoise.jpg",
                "callback":self.toDonorRegistration,
            },
        ]
        for button in buttons:
            self.button = Button(
                text=button["label"],
                background_normal=button["bg_normal"],
                background_down=button["bg_pressed"],
                font_size=30,
                color=(0,0,0,1),
                size_hint=(0.5,0.3),
            )
            self.button.bind(on_press=button["callback"])
            self.add_widget(self.button)

    # sends user to the donor register page
    def toDonorRegistration(self, *args):
        app.page_manager.current = "registerDonorPage"
        print("register donor")

    # sends user to the org register page
    def toOrgRegistration(self, *args):
        app.page_manager.current = "registerOrgPage"
        print("register organization")


class registerDonorPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.col = 1
        widgets = []
        header = Label(
            text="Register as a donor\n or a volunteer",
            color=(0.96, 0.65, 0.25,1),
            font_size=30,
        )
        widgets.append(header)
        field_labels = [
            "Full Name",
            "Profile Summary",
            "Volunteer Experience (optional)",
            "Email Address",
            "Password",
            "Password Again",
        ]
        for label in field_labels:
            widgets.append(
                Label(text=label, font_size=14)
            )
            widgets.append(
                TextInput()
            )

        for widget in widgets:
            self.add_widget(widget)

class registerOrgPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

# page manager
class Manager(App):
    def build(self):
        self.nav = []

        self.page_manager = ScreenManager()

        self.sign_in_page = signInPage()
        screen = Screen(name="signInPage")
        screen.add_widget(self.sign_in_page)
        self.page_manager.add_widget(screen)

        self.login_page = loginPage()
        screen = Screen(name="loginPage")
        screen.add_widget(self.login_page)
        self.page_manager.add_widget(screen)

        self.register_page = registerPage()
        screen = Screen(name="registerPage")
        screen.add_widget(self.register_page)
        self.page_manager.add_widget(screen)

        self.register_donor_page = registerDonorPage(orientation="vertical")
        screen = Screen(name="registerDonorPage")
        screen.add_widget(self.register_donor_page)
        self.page_manager.add_widget(screen)

        self.register_org_page = registerOrgPage(orientation="vertical")
        screen = Screen(name="registerOrgPage")
        screen.add_widget(self.register_org_page)
        self.page_manager.add_widget(screen)

        app.page_manager.current = "signInPage"

        def back(self):
            if not nav == []:
                app.page_manager.current = nav[-1]
                nav.pop()

        def on_touch_down(self, touch):
            print(touch.pos)

        return self.page_manager

if __name__=="__main__":
    app = Manager()
    app.run()
