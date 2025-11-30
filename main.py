from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
import json
import os

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login'
        
        layout = MDBoxLayout(orientation='vertical', spacing=20, adaptive_height=True, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        card = MDCard(size_hint=(0.8, None), height=400, pos_hint={'center_x': 0.5, 'center_y': 0.5}, padding=20)
        card_layout = MDBoxLayout(orientation='vertical', spacing=20)
        
        title = MDLabel(text='Login', theme_text_color='Primary', font_style='H4', halign='center', size_hint_y=None, height=50)
        
        self.username_field = MDTextField(hint_text='Username', size_hint_y=None, height=50)
        self.password_field = MDTextField(hint_text='Password', password=True, size_hint_y=None, height=50)
        
        login_btn = MDRaisedButton(text='Login', size_hint_y=None, height=40, on_release=self.login)
        register_btn = MDRaisedButton(text='Go to Register', size_hint_y=None, height=40, on_release=self.go_to_register)
        
        self.message_label = MDLabel(text='', theme_text_color='Error', halign='center', size_hint_y=None, height=30)
        
        card_layout.add_widget(title)
        card_layout.add_widget(self.username_field)
        card_layout.add_widget(self.password_field)
        card_layout.add_widget(login_btn)
        card_layout.add_widget(register_btn)
        card_layout.add_widget(self.message_label)
        
        card.add_widget(card_layout)
        layout.add_widget(card)
        self.add_widget(layout)
    
    def login(self, instance):
        username = self.username_field.text
        password = self.password_field.text
        
        if not username or not password:
            self.message_label.text = 'Please fill all fields'
            return
        
        users = self.load_users()
        if username in users and users[username] == password:
            self.manager.current = 'dashboard'
            self.manager.get_screen('dashboard').set_user(username)
        else:
            self.message_label.text = 'Invalid credentials'
    
    def go_to_register(self, instance):
        self.manager.current = 'register'
    
    def load_users(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r') as f:
                return json.load(f)
        return {}

class RegisterScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'register'
        
        layout = MDBoxLayout(orientation='vertical', spacing=20, adaptive_height=True, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        card = MDCard(size_hint=(0.8, None), height=400, pos_hint={'center_x': 0.5, 'center_y': 0.5}, padding=20)
        card_layout = MDBoxLayout(orientation='vertical', spacing=20)
        
        title = MDLabel(text='Register', theme_text_color='Primary', font_style='H4', halign='center', size_hint_y=None, height=50)
        
        self.username_field = MDTextField(hint_text='Username', size_hint_y=None, height=50)
        self.password_field = MDTextField(hint_text='Password', password=True, size_hint_y=None, height=50)
        
        register_btn = MDRaisedButton(text='Register', size_hint_y=None, height=40, on_release=self.register)
        login_btn = MDRaisedButton(text='Go to Login', size_hint_y=None, height=40, on_release=self.go_to_login)
        
        self.message_label = MDLabel(text='', theme_text_color='Error', halign='center', size_hint_y=None, height=30)
        
        card_layout.add_widget(title)
        card_layout.add_widget(self.username_field)
        card_layout.add_widget(self.password_field)
        card_layout.add_widget(register_btn)
        card_layout.add_widget(login_btn)
        card_layout.add_widget(self.message_label)
        
        card.add_widget(card_layout)
        layout.add_widget(card)
        self.add_widget(layout)
    
    def register(self, instance):
        username = self.username_field.text
        password = self.password_field.text
        
        if not username or not password:
            self.message_label.text = 'Please fill all fields'
            return
        
        users = self.load_users()
        if username in users:
            self.message_label.text = 'Username already exists'
            return
        
        users[username] = password
        self.save_users(users)
        self.message_label.text = 'Registration successful!'
        self.message_label.theme_text_color = 'Primary'
    
    def go_to_login(self, instance):
        self.manager.current = 'login'
    
    def load_users(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r') as f:
                return json.load(f)
        return {}
    
    def save_users(self, users):
        with open('users.json', 'w') as f:
            json.dump(users, f)

class DashboardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'dashboard'
        
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=20)
        
        self.welcome_label = MDLabel(text='Welcome!', theme_text_color='Primary', font_style='H4', halign='center', size_hint_y=None, height=100)
        
        logout_btn = MDRaisedButton(text='Logout', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5}, on_release=self.logout)
        
        layout.add_widget(self.welcome_label)
        layout.add_widget(logout_btn)
        self.add_widget(layout)
    
    def set_user(self, username):
        self.welcome_label.text = f'Welcome, {username}!'
    
    def logout(self, instance):
        self.manager.current = 'login'

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(DashboardScreen())
        
        return sm

if __name__ == '__main__':
    MyApp().run()