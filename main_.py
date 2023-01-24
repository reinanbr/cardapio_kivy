#from kivymd.uix.screen import MDScreen
#from turtle import Screen
from kivymd.app import MDApp
#from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
#from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
#from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
#from kivymd.uix.label import MDLabel
#from kivy.uix.scrollview import ScrollView

import os

#for ads
from kivmob import KivMob, TestIds

#size screen
from kivy.core.window import Window
Window.size = (320,620)

#from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen,ScreenManager
#from kivymd.uix.button import MDRectangleFlatButton
#from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.clock import Clock
#from kivy.uix.label import Label

#from kivy.utils import get_color_from_hex

from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
with open('main.kv','r') as app_file:
    app_file_str = str(app_file.read())

list_options = ['about']


from multiprocessing import Process, Queue, Event



class Manager(ScreenManager):
     pass

class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    '''Implements a material design v3 card.'''

    text = StringProperty()


# with open('data/asteroids_from_week.txt','r') as new_f:
#     new_features = new_f.read()
#     print(new_features)


## importting the API NASA  for getting asteroid's from week ##
from data.nasa_api import api_nasa_asteroid as ana_

class SysInfo(MDApp):
    
    
    def content_meteor(self,screen):
        ana,ping_api_nasa=ana_()
        ana=ana['near_earth_objects']
        screen.ids.painel_asteroid.add_widget(MDLabel(text=f'[size=11]*:[/size]\n[size=10]1 lunar = distância da terra até a lua (300 000 km)\nFonte: NASA\nping API NASA: {ping_api_nasa:.2f}s[/size]',
                                                      markup=True,
                                                      font_size=3,
                                                      #font_style='Body2',
                                                      size_hint=(200, None),))
        for _date_ in list(ana.keys()):
            
            screen.ids.painel_asteroid.add_widget(MDLabel(
                markup=True,
                text=f'[size=10]\nasteroides vistos no dia {_date_}[/size]',
                halign="center",
                font_size='10sp',
                font_style='Body2',
                font_name='data/Roboto-Light.ttf',
                size_hint=(200, None),
                #size= self.texture_size,
            ))
            for asteroid in ana[_date_]:
                text_card=[]
                name = asteroid["name"]
                hazardous=asteroid["is_potentially_hazardous_asteroid"]
                is_hazardous = 'sim' if hazardous else 'não'
                speed = float(asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"])
                date_approach = asteroid['close_approach_data'][0]["close_approach_date_full"]
                diameter_min = float(asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"])
                diameter_max = float(asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"])
                diameter = (diameter_max+diameter_min)/2

                dist = float(asteroid["close_approach_data"][0]["miss_distance"]["lunar"])
                mag = float(asteroid["absolute_magnitude_h"])
                text_card.append('')
              #  text_card.append('[b]..[/b]')
                text_card.append('[size=12]')
                text_card.append(f'[b][size=14]nome do asteroide:[/b] {name}[/size]')
                
                text_card.append(f"[b]Velocidade:[/b] {speed:.2f} km/s")
                text_card.append(f"[b]diamêtro médio:[/b] {diameter:.2f} m")
                text_card.append(f"[b]distância da Terra:[/b] {dist:.2f} lunar")
                text_card.append(f'[b]risco em potencial:[/b] {is_hazardous}')
                text_card.append(f"[b]magnetude:[/b] {mag}")
                
                #text_card.append(f"[b]data da abord. de dados:[/b] {date_approach}")
                text_card.append('[/size]')
                
                
                text_card_data = '\n'.join(text_card)
                print(text_card_data)
                # card = MDCard(orientation='vertical',pos_hint={
                #             'center_x': .5, 'center_y': .7},md_bg_color=get_color_from_hex("#f4dedc"),
                #             size_hint=(.9, None),width=150, height=200)

                screen.ids.painel_asteroid.add_widget(MDLabel(
                  #  line_color=(0.2, 0.2, 0.2, 0.8),
                    #style="filled",
                    halign='left',
                    #font_size='8sp',
                    markup=True,
                    font_size='11sp',
                    #font_style='Body2',
                    size_hint=(150, None),
                    text=text_card_data,
                    #md_bg_color=get_color_from_hex("#f4dedc"),
                ))
                #screen.ids.painel_asteroid.add_widget(card)
        
        return screen
                
    
    def update_content(self,*args):
        #self.content_meteor()
        pass
    
        ##configuration text from guide painel: New Features##
        #self.root.ids.info_guide_painel.text = new_features
        #self.root.ids.content.text = f"{os.popen('cat /proc/version').read()}"
       # self.root.ids.bar.title = f"Ssinf"
        #print(self.time())
        
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.accent_palette = "Teal"
        self.time = ''
        Clock.schedule_interval(self.update_content, 1)
        self.ads = KivMob(TestIds.APP)
        self.ads.new_banner(TestIds.BANNER, top_pos=True)
        self.ads.request_banner()
        self.ads.show_banner()
        
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                "height": dp(56),
                "on_release": lambda x=i: self.menu_callback(x),
             } for i in list_options
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        ## the new app_str
        
        self.screen_app = Builder.load_string(app_file_str)
        screen_app = self.content_meteor(self.screen_app)
        
        return screen_app
   
   
    def test(self,button):
        self.menu.caller = button
        self.menu.open()
        print('testado')
        #Snackbar(text="Hello World").open()
        
    def click(self,text):
        print(text)
    
    def menu_callback(self, text_item):
        self.menu.dismiss()
        if text_item=='about':
            Snackbar(text='Creator: ReinanBr').open()
        
        
if __name__=='__main__':
    SysInfo().run()

