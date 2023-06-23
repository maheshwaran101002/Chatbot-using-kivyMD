from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
Window_size = (350,550)


class ChatBot(MDApp):

    def change_screen(self, name):
        screen_manager.current = name


        def build(self):
            global screen_manager
            screen_manager = screenManager()
            screen_manager.add_widget(Builder.load_file("Main.kv"))
            screen_manager.add_widget(Builder.load_file("Chats.kv"))
            return
