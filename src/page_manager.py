import kivy
from kivy.app import App
import os

import json
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# home page
class signInPage(BoxLayout):
    def __init__(self, **kwargs):
        super(signInPage,self).__init__(**kwargs)
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
        self.widgets = []
        header = Label(
            text="Log in",
            color=(0.96, 0.65, 0.25,1),
            font_size=30,
        )
        self.widgets.append(header)
        field_labels = [
            "Username",
            "Password",
        ]
        for label in field_labels:
            self.widgets.append(
                Label(text=label, font_size=14,)
            )
            self.widgets.append(
                TextInput(multiline=False)
            )

        login_button = Button(text="Log in",
        background_normal="assets/light_turqoise.jpg",
        background_down="assets/dark_turqoise.jpg")
        login_button.bind(on_press=self.verifyUser)
        self.widgets.append(login_button)

        for widget in self.widgets:
            self.add_widget(widget)

    def verifyUser(self, *args):
        with open("users.json", "r") as users_file:
            users = json.load(users_file)
            for user in users["users"]:
                if user["username"] == self.widgets[2].text:
                    if user["password"] == self.widgets[4].text:
                        print("Access granted")
                else:
                    print("Access denied")

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
                size_hint=(0.5,0.15),
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
        self.widgets = []
        header = Label(
            text="Register as a donor\n or a volunteer",
            color=(0.96, 0.65, 0.25,1),
            font_size=30,
        )
        self.widgets.append(header)
        field_labels = [
            "Full Name",
            "Profile Summary",
            "Volunteer Experience (optional)",
            "Email Address",
            "Password",
            "Password Again",
        ]
        for label in field_labels:
            self.widgets.append(
                Label(text=label, font_size=14)
            )
            self.widgets.append(
                TextInput()
            )

        register_button = Button(text="Register")
        register_button.bind(on_press=self.registerDonor)
        self.widgets.append(register_button)

        for widget in self.widgets:
            self.add_widget(widget)

    def registerDonor(self, *args):
        with open("users.json", "r") as users_file:
            users = json.load(users_file)

            if self.widgets[2].text in users["users"]:
                print("user already exists")
            elif self.widgets[10].text == self.widgets[12].text:
                with open("users.json", "w") as users_file:
                    users["users"].append(
                        {
                            "username":self.widgets[2].text,
                            "profile_summary":self.widgets[4].text,
                            "volunteer_experience":self.widgets[6].text,
                            "email_address":self.widgets[8].text,
                            "password":self.widgets[10].text,
                            "type":"DONOR"
                        }
                    )
                    json.dump(users, users_file)

class registerOrgPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.widgets = []
        header = Label(
            text="Register as a donor\n or a volunteer",
            color=(0.96, 0.65, 0.25,1),
            font_size=30,
        )
        self.widgets.append(header)
        field_labels = [
            "Title of Organization",
            "Profile Summary",
            "Detailed Profile",
            "Website",
            "Street Address 1",
            "Street Address 2",
            "City",
            "State/Province/Region",
            "Zip Code",
            "Email Address",
            "Password",
            "Password Again",
        ]
        for label in field_labels:
            self.widgets.append(
                Label(text=label, font_size=14)
            )
            self.widgets.append(
                TextInput()
            )

        register_button = Button(text="Register")
        register_button.bind(on_press=self.registerOrg)
        self.widgets.append(register_button)

        for widget in self.widgets:
            self.add_widget(widget)

    def registerOrg(self, *args):
        with open("users.json", "r") as users_file:
            users = json.load(users_file)

            if self.widgets[2].text in users["users"]:
                print("user already exists")
            elif self.widgets[22].text == self.widgets[24].text:
                with open("users.json", "w") as users_file:
                    users["users"].append(
                        {
                            "org_title":self.widgets[2].text,
                            "profile_summary":self.widgets[4].text,
                            "detailed_profile":self.widgets[6].text,
                            "website":self.widgets[8].text,
                            "address_1":self.widgets[10].text,
                            "address_2":self.widgets[12].text,
                            "city":self.widgets[14].text,
                            "state_province_region":self.widgets[16].text,
                            "email_address":self.widgets[18].text,
                            "password":self.widgets[20].text,
                            "type":"ORG"
                        }
                    )
                    json.dump(users, users_file)

# page manager
class Manager(App):
    def build(self):
        self.nav = []

        self.page_manager = ScreenManager()

        self.sign_in_page = signInPage()
        screen = Screen(name="signInPage")
        screen.add_widget(self.sign_in_page)
        self.page_manager.add_widget(screen)

        self.login_page = loginPage(orientation="vertical")
        screen = Screen(name="loginPage")
        screen.add_widget(self.login_page)
        self.page_manager.add_widget(screen)

        self.register_page = registerPage(orientation="horizontal")
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
