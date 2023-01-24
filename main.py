#author: Reinan Br
#date init: ago 21 23:08  2022
#project: App Cardapio IF
#LICENSE: BSD-3
#

from kivymd.uix.toolbar import MDTopAppBar
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDRectangleFlatIconButton

import requests as rq
#import asynckivy as ak
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.clock import Clock
from adm_food import get_food_day,like,dislike
from user import save_user_opt,read_user_opt



#food_day = get_food_day()

#size window
Window.size = (320,650)


#kv file
with open('app.kv','r') as file_kv:
    app_kv = str(file_kv.read())


#MDCard 3D
class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    '''Implements a material design v3 card.'''

#card
class ElevationCard(MDCard, FakeRectangularElevationBehavior):
    pass



colors = {
    "Teal": {
        "200": "#212121",
        "500": "#212121",
        "700": "#212121",
    },
    "Dark":{
        "200":"#000000",
        "500":"#000000",
        "700":"#000000"
    },
    "Red": {
        "200": "#C25554",
        "500": "#C25554",
        "700": "#C25554",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "#28B463",
        "Background": "#2E3032",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
    },
}



# App
class Cardapio(MDApp):
    
    def build(self):
        #self.theme_cls.colors = colors
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Teal"
        self.screen_app = Builder.load_string(app_kv)
        return self.screen_app



    def on_press_like(self):
        if self.is_online:
            #await ak.event(like,self.food)
            #await ak.or_(like(self.food))
            like(self.food,self.user_data_device)

        else:
            pass
        self.on_start()


    #button for like
    def on_press_dislike(self):
        if self.is_online:
            dislike(self.food,self.user_data_device)
        else:
            pass
        self.on_start()
        
    
    
    def verify_like(self):
        user_key = self.user_data_device['userKey']
        if user_key in self.food['usersLikeList']:
            self.root.ids.like.disable = 'True'
        else:
            self.root.ids.dislike.disable = 'False'
        
    
    def verify_dislike(self):
        user_key = self.user_data_device['userKey']
        if user_key in self.food['usersLikeList']:
            self.root.ids.dislike.disable = 'True'
        else:
            self.root.ids.dislike.disable = 'False'
        
    def on_start(self):
        
        user_data_device = read_user_opt()
        self.user_data_device = user_data_device
        
        # self.disable_dislike = not user_data_device['dislike']
        # self.disable_like = not user_data_device['like']
        
        # self.root.ids.dislike.disable = self.disable_dislike
        # self.root.ids.like.disable = self.disable_like
        
        self.root.ids.like.text = str(user_data_device['likeCount'])
        self.root.ids.dislike.text = str(user_data_device['dislikeCount'])
        self.root.ids.food.text = str(user_data_device['food'])
        #self.food =  str(user_data_device['food'])
        
        try:
            rq.get('https://raw.githubusercontent.com/reinanbr/exogame/main/data/questions.json')
            self.is_online = True

        except:
            self.is_online = False
            print('oi')
            Snackbar(text='Ops! sem conexão a internet!').open()
            pass
        
        if self.is_online:
            food_day = get_food_day()
            self.food = food_day
            self.root.ids.food.text = food_day['name']
            
            self.root.ids.like.text = str(food_day['like'])
            
            self.root.ids.dislike.text = str(food_day['dislike'])
            
            #saving from data
            self.user_data_device['likeCount'] = food_day['like']
            self.user_data_device['dislikeCount'] = food_day['dislike']
            self.user_data_device['food'] = food_day['name']
            
            save_user_opt(self.user_data_device)
        
        self.verify_like()
        self.verify_dislike()
        
        # self.root.ids.box.add_widget(
        #         MD3Card(
        #             line_color=(0.2, 0.2, 0.2, 0.8),
        #             style='Filled',
        #             text='comida',
        #             md_bg_color= "#f4dedc",
        #         )
        #     )

if __name__=="__main__":
    Cardapio().run()