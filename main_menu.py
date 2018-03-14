import kivy
kivy.require('1.10.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.config import Config

Config.read('config.ini')

class Main_Menu(FloatLayout):
	def __init__(self, **kwargs): 
		super(Main_Menu, self).__init__(**kwargs)
		self.builder = Builder.load_file('Screens/main_menu.kv')

		
class myApp(App):
	icon = 'Resources/logo_hearthstone.ico'
	title = 'Hearthstone Card Generation'
	def build(self):
		return Main_Menu().builder

if __name__ == '__main__':
     myApp().run()