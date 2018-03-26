import kivy
kivy.require('1.10.0')

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup 
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import NumericProperty, ObjectProperty, ListProperty, StringProperty

from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

#from kivy.core.window import Window

import re

class HSButton(Button):
	background_normal = ObjectProperty('Resources/Buttons/SmallButton.png')
	background_down = 	ObjectProperty('Resources/Buttons/SmallButtonHover.png')
	color = ListProperty([0.20,0.18,0.02,0.8])
	font_name = ObjectProperty('Resources/Fonts/BelweBdBTBold.ttf')
	font_size = NumericProperty(18)

class HSLabel(Label):
	color = ListProperty([0.20,0.18,0.02,0.9])
	font_name = ObjectProperty('Resources/Fonts/BelweBdBTBold.ttf')
	font_size = NumericProperty(18)
'''
class ToolTip(Label):
	text=StringProperty("Click to edit") #default toop tip text
	#text color as list, rgba value default black with 100% opacity
	color = ListProperty([0,0,0,1])
	#background colour as an rgb list,value default yellow
	background = ListProperty([1,1,0.6])
	
	#initialise tooltip label
	def __init__(self, **kwargs):
		super(ToolTip, self).__init__(**kwargs)
		# set position at current mouse cursor position
		self.pos=(Window.mouse_pos[0], Window.mouse_pos[1]-self.font_size)
		# update the texture value of the widget
		self.texture_update()
		# set the size of the label to that of the text
		self.size=self.texture_size
		# draw the label background
		with self.canvas.before:
			#set the label background color to the background property as rgb list color
			#sure there must be a better method than this but it works
			Color(self.background[0],self.background[1],self.background[2])
			#draw in the background rectangle
			self.bg_rect = Rectangle(pos=self.pos, size=self.size)
'''								  	
	
class HSTextInput(TextInput):
	foreground_color = ListProperty([0.20,0.18,0.02,0.8])
	font_name = ObjectProperty('Resources/Fonts/BelweBdBTBold.ttf')
	font_size = NumericProperty(18)
	background_color = ListProperty([1, 1, 1, 0.5])
	#background_normal = ObjectProperty('Resources/Buttons/SmallButton.png')
	multiline=False
	
	#tooltiptext = ""
	#toolTip = ToolTip( text=tooltiptext)
	
	
class HSNumericInput(TextInput):
	foreground_color = ListProperty([0.20,0.18,0.02,0.8])
	font_name = ObjectProperty('Resources/Fonts/BelweBdBTBold.ttf')
	font_size = NumericProperty(18)
	background_color = ListProperty([1, 1, 1, 0.5])
	#background_normal = ObjectProperty('Resources/Buttons/SmallButton.png')
	multiline=False	
	min = 0
	max = 9999
	
	#tooltiptext = ""
	#toolTip = ToolTip( text=tooltiptext)

	
	def enforce_int(self, text_input):
		""" Ensure the text input contains only numeric characters or nothing"""
		if not text_input.text.isdigit():
			digit_list = [num for num in text_input.text if num.isdigit()]
			text_input.text = ''.join(digit_list)
		'''
		try: 
			if int(text_input.text) < self.min:
				text_input.text = str(self.min)
			
			if int(text_input.text) > self.max:
				text_input.text = str(self.max)			
		except:
			print('id: ' + text_input.id + '. HSNumericInput.enforce_int() error. ')
		'''
	def enforce_float(self, text_input):
		""" Ensure the text input contains a float"""
		regex = re.compile(r'[+-]?((\d+\.?\d*)|(\.\d+))$')
		
		if regex.match(text_input.text) == None:
			text_input.text = ''
		
	
class HSConfirmPopup(Popup):
	#foreground_color = ListProperty([0.20,0.18,0.02,0.8])
	#background_color = ListProperty([ 0.4, 0.37, 0.32, 0.8])
	#font_name = ObjectProperty('Resources/Fonts/BelweBdBTBold.ttf')
	#font_size = NumericProperty(18)
	
	
	def show(self, _title, _text):
		mytext = _text
		content = BoxLayout(orientation = 'vertical', 
							padding = (10),
							spacing= 20)
		content.add_widget(HSLabel(text = mytext, 
									color = [1,1,1,1], 
									font_size = 16,
									font_name = 'Resources/Fonts/Belwe-Medium.ttf'))
		
		hsbutton = HSButton(text = "OK!", size_hint=(.5,.75),pos_hint= {'x': .25,'top': 0})
		content.add_widget(hsbutton)
		
		mypopup = Popup(content = content,              
                title = _title,
				title_font = 'Resources/Fonts/Belwe-Medium.ttf',
                auto_dismiss = False,
				size_hint=(.5, .35),
				separator_color = [247/255,143/255,46/255,1])
		
		hsbutton.bind(on_press=mypopup.dismiss)		
		mypopup.open()
		

	
		